"""CLI entry point for the Secure File Transfer Monitoring System."""
from __future__ import annotations
import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from ftmon.hasher import hash_file  # noqa: E402
from ftmon.baseline import create_baseline  # noqa: E402
from ftmon.policy import DEFAULT_POLICY, load_policy  # noqa: E402


def run_demo(clean: bool = True, pace: float = 0, color: bool = True) -> int:
    from demo.run_demo import run
    return run(clean=clean, pace=pace, color=color)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Secure File Transfer Monitoring System")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("baseline", "monitor", "report"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--policy", default=str(DEFAULT_POLICY))
    verify = sub.add_parser("verify"); verify.add_argument("source_file"); verify.add_argument("copied_file")
    hashing = sub.add_parser("hash"); hashing.add_argument("file")
    demo = sub.add_parser("demo")
    demo.add_argument("--clean", action="store_true", help="start from a clean demo state (default behavior)")
    demo.add_argument("--pace", type=float, default=0, metavar="SECONDS", help="pause between scenario starts")
    demo.add_argument("--no-color", action="store_true", help="disable ANSI console colors")
    args = parser.parse_args(argv)
    if args.command == "hash":
        try:
            hashes = hash_file(args.file, ["sha256", "md5"])
            for key, value in hashes.items(): print(f"{key.upper()}: {value}")
            return 0
        except OSError as exc:
            print(f"ERROR: {exc}", file=sys.stderr); return 2
    if args.command == "verify":
        try:
            a, b = hash_file(args.source_file, ["sha256"])["sha256"], hash_file(args.copied_file, ["sha256"])["sha256"]
            print(f"Source SHA-256: {a}\nCopy SHA-256:   {b}")
            match = a == b; print("MATCH" if match else "MISMATCH"); return 0 if match else 1
        except OSError as exc:
            print(f"ERROR: {exc}", file=sys.stderr); return 2
    if args.command == "demo":
        if args.pace < 0:
            parser.error("--pace must be zero or greater")
        return run_demo(clean=True, pace=args.pace, color=not args.no_color)
    policy = load_policy(args.policy)
    if args.command == "baseline":
        output = ROOT / "data" / "baseline.json"
        result = create_baseline(policy, output)
        print(f"Baseline saved: {output} ({len(result)} files)"); return 0
    if args.command == "monitor":
        from ftmon.monitor import TransferMonitor
        monitor = TransferMonitor(policy, ROOT)
        monitor.start(); print("Monitoring. Press Ctrl+C to stop.")
        try:
            while True: time.sleep(1)
        except KeyboardInterrupt:
            monitor.stop(); print("Monitoring stopped.")
        return 0
    if args.command == "report":
        from ftmon.report import generate_report
        print(json.dumps(generate_report(ROOT), indent=2)); return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
