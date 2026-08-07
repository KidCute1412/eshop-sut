#!/usr/bin/env python3
"""Compute the real test-summary numbers (features, test cases automated/executed/passed/failed,
browser runs, bugs) across HW04 feature workspaces, for the submission README.md. Never hand-type
different numbers than what this script actually counts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from _common import ensure_utf8_stdio

AUTOMATABLE_ROW_RE = re.compile(r"^\|.*\|\s*Yes\s*\|[^|]*\|\s*$", re.MULTILINE)
BUG_HEADER_RE = re.compile(r"^## BUG-", re.MULTILINE)


def count_automated_cases(test_cases_md: Path) -> int:
    if not test_cases_md.is_file():
        return 0
    text = test_cases_md.read_text(encoding="utf-8", errors="replace")
    # Only look inside the main table (before "## Not Automated"), and only count rows whose
    # Automatable column (second-to-last cell) is exactly "Yes".
    main_section = text.split("## Not Automated", 1)[0]
    count = 0
    for line in main_section.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        if cells[-2].strip().lower() == "yes":
            count += 1
    return count


def count_bugs(bug_report_md: Path) -> int:
    if not bug_report_md.is_file():
        return 0
    text = bug_report_md.read_text(encoding="utf-8", errors="replace")
    if "No confirmed bugs recorded" in text and not BUG_HEADER_RE.search(text.replace("No confirmed bugs recorded", "")):
        return 0
    return len(BUG_HEADER_RE.findall(text))


def read_playwright_json_stats(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    stats = data.get("stats")
    if not isinstance(stats, dict):
        return None
    return stats


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Compute real HW04 test-summary numbers across feature workspaces.")
    parser.add_argument("--feature-dir", action="append", required=True, dest="feature_dirs",
                         help="A feature workspace directory (contains test-cases.md, bug-report.md, reports/). Repeatable.")
    args = parser.parse_args()

    total_automated = 0
    total_executed = 0
    total_passed = 0
    total_failed = 0
    total_browser_runs = 0
    total_bugs = 0

    for raw_dir in args.feature_dirs:
        feature_dir = Path(raw_dir)
        if not feature_dir.is_dir():
            print(f"WARNING: not a directory, skipping: {feature_dir}", file=sys.stderr)
            continue

        total_automated += count_automated_cases(feature_dir / "test-cases.md")
        total_bugs += count_bugs(feature_dir / "bug-report.md")

        reports_dir = feature_dir / "reports"
        if reports_dir.is_dir():
            for json_file in reports_dir.rglob("*.json"):
                stats = read_playwright_json_stats(json_file)
                if stats is None:
                    continue
                total_browser_runs += 1
                expected = int(stats.get("expected", 0))
                unexpected = int(stats.get("unexpected", 0))
                flaky = int(stats.get("flaky", 0))
                skipped = int(stats.get("skipped", 0))
                total_passed += expected
                total_failed += unexpected
                total_executed += expected + unexpected + flaky + skipped

    print(f"Features: {len(args.feature_dirs)}")
    print(f"Test cases automated: {total_automated}")
    print(f"Test cases executed: {total_executed}")
    print(f"Test cases passed: {total_passed}")
    print(f"Test cases failed: {total_failed}")
    print(f"Browser runs (JSON reports found): {total_browser_runs}")
    print(f"Bugs confirmed: {total_bugs}")

    if total_browser_runs < 9:
        print(f"\nNOTE: fewer than 9 browser runs found ({total_browser_runs}) -- the assignment "
              "requires each of the 3 features run on all 3 browsers (>= 9 total). Run "
              "`npx playwright test --reporter=json` per browser and pass each results.json here "
              "via --feature-dir's reports/ subfolder if this looks low.", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
