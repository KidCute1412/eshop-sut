#!/usr/bin/env python3
"""Create a feature report workspace from skill templates."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FILES = {
    "requirement-analysis.md": "requirement-analysis-template.md",
    "domain-testing.md": "domain-table-template.md",
    "boundary-value-analysis.md": "bva-table-template.md",
    "test-cases.md": "test-case-template.md",
    "traceability-matrix.md": "traceability-template.md",
    "ai-gap-analysis.md": "ai-gap-analysis-template.md",
}


def compact_id(feature_id: str) -> str:
    return feature_id.replace("-", "").upper()


def render(text: str, feature_id: str, feature_name: str, pool: str) -> str:
    return (
        text.replace("{{FEATURE_ID}}", feature_id)
        .replace("{{FEATURE_COMPACT}}", compact_id(feature_id))
        .replace("{{FEATURE_NAME}}", feature_name)
        .replace("{{POOL}}", pool)
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Domain Testing/BVA feature workspace.")
    parser.add_argument("--feature-id", required=True, help="Feature ID such as FR-01.")
    parser.add_argument("--feature-name", required=True, help="Feature name.")
    parser.add_argument("--pool", required=True, help="Feature pool, such as A, B, C, or D.")
    parser.add_argument("--output", required=True, help="Output root directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing report files.")
    args = parser.parse_args()

    feature_id = args.feature_id.upper()
    if not re.fullmatch(r"FR-\d{2}", feature_id):
        print(f"ERROR: invalid feature ID '{args.feature_id}'. Expected format FR-01.", file=sys.stderr)
        return 2

    skill_root = Path(__file__).resolve().parents[1]
    assets = skill_root / "assets"
    out_dir = Path(args.output) / feature_id
    evidence_dir = out_dir / "evidence"

    out_dir.mkdir(parents=True, exist_ok=True)
    evidence_dir.mkdir(parents=True, exist_ok=True)

    created = []
    skipped = []
    for output_name, template_name in FILES.items():
        target = out_dir / output_name
        if target.exists() and not args.force:
            skipped.append(str(target))
            continue
        template = assets / template_name
        if not template.exists():
            print(f"ERROR: missing template {template}", file=sys.stderr)
            return 3
        target.write_text(render(template.read_text(encoding="utf-8"), feature_id, args.feature_name, args.pool), encoding="utf-8")
        created.append(str(target))

    print(f"Workspace ready: {out_dir}")
    if created:
        print("Created/updated:")
        for item in created:
            print(f"  - {item}")
    if skipped:
        print("Skipped existing files (use --force to overwrite):")
        for item in skipped:
            print(f"  - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

