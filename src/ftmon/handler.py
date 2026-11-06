"""Thin watchdog adapter that submits filesystem notifications to the monitor."""
from __future__ import annotations
import time
from pathlib import Path
from watchdog.events import FileSystemEventHandler


class MonitorHandler(FileSystemEventHandler):
    """Hand file-level notifications to the monitor without blocking watchdog."""
    def __init__(self, monitor):
        self.monitor = monitor

    def on_created(self, event):
        if not event.is_directory:
            self.monitor.executor.submit(self.monitor._handle, "CREATE", Path(event.src_path), None, time.monotonic())

    def on_modified(self, event):
        if not event.is_directory:
            self.monitor.executor.submit(self.monitor._handle, "MODIFY", Path(event.src_path), None, time.monotonic())

    def on_deleted(self, event):
        if not event.is_directory:
            self.monitor._queue_delete(Path(event.src_path))

    def on_moved(self, event):
        if not event.is_directory:
            self.monitor.executor.submit(self.monitor._handle, "MOVE", Path(event.src_path), Path(event.dest_path), time.monotonic())
