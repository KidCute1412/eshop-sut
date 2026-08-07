#!/usr/bin/env python3
"""Scaffold one feature's HW04 automation workspace: test-cases.md, ai-gap-analysis.md,
bug-report.md (from assets/ templates), plus tests/, data/, and reports/ directories."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _common import ensure_utf8_stdio

TEMPLATES = {
    "test-cases.md": "test-cases-template.md",
    "ai-gap-analysis.md": "ai-gap-analysis-template.md",
    "bug-report.md": "bug-report-template.md",
}

SUBDIRS = ("tests", "data", "reports")


def non_empty(value: str) -> str:
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("value cannot be empty")
    return value


def render(text: str, feature_id: str, feature_name: str) -> str:
    return text.replace("{{FEATURE_ID}}", feature_id).replace("{{FEATURE_NAME}}", feature_name)


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Create an HW04 automation workspace for one feature.")
    parser.add_argument("--feature-id", required=True, type=non_empty, help="e.g. FR-01.")
    parser.add_argument("--feature-name", required=True, type=non_empty, help="e.g. 'Account registration'.")
    parser.add_argument("--output", required=True, type=non_empty, help="Output root directory, e.g. reports/HW4.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    args = parser.parse_args()

    assets = Path(__file__).resolve().parents[1] / "assets"
    missing = [str(assets / t) for t in TEMPLATES.values() if not (assets / t).is_file()]
    if missing:
        print("ERROR: required templates are missing; no output was written:", file=sys.stderr)
        for item in missing:
            print(f"  - {item}", file=sys.stderr)
        return 3

    feature_dir = Path(args.output) / args.feature_id
    created: list[str] = []
    skipped: list[str] = []

    for filename, template_name in TEMPLATES.items():
        target = feature_dir / filename
        if target.exists() and not args.force:
            skipped.append(str(target))
            continue
        content = render((assets / template_name).read_text(encoding="utf-8"), args.feature_id, args.feature_name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        created.append(str(target))

    for sub in SUBDIRS:
        (feature_dir / sub).mkdir(parents=True, exist_ok=True)

    print(f"Workspace: {feature_dir}")
    print(f"Created: {len(created)}")
    for item in created:
        print(f"  - {item}")
    print(f"Skipped existing: {len(skipped)}")
    for item in skipped:
        print(f"  - {item}")
    print(f"Subdirectories ready: {', '.join(str(feature_dir / s) for s in SUBDIRS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
