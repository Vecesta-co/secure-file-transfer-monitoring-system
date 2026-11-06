import hashlib
import json
import time
from pathlib import Path

from ftmon.hasher import hash_file
from ftmon.baseline import create_baseline
from ftmon.monitor import TransferMonitor
from ftmon.policy import Policy, evaluate
from ftmon.report import generate_report


def values():
    return {
        "watched_dirs": ["watched"], "sensitive_dirs": ["watched/private"],
        "restricted_extensions": [".key"], "restricted_name_keywords": ["salary"],
        "allowed_destinations": ["watched/approved"],
        "external_zones": {"USB": ["watched/usb"], "CLOUD": ["watched/cloud"], "NETWORK_SHARE": ["watched/share"]},
        "authorized_users": [], "bulk_transfer": {"threshold_files": 2, "window_seconds": 10},
        "hash_algorithms": ["sha256", "md5"], "ignore_patterns": []
    }


def test_hash_known_vector(tmp_path):
    file = tmp_path / "abc.txt"
    file.write_bytes(b"abc")
    result = hash_file(file, ["sha256", "md5"])
    assert result["sha256"] == hashlib.sha256(b"abc").hexdigest()
    assert result["md5"] == hashlib.md5(b"abc").hexdigest()


def test_policy_sensitive_zone_and_authorization(tmp_path):
    policy = Policy(values(), tmp_path)
    assert policy.is_sensitive(tmp_path / "watched/private/a.txt")
    assert policy.is_sensitive(tmp_path / "watched/a.key")
    assert policy.is_sensitive(tmp_path / "watched/salary.txt")
    assert policy.zone_of("watched/usb/a.txt") == "USB"
    assert policy.zone_of("watched/approved/a.txt") == "ALLOWED"
    assert policy.zone_of("watched/a.txt") == "INTERNAL"
    assert policy.is_authorized_user("any-user")


def test_policy_rules_integrity_and_access(tmp_path):
    policy = Policy({**values(), "authorized_users": ["alice"]}, tmp_path)
    event = {"event_type": "COPY", "sensitive": True, "dest_zone": "USB", "dest_path": "watched/usb/a.key", "user": "mallory", "integrity": "MISMATCH"}
    findings = evaluate(event, policy)
    assert {f[0] for f in findings} == {"R1", "R2", "R3", "R6"}
    assert any(f[1] == "CRITICAL" for f in findings)
    deletion = evaluate({"event_type": "DELETE", "sensitive": True, "dest_zone": "UNKNOWN", "user": "alice"}, policy)
    assert deletion[0][0] == "R5"
    approved = evaluate({"event_type": "COPY", "sensitive": True, "dest_zone": "ALLOWED", "dest_path": "watched/approved/a.txt", "user": "alice"}, policy)
    assert approved == [("R0", "INFO", "Authorized transfer")]


def test_copy_detection_and_integrity_mismatch(tmp_path):
    policy = Policy(values(), tmp_path)
    watched = tmp_path / "watched"; source = watched / "private" / "report.txt"
    source.parent.mkdir(parents=True); source.write_text("original")
    baseline = tmp_path / "data" / "baseline.json"
    create_baseline(policy, baseline)
    monitor = TransferMonitor(policy, tmp_path, baseline)
    copy = watched / "usb" / "report.txt"; copy.parent.mkdir(parents=True); copy.write_text("original")
    monitor._handle("CREATE", copy)
    events = [json.loads(x) for x in (tmp_path / "logs" / "file_events.jsonl").read_text().splitlines()]
    assert events[0]["event_type"] == "COPY" and events[0]["integrity"] == "OK"
    copy.write_text("changed")
    monitor._handle("MODIFY", copy)
    events = [json.loads(x) for x in (tmp_path / "logs" / "file_events.jsonl").read_text().splitlines()]
    assert events[-1]["integrity"] == "MISMATCH"


def test_bulk_window_aggregates_real_count(tmp_path):
    policy = Policy(values(), tmp_path)
    monitor = TransferMonitor(policy, tmp_path)
    directory = str(tmp_path / "watched" / "unknown")
    event = {"event_type": "CREATE", "dest_path": str(Path(directory) / "x.txt"), "dest_zone": "INTERNAL", "timestamp": "test", "user": "tester", "process": "unknown", "severity": "INFO", "rule_id": "R0", "message": "created"}
    start = time.monotonic()
    for i in range(3): monitor._count_bulk({**event, "dest_path": str(Path(directory) / f"{i}.txt")}, start + i * .01)
    monitor._flush_bulk(directory)
    alerts = (tmp_path / "logs" / "alerts.log").read_text()
    assert "Suspicious movement: 3 files transferred to unknown directory" in alerts


def test_report_generation(tmp_path):
    log_dir = tmp_path / "logs"; log_dir.mkdir()
    event = {"timestamp": "2026-01-01T00:00:00+00:00", "event_type": "COPY", "src_path": "a", "dest_path": "b", "user": "u", "process": "p", "size": 1, "sha256_before": "x", "sha256_after": "y", "integrity": "MISMATCH", "sensitive": True, "dest_zone": "USB", "severity": "CRITICAL", "rule_id": "R3", "message": "Integrity Failure"}
    (log_dir / "file_events.jsonl").write_text(json.dumps(event) + "\n")
    summary = generate_report(tmp_path)
    assert summary["events"] == 1 and summary["violations"] == 1
    assert "<table class='violations'>" in (tmp_path / "reports" / "audit_report.html").read_text()
    assert "Integrity Failure" in (tmp_path / "reports" / "audit_report.md").read_text()


def test_watchdog_end_to_end_with_polling(tmp_path):
    policy = Policy(values(), tmp_path)
    create_baseline(policy, tmp_path / "data" / "baseline.json")
    monitor = TransferMonitor(policy, tmp_path)
    monitor.start()
    try:
        target = tmp_path / "watched" / "new.txt"
        target.write_text("new file")
        deadline = time.monotonic() + 8
        while time.monotonic() < deadline:
            log = tmp_path / "logs" / "file_events.jsonl"
            if log.exists() and any(json.loads(line).get("event_type") == "CREATE" for line in log.read_text().splitlines()):
                break
            time.sleep(.05)
        else:
            raise AssertionError("watchdog did not record the created file before timeout")
    finally:
        monitor.stop()
