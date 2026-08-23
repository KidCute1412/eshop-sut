#!/usr/bin/env python3
import argparse
from datetime import datetime
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Append an HW6 AI audit entry.")
    parser.add_argument("audit_file")
    parser.add_argument("--tool", required=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--corrections", default="")
    args = parser.parse_args()

    path = Path(args.audit_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("# HW6 - AI Audit Report\n\n## Interaction Log\n\n", encoding="utf-8")

    entry = (
        f"### {datetime.now().isoformat(timespec='seconds')} - {args.task}\n\n"
        f"- Tool: {args.tool}\n"
        f"- Prompt: {args.prompt}\n"
        f"- AI Output: {args.output}\n"
        f"- Human Review / Corrections: {args.corrections or 'Pending human review'}\n\n"
    )
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"Appended audit entry to {path}")


if __name__ == "__main__":
    raise SystemExit(main())
