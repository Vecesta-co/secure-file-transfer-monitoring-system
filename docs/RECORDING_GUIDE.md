# Real screen recording guide

This repository contains rendered terminal transcripts, not a recording of the user's desktop. Record the live demo on the target computer if a real screen video is required.

## Windows

1. Open PowerShell in the project folder and activate `.venv`.
2. Start Xbox Game Bar with `Win+G` or use Snipping Tool screen recording.
3. Run `python main.py demo --clean` and keep the full terminal visible.
4. Show the nine scenario headings, the USB and integrity alerts, the 200-file R4 alert, and the report paths.
5. Stop recording after the final PASS lines and save the video under the internship submission folder.

## macOS

1. Open Terminal in the project folder and activate `.venv`.
2. Start the built-in screen capture with `Shift+Command+5` and select Record.
3. Run `python main.py demo --clean` and keep the output visible until its final summary.
4. Stop the recording and save the resulting video.

## Linux

1. Open a terminal in the project folder and activate `.venv`.
2. Use the desktop's built-in screen recorder or an installed recorder such as OBS.
3. Run `python main.py demo --clean` and show the scenario headings, required alerts, and final report paths.
4. Stop and save the recording when the process finishes.

## Suggested two-minute narration

“This project monitors configured folders and records file activity with timestamps and SHA-256 hashes. The demo data is synthetic. First, a normal document copy and an approved sensitive backup are logged. Next, I copy sensitive files into a simulated USB and cloud folder; the policy raises alerts. The next examples move a sensitive file and alter a copied file, then modify another file in place. Both integrity failures are detected by comparing hashes. A sensitive deletion is also logged. Finally, two hundred small files arrive in one directory and trigger the bulk-transfer rule. The program writes a JSONL audit log, readable alerts, and Markdown, HTML, and CSV reports. The policy can be adjusted to map folders on the target computer.”
