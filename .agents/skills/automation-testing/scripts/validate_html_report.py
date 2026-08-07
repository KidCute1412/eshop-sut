#!/usr/bin/env python3
"""Check that a generated HTML test report contains the required 'Run by: {StudentID}' tag
together with a plausible ISO-8601 timestamp, per the assignment's anti-cheat requirement."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _common import ensure_utf8_stdio

RUN_BY_RE = re.compile(r"run\s*by\s*[:\-]?\s*", re.IGNORECASE)
ISO_TIMESTAMP_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


def find_html_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        candidates = sorted(path.rglob("*.html"))
        return candidates
    return []


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Validate an HTML report shows 'Run by: {StudentID}' + an ISO timestamp.")
    parser.add_argument("report_path", help="Path to an HTML report file, or a directory to search for one.")
    parser.add_argument("--student-id", help="If given, also require this exact string to appear near the 'Run by' tag.")
    args = parser.parse_args()

    path = Path(args.report_path)
    if not path.exists():
        print(f"ERROR: path not found: {path}", file=sys.stderr)
        return 2

    html_files = find_html_files(path)
    if not html_files:
        print(f"ERROR: no .html file found at or under {path}", file=sys.stderr)
        return 2

    errors: list[str] = []
    checked = 0
    for html_file in html_files:
        text = html_file.read_text(encoding="utf-8", errors="replace")
        run_by_match = RUN_BY_RE.search(text)
        if not run_by_match:
            # Not every .html under a report directory needs the tag (e.g. asset files);
            # only flag files that look like the actual report page.
            if html_file.name.lower() in ("index.html",) or "report" in html_file.name.lower():
                errors.append(f"{html_file}: missing a 'Run by' tag")
            continue

        checked += 1
        window = text[run_by_match.end(): run_by_match.end() + 200]
        if args.student_id and args.student_id not in window:
            errors.append(f"{html_file}: 'Run by' tag found but student ID '{args.student_id}' not found nearby")
        if not ISO_TIMESTAMP_RE.search(window) and not ISO_TIMESTAMP_RE.search(text):
            errors.append(f"{html_file}: 'Run by' tag found but no ISO-8601 timestamp (YYYY-MM-DDTHH:MM:SS) found in the report")

    if checked == 0:
        errors.append(f"{path}: no report-like HTML file (index.html or *report*.html) contained a 'Run by' tag at all")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Validation passed: {checked} report file(s) show a 'Run by' tag with an ISO timestamp.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
