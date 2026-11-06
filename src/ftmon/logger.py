"""Thread-safe JSONL event and human-readable alert logging."""
from __future__ import annotations
import json
import os
import threading
from datetime import datetime, timezone
from pathlib import Path

LOCK = threading.Lock()
COLORS = {"INFO": "37", "MEDIUM": "33", "HIGH": "31", "CRITICAL": "1;31"}
COLOR_ENABLED = True


def configure_colors(enabled: bool) -> None:
    """Set console color output and safely request Windows virtual-terminal mode."""
    global COLOR_ENABLED
    COLOR_ENABLED = enabled
    if not enabled or os.name != "nt":
        return
    try:
        import ctypes
        kernel = ctypes.windll.kernel32
        handle = kernel.GetStdHandle(-11)
        mode = ctypes.c_uint()
        if handle not in (0, -1) and kernel.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel.SetConsoleMode(handle, mode.value | 0x0004)
    except (AttributeError, OSError):
        pass


def write_event(event: dict, root: Path) -> None:
    logs = root / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    if not event.get("timestamp"):
        event["timestamp"] = datetime.now(timezone.utc).isoformat()
    with LOCK, (logs / "file_events.jsonl").open("a", encoding="utf-8") as out:
        out.write(json.dumps(event, ensure_ascii=False) + "\n")


def write_alert(event: dict, finding: tuple[str, str, str], root: Path) -> None:
    rule, severity, message = finding
    line = f"{event.get('timestamp')} [{severity}] {rule}: {message} | {event.get('src_path')} -> {event.get('dest_path')}"
    logs = root / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    with LOCK, (logs / "alerts.log").open("a", encoding="utf-8") as out:
        out.write(line + "\n")
    if COLOR_ENABLED and getattr(__import__("sys").stdout, "isatty", lambda: False)():
        print(f"\033[{COLORS.get(severity, '37')}m{line}\033[0m", flush=True)
    else:
        print(line, flush=True)
