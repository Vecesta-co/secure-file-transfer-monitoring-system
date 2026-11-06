# Code walkthrough

## `main.py`
- Defines the command-line interface and dispatches baseline, monitor, report, hash, verify, and demo actions.
- Uses `argparse` so command names and options stay discoverable.
- The `baseline` command calls the baseline builder and saves hashes under `data/`.
- The `monitor` command starts the observer and stops it cleanly after Ctrl+C.
- The `hash` and `verify` commands expose integrity checks without requiring the monitor.

## `src/ftmon/hasher.py`
- `wait_until_stable` polls file size so hashing does not race a write in progress.
- `hash_file` reads in chunks and creates any requested hashlib digest.
- Temporary permission and disappearance errors are retried a few times.
- Keeping this code separate makes the hash behavior easy to test.

## `src/ftmon/policy.py`
- `Policy` resolves configured paths against the project root.
- `is_sensitive` checks directory membership, extensions, and name keywords.
- `zone_of` labels approved, internal, USB, cloud, network-share, and unknown paths.
- `is_authorized_user` implements the empty-list policy rule.
- `evaluate` returns rule IDs, severity, and messages for one event.

## `src/ftmon/baseline.py`
- `create_baseline` walks the configured folders and hashes each readable file.
- The baseline stores SHA-256, MD5, size, and modification time for later comparisons.
- Unreadable or disappearing files are skipped so one path does not stop the initial scan.

## `src/ftmon/logger.py`
- `write_event` appends structured event dictionaries to JSONL.
- `write_alert` appends readable alerts and prints them to the terminal.
- A shared thread lock prevents concurrent observer workers from mixing log lines.
- ANSI colors are used only when standard output is interactive.

## `src/ftmon/monitor.py`
- `TransferMonitor` loads the baseline and maintains path and hash indexes.
- It turns filesystem notifications into create, copy, move, delete, or modify records.
- A worker pool handles event bursts while preserving error isolation.
- A short delete delay joins Windows delete/create rename pairs into a move.
- Bulk events are aggregated by destination and time window.

## `src/ftmon/handler.py`
- `MonitorHandler` is the small adapter between watchdog and `TransferMonitor`.
- It submits created, modified, and moved files to the monitor's worker pool.
- It sends deletes through a short delay so Windows rename pairs can be recognized.

## `src/ftmon/report.py`
- Reads JSON Lines defensively, skipping malformed records.
- Builds totals, violation and integrity tables, top users/processes, and a full event timeline.
- Writes Markdown, CSV, and a standalone HTML report with highlighted findings.
- The generator returns summary counts for the CLI and acceptance checks.

## `demo/run_demo.py`
- Recreates only synthetic content under `demo_workspace/`.
- Runs the baseline and monitor, then performs nine readable scenarios.
- Polls the real JSONL log for expected events rather than assuming a fixed delay is enough.
- Confirms the three required sample alert messages before exiting successfully.

## `tools/verify_all.py`
- Reads the current demo event and alert logs.
- Prints a PASS/FAIL checklist for all nine scenarios and five project objectives.
- Saves the same checklist in `evidence/verify_all.txt`.

## Tests
- `tests/test_core.py` covers hashing, policy, rules, copy detection, bulk aggregation, reports, and a real watchdog event.
- The end-to-end monitor test uses polling with a timeout, avoiding a fixed sleep as the success condition.
