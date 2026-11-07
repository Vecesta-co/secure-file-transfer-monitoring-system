# Double-run verification summary

- Run 1 rows: 210.
- Run 2 rows: 210.
- Run 1 event types: BULK=1, COPY=5, CREATE=200, DELETE=1, MODIFY=2, MOVE=1.
- Run 2 event types: BULK=1, COPY=5, CREATE=200, DELETE=1, MODIFY=2, MOVE=1.
- Run 1 severity: CRITICAL=2, HIGH=6, INFO=202.
- Run 2 severity: CRITICAL=2, HIGH=6, INFO=202.
- Event and severity totals match: yes.
- Run 1 acceptance: 16/16 checks.
- Run 2 acceptance: 16/16 checks.

| Run | Rule IDs | Alert messages |
|---|---|---|
| 1 | R1, R2, R3, R4, R5 | Integrity Failure: File hash mismatch detected; Sensitive file copied to USB drive; Sensitive file copied to cloud folder; Sensitive file copied to network share; Sensitive file deleted; Sensitive file moved outside approved location; Suspicious movement: 200 files transferred to unknown directory |
| 2 | R1, R2, R3, R4, R5 | Integrity Failure: File hash mismatch detected; Sensitive file copied to USB drive; Sensitive file copied to cloud folder; Sensitive file copied to network share; Sensitive file deleted; Sensitive file moved outside approved location; Suspicious movement: 200 files transferred to unknown directory |
