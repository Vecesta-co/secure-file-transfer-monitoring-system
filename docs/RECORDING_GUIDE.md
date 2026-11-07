# Windows screen recording guide

Use a real screen recording for the submission video. The PNG files in `evidence/screenshots/` are rendered from terminal transcripts and are supporting images, not a recording of your desktop.

## Prepare the recording

1. Open PowerShell in the project folder and activate the Python environment you created for this project.
2. Set the terminal to a readable size and font. Keep the project path, command, and complete output visible.
3. Open Xbox Game Bar with **Win+G**. In Settings, confirm that the capture shortcut is enabled.
4. Start recording with **Win+Alt+R**. A small capture indicator should appear.
5. Run `python main.py demo --clean --pace 3`. The three-second pauses give time to read each scenario header.
6. Keep the USB, integrity, bulk alerts, final summary, and report paths on screen. Stop with **Win+Alt+R** and save the MP4 in the submission folder.

**Win+Shift+S takes a screenshot. It does not record video.** Use Snipping Tool's separate **Record** control if available on the installed Windows version. If Game Bar cannot capture the terminal or the recording shortcut is disabled, install OBS Studio, choose **Display Capture**, confirm the preview includes the terminal, then start and stop with OBS controls.

## What to show

- The project folder and the demo command.
- Scenario 1 and 2 as safe INFO controls.
- The sensitive USB and cloud transfer alerts.
- The altered-copy and in-place integrity failures.
- The deletion alert and the one 200-file bulk summary.
- The final event/severity summary and generated report paths.
- Optionally, open `reports/audit_report.md` and show the event log.

Do not show real personal or confidential files. The demo workspace uses synthetic data.

## Two-minute narration

“This project is a local file transfer monitoring demonstration. It watches folders configured in a JSON policy and writes a timestamped event log. The first two scenarios are controls: a normal document copy and an approved sensitive backup. Both should remain informational. The next examples send dummy sensitive files into simulated USB and cloud folders, then move a file to an unknown directory. The monitor applies path rules and writes alerts. Next, I alter a copied file and change another file in place. SHA-256 comparisons detect both mismatches. The next case deletes a sensitive file. Finally, two hundred small files arrive in one destination and the bulk rule creates one summary alert. The final output shows the event totals and report files. This tool detects and records; it does not block transfers or inspect network traffic. USB, cloud, and share zones are configured paths, and the process field may show unknown. The report and presentation include the tests, evidence, and limits.”

## Other operating systems

- **macOS:** use the built-in screen capture controls opened with **Shift+Command+5**, then choose a recording region.
- **Linux:** use the desktop recorder or OBS Studio and keep the terminal and final summary visible.
