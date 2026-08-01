#!/usr/bin/env python3
"""Read-only validator for gui-usability GUI-checklist Markdown files.

Schema matches the professor's Web GUI checklist Template.xlsx taxonomy
(No./Checkpoint/Yes/No/Remarks) plus the extra columns HW03 requires
(IA/Source/AI-Miss Reason/Evidence/Bug ID). See references/checklist-item-schema.md.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

from _table_utils import ensure_utf8_stdio, is_empty_or_placeholder, parse_table

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

MD_LINK_RE = re.compile(r"^\[([^\]]*)\]\(([^)]+)\)$")


def resolve_evidence_target(value: str) -> str:
    """If Evidence is written as a clickable Markdown link (`[label](path)`,
    e.g. so the rendered table can be clicked straight to a screenshot),
    validate the link's target path/URL rather than the literal `[...](...)`
    string. Plain (non-link) Evidence values pass through unchanged."""
    match = MD_LINK_RE.match(value.strip())
    return match.group(2).strip() if match else value


NO_RE = re.compile(r"^\d+(\.\d+)*$")
VALID_TYPES = {"Section", "Item"}
ITEM_IA = {"IA-01", "IA-02", "IA-03", "IA-04", "Task-3"}
SECTION_IA = ITEM_IA | {"Mixed"}
REQUIRED_ITEM_IA = {"IA-01", "IA-02", "IA-03", "IA-04"}
VALID_SOURCE = {"Template-Provided", "AI-Generated", "Human-Added"}
MARK_VALUES = {"", "X", "x"}
MIN_ITEMS = 40
URL_SCHEMES = {"http", "https"}


def is_valid_url(value: str) -> bool:
    parsed = urlparse(value.strip())
    return parsed.scheme in URL_SCHEMES and bool(parsed.netloc)


def looks_like_url(value: str) -> bool:
    """Heuristic: does this value look like an attempted (possibly malformed) URL?

    Guards against two false-positive classes urlparse would otherwise produce:
    a Windows absolute path ("C:\\...") parses with a one-letter "scheme" (the
    drive letter), and a source citation like "Register.jsx:70-73" parses with
    a dotted "scheme" (the filename). Neither is a URL attempt.
    """
    stripped = value.strip()
    parsed = urlparse(stripped)
    scheme = parsed.scheme
    if scheme and len(scheme) > 1 and "." not in scheme:
        return True
    return stripped.lower().startswith("www.")


def evidence_exists(checklist_path: Path, reference: str) -> bool:
    if is_valid_url(reference):
        return True
    candidate = Path(reference)
    if candidate.is_absolute():
        return candidate.is_file()
    return (checklist_path.parent / candidate).is_file() or (Path.cwd() / candidate).is_file()


def validate_file(path: Path) -> tuple[list[str], int]:
    """Validate one checklist file. Returns (errors, Item-row count).

    The >40-item minimum is NOT enforced here: the assignment requires more
    than 40 items for the checklist you design, which may span several screen
    files. That combined total is checked once across every file passed to
    this script in a single invocation (see main()), not per file.
    """
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{path}: cannot read UTF-8 Markdown: {exc}"], 0

    rows = parse_table(text, HEADER)
    if not rows:
        return [f"{path}: zero checklist rows parsed; expected the checklist table header"], 0

    item_count = 0
    ia_seen: set[str] = set()
    numbers_seen: Counter[str] = Counter()

    for index, row in enumerate(rows, 1):
        no = row.get("No.", "")
        label = no or f"row #{index}"
        row_type = row.get("Type", "")
        checkpoint = row.get("Checkpoint", "")
        ia = row.get("IA", "")
        requirement_ref = row.get("Requirement / Heuristic Reference", "")
        source = row.get("Source", "")
        ai_miss_reason = row.get("AI-Miss Reason", "")
        yes = row.get("Yes", "").strip()
        no_mark = row.get("No", "").strip()
        remarks = row.get("Remarks", "")
        evidence = row.get("Evidence", "")

        numbers_seen[no] += 1

        if not NO_RE.match(no):
            errors.append(f"{path}: {label}: invalid No. '{no}'; expected dotted-decimal e.g. 1, 1.1, 1.1.1")

        if row_type not in VALID_TYPES:
            errors.append(f"{path}: {label}: invalid Type '{row_type}'; expected Section or Item")

        if is_empty_or_placeholder(checkpoint):
            errors.append(f"{path}: {label}: Checkpoint is empty or a placeholder")

        if source not in VALID_SOURCE:
            errors.append(f"{path}: {label}: invalid Source '{source}'; expected {sorted(VALID_SOURCE)}")
        elif source == "Human-Added" and is_empty_or_placeholder(ai_miss_reason):
            errors.append(f"{path}: {label}: Human-Added item requires a concrete AI-Miss Reason")
        elif source != "Human-Added" and ai_miss_reason.strip() == "":
            errors.append(f"{path}: {label}: non-Human-Added rows should use 'N/A' for AI-Miss Reason, not blank")

        if yes not in MARK_VALUES or no_mark not in MARK_VALUES:
            errors.append(f"{path}: {label}: Yes/No must be blank or 'X'")
        if yes.upper() == "X" and no_mark.upper() == "X":
            errors.append(f"{path}: {label}: Yes and No cannot both be marked")

        if row_type == "Section":
            if ia not in SECTION_IA:
                errors.append(f"{path}: {label}: invalid Section IA '{ia}'; expected one of {sorted(SECTION_IA)}")
            if yes.upper() == "X" or no_mark.upper() == "X":
                errors.append(f"{path}: {label}: Section rows must not be marked Yes/No; only child Items are executed")
            continue

        # row_type == "Item" (or invalid, already reported above; still check what we can)
        item_count += 1

        if ia not in ITEM_IA:
            errors.append(f"{path}: {label}: invalid Item IA '{ia}'; expected one of {sorted(ITEM_IA)}")
        elif ia in REQUIRED_ITEM_IA:
            ia_seen.add(ia)

        if ia != "Task-3" and is_empty_or_placeholder(requirement_ref):
            errors.append(f"{path}: {label}: Item requires a Requirement / Heuristic Reference")

        executed = yes.upper() == "X" or no_mark.upper() == "X"

        if no_mark.upper() == "X":
            if is_empty_or_placeholder(remarks):
                errors.append(f"{path}: {label}: item marked No requires a concrete Remarks reason")
            if is_empty_or_placeholder(evidence):
                errors.append(f"{path}: {label}: item marked No requires a real Evidence reference")
            else:
                evidence_target = resolve_evidence_target(evidence)
                if not is_valid_url(evidence_target) and looks_like_url(evidence_target):
                    errors.append(f"{path}: {label}: invalid evidence URL format: {evidence}")
                elif not is_valid_url(evidence_target) and not evidence_exists(path, evidence_target):
                    errors.append(f"{path}: {label}: evidence file does not exist: {evidence}")
        else:
            if evidence.strip() not in ("", "None", "N/A"):
                errors.append(f"{path}: {label}: only items marked No may carry an Evidence reference")

        if not executed and not is_empty_or_placeholder(remarks):
            errors.append(f"{path}: {label}: unexecuted item (neither Yes nor No marked) should not have Remarks")

    for ia in REQUIRED_ITEM_IA:
        if ia not in ia_seen:
            errors.append(f"{path}: no checklist item covers required interface aspect {ia}")

    for no, count in numbers_seen.items():
        if no and count > 1:
            errors.append(f"{path}: duplicate No.: {no}")

    return errors, item_count


def collect_targets(paths: list[str]) -> tuple[list[Path], list[str]]:
    targets: list[Path] = []
    errors: list[str] = []
    for raw in paths:
        path = Path(raw)
        if not path.exists():
            errors.append(f"{path}: path not found")
            continue
        if path.is_dir():
            found = sorted(path.rglob("checklist*.md"))
            targets.extend(found)
            continue
        targets.append(path)
    targets = list(dict.fromkeys(targets))
    if not targets:
        errors.append("no checklist*.md files found")
    return targets, errors


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Validate gui-usability GUI-checklist Markdown files.")
    parser.add_argument("paths", nargs="+", help="checklist*.md files or directories to search.")
    parser.add_argument(
        "--no-min-items-check",
        action="store_true",
        help="Skip the combined >40-item check (useful when validating a single screen mid-design, "
        "before the rest of the checklist's screens are ready).",
    )
    args = parser.parse_args()

    targets, errors = collect_targets(args.paths)
    total_items = 0
    for target in targets:
        file_errors, item_count = validate_file(target)
        errors.extend(file_errors)
        if not file_errors:
            total_items += item_count

    if not args.no_min_items_check and not errors and total_items <= MIN_ITEMS:
        errors.append(
            f"combined total across {len(targets)} file(s) is only {total_items} Item row(s); "
            f"the checklist you design must have more than {MIN_ITEMS} in total (pass every screen's "
            "checklist.md together in one invocation, or use --no-min-items-check while iterating on "
            "a single screen)"
        )

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Validation passed: {len(targets)} file(s), {total_items} total Item row(s) across clean files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
