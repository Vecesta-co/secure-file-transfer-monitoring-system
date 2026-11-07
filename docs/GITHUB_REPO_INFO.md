# GitHub repository setup

- **Repository name:** `secure-file-transfer-monitoring-system`
- **Description:** A Python file-system monitoring demo with path-based DLP rules, SHA-256 integrity checks, alerts, and audit reports.
- **Topics:** `python`, `cybersecurity`, `blue-team`, `data-loss-prevention`, `file-integrity`, `audit-logging`, `watchdog`
- **Visibility:** Public (`Vecesta-co/secure-file-transfer-monitoring-system`).

Create an empty GitHub repository with the suggested name. From this local project folder, run the commands below and replace the sample account with your GitHub username or organization:

```powershell
git remote add origin https://github.com/<YOUR-ACCOUNT>/secure-file-transfer-monitor.git
git remote -v
git push -u origin main
git push origin v1.0.0
```

The tag should point to the final local commit. Do not add virtual-environment folders, caches, demo workspace files, or real monitored data to the remote.
