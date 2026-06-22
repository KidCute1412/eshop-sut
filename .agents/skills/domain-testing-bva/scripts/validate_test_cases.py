#!/usr/bin/env python3
"""Read-only validator for black-box Domain Testing/BVA Markdown cases."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path


FEATURE_ID_RE = re.compile(r"(?:FR|D)-\d{2}")
TEST_CASE_ID_RE = re.compile(r"(?:FR|D)\d{2}-(?:DT|BVA)-\d{3}")
ALLOWED_STATUSES = {"Not Executed", "Pass", "Fail", "Blocked"}
REQUIRED_FIELDS = (
    "Test Case ID", "Technique", "Objective", "Requirement or Rule Reference",
    "Preconditions", "Test Data", "Steps", "Expected Result", "Actual Result",
    "Status", "Evidence", "Partition or Boundary Covered", "Test Basis Reference",
    "Notes and Assumptions",
)
KNOWN_FIELDS = set(REQUIRED_FIELDS) | {"Blocking Reason"}
FIELD_RE = re.compile(r"^\s*-\s*([^:\n]+):\s*(.*)$")
EMPTY_VALUES = {"", "todo", "tbd", "n/a"}


def split_cases(text: str) -> list[str]:
    matches = list(re.finditer(r"(?m)^##\s+(?:(?:FR|D)\d{2}-(?:DT|BVA)-\d{3})\s*$", text))
    return [text[m.start():(matches[i + 1].start() if i + 1 < len(matches) else len(text))].strip()
            for i, m in enumerate(matches)]


def fields_for(case: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current: str | None = None
    for line in case.splitlines():
        match = FIELD_RE.match(line)
        if match and match.group(1).strip() in KNOWN_FIELDS:
            current = match.group(1).strip()
            fields[current] = match.group(2).strip()
        elif current and line.strip() and not line.startswith("#"):
            fields[current] += "\n" + line.strip()
    return fields


def empty(value: str) -> bool:
    return value.strip().lower() in EMPTY_VALUES


def expected_feature(path: Path) -> str | None:
    for parent in [path.parent, *path.parents]:
        candidate = parent.name.upper()
        if FEATURE_ID_RE.fullmatch(candidate):
            return candidate.replace("-", "")
    return None


def fingerprint(fields: dict[str, str]) -> str:
    return " ".join(fields.get(key, "") for key in ("Objective", "Test Data", "Steps", "Expected Result")).lower()


def validate_file(path: Path) -> tuple[list[str], list[tuple[str, str]]]:
    errors: list[str] = []
    records: list[tuple[str, str]] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{path}: cannot read UTF-8 Markdown: {exc}"], []
    cases = split_cases(text)
    if not cases:
        return [f"{path}: zero test cases parsed; use a level-two heading such as '## FR01-DT-001'"], []

    feature = expected_feature(path)
    for index, case in enumerate(cases, 1):
        fields = fields_for(case)
        tc_id = fields.get("Test Case ID", "")
        label = tc_id or f"case #{index}"
        for field in REQUIRED_FIELDS:
            if field not in fields or empty(fields[field]):
                errors.append(f"{path}: {label}: missing, empty, or placeholder field '{field}'")
        if not TEST_CASE_ID_RE.fullmatch(tc_id):
            errors.append(f"{path}: {label}: invalid ID; expected FR01-DT-001, FR01-BVA-001, D01-DT-001, or D01-BVA-001")
        elif feature and not tc_id.startswith(feature + "-"):
            errors.append(f"{path}: {tc_id}: ID does not match feature directory {feature}")

        status = fields.get("Status", "")
        evidence = fields.get("Evidence", "")
        actual = fields.get("Actual Result", "")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{path}: {label}: invalid Status '{status}'; allowed: {', '.join(sorted(ALLOWED_STATUSES))}")
        if status in {"Pass", "Fail"} and evidence.strip().lower() in {"", "none", "not executed", "todo", "tbd"}:
            errors.append(f"{path}: {label}: {status} requires a real evidence reference")
        if status == "Blocked" and empty(fields.get("Blocking Reason", "")):
            errors.append(f"{path}: {label}: Blocked requires a non-empty 'Blocking Reason' field")
        if status == "Not Executed":
            if actual != "Not Executed":
                errors.append(f"{path}: {label}: Not Executed status requires 'Actual Result: Not Executed'")
            if evidence != "None":
                errors.append(f"{path}: {label}: Not Executed must use 'Evidence: None'")

        coverage = fields.get("Partition or Boundary Covered", "")
        technique = fields.get("Technique", "")
        if "-DT-" in tc_id:
            if technique != "Domain Testing":
                errors.append(f"{path}: {label}: DT ID requires 'Technique: Domain Testing'")
            if not re.search(r"\b(?:partition|ep)[-_ ]?[a-z0-9]+\b", coverage, re.I):
                errors.append(f"{path}: {label}: DT case must reference a partition ID")
        if "-BVA-" in tc_id:
            if technique != "Boundary Value Analysis":
                errors.append(f"{path}: {label}: BVA ID requires 'Technique: Boundary Value Analysis'")
            if not re.search(r"\bboundary[-_ ]?[a-z0-9]+\b", coverage, re.I):
                errors.append(f"{path}: {label}: BVA case must reference a Boundary ID")
        records.append((tc_id or label, fingerprint(fields)))
    return errors, records


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate black-box DT/BVA Markdown test cases without modifying them.")
    parser.add_argument("paths", nargs="+", help="test-cases.md files or feature/report directories.")
    args = parser.parse_args()

    targets: list[Path] = []
    errors: list[str] = []
    for raw in args.paths:
        path = Path(raw)
        if not path.exists():
            errors.append(f"{path}: path not found")
        elif path.is_dir():
            direct = path / "test-cases.md"
            found = [direct] if direct.is_file() else sorted(path.rglob("test-cases.md"))
            targets.extend(found)
        else:
            targets.append(path)
    # Stable de-duplication for overlapping input paths.
    targets = list(dict.fromkeys(targets))
    if not targets:
        errors.append("no test-case files found")

    all_records: list[tuple[str, str, Path]] = []
    for target in targets:
        file_errors, records = validate_file(target)
        errors.extend(file_errors)
        all_records.extend((case_id, fp, target) for case_id, fp in records)
    for case_id, count in Counter(case_id for case_id, _, _ in all_records if TEST_CASE_ID_RE.fullmatch(case_id)).items():
        if count > 1:
            errors.append(f"duplicate test case ID across inputs: {case_id}")
    for i, (left_id, left_fp, left_path) in enumerate(all_records):
        for right_id, right_fp, right_path in all_records[i + 1:]:
            left_technique = left_id.split("-")[1] if TEST_CASE_ID_RE.fullmatch(left_id) else ""
            right_technique = right_id.split("-")[1] if TEST_CASE_ID_RE.fullmatch(right_id) else ""
            if left_technique != right_technique:
                continue
            if left_fp and right_fp and SequenceMatcher(None, left_fp, right_fp).ratio() >= 0.95:
                errors.append(f"probable duplicate cases: {left_id} ({left_path}) and {right_id} ({right_path}); review or differentiate them")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"Validation passed: {len(all_records)} test case(s) in {len(targets)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
