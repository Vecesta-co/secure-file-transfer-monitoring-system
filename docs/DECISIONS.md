# Decisions

- **Runtime and evidence:** Python 3.11 on Windows is the available build environment. Cross-platform behavior is implemented with pathlib and watchdog, but this session can directly verify Windows only.
- **Demo timing:** the automatic demo uses brief polling-based waits for filesystem notifications; scenarios are deterministic and all demo content is synthetic.
- **Optional process attribution:** `psutil` is not installed. The monitor records `unknown` as permitted by the brief.
- **PDF export:** no LibreOffice/soffice executable is available; the DOCX is delivered without PDF.
- **Draw.io:** diagrams will be delivered as PNG; draw.io XML is omitted if the straightforward flowchart cannot be represented cleanly, and documented here.
- **Authorization:** empty `authorized_users` means local users are treated as authorized. A sensitive transfer to an explicitly approved destination is recorded as `Authorized transfer`.
- **Local Git identity:** Git had no configured author identity; repository-local commits use Project Intern <project-intern@localhost> and do not modify global Git settings.
