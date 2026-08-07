#!/usr/bin/env python3
"""Check that a feature's automation is actually data-driven: an external .csv/.json data file
exists, and no spec file contains a suspicious hardcoded inline array-of-objects (the pattern the
assignment explicitly rejects)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _common import ensure_utf8_stdio

SPEC_GLOBS = ("*.spec.ts", "*.spec.js", "*.spec.tsx", "*.spec.jsx", "*Test.java", "*_test.py")
DATA_GLOBS = ("*.json", "*.csv")

# Matches e.g. `const testCases = [` immediately followed by `{` (array-of-objects literal) --
# a strong signal of inline hardcoded test data rather than an externally loaded file.
INLINE_ARRAY_OF_OBJECTS_RE = re.compile(
    r"(?:const|let|var)\s+\w*(?:[Cc]ases?|[Dd]ata|[Uu]sers?|[Ff]ixtures?)\w*\s*=\s*\[\s*\{",
)

IMPORT_HINTS = (
    ".json", ".csv", "readFileSync", "parseCsv", "csv-parse", "require(", "import ",
)


def find_spec_files(tests_dir: Path) -> list[Path]:
    found: list[Path] = []
    for pattern in SPEC_GLOBS:
        found.extend(tests_dir.rglob(pattern))
    return sorted(set(found))


def find_data_files(data_dir: Path) -> list[Path]:
    found: list[Path] = []
    for pattern in DATA_GLOBS:
        found.extend(data_dir.rglob(pattern))
    return sorted(set(found))


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Validate a feature's automation is data-driven.")
    parser.add_argument("feature_dir", help="Feature workspace directory (contains tests/ and data/).")
    args = parser.parse_args()

    feature_dir = Path(args.feature_dir)
    if not feature_dir.is_dir():
        print(f"ERROR: not a directory: {feature_dir}", file=sys.stderr)
        return 2

    tests_dir = feature_dir / "tests"
    data_dir = feature_dir / "data"
    errors: list[str] = []

    data_files = find_data_files(data_dir) if data_dir.is_dir() else []
    if not data_files:
        errors.append(f"{data_dir}: no external .json/.csv data file found")

    spec_files = find_spec_files(tests_dir) if tests_dir.is_dir() else []
    if not spec_files:
        errors.append(f"{tests_dir}: no spec files found")

    for spec in spec_files:
        text = spec.read_text(encoding="utf-8", errors="replace")
        if INLINE_ARRAY_OF_OBJECTS_RE.search(text):
            has_import_hint = any(hint in text for hint in IMPORT_HINTS)
            if not has_import_hint:
                errors.append(
                    f"{spec}: looks like a hardcoded inline array-of-objects test-data literal, "
                    "with no external-file import in the same file -- move this data to a .json/.csv "
                    "file per references/data-driven-and-assertions.md"
                )

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Validation passed: {len(spec_files)} spec file(s), {len(data_files)} external data file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
