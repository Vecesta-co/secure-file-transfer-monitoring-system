"""Generate Markdown, HTML, and CSV audit reports from JSONL logs."""
from __future__ import annotations
import csv
import html
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def read_events(path: Path) -> list[dict]:
    if not path.exists():
        return []
    events = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events


def generate_report(root: Path, logs_path: Path | None = None) -> dict:
    """Create audit artifacts and return report counts."""
    events = read_events(logs_path or root / "logs" / "file_events.jsonl")
    out = root / "reports"
    out.mkdir(parents=True, exist_ok=True)
    event_counts = Counter(e.get("event_type", "UNKNOWN") for e in events)
    severities = Counter(e.get("severity", "INFO") for e in events)
    violations = [e for e in events if e.get("rule_id", "R0") != "R0" and e.get("event_type") != "ERROR"]
    integrity = [e for e in events if e.get("integrity") in {"OK", "MISMATCH"}]
    times = [e.get("timestamp", "") for e in events if e.get("timestamp")]
    users, processes = Counter(e.get("user", "unknown") for e in events), Counter(e.get("process", "unknown") for e in events)
    generated = datetime.now(timezone.utc).isoformat()
    period = f"{min(times)} to {max(times)}" if times else "No events recorded"
    lines = ["# Secure File Transfer Monitoring System — Audit Report", "", f"Generated: {generated}", f"Monitoring period: {period}", "", "## Totals by event type", "| Event | Count |", "|---|---:|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(event_counts.items())] or ["| None | 0 |"]
    lines += ["", "## Totals by severity", "| Severity | Count |", "|---|---:|"] + [f"| {k} | {v} |" for k, v in sorted(severities.items())]
    lines += ["", "## Violations", "| Time | Rule | Severity | File | Destination | Message |", "|---|---|---|---|---|---|"]
    lines += ["| " + " | ".join(str(e.get(k, "")).replace("|", "\\|") for k in ["timestamp", "rule_id", "severity", "src_path", "dest_path", "message"]) + " |" for e in violations] or ["| None | | | | | No violations |"]
    lines += ["", "## Integrity results", "| File | Hash before | Hash after | Status |", "|---|---|---|---|"]
    lines += [f"| {e.get('src_path','')} | {e.get('sha256_before','')} | {e.get('sha256_after','')} | {e.get('integrity','')} |" for e in integrity] or ["| None | | | No checks |"]
    lines += ["", "## Top users and processes", "", "Users: " + (", ".join(f"{k} ({v})" for k, v in users.most_common(5)) or "none"), "", "Processes: " + (", ".join(f"{k} ({v})" for k, v in processes.most_common(5)) or "none"), "", "## Full timeline", "| Time | Type | User | Process | File | Destination | Severity | Rule | Message |", "|---|---|---|---|---|---|---|---|---|"]
    for e in events:
        vals = [e.get(k, "") for k in ["timestamp", "event_type", "user", "process", "src_path", "dest_path", "severity", "rule_id", "message"]]
        lines.append("| " + " | ".join(str(x).replace("|", "\\|") for x in vals) + " |")
    lines += ["", "## Conclusion", f"The monitor recorded {len(events)} events and {len(violations)} rule findings. Review high and critical findings, then retain this report with the JSONL audit log.", ""]
    md = "\n".join(lines)
    (out / "audit_report.md").write_text(md, encoding="utf-8")
    with (out / "events.csv").open("w", newline="", encoding="utf-8-sig") as stream:
        fields = ["timestamp", "event_type", "src_path", "dest_path", "user", "process", "size", "sha256_before", "sha256_after", "integrity", "sensitive", "dest_zone", "severity", "rule_id", "message"]
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader(); writer.writerows(events)
    rendered, in_table, section = [], False, ""
    for line in md.splitlines():
        if line.startswith("## "):
            if in_table: rendered.append("</tbody></table>"); in_table = False
            section = line[3:].strip().lower()
            rendered.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("# "):
            rendered.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.startswith("|---") or not line.strip():
            continue
        elif line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not in_table:
                cls = "violations" if section == "violations" else ""
                rendered.append(f"<table class='{cls}'><thead><tr>" + "".join(f"<th>{html.escape(c)}</th>" for c in cells) + "</tr></thead><tbody>")
                in_table = True
            else:
                severity = next((c for c in cells if c in {"CRITICAL", "HIGH", "MEDIUM", "INFO"}), "")
                css = f" class='{severity.lower()}'" if severity else ""
                rendered.append(f"<tr{css}>" + "".join(f"<td>{html.escape(c)}</td>" for c in cells) + "</tr>")
        else:
            if in_table: rendered.append("</tbody></table>"); in_table = False
            rendered.append(f"<p>{html.escape(line)}</p>")
    if in_table: rendered.append("</tbody></table>")
    document = "<!doctype html><html><head><meta charset='utf-8'><title>Audit report</title><style>body{font:15px system-ui;max-width:1200px;margin:2rem auto;padding:0 1rem;color:#182230}h1{color:#133b5c}table{border-collapse:collapse;width:100%;margin:1rem 0 2rem;font-size:13px}th,td{border:1px solid #d6dee8;text-align:left;padding:.45rem;overflow-wrap:anywhere}th{background:#edf2f7}.high,.critical{background:#ffe7e5;color:#8f160e}.medium{background:#fff2cc;color:#704900}</style></head><body>" + "\n".join(rendered) + "</body></html>"
    (out / "audit_report.html").write_text(document, encoding="utf-8")
    return {"events": len(events), "violations": len(violations), "event_counts": dict(event_counts), "severities": dict(severities)}
