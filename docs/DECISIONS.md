# Decisions

- **Runtime and evidence:** Python 3.11 on Windows is the available build environment. Cross-platform behavior is implemented with pathlib and watchdog, but this session can directly verify Windows only.
- **Demo timing:** the automatic demo uses brief polling-based waits for filesystem notifications; scenarios are deterministic and all demo content is synthetic.
- **Optional process attribution:** `psutil` is not installed. The monitor records `unknown` as permitted by the brief.
- **PDF and DOCX rendering:** no LibreOffice `soffice.exe`, `docx2pdf`, or Word executable is available. PDF export and visual DOCX rendering were skipped. The DOCX was re-opened and checked with python-docx; the PPTX was rendered and visually inspected.
- **Draw.io:** draw.io XML is omitted; the architecture and flowchart are repeatable PNG outputs from `tools/make_docs.py`.
- **Path privacy:** paths inside the project root are logged relative to that root, keeping machine-specific user paths out of evidence. Configured paths outside the root remain absolute at runtime.
- **Windows move events:** this watchdog backend reports some renames as delete/create pairs. A brief delete delay correlates the pair so the event is recorded as MOVE rather than DELETE plus CREATE.
- **Fresh environment test:** Windows denied `python -m venv --clear .venv` while trying to remove `.venv\Include`; a newly created `.venv_fresh` installed the pinned requirements and was used for the clean-install verification instead.
- **Authorization:** empty `authorized_users` means local users are treated as authorized. A sensitive transfer to an explicitly approved destination is recorded as `Authorized transfer`.
- **Local Git identity:** Git had no configured author identity; repository-local commits use Project Intern <project-intern@localhost> and do not modify global Git settings.
