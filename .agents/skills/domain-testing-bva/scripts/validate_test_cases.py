#!/usr/bin/env python3
"""Validate Markdown test cases for Domain Testing/BVA reports."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path


REQUIRED_FIELDS = [
    "Test Case ID",
    "Technique",
    "Objective",
    "Requirement or Rule Reference",
    "Preconditions",
    "Test Data",
    "Steps",
    "Expected Result",
    "Actual Result",
    "Status",
    "Evidence",
    "Partition or Boundary Covered",
    "Source Code Reference",
    "Notes and Assumptions",
]

ID_RE = re.compile(r"\b(FR\d{2}-(?:DT|BVA)-\d{3})\b")
FIELD_RE = re.compile(r"^\s*-?\s*([^:\n]+):\s*(.*)$")


def split_cases(text: str) -> list[str]:
    starts = [m.start() for m in re.finditer(r"(?m)^##\s+", text)]
    if not starts:
        return [text] if "Test Case ID:" in text else []
    starts.append(len(text))
    return [text[starts[i] : starts[i + 1]].strip() for i in range(len(starts) - 1)]


def fields_for(case: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current = None
    for line in case.splitlines():
        match = FIELD_RE.match(line)
        if match and match.group(1).strip() in REQUIRED_FIELDS:
            current = match.group(1).strip()
            fields[current] = match.group(2).strip()
        elif current and line.strip() and not line.startswith("#"):
            fields[current] += "\n" + line.strip()
    return fields


def normalize_for_similarity(fields: dict[str, str]) -> str:
    parts = [fields.get("Objective", ""), fields.get("Test Data", ""), fields.get("Steps", ""), fields.get("Expected Result", "")]
    return " ".join(parts).lower()


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    cases = split_cases(text)
    ids = []
    fingerprints = []

    if not cases:
        return [f"{path}: no test cases found"]

    for index, case in enumerate(cases, 1):
        fields = fields_for(case)
        tc_id = fields.get("Test Case ID", "")
        label = tc_id or f"case #{index}"
        if not tc_id:
            errors.append(f"{path}: {label}: missing Test Case ID")
        elif not ID_RE.fullmatch(tc_id):
            errors.append(f"{path}: {tc_id}: invalid ID format; expected FR01-DT-001 or FR01-BVA-001")
        else:
            ids.append(tc_id)

        for field in REQUIRED_FIELDS:
            if not fields.get(field):
                errors.append(f"{path}: {label}: missing or empty field '{field}'")

        expected = fields.get("Expected Result", "")
        if not expected or expected.lower() in {"tbd", "n/a", "none"}:
            errors.append(f"{path}: {label}: missing actionable expected result")

        status = fields.get("Status", "")
        evidence = fields.get("Evidence", "")
        if status in {"Pass", "Fail"} and evidence.lower() in {"none", "not executed", ""}:
            errors.append(f"{path}: {label}: Pass/Fail requires real evidence")
        if status != "Not Executed" and evidence.lower() == "none":
            errors.append(f"{path}: {label}: executed status cannot use Evidence: None")

        coverage = fields.get("Partition or Boundary Covered", "")
        if not coverage:
            errors.append(f"{path}: {label}: missing partition or boundary reference")

        if not fields.get("Requirement or Rule Reference", ""):
            errors.append(f"{path}: {label}: missing requirement reference")
        if not fields.get("Source Code Reference", ""):
            errors.append(f"{path}: {label}: missing source-code reference")

        technique = fields.get("Technique", "")
        if tc_id:
            if "-DT-" in tc_id and "Domain" not in technique:
                errors.append(f"{path}: {label}: DT ID should use Domain Testing technique")
            if "-BVA-" in tc_id and "Boundary" not in technique:
                errors.append(f"{path}: {label}: BVA ID should use Boundary Value Analysis technique")
        if "Boundary" in technique and not re.search(r"\b(min|max|boundary|threshold|length|count|attempt|date|expiration|zero|one|capacity|[+-]1)\b", coverage, re.I):
            errors.append(f"{path}: {label}: BVA case lacks detectable boundary wording")

        fingerprints.append((label, normalize_for_similarity(fields)))

    for dup_id, count in Counter(ids).items():
        if count > 1:
            errors.append(f"{path}: duplicate test case ID {dup_id}")

    for i in range(len(fingerprints)):
        for j in range(i + 1, len(fingerprints)):
            a_id, a_text = fingerprints[i]
            b_id, b_text = fingerprints[j]
            if a_text and b_text and SequenceMatcher(None, a_text, b_text).ratio() > 0.94:
                errors.append(f"{path}: highly similar test cases: {a_id} and {b_id}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Markdown Domain Testing/BVA test cases.")
    parser.add_argument("paths", nargs="+", help="Markdown files or directories containing test-cases.md.")
    args = parser.parse_args()

    targets: list[Path] = []
    for raw in args.paths:
        path = Path(raw)
        if path.is_dir():
            candidate = path / "test-cases.md"
            if candidate.exists():
                targets.append(candidate)
            else:
                targets.extend(path.rglob("*test-cases*.md"))
        else:
            targets.append(path)

    errors: list[str] = []
    for target in targets:
        if not target.exists():
            errors.append(f"{target}: file not found")
            continue
        errors.extend(validate_file(target))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"Validation passed for {len(targets)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

