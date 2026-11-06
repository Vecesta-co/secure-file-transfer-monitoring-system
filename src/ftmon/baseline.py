"""Creation and persistence of the initial file-hash baseline."""
from __future__ import annotations
import json
from pathlib import Path
from .hasher import hash_file
from .policy import Policy


def create_baseline(policy: Policy, output: Path) -> dict:
    """Hash every readable file below watched folders and save its metadata."""
    result = {}
    for folder in policy.watched:
        if not folder.exists():
            continue
        for path in folder.rglob("*"):
            if not path.is_file():
                continue
            try:
                stat = path.stat()
                hashes = hash_file(path, policy.values.get("hash_algorithms", ["sha256", "md5"]))
                try:
                    key = path.resolve().relative_to(policy.root).as_posix()
                except ValueError:
                    key = str(path.resolve())
                result[key] = {**hashes, "size": stat.st_size, "mtime_ns": stat.st_mtime_ns}
            except OSError:
                continue
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result
