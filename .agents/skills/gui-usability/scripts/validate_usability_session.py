#!/usr/bin/env python3
"""Read-only validator for Task 2 usability-evaluation Markdown artifacts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _table_utils import ensure_utf8_stdio, is_empty_or_placeholder, parse_fields, parse_table

PARTICIPANT_HEADER = [
    "#",
    "Name",
    "Contact (Zalo/Email/Phone, masked)",
    "Profile Notes",
    "Confirmed Outside Class",
    "Session Date",
    "Session Type",
    "Consent to Record",
]

OBSERVATION_HEADER = [
    "Timestamp",
    "Observation (friction, error, hesitation, verbalized frustration/quote)",
    "Screen/Step",
]

SUS_HEADER = ["#", "Statement", "Score (1-5)"]
UEQS_HEADER = ["#", "Item Pair (-3 .. +3)", "Score"]

REQUIRED_SESSION_IDS = ("P01", "P02", "P03", "P04", "P05", "P06", "P07")
REQUIRED_SESSION_FIELDS = (
    "Date and Time",
    "Environment",
    "Completed",
    "Clarity",
    "Error recovery",
    "Speed",
    "Trust",
)


def contact_is_properly_masked(contact: str) -> bool:
    """Accept an email address as-is; require phone/Zalo numbers to be masked."""
    value = contact.strip()
    if "@" in value:
        return True
    if any(ch.isdigit() for ch in value):
        return "*" in value
    return False


def validate_participants(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"{path}: participants file not found"]
    text = path.read_text(encoding="utf-8")
    rows = parse_table(text, PARTICIPANT_HEADER)
    if not rows:
        return [f"{path}: zero participant rows parsed"]

    real_sessions = [r for r in rows if r.get("Session Type", "").strip() == "Real Session"]
    pilot_sessions = [r for r in rows if r.get("Session Type", "").strip() == "Pilot"]

    if len(real_sessions) != 7:
        errors.append(f"{path}: expected exactly 7 'Real Session' rows, found {len(real_sessions)}")
    if not pilot_sessions:
        errors.append(f"{path}: expected at least 1 'Pilot' row, found 0")

    for row in rows:
        label = row.get("Name", "") or f"row {row.get('#', '?')}"
        if is_empty_or_placeholder(row.get("Name", "")):
            errors.append(f"{path}: {label}: Name is empty or a placeholder")
        contact = row.get("Contact (Zalo/Email/Phone, masked)", "")
        if is_empty_or_placeholder(contact):
            errors.append(f"{path}: {label}: Contact is empty or a placeholder")
        elif not contact_is_properly_masked(contact):
            errors.append(f"{path}: {label}: phone/Zalo contact must mask digits with '*', got '{contact}'")
        if row.get("Confirmed Outside Class", "").strip() != "Yes":
            errors.append(f"{path}: {label}: Confirmed Outside Class must be 'Yes'")

    return errors


def sus_table_complete(text: str) -> bool:
    rows = parse_table(text, SUS_HEADER)
    if len(rows) != 10:
        return False
    for row in rows:
        score = row.get("Score (1-5)", "").strip()
        if not score.isdigit() or not (1 <= int(score) <= 5):
            return False
    return True


def ueqs_table_complete(text: str) -> bool:
    rows = parse_table(text, UEQS_HEADER)
    if len(rows) != 8:
        return False
    for row in rows:
        score = row.get("Score", "").strip()
        try:
            value = int(score)
        except ValueError:
            return False
        if not (-3 <= value <= 3):
            return False
    return True


def validate_session(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"{path}: session file not found"]
    text = path.read_text(encoding="utf-8")
    fields = parse_fields(text)

    for field in REQUIRED_SESSION_FIELDS:
        if field not in fields or is_empty_or_placeholder(fields[field]):
            errors.append(f"{path}: missing, empty, or placeholder field '{field}'")

    observations = parse_table(text, OBSERVATION_HEADER)
    real_observations = [
        row for row in observations
        if not is_empty_or_placeholder(row.get("Observation (friction, error, hesitation, verbalized frustration/quote)", ""))
    ]
    if not real_observations:
        errors.append(f"{path}: Observation Log has no real (non-placeholder) rows")

    if not sus_table_complete(text) and not ueqs_table_complete(text):
        errors.append(f"{path}: neither the SUS table (10 items, 1-5) nor the UEQ-S table (8 items, -3..3) is fully completed")

    return errors


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Validate Task 2 usability-evaluation Markdown artifacts.")
    parser.add_argument("root", help="usability-evaluation workspace directory (contains participants.md and session-notes/).")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 2

    errors = validate_participants(root / "participants.md")

    session_dir = root / "session-notes"
    if not session_dir.is_dir():
        errors.append(f"{session_dir}: session-notes directory not found")
    else:
        for session_id in REQUIRED_SESSION_IDS:
            errors.extend(validate_session(session_dir / f"{session_id}.md"))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Validation passed: participants.md and {len(REQUIRED_SESSION_IDS)} session file(s) are complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
