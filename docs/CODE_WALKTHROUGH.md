# Beginner code walkthrough

## What happens when a file changes

The program follows a simple chain: it watches a folder, identifies the path and change, checks the policy, compares file hashes when possible, writes an event, and later builds a report. The JSON policy tells the monitor which folders are sensitive and which destinations represent approved backup, USB, cloud, or network-share locations.

## Hash integrity in plain language

A hash is a short fingerprint calculated from a file's bytes. SHA-256 is deterministic: identical content gives the same fingerprint. If one byte changes, the fingerprint changes. The baseline stores the first fingerprint. When a later event produces a different value, rule R3 reports an integrity mismatch. A hash does not prove that the original content was safe, so the baseline must come from a trusted state.

## File transfer monitoring and DLP

The project uses folder notifications as signals that a file was created, changed, renamed, or removed. A native notification does not always say “copy,” so the monitor compares content and paths to infer a copy-like event. Data-loss prevention (DLP) describes rules that help identify sensitive information moving to an unapproved place. Here, R1 and R2 implement a small path-based example. The monitor records and alerts; it does not block the operation.

## Auditing

Each event is written as JSON on its own line. JSON Lines is convenient because new events can be appended while the program runs. The separate alert log is easier to read quickly. The report generator summarizes event types, severities, rule findings, integrity results, users, processes, and the full timeline. Keeping both detailed records and a summary supports later review.

## Source files

- `main.py` defines the commands and sends each command to the appropriate module.
- `config/policy.json` contains watched folders, sensitive locations, approved destinations, external zones, and ignored file names.
- `src/ftmon/hasher.py` waits briefly for a stable file and calculates requested digests in chunks.
- `src/ftmon/baseline.py` scans the watched folders and stores starting hashes and metadata.
- `src/ftmon/policy.py` resolves paths, labels zones, checks usernames, and applies R0–R6.
- `src/ftmon/handler.py` receives watchdog notifications and submits work.
- `src/ftmon/monitor.py` keeps path/hash indexes, correlates some Windows rename notifications, checks integrity, and groups bulk activity.
- `src/ftmon/logger.py` writes event and alert records.
- `src/ftmon/report.py` converts JSONL events into Markdown, HTML, and CSV.
- `demo/run_demo.py` creates safe dummy files and executes the nine example scenarios.
- `tools/verify_all.py` checks the expected scenarios and essential output fields.

## Detection rules

| Rule | Meaning |
|---|---|
| R0 | Record routine or approved activity. |
| R1 | Sensitive file moved or copied outside an approved folder. |
| R2 | File entered a configured USB, cloud, or network-share zone. |
| R3 | SHA-256 changed from the indexed value. |
| R4 | File count passed the configured burst threshold in a window. |
| R5 | Sensitive file was deleted. |
| R6 | Observed sensitive activity came from a user outside the allow-list. |

## Run the project

From PowerShell in the project folder:

```powershell
python main.py demo --clean --pace 3
python -m pytest -q
python main.py report
```

The demo uses only its synthetic workspace. The report command summarizes the current event log.

## Important limits

Configured paths stand in for external destinations; the program does not detect USB hardware or inspect network traffic. Windows open/read access is not monitored. Process attribution uses optional psutil data and remains `unknown` when no matching open-file information is available. Filesystem notification timing varies, especially in synchronized folders, so deployments need platform-specific verification.
