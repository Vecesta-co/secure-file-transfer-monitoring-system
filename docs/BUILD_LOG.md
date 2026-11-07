# Build log

## Phase 0 — Environment
- Checked Python 3.11.9 and Git 2.56.0 on Windows; initialized the local repository on `main`.
- Created a local Python environment and installed watchdog, pytest, python-docx, python-pptx, Pillow, and matplotlib. First package install encountered a transient Windows file-lock (`WinError 32`) during concurrent package setup; rerunning sequentially succeeded.
- Created the requested directory skeleton and pinned direct dependencies in `requirements.txt`.
- Result: environment ready. No external services or network features are part of the application.

## Phase 1 — Core
- Implemented chunked SHA-256/MD5 hashing, stable-size polling, path policy resolution, JSONL/alert logging, and the argparse CLI.
- Ran `python main.py hash requirements.txt`, `python main.py baseline`, and module compilation; each completed successfully. The initial baseline found zero files because the workspace had not yet been created.
- Result: core commands work.

## Phase 2 — Monitor and rules
- Added recursive watchdog monitoring, a baseline hash index, copy inference, Windows delete/create move correlation, integrity checks, rule evaluation, and thread-pool processing for event bursts.
- First demo attempts exposed delayed file events and Windows folder-delete restrictions. Cleanup now clears generated children while retaining protected project directories; monitoring waits for logged events, and the event handler batches file work. R4 uses observation time to evaluate the real burst window.
- Result: all nine scenarios fired their expected events and rules.

## Phase 3 — Reports
- Added Markdown, standalone HTML with highlighted violation rows, and CSV report generation.
- Checked generated files and report counts: 415 events, 8 violation records in each clean demo run.
- Result: report outputs generated and report test passed.

## Phase 4 — Demo
- Implemented nine synthetic scenarios and an end-to-end status check.
- Ran `python main.py demo --clean` repeatedly. The final two runs each recorded 415 events and printed all three required alert messages, including the 200-file bulk alert.
- Result: both final clean runs exited 0.

## Phase 5 — Tests
- Added seven tests covering known hashes, path policy, rule evaluation, copy and integrity detection, bulk aggregation, report output, and a polling-based watchdog test.
- Ran `python -m pytest -q` twice in a fresh local Python environment after the monitor/baseline module split: both runs passed 7 tests (3.42 and 3.40 seconds).
- Result: PASS.

## Phase 6 — Double verification
- Saved the two demo transcripts, logs, reports, and acceptance outputs under `evidence/run1/` and `evidence/run2/`.
- `tools/verify_all.py` reported 14/14 checks on each run. Alert rule IDs matched across runs: R1, R2, R3, R4, and R5.
- Saved real MATCH and MISMATCH CLI outputs and SHA-256 values under `evidence/integrity/`; rendered terminal transcripts into eight PNGs under `evidence/screenshots/`.
- Result: PASS.

## Phase 7 — Diagrams and documents
- Generated architecture and decision-flow diagrams, the project report DOCX, and an 11-slide PPTX with `tools/make_docs.py`. Re-opened both office files with python-docx/python-pptx; the DOCX contains 7 embedded images and the deck has 11 slides.
- Rendered and visually inspected all 11 PPTX slides with the bundled slide renderer. The DOCX renderer could not run because LibreOffice `soffice.exe` and `docx2pdf` are unavailable in this Windows environment. No PDF was produced.
- Result: office files load; PDF export skipped for the recorded environment limitation.

## Phase 8 — Final audit
- Replaced the direct dependency list with 22 exact pins from `pip freeze` so the full working environment can be reproduced.
- Replacing an existing local environment folder was denied by Windows (`WinError 5`); created a separate fresh environment, installed `requirements.txt`, ran the suite twice, then ran the full demo and `verify_all.py` from that environment.
- Fresh environment result: 7/7 tests on both runs, 415 demo event records, the three required alerts printed, and the acceptance checklist passed 14/14.
- Reopened the DOCX and PPTX with their Python libraries and confirmed the expected embedded images and 11 slides. PPTX slide rendering was inspected. DOCX page rendering and PDF export remain skipped because LibreOffice/Word are unavailable.
- Final repository audit found no machine-specific personal paths in source, config, reports, logs, or text evidence. Runtime baseline keys are also project-relative for files inside the root.
- Local commits were created for Phases 1–8 after their implementation groups were complete; Phase 0 was committed at environment setup.
- Result: PASS with recorded Windows folder-removal and DOCX-rendering limitations.

## Verification pass — independent audit and remediation

- Re-read the build log, decisions, commit history, repository tree, source, tests, and initial evidence. Created `docs/AUDIT_FINDINGS.md` and `docs/IMPROVEMENT_PLAN.md` before changing the code.
- Initial independent run: 7 tests passed twice; the clean demo produced 415 rows and 14/14 acceptance checks. Found incorrect first-process attribution, unstable bulk-window timing, missing demo controls, duplicate watcher notifications, and incomplete edge-case coverage.
- Fixed event attribution matching, bulk window anchoring, demo `--pace` / `--no-color` / summary, acceptance validation, stable-file polling, path privacy, and same-path callback ordering. Added Windows metadata ignore patterns and tests. Commits: `3912e16`, `d1b1b76`, `28e04f1`.
- Expanded the suite to 19 tests. The last clean demo produced 210 event rows: 200 CREATE, five COPY, two integrity MODIFY, one MOVE, one DELETE, and one BULK summary. Acceptance checks passed 16/16.
- Ran real PowerShell and `cmd.exe` file operations against a temporary watched policy. Logs flushed after Ctrl+C. OneDrive sidecar and rename noise limited classification fidelity; the limitation and exact actions are recorded in `docs/AUDIT_FINDINGS.md`.
- Independent PowerShell SHA-256 checks agreed with the integrity artifacts. The original 11-slide deck was rendered and all slides scored below 8; the report and presentation are being rebuilt from frozen evidence.
- DOCX page rendering and PDF export remain unavailable because Word and LibreOffice are absent. Cross-platform runtime checks remain unrun on this Windows host.
