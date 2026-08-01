#!/usr/bin/env python3
"""Export a gui-usability checklist.md table to CSV for the required Excel deliverable."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

from _table_utils import ensure_utf8_stdio, parse_table

HEADER = [
    "No.",
    "Type",
    "Checkpoint",
    "IA",
    "Requirement / Heuristic Reference",
    "Platform",
    "Source",
    "AI-Miss Reason",
    "Yes",
    "No",
    "Remarks",
    "Evidence",
    "Bug ID",
]


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Convert checklist.md into a CSV file (open in Excel).")
    parser.add_argument("--input", required=True, help="Path to checklist.md.")
    parser.add_argument("--output", required=True, help="Path to write the CSV file.")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.is_file():
        print(f"ERROR: input file not found: {input_path}", file=sys.stderr)
        return 2

    rows = parse_table(input_path.read_text(encoding="utf-8"), HEADER)
    if not rows:
        print(f"ERROR: zero checklist rows parsed from {input_path}", file=sys.stderr)
        return 2

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} row(s) to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
