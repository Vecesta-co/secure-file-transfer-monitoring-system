# Fresh-clone verification

- Source commit cloned: `d577902510c8c7cd1331acb335dd21d9818b843c`.
- Method: `git clone . "$env:TEMP\ftmon_clone_test"`.
- Environment: Python 3.11.9; created `.venv_check` in the clone and installed the 22 exact pins from `requirements.txt` (pip exit 0).
- Tests: `.venv_check\Scripts\python.exe -m pytest -q` — exit 0, 20 passed in 19.84s.
- Demo: `python main.py demo --clean --no-color` — exit 0; 210 events; required USB, integrity-mismatch, and exact 200-file R4 alerts appeared.
- Acceptance: `python tools/verify_all.py` — exit 0, 16/16 checks passed.
- Raw outputs and generated clone logs/reports are stored beside this note.
- Cleanup was attempted after capture. Windows denied recursive removal (WinError 5 / automatic command policy); the temporary clone remains outside the project workspace and is not part of the Git repository.
