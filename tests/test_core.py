import hashlib
import json
import sys
import threading
import time
import types
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


def test_hash_empty_unicode_and_50mb_file(tmp_path):
    empty = tmp_path / "empty (QA) ü.txt"
    empty.write_bytes(b"")
    assert hash_file(empty, ["sha256"])["sha256"] == hashlib.sha256(b"").hexdigest()
    large = tmp_path / "50 MB (large) ü.bin"
    payload = b"FTMON-50MB-" * (50 * 1024 * 1024 // 11) + b"x"
    large.write_bytes(payload)
    start = time.monotonic()
    actual = hash_file(large, ["sha256"])["sha256"]
    assert actual == hashlib.sha256(payload).hexdigest()
    assert time.monotonic() - start < 10


def test_hash_waits_for_a_file_still_being_written(tmp_path):
    path = tmp_path / "nested" / "writing file (QA) ü.txt"
    path.parent.mkdir()
    expected = b""
    parts = [bytes([65 + i]) * 1024 for i in range(12)]
    def writer():
        with path.open("wb") as stream:
            for part in parts:
                stream.write(part)
                stream.flush()
                time.sleep(.05)
    thread = threading.Thread(target=writer)
    thread.start()
    while not path.exists():
        time.sleep(.005)
    result = hash_file(path, ["sha256"])["sha256"]
    thread.join(timeout=2)
    expected = b"".join(parts)
    assert not thread.is_alive()
    assert result == hashlib.sha256(expected).hexdigest()


def test_policy_sensitive_zone_and_authorization(tmp_path):
    policy = Policy(values(), tmp_path)
    assert policy.is_sensitive(tmp_path / "watched/private/a.txt")
    assert policy.is_sensitive(tmp_path / "watched/a.key")
    assert policy.is_sensitive(tmp_path / "watched/salary.txt")
    assert policy.zone_of("watched/usb/a.txt") == "USB"
    assert policy.zone_of("watched/approved/a.txt") == "ALLOWED"
    assert policy.zone_of("watched/a.txt") == "INTERNAL"
    assert policy.is_authorized_user("any-user")


def test_missing_policy_paths_and_real_world_windows_zones(tmp_path):
    missing = Policy({**values(), "watched_dirs": ["missing/folder"]}, tmp_path)
    assert not missing.watched[0].exists()
    assert missing.zone_of("missing/folder/file.txt") == "INTERNAL"
    assert missing.zone_of("elsewhere/file.txt") == "UNKNOWN"
    example = Policy(json.loads((Path(__file__).resolve().parents[1] / "config" / "policy.real-world.example.json").read_text()), tmp_path)
    assert example.zone_of("e:/AuditCase/file.key") == "USB"
    assert example.zone_of("C:/USERS/YOuRName/ONEDRIVE/Reports/file.key") == "CLOUD"
    assert example.zone_of("//SERVER/SHARE/Reports/file.key") == "NETWORK_SHARE"


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


def test_quick_successive_content_changes_are_not_deduplicated(tmp_path):
    policy = Policy(values(), tmp_path)
    source = tmp_path / "watched" / "private" / "rapid.txt"
    source.parent.mkdir(parents=True)
    source.write_text("original")
    baseline = tmp_path / "data" / "baseline.json"
    create_baseline(policy, baseline)
    monitor = TransferMonitor(policy, tmp_path, baseline)
    source.write_text("changed1")
    monitor._handle("MODIFY", source)
    source.write_text("changed2")
    monitor._handle("MODIFY", source)
    events = [json.loads(line) for line in (tmp_path / "logs" / "file_events.jsonl").read_text().splitlines()]
    assert len(events) == 2
    assert all(event["integrity"] == "MISMATCH" for event in events)


def test_metadata_only_notification_does_not_create_duplicate_change(tmp_path):
    policy = Policy(values(), tmp_path)
    source = tmp_path / "watched" / "private" / "same-content.txt"
    source.parent.mkdir(parents=True)
    source.write_text("unchanged")
    baseline = tmp_path / "data" / "baseline.json"
    create_baseline(policy, baseline)
    monitor = TransferMonitor(policy, tmp_path, baseline)
    before = source.stat().st_mtime
    import os
    os.utime(source, (before + 2, before + 2))
    monitor._handle("MODIFY", source)
    assert not (tmp_path / "logs" / "file_events.jsonl").exists()


def test_first_write_notification_can_arrive_before_create(tmp_path):
    policy = Policy(values(), tmp_path)
    source = tmp_path / "watched" / "new-file.txt"
    source.parent.mkdir(parents=True)
    source.write_text("complete contents")
    monitor = TransferMonitor(policy, tmp_path)
    monitor._handle("MODIFY", source)
    monitor._handle("CREATE", source)
    events = [json.loads(line) for line in (tmp_path / "logs" / "file_events.jsonl").read_text().splitlines()]
    assert len(events) == 1
    assert events[0]["event_type"] == "CREATE"


def test_late_create_after_content_change_is_recorded_as_integrity_failure(tmp_path):
    policy = Policy(values(), tmp_path)
    source = tmp_path / "watched" / "late-create.txt"
    source.parent.mkdir(parents=True)
    source.write_text("original")
    baseline = tmp_path / "data" / "baseline.json"
    create_baseline(policy, baseline)
    monitor = TransferMonitor(policy, tmp_path, baseline)
    source.write_text("modified")
    monitor._handle("CREATE", source)
    event = json.loads((tmp_path / "logs" / "file_events.jsonl").read_text().splitlines()[-1])
    assert event["event_type"] == "MODIFY"
    assert event["integrity"] == "MISMATCH"
    assert "R3" in event["rule_id"]


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


def test_bulk_window_emits_once_when_events_arrive_slowly(tmp_path):
    policy = Policy({**values(), "bulk_transfer": {"threshold_files": 1, "window_seconds": .4}}, tmp_path)
    monitor = TransferMonitor(policy, tmp_path)
    directory = str(tmp_path / "watched" / "unknown")
    event = {"event_type": "CREATE", "dest_path": str(Path(directory) / "x.txt"), "dest_zone": "INTERNAL",
             "timestamp": "test", "user": "tester", "process": "unknown", "severity": "INFO", "rule_id": "R0", "message": "created"}
    start = time.monotonic()
    for i in range(4):
        monitor._count_bulk({**event, "dest_path": str(Path(directory) / f"{i}.txt")}, start + i * .05)
        time.sleep(.06)
    time.sleep(.45)
    records = [json.loads(line) for line in (tmp_path / "logs" / "file_events.jsonl").read_text().splitlines()]
    bulk = [event for event in records if event.get("rule_id") == "R4"]
    assert len(bulk) == 1
    assert bulk[0]["message"] == "Suspicious movement: 4 files transferred to unknown directory"


def test_process_attribution_only_matches_opened_path(tmp_path, monkeypatch):
    target = tmp_path / "watched" / "private" / "a.key"
    other = tmp_path / "other.txt"
    class Proc:
        def __init__(self, name, opened):
            self.info = {"name": name, "open_files": [types.SimpleNamespace(path=str(opened))]}
    fake = types.SimpleNamespace(process_iter=lambda _attrs: [Proc("unrelated.exe", other), Proc("writer.exe", target)])
    monkeypatch.setitem(sys.modules, "psutil", fake)
    monitor = TransferMonitor(Policy(values(), tmp_path), tmp_path)
    assert monitor._process(target) == "writer.exe"


def test_external_configured_paths_are_logged_without_user_directory(tmp_path):
    root = tmp_path / "project"
    external = tmp_path / "external-drive"
    root.mkdir(); external.mkdir()
    values_outside = {**values(), "watched_dirs": [str(external)],
                      "external_zones": {"CLOUD": [str(external / "OneDrive")]}}
    policy = Policy(values_outside, root)
    monitor = TransferMonitor(policy, root)
    shown = monitor._display(external / "OneDrive" / "Personal" / "file.txt")
    assert shown == "CLOUD:/Personal/file.txt"
    assert "external-drive" not in shown


def test_policy_ignore_pattern_suppresses_windows_folder_metadata(tmp_path):
    policy = Policy({**values(), "ignore_patterns": ["desktop.ini"]}, tmp_path)
    monitor = TransferMonitor(policy, tmp_path)
    sidecar = tmp_path / "watched" / "desktop.ini"
    sidecar.parent.mkdir()
    sidecar.write_text("folder metadata")
    monitor._handle("CREATE", sidecar)
    assert not (tmp_path / "logs" / "file_events.jsonl").exists()


def test_authorized_user_policy_fires_for_current_and_allows_listed_user(tmp_path, monkeypatch):
    policy = Policy({**values(), "authorized_users": ["approved-user"]}, tmp_path)
    monitor = TransferMonitor(policy, tmp_path)
    secret = tmp_path / "watched" / "private" / "confidential.txt"
    secret.parent.mkdir(parents=True)
    secret.write_text("private")
    monkeypatch.setattr("ftmon.monitor.getpass.getuser", lambda: "current-user")
    monitor._handle("CREATE", secret)
    event = json.loads((tmp_path / "logs" / "file_events.jsonl").read_text().splitlines()[-1])
    assert "R6" in event["rule_id"]
    allowed = Policy({**values(), "authorized_users": ["current-user"]}, tmp_path)
    assert allowed.is_authorized_user("current-user")
    assert not any(rule == "R6" for rule, _severity, _message in evaluate(
        {"event_type": "CREATE", "sensitive": True, "dest_zone": "INTERNAL", "user": "current-user"}, allowed))


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
