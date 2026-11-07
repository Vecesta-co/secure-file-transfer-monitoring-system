"""Acceptance checklist for the deterministic synthetic demo."""
from __future__ import annotations
import json
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "logs" / "file_events.jsonl"
ALERTS = ROOT / "logs" / "alerts.log"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--events", type=Path, default=LOG, help="JSONL event log to inspect")
    parser.add_argument("--alerts", type=Path, default=ALERTS, help="human-readable alert log to inspect")
    parser.add_argument("--output", type=Path, default=ROOT / "evidence" / "verify_all.txt", help="where to save this checklist")
    args = parser.parse_args()
    events = []
    if args.events.exists():
        for line in args.events.read_text(encoding="utf-8").splitlines():
            try: events.append(json.loads(line))
            except json.JSONDecodeError: pass
    alert_text = args.alerts.read_text(encoding="utf-8") if args.alerts.exists() else ""
    has = lambda kind, part="": any(e.get("event_type") == kind and part.lower() in (e.get("src_path", "") + " " + e.get("dest_path", "")).lower() for e in events)
    checks = [
        ("Scenario 1 - normal copy", any(e.get("event_type") == "COPY" and "meeting_notes_copy.txt" in e.get("dest_path", "") and e.get("rule_id") == "R0" and e.get("severity") == "INFO" for e in events)),
        ("Scenario 2 - approved sensitive copy", any(e.get("message") == "Authorized transfer" and "approved_backup" in e.get("dest_path", "") for e in events)),
        ("Scenario 3 - sensitive USB copy", "Sensitive file copied to USB drive" in alert_text),
        ("Scenario 4 - sensitive cloud copy", "Sensitive file copied to cloud folder" in alert_text),
        ("Scenario 5 - sensitive move", has("MOVE", "employee_salaries.csv")),
        ("Scenario 6 - altered copy integrity alert", any(e.get("rule_id", "").find("R3") >= 0 and "network_share_sim" in e.get("src_path", "") for e in events)),
        ("Scenario 7 - in-place tamper", any(e.get("rule_id", "").find("R3") >= 0 and "sensitive/client_database.csv" in e.get("src_path", "").lower().replace("\\", "/") for e in events)),
        ("Scenario 8 - sensitive deletion", has("DELETE", "server.key")),
        ("Scenario 9 - one accurate 200-file bulk alert", sum(1 for e in events if e.get("rule_id") == "R4") == 1 and any(e.get("rule_id") == "R4" and e.get("message") == "Suspicious movement: 200 files transferred to unknown directory" for e in events)),
        ("Event records have required fields", bool(events) and all(all(k in e for k in ("timestamp", "src_path", "dest_path", "user", "process")) for e in events)),
        ("Control scenarios have no high/critical alerts", sum(1 for e in events if e.get("event_type") == "COPY" and ("meeting_notes_copy.txt" in e.get("dest_path", "") or "approved_backup" in e.get("dest_path", ""))) == 2 and all(e.get("severity") not in {"HIGH", "CRITICAL"} for e in events if e.get("event_type") == "COPY" and ("meeting_notes_copy.txt" in e.get("dest_path", "") or "approved_backup" in e.get("dest_path", "")))),
        ("Objective - event logging", len(events) >= 200 and args.events.exists()),
        ("Objective - unauthorized movement detection", "R1" in alert_text and "R2" in alert_text),
        ("Objective - file integrity", "Integrity Failure: File hash mismatch detected" in alert_text),
        ("Objective - alerts", bool(alert_text.strip())),
        ("Objective - audit report", all((args.events.parent.parent / "reports" / name).exists() if args.events.parent.name == "logs" else (ROOT / "reports" / name).exists() for name in ["audit_report.md", "audit_report.html", "events.csv"])),
    ]
    lines = ["Secure File Transfer Monitoring System - acceptance checklist", ""]
    for label, passed in checks:
        lines.append(f"{'PASS' if passed else 'FAIL'}  {label}")
    lines.append(f"\nResult: {sum(ok for _, ok in checks)}/{len(checks)} checks passed")
    output = "\n".join(lines) + "\n"
    print(output, end="")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
