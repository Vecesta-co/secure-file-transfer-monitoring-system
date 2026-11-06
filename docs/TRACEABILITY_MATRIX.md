# Traceability matrix

| Objective | Feature | Test(s) | Evidence |
|---|---|---|---|
| File transfer logging | Watchdog event classification and JSONL writer | `test_watchdog_end_to_end_with_polling`, `test_copy_detection_and_integrity_mismatch` | `evidence/run1/logs/file_events.jsonl`, `evidence/run1/verify_all.txt` |
| Unauthorized movement detection | Policy zones and R1/R2/R5/R6 evaluation | `test_policy_rules_integrity_and_access`, `test_policy_sensitive_zone_and_authorization` | `evidence/run1/logs/alerts.log`, `evidence/run1/verify_all.txt` |
| File integrity checks | Stable SHA-256/MD5 hashes and modification comparisons | `test_hash_known_vector`, `test_copy_detection_and_integrity_mismatch` | `evidence/integrity/`, `evidence/run1/logs/file_events.jsonl` |
| Reporting and alerting | Thread-safe alerts plus Markdown, HTML, CSV outputs | `test_report_generation` | `evidence/run1/reports/`, `evidence/run1/logs/alerts.log` |
| Demonstration / acceptance | Nine synthetic scenarios and checklist tool | `test_watchdog_end_to_end_with_polling`, full demo | `evidence/run1/console_transcript.txt`, `evidence/run1/verify_all.txt` |

The evidence directories contain the two clean demo runs, their separate 14/14 verification checklists, and a fresh-environment verification. The test transcript files record the two final test executions.
