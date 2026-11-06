"""Deterministic, synthetic end-to-end monitoring demonstration."""
from __future__ import annotations
import json
import shutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from ftmon.baseline import create_baseline  # noqa: E402
from ftmon.monitor import TransferMonitor  # noqa: E402
from ftmon.policy import load_policy  # noqa: E402
from ftmon.report import generate_report  # noqa: E402

WORK = ROOT / "demo_workspace"
DIRS = ["documents", "sensitive", "approved_backup", "usb_drive_sim", "cloud_sync_sim", "network_share_sim", "unknown_dir"]


def _clear_contents(folder: Path) -> None:
    """Delete generated children while retaining project-owned output folders."""
    if not folder.exists():
        return
    for child in folder.iterdir():
        if child.is_dir():
            _clear_contents(child)
        else:
            child.unlink()


def _wait_for(predicate, timeout=5.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if predicate(): return True
        time.sleep(0.05)
    return False


def _logged(predicate, timeout=20.0):
    """Poll the actual JSONL output until the expected filesystem event arrives."""
    log = ROOT / "logs" / "file_events.jsonl"
    def check():
        if not log.exists(): return False
        records = []
        for line in log.read_text(encoding="utf-8").splitlines():
            try: records.append(json.loads(line))
            except json.JSONDecodeError: pass
        return predicate(records)
    return _wait_for(check, timeout)


def _rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def run(clean: bool = True) -> int:
    if clean:
        for folder in (WORK, ROOT / "logs", ROOT / "reports", ROOT / "data"):
            _clear_contents(folder)
    for name in DIRS: (WORK / name).mkdir(parents=True, exist_ok=True)
    (WORK / "documents" / "meeting_notes.txt").write_text("Synthetic meeting notes.\n", encoding="utf-8")
    (WORK / "documents" / "project_plan.txt").write_text("Synthetic project plan.\n", encoding="utf-8")
    (WORK / "sensitive" / "employee_salaries.csv").write_text("name,salary\nExample Person,0\n", encoding="utf-8")
    (WORK / "sensitive" / "passwords_backup.txt").write_text("FAKE password: not-a-secret\n", encoding="utf-8")
    (WORK / "sensitive" / "client_database.csv").write_text("FAKE client id,name\n0,Example\n", encoding="utf-8")
    (WORK / "sensitive" / "server.key").write_text("FAKE KEY MATERIAL FOR DEMO ONLY\n", encoding="utf-8")
    policy = load_policy(ROOT / "config" / "policy.json")
    count = create_baseline(policy, ROOT / "data" / "baseline.json")
    print(f"Baseline created for {len(count)} synthetic files")
    monitor = TransferMonitor(policy, ROOT)
    monitor.start()
    alerts_file = ROOT / "logs" / "alerts.log"
    scenarios = [
        "Normal copy inside documents", "Sensitive file copied to approved backup", "Sensitive file copied to USB",
        "Sensitive file copied to cloud folder", "Sensitive file moved to unknown directory",
        "Altered copy to network share", "In-place sensitive file tamper", "Sensitive file deletion", "200-file bulk transfer"
    ]
    def scenario(i):
        print(f"\nSCENARIO {i}/9: {scenarios[i-1]}", flush=True)
    try:
        scenario(1); p = WORK / "documents" / "meeting_notes_copy.txt"; shutil.copy2(WORK / "documents" / "meeting_notes.txt", p); assert _logged(lambda es: any(e.get("dest_path") == _rel(p) for e in es))
        scenario(2); p = WORK / "approved_backup" / "employee_salaries.csv"; shutil.copy2(WORK / "sensitive" / "employee_salaries.csv", p); assert _logged(lambda es: any(e.get("dest_path") == _rel(p) for e in es))
        scenario(3); p = WORK / "usb_drive_sim" / "server.key"; shutil.copy2(WORK / "sensitive" / "server.key", p); assert _logged(lambda es: any("Sensitive file copied to USB drive" in e.get("message", "") for e in es))
        scenario(4); p = WORK / "cloud_sync_sim" / "client_database.csv"; shutil.copy2(WORK / "sensitive" / "client_database.csv", p); assert _logged(lambda es: any(e.get("dest_path") == _rel(p) and e.get("event_type") == "COPY" for e in es))
        scenario(5); p = WORK / "unknown_dir" / "employee_salaries.csv"; shutil.move(str(WORK / "sensitive" / "employee_salaries.csv"), str(p)); assert _logged(lambda es: any(e.get("event_type") == "MOVE" and e.get("dest_path") == _rel(p) for e in es))
        scenario(6); altered = WORK / "network_share_sim" / "passwords_backup.txt"; shutil.copy2(WORK / "sensitive" / "passwords_backup.txt", altered); assert _logged(lambda es: any(e.get("dest_path") == _rel(altered) for e in es)); altered.write_text(altered.read_text(encoding="utf-8") + "ALTERED\n", encoding="utf-8"); assert _logged(lambda es: any(e.get("integrity") == "MISMATCH" and _rel(altered) in e.get("src_path", "") for e in es))
        scenario(7); tamper = WORK / "sensitive" / "client_database.csv"; tamper.write_text(tamper.read_text(encoding="utf-8") + "changed,record\n", encoding="utf-8"); assert _logged(lambda es: any(e.get("integrity") == "MISMATCH" and _rel(tamper) in e.get("src_path", "") for e in es))
        scenario(8); deleted = WORK / "sensitive" / "server.key"; deleted.unlink(); assert _logged(lambda es: any(e.get("event_type") == "DELETE" and _rel(deleted) in e.get("src_path", "") for e in es))
        scenario(9); bulk = WORK / "unknown_dir" / "bulk"; bulk.mkdir(exist_ok=True)
        for i in range(200): (bulk / f"tiny_{i:03}.txt").write_text(f"dummy {i}\n", encoding="utf-8")
        assert _logged(lambda es: sum(1 for e in es if e.get("event_type") == "CREATE" and _rel(bulk) in e.get("src_path", "")) >= 200, timeout=180)
        _wait_for(lambda: alerts_file.exists() and "Suspicious movement: 200 files transferred to unknown directory" in alerts_file.read_text(encoding="utf-8"), timeout=5)
    finally:
        monitor.stop()
    summary = generate_report(ROOT)
    alerts = alerts_file.read_text(encoding="utf-8") if alerts_file.exists() else ""
    expected = ["Sensitive file copied to USB drive", "Integrity Failure: File hash mismatch detected", "Suspicious movement: 200 files transferred to unknown directory"]
    ok = all(msg in alerts for msg in expected)
    print("\nFINAL SUMMARY")
    print(json.dumps(summary, indent=2))
    print("Expected alerts:")
    for msg in expected: print(f"{'PASS' if msg in alerts else 'FAIL'} {msg}")
    print("Reports: reports/audit_report.md, reports/audit_report.html, reports/events.csv")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
