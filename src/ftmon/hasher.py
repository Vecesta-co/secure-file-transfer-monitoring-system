"""Stable-file hashing helpers."""
from __future__ import annotations
import hashlib
import time
from pathlib import Path


def wait_until_stable(path: Path, timeout: float = 3.0) -> bool:
    """Wait for a file's size to remain unchanged for two polls."""
    deadline, previous, stable = time.monotonic() + timeout, None, 0
    while time.monotonic() < deadline:
        try:
            size = path.stat().st_size
        except (PermissionError, FileNotFoundError):
            time.sleep(0.2)
            continue
        stable = stable + 1 if size == previous else 0
        if stable >= 1:
            return True
        previous = size
        time.sleep(0.2)
    return False


def hash_file(path: str | Path, algorithms: list[str] | None = None) -> dict[str, str]:
    """Hash a file in chunks, retrying transient access and disappearance errors."""
    file_path = Path(path)
    names = algorithms or ["sha256"]
    for attempt in range(4):
        try:
            wait_until_stable(file_path)
            digests = {name.lower(): hashlib.new(name.lower()) for name in names}
            with file_path.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    for digest in digests.values():
                        digest.update(chunk)
            return {name: digest.hexdigest() for name, digest in digests.items()}
        except (PermissionError, FileNotFoundError):
            if attempt == 3:
                raise
            time.sleep(0.2)
    raise OSError(f"Unable to hash {file_path}")
