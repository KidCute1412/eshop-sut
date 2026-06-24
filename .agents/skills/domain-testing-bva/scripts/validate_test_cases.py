#!/usr/bin/env python3
"""Read-only validator for black-box Domain Testing/BVA Markdown cases."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urlparse


FEATURE_ID_RE = re.compile(r"(?:FR|D)-\d{2}")
TEST_CASE_ID_RE = re.compile(r"(?:FR|D)\d{2}-(?:DT|BVA)-\d{3}")
TEST_CASE_HEADING_RE = re.compile(r"(?m)^##\s+((?:FR|D)\d{2}-(?:DT|BVA)-\d{3})\s*$")

ALLOWED_STATUSES = {"Not Executed", "Pass", "Fail", "Blocked"}

REQUIRED_FIELDS = (
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
    "Test Basis Reference",
    "Notes and Assumptions",
)

KNOWN_FIELDS = set(REQUIRED_FIELDS) | {"Blocking Reason"}

FIELD_RE = re.compile(r"^\s*-\s*([^:\n]+):\s*(.*)$")
SOURCE_CODE_REFERENCE_RE = re.compile(r"(?mi)^\s*-\s*Source Code Reference\s*:")

EMPTY_VALUES = {"", "todo", "tbd", "n/a"}
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|PLACEHOLDER)\b", re.IGNORECASE)

INVALID_EVIDENCE_VALUES = {
    "",
    "none",
    "not executed",
    "todo",
    "tbd",
    "placeholder",
    "pending",
    "n/a",
}

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
EVIDENCE_SPLIT_RE = re.compile(r"[\n,;]+")

URL_SCHEMES = {"http", "https"}


def split_cases(text: str) -> list[str]:
    """Split Markdown text into test-case sections.

    A test case must start with a level-two heading such as:

        ## FR01-DT-001
        ## FR01-BVA-001
        ## D01-DT-001
        ## D01-BVA-001
    """
    # Stop at the next level-two heading, including report sections such as
    # "## Human Review - Phase 5". Otherwise fields in that section can
    # overwrite fields belonging to the final test case.
    case_section_re = re.compile(
        r"(?ms)^##\s+(?:FR|D)\d{2}-(?:DT|BVA)-\d{3}\s*$"
        r".*?(?=^##\s+|\Z)"
    )
    return [match.group(0).strip() for match in case_section_re.finditer(text)]


def heading_id(case: str) -> str | None:
    """Return the test-case ID from the section heading."""
    match = TEST_CASE_HEADING_RE.search(case)
    return match.group(1) if match else None


def fields_for(case: str) -> dict[str, str]:
    """Parse known '- Field: value' lines from a test-case section."""
    fields: dict[str, str] = {}
    current: str | None = None

    for line in case.splitlines():
        match = FIELD_RE.match(line)

        if match and match.group(1).strip() in KNOWN_FIELDS:
            current = match.group(1).strip()
            fields[current] = match.group(2).strip()
            continue

        # Continue multiline values, but do not accidentally absorb unknown
        # field-like bullet lines such as "- Source Code Reference: ...".
        if (
            current
            and line.strip()
            and not line.startswith("#")
            and not FIELD_RE.match(line)
        ):
            fields[current] += "\n" + line.strip()

    return fields


def empty(value: str) -> bool:
    """Return True when a value is empty or explicitly not filled."""
    return value.strip().lower() in EMPTY_VALUES


def has_placeholder(value: str) -> bool:
    """Return True when a value still contains TODO/TBD/PLACEHOLDER text."""
    return bool(PLACEHOLDER_RE.search(value or ""))


def empty_or_placeholder(value: str) -> bool:
    """Return True when a required field is empty or still placeholder text."""
    return empty(value) or has_placeholder(value)


def expected_feature(path: Path) -> str | None:
    """Infer compact feature ID such as FR01 or D01 from parent directories."""
    for parent in path.parents:
        candidate = parent.name.upper()
        if FEATURE_ID_RE.fullmatch(candidate):
            return candidate.replace("-", "")
    return None


def fingerprint(fields: dict[str, str]) -> str:
    """Build a content fingerprint for probable duplicate detection."""
    return " ".join(
        fields.get(key, "")
        for key in ("Objective", "Test Data", "Steps", "Expected Result")
    ).lower()


def is_valid_url(value: str) -> bool:
    """Accept only http(s) URLs with a network location."""
    parsed = urlparse(value.strip())
    return parsed.scheme in URL_SCHEMES and bool(parsed.netloc)


def looks_like_url(value: str) -> bool:
    """Return True when a value appears intended to be a URL."""
    stripped = value.strip()
    parsed = urlparse(stripped)
    return bool(parsed.scheme) or stripped.lower().startswith("www.")


def extract_evidence_references(value: str) -> list[str]:
    """Extract evidence path or URL references from an Evidence field."""
    raw = value.strip()

    if raw.lower() in INVALID_EVIDENCE_VALUES or has_placeholder(raw):
        return []

    markdown_targets = [
        match.group(1).strip().strip("`'\"<>")
        for match in MARKDOWN_LINK_RE.finditer(raw)
        if match.group(1).strip()
    ]
    if markdown_targets:
        return markdown_targets

    references: list[str] = []
    for part in EVIDENCE_SPLIT_RE.split(raw):
        reference = part.strip()
        reference = re.sub(r"^\s*[-*]\s*", "", reference)
        reference = reference.strip("`'\"<>")

        if reference:
            references.append(reference)

    return references


def evidence_reference_exists(test_case_path: Path, evidence_reference: str) -> bool:
    """Check whether a local evidence file exists.

    Relative paths are checked against:
    1. The directory containing test-cases.md.
    2. The current working directory.

    URLs are not checked over the network; they are validated by format only.
    """
    reference = evidence_reference.strip()

    if is_valid_url(reference):
        return True

    evidence_path = Path(reference)

    if evidence_path.is_absolute():
        return evidence_path.is_file()

    relative_to_test_case = test_case_path.parent / evidence_path
    relative_to_cwd = Path.cwd() / evidence_path

    return relative_to_test_case.is_file() or relative_to_cwd.is_file()


def looks_like_partition_reference(value: str) -> bool:
    """Validate that a DT case references a plausible partition ID."""
    if empty_or_placeholder(value):
        return False

    # Accept explicit wording such as "partition-email-valid" or "EP-EMAIL-01".
    if re.search(r"\b(?:partition|ep)[-_ ]?[a-z0-9][a-z0-9_-]*\b", value, re.I):
        return True

    # Accept concise partition IDs such as EMAIL-V01, EMAIL-I01, PASSWORD-I02.
    if re.search(r"\b[A-Z][A-Z0-9]*-(?:V|I)\d{2}\b", value):
        return True

    # Accept more verbose IDs such as EMAIL-VALID-01 or EMAIL-INVALID-01.
    if re.search(r"\b[A-Z][A-Z0-9]*-(?:VALID|INVALID)-?\d*\b", value, re.I):
        return True

    return False


def looks_like_boundary_reference(value: str) -> bool:
    """Validate that a BVA case references a plausible boundary ID.

    This intentionally allows more than one naming convention so valid BVA
    cases are not rejected only because a specific English keyword is absent.
    """
    if empty_or_placeholder(value):
        return False

    # Accept explicit wording such as BOUNDARY-LENGTH-MIN or boundary length min.
    if re.search(r"\bboundary[-_ ]?[a-z0-9][a-z0-9_-]*\b", value, re.I):
        return True

    # Accept boundary IDs (Bxx) and approved nominal internal points (Nxx),
    # such as PASSWORD-B01 or FR01-PASSWORD-LENGTH-N01.
    if re.search(r"\b[A-Z][A-Z0-9_-]*-(?:B|N)\d{2}\b", value):
        return True

    # Accept IDs/descriptions containing boundary semantics.
    if re.search(
        r"\b[A-Z][A-Z0-9_-]*(?:MIN|MAX|LOWER|UPPER|ON|OFF|IN)[A-Z0-9_-]*\d*\b",
        value,
        re.I,
    ):
        return True

    return False


def validate_evidence_for_executed_case(
    path: Path,
    label: str,
    status: str,
    actual: str,
    evidence: str,
) -> list[str]:
    """Validate Actual Result and Evidence for Pass/Fail cases."""
    errors: list[str] = []
    actual_normalized = actual.strip().lower()
    evidence_normalized = evidence.strip().lower()

    if actual_normalized == "not executed":
        errors.append(
            f"{path}: {label}: {status} cannot use "
            "'Actual Result: Not Executed'"
        )

    if empty_or_placeholder(actual) or actual_normalized in {"none", "n/a"}:
        errors.append(
            f"{path}: {label}: {status} requires a concrete Actual Result"
        )

    if evidence_normalized in INVALID_EVIDENCE_VALUES or has_placeholder(evidence):
        errors.append(
            f"{path}: {label}: {status} requires a real evidence reference"
        )
        return errors

    references = extract_evidence_references(evidence)
    if not references:
        errors.append(
            f"{path}: {label}: {status} requires a real evidence reference"
        )
        return errors

    for reference in references:
        if is_valid_url(reference):
            continue

        if looks_like_url(reference):
            errors.append(
                f"{path}: {label}: invalid evidence URL format: {reference}"
            )
            continue

        if not evidence_reference_exists(path, reference):
            errors.append(
                f"{path}: {label}: evidence file does not exist: {reference}"
            )

    return errors


def validate_file(path: Path) -> tuple[list[str], list[tuple[str, str, str]]]:
    """Validate one test-cases.md file."""
    errors: list[str] = []
    records: list[tuple[str, str, str]] = []

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{path}: cannot read UTF-8 Markdown: {exc}"], []

    cases = split_cases(text)
    if not cases:
        return [
            f"{path}: zero test cases parsed; use a level-two heading such "
            "as '## FR01-DT-001'"
        ], []

    feature = expected_feature(path)

    for index, case in enumerate(cases, 1):
        fields = fields_for(case)
        tc_id = fields.get("Test Case ID", "")
        case_heading_id = heading_id(case)
        label = tc_id or case_heading_id or f"case #{index}"

        if SOURCE_CODE_REFERENCE_RE.search(case):
            errors.append(
                f"{path}: {label}: use 'Test Basis Reference', not "
                "'Source Code Reference'"
            )

        if case_heading_id and tc_id and case_heading_id != tc_id:
            errors.append(
                f"{path}: {label}: heading ID '{case_heading_id}' does not "
                f"match 'Test Case ID: {tc_id}'"
            )

        for field in REQUIRED_FIELDS:
            if field not in fields or empty_or_placeholder(fields[field]):
                errors.append(
                    f"{path}: {label}: missing, empty, or placeholder field "
                    f"'{field}'"
                )

        if not TEST_CASE_ID_RE.fullmatch(tc_id):
            errors.append(
                f"{path}: {label}: invalid ID; expected FR01-DT-001, "
                "FR01-BVA-001, D01-DT-001, or D01-BVA-001"
            )
        elif feature and not tc_id.startswith(feature + "-"):
            errors.append(
                f"{path}: {tc_id}: ID does not match feature directory {feature}"
            )

        status = fields.get("Status", "")
        evidence = fields.get("Evidence", "")
        actual = fields.get("Actual Result", "")

        if status not in ALLOWED_STATUSES:
            errors.append(
                f"{path}: {label}: invalid Status '{status}'; allowed: "
                f"{', '.join(sorted(ALLOWED_STATUSES))}"
            )

        if status in {"Pass", "Fail"}:
            errors.extend(
                validate_evidence_for_executed_case(
                    path=path,
                    label=label,
                    status=status,
                    actual=actual,
                    evidence=evidence,
                )
            )

        if status == "Blocked" and empty_or_placeholder(
            fields.get("Blocking Reason", "")
        ):
            errors.append(
                f"{path}: {label}: Blocked requires a non-empty "
                "'Blocking Reason' field"
            )

        if status == "Not Executed":
            if actual.strip() != "Not Executed":
                errors.append(
                    f"{path}: {label}: Not Executed status requires "
                    "'Actual Result: Not Executed'"
                )
            if evidence.strip() != "None":
                errors.append(
                    f"{path}: {label}: Not Executed must use 'Evidence: None'"
                )

        coverage = fields.get("Partition or Boundary Covered", "")
        technique = fields.get("Technique", "")

        if "-DT-" in tc_id:
            if technique != "Domain Testing":
                errors.append(
                    f"{path}: {label}: DT ID requires "
                    "'Technique: Domain Testing'"
                )
            if not looks_like_partition_reference(coverage):
                errors.append(
                    f"{path}: {label}: DT case must reference a valid "
                    "partition ID"
                )

        if "-BVA-" in tc_id:
            if technique != "Boundary Value Analysis":
                errors.append(
                    f"{path}: {label}: BVA ID requires "
                    "'Technique: Boundary Value Analysis'"
                )
            if not looks_like_boundary_reference(coverage):
                errors.append(
                    f"{path}: {label}: BVA case must reference a valid "
                    "Boundary ID"
                )

        records.append((tc_id or label, fingerprint(fields), coverage))

    return errors, records


def collect_targets(paths: list[str]) -> tuple[list[Path], list[str]]:
    """Collect test-cases.md targets from files or directories."""
    targets: list[Path] = []
    errors: list[str] = []

    for raw in paths:
        path = Path(raw)

        if not path.exists():
            errors.append(f"{path}: path not found")
            continue

        if path.is_dir():
            direct = path / "test-cases.md"
            found = [direct] if direct.is_file() else sorted(path.rglob("test-cases.md"))
            targets.extend(found)
            continue

        targets.append(path)

    # Stable de-duplication for overlapping input paths.
    targets = list(dict.fromkeys(targets))

    if not targets:
        errors.append("no test-case files found")

    return targets, errors


def detect_global_duplicates(
    all_records: list[tuple[str, str, str, Path]],
) -> list[str]:
    """Detect duplicate IDs and probable duplicate test cases."""
    errors: list[str] = []

    for case_id, count in Counter(
        case_id
        for case_id, _, _, _ in all_records
        if TEST_CASE_ID_RE.fullmatch(case_id)
    ).items():
        if count > 1:
            errors.append(f"duplicate test case ID across inputs: {case_id}")

    for index, (left_id, left_fp, left_coverage, left_path) in enumerate(
        all_records
    ):
        for right_id, right_fp, right_coverage, right_path in all_records[
            index + 1 :
        ]:
            left_technique = (
                left_id.split("-")[1]
                if TEST_CASE_ID_RE.fullmatch(left_id)
                else ""
            )
            right_technique = (
                right_id.split("-")[1]
                if TEST_CASE_ID_RE.fullmatch(right_id)
                else ""
            )

            if left_technique != right_technique:
                continue

            # Similar procedures that cover different equivalence partitions
            # or boundary points are intentional, not duplicate test cases.
            if left_coverage.strip().lower() != right_coverage.strip().lower():
                continue

            if (
                left_fp
                and right_fp
                and SequenceMatcher(None, left_fp, right_fp).ratio() >= 0.95
            ):
                errors.append(
                    f"probable duplicate cases: {left_id} ({left_path}) and "
                    f"{right_id} ({right_path}); review or differentiate them"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate black-box DT/BVA Markdown test cases without modifying them."
        )
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="test-cases.md files or feature/report directories.",
    )
    args = parser.parse_args()

    targets, errors = collect_targets(args.paths)

    all_records: list[tuple[str, str, str, Path]] = []

    for target in targets:
        file_errors, records = validate_file(target)
        errors.extend(file_errors)
        all_records.extend(
            (case_id, fp, coverage, target)
            for case_id, fp, coverage in records
        )

    errors.extend(detect_global_duplicates(all_records))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(
        f"Validation passed: {len(all_records)} test case(s) "
        f"in {len(targets)} file(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
