# Audit findings

Audit date: 2026-11-06 (Windows 11, Python 3.11.9). Commands ran from the project directory whose parent path contains spaces and parentheses and is synchronized by OneDrive. Results below distinguish the initial audit from post-fix verification.

## Stage 1 summary

| Area | Status | Result |
|---|---|---|
| REQ-1 event logging | PARTIAL | Event schema and core file changes work. Process attribution was always `unknown`; OS-level open/read events are not implemented. |
| REQ-2 movement and access policy | PARTIAL | R1/R2/R5 work in the demo. R6 is covered by a policy/unit path; real open/read access is not observed. |
| REQ-3 SHA-256 integrity | PASS | MATCH and MISMATCH outputs are correct; five independent file hashes agree with the evidence values. |
| REQ-4 console and file alerts | PASS | Required USB, integrity, bulk alerts appear in the console and `logs/alerts.log`. |
| REQ-5 audit logs and reports | PASS | JSONL event log and Markdown, HTML, CSV reports are generated and readable. |
| REQ-6 three required examples | PASS | All three exact messages occur in the clean demo output. |
| REQ-7 workflow branches | PARTIAL | Classification, hashing, authorization evaluation, logging, alerts, and reports exist. Windows open/read access cannot drive the access branch. |
| REQ-8 deliverables | PARTIAL | Toolkit, DOCX, PPTX, screenshots, and PNG diagrams exist. DOCX/PDF visual output was unavailable; editable draw.io files were missing; the original deck was weak. |
| REQ-9 learning outcomes | PARTIAL | The walkthrough gives a useful module outline but does not yet explain DLP, transfers, hashing, and auditing in enough beginner detail. |
| Clean demo and 9 scenario records | PASS | Post-fix run: all nine scenarios verified against event type, paths, rule, severity, integrity, sensitivity, zone, and exact alert. See `evidence/final/run1/`. |
| R4 aggregation window | PASS | A fixed 60-second demo window produced one R4 event and the real count of 200. A separate short-window test confirms a single alert per configured window. |
| Scenario 1/2 false positives | PASS | Normal copy and approved backup are INFO/R0 and produce no HIGH/CRITICAL alert. Acceptance check covers both. |
| Independent hash check | PASS | PowerShell `Get-FileHash -Algorithm SHA256` checked the five `.txt` files in `evidence/integrity/`; project SHA-256 values match for original, correct copy, and altered copy. |
| Real Windows commands | PARTIAL | Ran PowerShell `Copy-Item`, `Move-Item`, `Set-Content`, `Add-Content`, `Remove-Item`, plus `cmd.exe copy` and `move`. The watcher logged changes and shut down on Ctrl+C, but OneDrive generated `desktop.ini` events and some rename notifications were misclassified. See the detailed note below. |
| Edge cases | PASS | Unit checks cover Unicode, spaces, parentheses, empty/50 MiB files, a file being written, nested/missing paths, Windows drive/UNC/case-insensitive zones, fast distinct edits, and authorization decisions. |
| Process attribution | PARTIAL | All 210 final demo records show `unknown`. The original psutil loop attributed the first unrelated process. It now matches the opened file path; psutil is absent here, so positive attribution remains unverified. |
| Path privacy | PASS | Project paths are relative; configured external paths are represented with zone labels. No personal path appears in final event logs, report files, or office document text. |
| Tests, initial audit | FAIL | Initial suite had 7 tests. It passed twice (3.44s and 3.42s) but did not test file-write ordering, rapid distinct writes, process matching, large files, path privacy, or a slow burst window. |
| Tests, post-fix | PASS | Final suite has 20 tests; both final runs passed. |
| Sabotage verification | PASS | Three deliberate code faults each caused the target regression test to fail, then source files were restored. Negative acceptance input exits nonzero. Details in `evidence/final/sabotage/`. |
| README / CLI | PASS | Quick start and CLI reference were rewritten; `main.py --help` and subcommand help were checked against the reference. |
| DOCX | PARTIAL | Original file opened with python-docx: 12 headings, 1 table, 7 images, 1 section, no TODO/lorem/XXX/undefined text. Original report was too short and lacked TOC, fields, chapter pagination, and live evidence values. Final page rendering remains unavailable because LibreOffice and Word are not installed. |
| PPTX | FAIL | Original 11-slide deck rendered and visually inspected. It used a light template, had no notes or charts, and rasterized the diagrams. Per-slide baseline scores were all below 8. |
| Diagrams | PARTIAL | Original architecture and flowchart PNGs existed; flow had Yes/No labels, but 180 dpi was below the requested 200 dpi and dark palette. No `.drawio` files existed. |
| Repo hygiene | PASS | No venv, cache, or demo workspace is tracked; `requirements.txt` and MIT license exist; no tracked file exceeds 10 MB. Fresh clone is part of final verification. |
| Recording guide | PARTIAL | It incorrectly implied Snipping Tool was a screen recorder and omitted the Xbox Game Bar shortcut details and a complete two-minute script. |

## Commands and observed results

| Check | Command / method | Result |
|---|---|---|
| Initial tests | `python -m pytest -q` twice | Both passed 7 tests. The original suite did not cover the edge cases listed above. |
| Initial clean demo | `python main.py demo --clean` | Exit 0; 415 event records, 11 rule alert lines, required three messages. |
| Initial acceptance | `python tools/verify_all.py` twice | 14/14 on both runs. |
| Final clean demo | `python main.py demo --clean --no-color` | Exit 0; 210 event rows: CREATE=200, COPY=5, MODIFY=2, MOVE=1, DELETE=1, BULK=1. Severity totals: INFO=202, HIGH=6, CRITICAL=2. |
| Final acceptance | `python tools/verify_all.py` | 16/16, including required fields, no control false positives, and exactly one R4 with count 200. |
| Independent hash | `Get-FileHash -Algorithm SHA256 -LiteralPath <file>` for `original.txt`, `correct_copy.txt`, `altered_copy.txt`, `verify_match.txt`, `verify_mismatch.txt` | Three report-listed hashes match exactly: original/correct copy `6ce3452e9266c630f079baaa8a4f0f18576c11bc1857a94b4da5ee7a70af0118`; altered copy `71f06f874c7584504ea350174c5eae3c193136f9f947cf5e00cd19c4f3cc0157`. The verify transcript files were also independently hashed and recorded. |
| Windows-style path policy | Load `config/policy.real-world.example.json`; classify `e:/AuditCase/file.key`, mixed-case OneDrive path, and mixed-case UNC path | Loaded without error; zones were USB, CLOUD, and NETWORK_SHARE. Missing configured watched path returned safely. |
| CLI reference | `python main.py --help` | Commands: baseline, monitor, report, verify, hash, demo. Demo help also exposes `--clean`, `--pace SECONDS`, and `--no-color`. |
| Office structure | python-docx and python-pptx inspection | Original DOCX structure and old deck counts are recorded above. The original PPTX had 11 slides, 4 pictures, 0 charts, 0 notes. |
| DOCX render / PDF | Bundled `render_docx.py`; `where.exe soffice` | SKIPPED: renderer reports missing LibreOffice; `soffice` not found, and Word is not installed. |

## Scenario review

The final scenario-specific checks inspect the record, not only the summary count:

| Scenario | Expected record | Post-fix observation |
|---|---|---|
| 1. Normal copy | COPY, R0, INFO, internal destination, not sensitive | Pass; no HIGH/CRITICAL rule. |
| 2. Approved sensitive backup | COPY, R0, INFO, ALLOWED destination, sensitive | Pass; message `Authorized transfer`, no HIGH/CRITICAL rule. |
| 3. USB copy | COPY, R1/R2, HIGH, integrity OK, sensitive, USB | Pass; both rule messages appear. |
| 4. Cloud copy | COPY, R1/R2, HIGH, integrity OK, sensitive, CLOUD | Pass. |
| 5. Move | MOVE, R1, HIGH, integrity OK, sensitive, UNKNOWN | Pass. |
| 6. Altered share copy | COPY to NETWORK_SHARE, followed by MODIFY/R3/CRITICAL/MISMATCH | Pass after event-order fix; one copy record and one integrity finding. |
| 7. In-place tamper | MODIFY/R3/CRITICAL/MISMATCH | Pass. |
| 8. Delete | DELETE/R5/HIGH/sensitive | Pass. |
| 9. Bulk transfer | 200 CREATE records and one BULK/R4/HIGH with exact count | Pass. |

Initial 415-event totals included 207 MODIFY rows, most from first-write and duplicate OneDrive/watchdog notifications. Per-path serialization, first-observation classification, and content-hash checks removed that noise. The final 210-row composition is the scenario activity above, with the two deliberate integrity changes retained.

## Real Windows operation note

The watcher was started with `python main.py monitor --policy evidence\real_os\policy.json`. Files were then copied and moved with PowerShell and `cmd.exe`, written with `Set-Content`/`Add-Content`, and deleted with `Remove-Item`; Ctrl+C printed `Monitoring stopped.` and flushed logs. The project path itself includes spaces and parentheses. This run is PARTIAL because OneDrive created sidecar metadata while the test folders were watched, and the paired rename events included same-path/misclassified records. Default and example policy now ignore `desktop.ini`; the project remains a path-based monitor and Windows sync software can still add event noise. No real USB hardware or cloud service was used.

## Original presentation visual scores

Scores are the baseline inspection of the 11 rendered original slides, before redesign. Criteria considered hierarchy, alignment, spacing, contrast, consistency, visual interest, and overflow.

| Slide | Baseline score / 10 | Main reason |
|---:|---:|---|
| 1 | 4 | Plain white cover, little hierarchy or visual identity. |
| 2 | 4 | Sparse text without a visual problem model. |
| 3 | 4 | Limitations and conclusion are crowded into one weakly structured slide. |
| 4 | 4 | Problem statement is text-only. |
| 5 | 4 | Objectives lack visual grouping and implementation evidence. |
| 6 | 3 | Architecture is a small raster image instead of editable shapes. |
| 7 | 3 | Flowchart is a small raster image with tiny labels. |
| 8 | 4 | Rules are compressed into four text lines. |
| 9 | 4 | Scenarios are a text list with no timeline. |
| 10 | 3 | Results screenshot is tiny and the slide has no native chart. |
| 11 | 4 | Integrity screenshot text is too small to read at presentation size. |

The rendered contact sheet used for this inspection is an intermediate audit artifact; the final deck receives a fresh render, individual slide scores, and a contact sheet under `docs/ppt_preview/`.


## Final post-remediation verification

This section supersedes the earlier baseline notes where they say document rendering, draw.io files, or the redesigned deck are unavailable. Those earlier entries describe the initial audit state and are retained to show what was fixed.

| Area | Final status | Final evidence |
|---|---|---|
| Application behavior | PASS | `python main.py demo --clean --no-color` run twice; both exit 0 and record 210 events with the same event mix. |
| Automated tests | PASS | Fresh local environment; `python -m pytest -q` twice: 20 passed in 19.23s and 20 passed in 13.62s. Outputs: `evidence/final/pytest_run1.txt`, `pytest_run2.txt`. |
| Acceptance checks | PASS | `python tools/verify_all.py` returned 16/16 for each clean demo. Both raw logs and reports are captured under `evidence/final/run1/` and `run2/`. |
| Required alert examples | PASS | Final console and alert logs contain USB, hash-mismatch, and one R4 alert stating 200 files. The final run has 11 alert lines; R4 is one summary. |
| Report and artifacts | PASS | README, traceability, double-run summary, DOCX, PPTX, and screenshot inputs regenerated from the two frozen runs by `tools/make_docs.py`. |
| DOCX/PDF rendering | PASS | Word COM refreshed fields and TOC, exported `docs/Project_Report.pdf`; Poppler reported 20 letter pages. All page images are in `evidence/final/docx_render_final/`; contact sheet inspected. A table previously split across pages was removed; chapter starts now use page-break-before. |
| Presentation | PASS | Rendered all 15 final slides into `docs/ppt_preview/` and inspected the contact sheet plus alert/hash slides individually. Deck structure: 15 slides, speaker notes on all 15, 3 terminal screenshots with alt text, and 1 native chart. All programmatic bounds/font/body-text checks in the generator passed. |
| Slide scores | PASS | Hierarchy, alignment, spacing, contrast, consistency, visual interest, and overflow were reviewed. Every slide scores at least 8/10 (table below). |
| Diagrams | PASS | `tools/make_docs.py` generated matching 300-dpi PNGs and editable architecture/flowchart `.drawio` XML. Generator parses the XML. Flow diagram shows Yes/No branches. |
| Windows path and OS checks | PARTIAL | Windows drive, UNC, case-insensitive zones and path-with-spaces work in unit coverage. Real PowerShell and `cmd.exe` operations were observed and logs flushed on Ctrl+C, but OneDrive rename/sidecar events reduced classification fidelity; no real hardware or cloud service was used. |
| Process attribution | PARTIAL | All 210 final demo rows show `unknown` because psutil is unavailable in this environment. Matching logic is best-effort and documented. |
| Privacy scan | PASS | Final repository text and Office XML scan found no absolute personal paths; the temporary real-OS policy containing a local path was removed before commit. Example policy paths use the explicit placeholder `YourName`. OneDrive synchronized folders carry a ReadOnly/ReparsePoint attribute and deny delete-subdirectories; empty directories from the old OS probe and old preview images remain on disk but are ignored by Git. |
| Fresh clone | PENDING | Clone the final commit, install pinned requirements in a new environment, run tests/demo/acceptance, and record results in `evidence/final/clone_check.md`. |
| Git hygiene | PENDING | Check after the clone run, final commit, and tag. |

### Final slide scores

| Slide | Score / 10 | Review note |
|---:|---:|---|
| 1 | 9 | Clear identity and abstract network motif; identity placeholders are intentional. |
| 2 | 8 | Four threat cards are aligned and differentiated by severity color. |
| 3 | 9 | Five objectives form a consistent, readable card grid. |
| 4 | 9 | Six-step pipeline has strong sequence and spacing. |
| 5 | 9 | Editable module architecture is balanced and legible. |
| 6 | 8 | Decision branches and Yes/No labels are visible; diagram is information-dense. |
| 7 | 9 | Rule cards use consistent severity cues and concise conditions. |
| 8 | 9 | Copy-detection sequence is clear and visually ordered. |
| 9 | 8 | Nine outcomes fit the timeline grid; labels are concise. |
| 10 | 9 | Run-derived metrics and native bar chart share a clear hierarchy. |
| 11 | 8 | Real console captures show the three required alerts; fine log paths are small at overview scale. |
| 12 | 8 | Match and mismatch hashes are side by side; long strings wrap but remain legible at full slide size. |
| 13 | 9 | Repeat-run evidence is summarized cleanly with a traceability link. |
| 14 | 9 | Limitations and future work are separated and honest. |
| 15 | 8 | Three takeaways and Q&A close the story with sufficient whitespace. |

### Final run comparison

Both demos recorded 210 rows: CREATE=200, COPY=5, MODIFY=2, MOVE=1, DELETE=1, BULK=1. Severity totals were INFO=202, HIGH=6, CRITICAL=2. Each acceptance report passed 16/16. The generated report uses the final logs rather than manually entered totals. Run-specific test timings are recorded in the raw pytest transcripts.
