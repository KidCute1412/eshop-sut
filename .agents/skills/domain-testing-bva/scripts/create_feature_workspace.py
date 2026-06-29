#!/usr/bin/env python3
"""Create a complete black-box DT/BVA feature workspace atomically."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FEATURE_ID_RE = re.compile(r"(?:FR|D)-\d{2}")
FILES = {
    "requirement-analysis.md": "requirement-analysis-template.md",
    "domain-testing.md": "domain-table-template.md",
    "boundary-value-analysis.md": "bva-table-template.md",
    "test-cases.md": "test-case-template.md",
    "bug-report.md": "bug-report-template.md",
    "ai-gap-analysis.md": "ai-gap-analysis-template.md",
}
EXTRA_DIRS = ("evidence",)


def non_empty(value: str) -> str:
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("value cannot be empty")
    return value


def render(text: str, feature_id: str, feature_name: str, pool: str) -> str:
    return (text.replace("{{FEATURE_ID}}", feature_id)
            .replace("{{FEATURE_COMPACT}}", feature_id.replace("-", ""))
            .replace("{{FEATURE_NAME}}", feature_name)
            .replace("{{POOL}}", pool))


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a complete black-box Domain Testing/BVA workspace.")
    parser.add_argument("--feature-id", required=True, help="Feature ID: FR-01 or D-01.")
    parser.add_argument("--feature-name", required=True, type=non_empty, help="Non-empty feature name.")
    parser.add_argument("--pool", required=True, type=str.upper, choices="ABCD", help="Official pool A, B, C, or D.")
    parser.add_argument("--output", required=True, type=non_empty, help="Output root; feature ID is appended.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing report files.")
    args = parser.parse_args()

    feature_id = args.feature_id.strip().upper()
    if not FEATURE_ID_RE.fullmatch(feature_id):
        print(f"ERROR: invalid feature ID '{args.feature_id}'; expected FR-01 or D-01.", file=sys.stderr)
        return 2
    if feature_id.startswith("D-") and args.pool != "D":
        print(f"WARNING: {feature_id} appears to be a mobile feature but pool is {args.pool}.", file=sys.stderr)
    if feature_id.startswith("FR-") and args.pool == "D":
        print(f"WARNING: {feature_id} prefix appears inconsistent with mobile Pool D.", file=sys.stderr)

    assets = Path(__file__).resolve().parents[1] / "assets"
    missing = [str(assets / template) for template in FILES.values() if not (assets / template).is_file()]
    if missing:
        print("ERROR: required templates are missing; no output was written:", file=sys.stderr)
        for item in missing:
            print(f"  - {item}", file=sys.stderr)
        return 3

    # Read and render every template before creating directories or files.
    rendered = {
        relative: render((assets / template).read_text(encoding="utf-8"), feature_id, args.feature_name, args.pool)
        for relative, template in FILES.items()
    }
    out_dir = Path(args.output) / feature_id
    created: list[str] = []
    skipped: list[str] = []
    failed: list[str] = []
    for relative, content in rendered.items():
        target = out_dir / relative
        if target.exists() and not args.force:
            skipped.append(str(target))
            continue
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            created.append(str(target))
        except OSError as exc:
            failed.append(f"{target}: {exc}")
    for relative in EXTRA_DIRS:
        target_dir = out_dir / relative
        try:
            target_dir.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            failed.append(f"{target_dir}: {exc}")

    print(f"Workspace: {out_dir}")
    for label, items in (("Created/updated", created), ("Skipped existing", skipped), ("Failed", failed)):
        print(f"{label}: {len(items)}")
        for item in items:
            print(f"  - {item}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
