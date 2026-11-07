# Design decisions

- **Runtime:** Python 3.11 on Windows is the available verification platform. Paths use pathlib and monitoring uses watchdog; other systems still need direct checks.
- **Evidence:** The demo uses synthetic dummy data and local JSONL, alert, report, screenshot, and office files. Final totals are derived from the frozen run folders.
- **Monitoring scope:** The project records observed file changes; it does not block activity or inspect network protocols. USB, cloud, and network-share labels come from configured folders.
- **Stable hashing:** Files are read in chunks after three equal-size polls. This reduces the chance of hashing during a write; it cannot guarantee stability against every writer or filesystem.
- **Process attribution:** psutil is optional. The monitor only returns a process whose reported open-file path matches the event path. When that data is absent it records `unknown`.
- **Bulk rule:** Each destination uses a fixed window anchored at its first event. The synthetic policy uses a 60-second window so all 200 demo writes produce one accurate summary in the OneDrive environment.
- **Windows notifications:** Rename operations can arrive as delete/create pairs. A short correlation delay joins likely pairs; sync tools can still add metadata or rename noise.
- **Path privacy:** Paths inside the project are relative. External configured paths are logged relative to a named zone or watched root where possible.
- **Authorization:** An empty `authorized_users` list allows the local user. A non-empty list allows only listed usernames. Windows open/read access is not monitored, so R6 applies to events the watcher observes.
- **Office rendering:** DOCX visual rendering and PDF export were skipped because Word and LibreOffice are not installed. The generated PPTX is rendered with the bundled presentation renderer.
- **Draw.io:** Editable `.drawio` mxfile diagrams are generated alongside the high-resolution PNGs and checked as XML.
- **Git identity:** Repository-local commits use `Project Intern <project-intern@localhost>`; global Git settings were not modified.


## Final verification and presentation decisions
- Generate report and presentation facts from the two captured final runs. Keep historical audit findings labeled as baseline, with the final post-remediation table taking precedence.
- Use Word's page-break-before heading setting and omit the redundant six-row workflow table; the text and flowchart already describe that process, and the table had split onto a nearly empty page.
- Keep the PDF alongside the DOCX because Microsoft Word is installed and the final report has been exported and visually checked here.
- Retain honest limitations: simulated USB/cloud zones, no blocking, no reliable open/read audit, and best-effort process attribution.
