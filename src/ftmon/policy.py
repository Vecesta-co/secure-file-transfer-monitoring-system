"""Policy loading, path classification, and event rules."""
from __future__ import annotations
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_POLICY = ROOT / "config" / "policy.json"


class Policy:
    """Resolved policy settings for one project root."""
    def __init__(self, values: dict, root: Path = ROOT):
        self.values, self.root = values, root.resolve()
        self.watched = [self.resolve(p) for p in values.get("watched_dirs", [])]
        self.sensitive_dirs = [self.resolve(p) for p in values.get("sensitive_dirs", [])]
        self.allowed = [self.resolve(p) for p in values.get("allowed_destinations", [])]
        self.zones = {k: [self.resolve(p) for p in v] for k, v in values.get("external_zones", {}).items()}
        self.extensions = {e.lower() for e in values.get("restricted_extensions", [])}
        self.keywords = [s.lower() for s in values.get("restricted_name_keywords", [])]
        self.authorized_users = set(values.get("authorized_users", []))

    def resolve(self, path: str | Path) -> Path:
        p = Path(path)
        return (p if p.is_absolute() else self.root / p).resolve()

    def contains(self, parent: Path, path: Path) -> bool:
        try:
            a, b = os.path.normcase(str(parent.resolve())), os.path.normcase(str(path.resolve()))
            return os.path.commonpath([a, b]) == a
        except (ValueError, OSError):
            return False

    def is_sensitive(self, path: str | Path) -> bool:
        p = self.resolve(path)
        return (any(self.contains(d, p) for d in self.sensitive_dirs)
                or p.suffix.lower() in self.extensions
                or any(k in p.name.lower() for k in self.keywords))

    def zone_of(self, path: str | Path | None) -> str:
        if not path:
            return "UNKNOWN"
        p = self.resolve(path)
        if any(self.contains(d, p) for d in self.allowed):
            return "ALLOWED"
        for zone, dirs in self.zones.items():
            if any(self.contains(d, p) for d in dirs):
                return zone
        if any(self.contains(d, p) for d in self.watched):
            return "INTERNAL"
        return "UNKNOWN"

    def is_authorized_user(self, user: str) -> bool:
        return not self.authorized_users or user in self.authorized_users


def load_policy(path: str | Path = DEFAULT_POLICY) -> Policy:
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    return Policy(json.loads(p.read_text(encoding="utf-8")), ROOT)


def evaluate(event: dict, policy: Policy) -> list[tuple[str, str, str]]:
    """Return (rule, severity, message) findings for one event."""
    findings = []
    kind, sensitive, zone = event.get("event_type"), event.get("sensitive", False), event.get("dest_zone", "UNKNOWN")
    dest = event.get("dest_path")
    allowed = bool(dest) and any(policy.contains(d, policy.resolve(dest)) for d in policy.allowed)
    if sensitive and kind in {"COPY", "MOVE"} and not allowed:
        findings.append(("R1", "HIGH", "Sensitive file moved outside approved location"))
    if kind in {"COPY", "MOVE"} and zone in {"USB", "CLOUD", "NETWORK_SHARE"}:
        label = {"USB": "USB drive", "CLOUD": "cloud folder", "NETWORK_SHARE": "network share"}[zone]
        findings.append(("R2", "HIGH" if sensitive else "MEDIUM", f"Sensitive file copied to {label}" if sensitive else f"File transferred to {label}"))
    if event.get("integrity") == "MISMATCH":
        findings.append(("R3", "CRITICAL", "Integrity Failure: File hash mismatch detected"))
    if sensitive and kind == "DELETE":
        findings.append(("R5", "HIGH", "Sensitive file deleted"))
    if sensitive and not policy.is_authorized_user(event.get("user", "")):
        findings.append(("R6", "HIGH", "Unauthorized user accessed sensitive file"))
    if not findings:
        findings.append(("R0", "INFO", "Authorized transfer" if sensitive and allowed else "File activity recorded"))
    return findings
