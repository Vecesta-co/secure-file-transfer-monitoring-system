"""Watchdog adapter, event classification, and rolling file index."""
from __future__ import annotations
import getpass
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from watchdog.observers import Observer
from .hasher import hash_file
from .handler import MonitorHandler
from .logger import write_alert, write_event
from .policy import Policy, evaluate


class TransferMonitor:
    """Observe configured folders and turn filesystem changes into audit events."""
    def __init__(self, policy: Policy, root: Path, baseline_path: Path | None = None):
        self.policy, self.root = policy, root.resolve()
        self.baseline_path = baseline_path or self.root / "data" / "baseline.json"
        self.index: dict[str, dict] = {}
        self.by_hash: dict[str, list[str]] = {}
        self.last_events: dict[tuple, float] = {}
        self.bulk: dict[str, list] = {}
        self.bulk_timers: dict[str, threading.Timer] = {}
        self.pending_deletes: dict[str, tuple[threading.Timer, dict, float]] = {}
        self.lock = threading.RLock()
        self.observer = Observer()
        self.executor = ThreadPoolExecutor(max_workers=8, thread_name_prefix="ftmon-event")
        self._load_index()

    def _key(self, path: str | Path) -> str:
        return str(Path(path).resolve())

    def _display(self, path: str | Path | None) -> str:
        if not path:
            return ""
        p = Path(path).resolve()
        try:
            return p.relative_to(self.root).as_posix()
        except ValueError:
            return str(p)

    def _load_index(self) -> None:
        try:
            raw = json.loads(self.baseline_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            raw = {}
        self.index = {self._key(Path(k) if Path(k).is_absolute() else self.root / k): v for k, v in raw.items()}
        for path, meta in self.index.items():
            if meta.get("sha256"):
                self.by_hash.setdefault(meta["sha256"], []).append(path)

    def _add_index(self, path: str | Path, meta: dict) -> None:
        key = self._key(path)
        with self.lock:
            self.index[key] = meta
            if meta.get("sha256"):
                self.by_hash.setdefault(meta["sha256"], []).append(key)

    def _remove_index(self, path: str | Path) -> dict | None:
        key = self._key(path)
        with self.lock:
            meta = self.index.pop(key, None)
            if meta and meta.get("sha256"):
                self.by_hash[meta["sha256"]] = [p for p in self.by_hash.get(meta["sha256"], []) if p != key]
            return meta

    def _hash(self, path: Path) -> dict:
        return hash_file(path, self.policy.values.get("hash_algorithms", ["sha256", "md5"]))

    def _process(self, path: Path) -> str:
        # psutil is optional; process-to-open-file attribution is best-effort.
        try:
            import psutil  # type: ignore
            target = str(path.resolve()).casefold()
            for proc in psutil.process_iter(["name", "open_files"]):
                for opened in proc.info.get("open_files") or []:
                    try:
                        if str(Path(opened.path).resolve()).casefold() == target:
                            return proc.info.get("name") or "unknown"
                    except (OSError, TypeError, ValueError):
                        continue
        except Exception:
            pass
        return "unknown"

    def start(self) -> None:
        handler = MonitorHandler(self)
        for folder in self.policy.watched:
            folder.mkdir(parents=True, exist_ok=True)
            self.observer.schedule(handler, str(folder), recursive=True)
        self.observer.start()

    def stop(self) -> None:
        self.observer.stop()
        self.observer.join(timeout=5)
        self.executor.shutdown(wait=True)
        for key, (timer, _meta, _when) in list(self.pending_deletes.items()):
            timer.cancel()
            self.pending_deletes.pop(key, None)
            self._handle("DELETE", Path(key))
        for timer in list(self.bulk_timers.values()):
            timer.cancel()
        for directory in list(self.bulk):
            self._flush_bulk(directory)

    def _dedup(self, event_type: str, src: str, dest: str) -> bool:
        now = time.monotonic()
        key = (event_type, src, dest)
        if now - self.last_events.get(key, 0) < 0.5:
            return True
        self.last_events[key] = now
        return False

    def _handle(self, event_type: str, src: Path, dest: Path | None = None, observed_at: float | None = None) -> None:
        try:
            import fnmatch
            if any(fnmatch.fnmatch(src.name, pat) for pat in self.policy.values.get("ignore_patterns", [])):
                return
            if src.is_dir() and (dest is None or dest.is_dir()):
                return
            dest = dest or src
            if self._dedup(event_type, str(src), str(dest)):
                return
            old = self.index.get(self._key(src))
            before = (old or {}).get("sha256", "")
            after = ""
            if event_type == "MODIFY" and old and src.exists():
                try:
                    st = src.stat()
                    if old.get("size") == st.st_size and old.get("mtime_ns") == st.st_mtime_ns:
                        return
                except OSError:
                    pass
            if event_type != "DELETE" and dest.exists() and dest.is_file():
                after = self._hash(dest).get("sha256", "")
            kind, sensitive, integrity, source = event_type, self.policy.is_sensitive(src), "N/A", str(src)
            pending = self._take_pending_move(dest, after) if event_type == "CREATE" else None
            if pending:
                moved_from, old = pending
                source, kind = moved_from, "MOVE"
                sensitive = sensitive or self.policy.is_sensitive(moved_from)
                before = old.get("sha256", "")
                integrity = "OK" if before and before == after else "MISMATCH" if before and after else "N/A"
                self._remove_index(moved_from)
            elif event_type == "CREATE":
                matches = [p for p in self.by_hash.get(after, []) if p != self._key(dest)] if after else []
                if matches:
                    source, kind, sensitive, before, integrity = matches[0], "COPY", sensitive or self.policy.is_sensitive(matches[0]), after, "OK"
                else:
                    peers = [p for p in self.index if Path(p).name.lower() == dest.name.lower() and p != self._key(dest)]
                    if peers:
                        source, kind, sensitive = peers[0], "COPY", sensitive or self.policy.is_sensitive(peers[0])
                        before, integrity = self.index[peers[0]].get("sha256", ""), "MISMATCH"
                    else:
                        kind = "CREATE"
            elif event_type == "MOVE":
                integrity = "OK" if before and before == after else "MISMATCH" if before and after else "N/A"
                self._remove_index(src)
            elif event_type == "DELETE":
                self._remove_index(src)
            elif event_type == "MODIFY":
                integrity = "MISMATCH" if before and after and before != after else "OK" if before and after else "N/A"
                source = str(src)
            if kind != "DELETE" and dest.exists() and dest.is_file():
                try:
                    stat = dest.stat()
                    self._add_index(dest, {**self._hash(dest), "size": stat.st_size, "mtime_ns": stat.st_mtime_ns})
                except OSError:
                    pass
            user = __import__("getpass").getuser()
            event = {"timestamp": None, "event_type": kind, "src_path": self._display(source),
                     "dest_path": self._display(dest) if kind in {"COPY", "MOVE", "CREATE"} else "",
                     "user": user, "process": self._process(dest), "size": dest.stat().st_size if dest.exists() and dest.is_file() else 0,
                     "sha256_before": before, "sha256_after": after, "integrity": integrity,
                     "sensitive": sensitive, "dest_zone": self.policy.zone_of(dest) if kind in {"COPY", "MOVE", "CREATE"} else "UNKNOWN",
                     "severity": "INFO", "rule_id": "R0", "message": "File activity recorded"}
            findings = evaluate(event, self.policy)
            event["severity"] = max((f[1] for f in findings), key=lambda s: ["INFO", "MEDIUM", "HIGH", "CRITICAL"].index(s))
            event["rule_id"] = ",".join(f[0] for f in findings)
            event["message"] = "; ".join(f[2] for f in findings)
            write_event(event, self.root)
            for finding in findings:
                if finding[0] != "R0":
                    write_alert(event, finding, self.root)
            if kind in {"COPY", "MOVE", "CREATE"} and event["dest_path"]:
                self._count_bulk(event, observed_at)
        except Exception as exc:  # Observer callbacks must not die on one bad path.
            write_event({"timestamp": None, "event_type": "ERROR", "src_path": self._display(src), "dest_path": self._display(dest),
                         "user": getpass.getuser(), "process": "unknown", "size": 0, "sha256_before": "",
                         "sha256_after": "", "integrity": "N/A", "sensitive": False, "dest_zone": "UNKNOWN",
                         "severity": "MEDIUM", "rule_id": "ERROR", "message": f"Event processing error: {type(exc).__name__}: {exc}"}, self.root)

    def _count_bulk(self, event: dict, observed_at: float | None = None) -> None:
        directory = str(Path(event["dest_path"]).parent)
        now = observed_at if observed_at is not None else time.monotonic()
        with self.lock:
            entries = self.bulk.setdefault(directory, [])
            entries.append((now, event))
            window = float(self.policy.values.get("bulk_transfer", {}).get("window_seconds", 10))
            self.bulk[directory] = [(t, e) for t, e in entries if now - t <= window]
            # Anchor one timer to the start of the configured window. Resetting
            # it on every event can split a slow transfer into repeated alerts.
            if directory not in self.bulk_timers:
                timer = threading.Timer(window, self._flush_bulk, args=(directory,))
                timer.daemon = True
                self.bulk_timers[directory] = timer
                timer.start()

    def _flush_bulk(self, directory: str) -> None:
        with self.lock:
            entries = self.bulk.pop(directory, [])
            self.bulk_timers.pop(directory, None)
        threshold = int(self.policy.values.get("bulk_transfer", {}).get("threshold_files", 50))
        if len(entries) <= threshold:
            return
        base = dict(entries[-1][1])
        zone = base.get("dest_zone", "UNKNOWN")
        label = {"USB": "USB drive", "CLOUD": "cloud folder", "NETWORK_SHARE": "network share"}.get(zone, "unknown directory")
        base.update({"event_type": "BULK", "src_path": "", "size": 0, "integrity": "N/A",
                     "severity": "HIGH", "rule_id": "R4", "message": f"Suspicious movement: {len(entries)} files transferred to {label}"})
        write_event(base, self.root)
        write_alert(base, ("R4", "HIGH", base["message"]), self.root)

    def _queue_delete(self, path: Path) -> None:
        """Hold a Windows delete briefly so delete+create rename pairs can be logged as MOVE."""
        key = self._key(path)
        old = self.index.get(key, {})
        def flush():
            with self.lock:
                pending = self.pending_deletes.pop(key, None)
            if pending:
                self._handle("DELETE", path)
        timer = threading.Timer(0.75, flush)
        timer.daemon = True
        with self.lock:
            previous = self.pending_deletes.pop(key, None)
            if previous: previous[0].cancel()
            self.pending_deletes[key] = (timer, old, time.monotonic())
        timer.start()

    def _take_pending_move(self, dest: Path, digest: str) -> tuple[str, dict] | None:
        with self.lock:
            candidates = list(self.pending_deletes.items())
            for key, (timer, meta, when) in candidates:
                if time.monotonic() - when <= 0.75 and (Path(key).name.lower() == dest.name.lower() or (digest and meta.get("sha256") == digest)):
                    timer.cancel()
                    self.pending_deletes.pop(key, None)
                    return key, meta
        return None


