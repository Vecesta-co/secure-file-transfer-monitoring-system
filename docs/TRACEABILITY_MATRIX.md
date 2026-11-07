# Traceability matrix

All counts and evidence references derive from the final captured run.

| Requirement | Feature | Test / check | Evidence |
|---|---|---|---|
| REQ-1 Event logging | watchdog + JSONL | `test_watchdog_end_to_end_with_polling` | `evidence/final/run1/logs/file_events.jsonl` |
| REQ-2 Movement policy | Policy zones R1/R2/R5/R6 | `test_policy_rules_integrity_and_access` | `evidence/final/run1/logs/alerts.log` |
| REQ-3 Integrity | SHA-256 baseline and comparisons | `test_hash_known_vector; test_copy_detection_and_integrity_mismatch` | `evidence/final/run1/evidence/integrity/` |
| REQ-4 Alerts | console and alert log | `scenario acceptance checks` | `evidence/final/run1/logs/alerts.log` |
| REQ-5 Reports | Markdown, HTML, CSV | `test_report_generation` | `evidence/final/run1/reports/` |
| REQ-6 Required messages | nine scenarios | `tools/verify_all.py` | `evidence/final/run1/console_transcript.txt` |
| REQ-7 Workflow | monitor → classify → hash → authorize → log → report | `tests/test_core.py` | `evidence/final/run1/reports/audit_report.md` |
| REQ-8 Deliverables | DOCX, PPTX, diagrams, evidence | `structural and visual checks` | `evidence/final/run1/docs/ and evidence/final/` |
| REQ-9 Learning outcomes | walkthrough and report | `manual review` | `evidence/final/run1/docs/CODE_WALKTHROUGH.md` |

Run 1: 210 rows; events BULK=1, COPY=5, CREATE=200, DELETE=1, MODIFY=2, MOVE=1; severity CRITICAL=2, HIGH=6, INFO=202.
Acceptance: 16/16 checks.
