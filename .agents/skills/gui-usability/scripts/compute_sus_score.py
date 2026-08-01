#!/usr/bin/env python3
"""Compute System Usability Scale (SUS) scores from raw per-item Likert responses.

Input CSV format (header required):
    Participant,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10
    P01,4,2,5,1,4,2,5,1,5,2
    ...

Odd items (1,3,5,7,9) contribute (score-1); even items (2,4,6,8,10) contribute (5-score).
SUS score = sum(contributions) * 2.5, range 0-100.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

from _table_utils import ensure_utf8_stdio

ODD_ITEMS = {1, 3, 5, 7, 9}
EVEN_ITEMS = {2, 4, 6, 8, 10}
EXPECTED_COLUMNS = ["Participant"] + [f"Q{i}" for i in range(1, 11)]


def sus_score(responses: list[int]) -> float:
    if len(responses) != 10:
        raise ValueError(f"expected 10 responses, got {len(responses)}")
    total = 0
    for item_number, score in enumerate(responses, 1):
        if not (1 <= score <= 5):
            raise ValueError(f"Q{item_number} score {score} is out of the 1-5 range")
        if item_number in ODD_ITEMS:
            total += score - 1
        else:
            total += 5 - score
    return total * 2.5


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Compute SUS scores from a CSV of raw responses.")
    parser.add_argument("--input", required=True, help="CSV file with columns Participant,Q1..Q10.")
    parser.add_argument("--expect-count", type=int, default=7, help="Required number of participant rows (default 7; the assignment requires 7 real sessions).")
    parser.add_argument("--allow-any-count", action="store_true", help="Skip the participant-count check (useful for partial/pilot runs).")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.is_file():
        print(f"ERROR: input file not found: {path}", file=sys.stderr)
        return 2

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_COLUMNS:
            print(
                f"ERROR: expected header {','.join(EXPECTED_COLUMNS)}, got "
                f"{','.join(reader.fieldnames or [])}",
                file=sys.stderr,
            )
            return 2
        rows = list(reader)

    if not rows:
        print("ERROR: no participant rows found.", file=sys.stderr)
        return 2

    if not args.allow_any_count and len(rows) != args.expect_count:
        print(
            f"ERROR: expected {args.expect_count} participant rows, found {len(rows)}. "
            "Use --allow-any-count to bypass for partial runs.",
            file=sys.stderr,
        )
        return 2

    scores: list[float] = []
    for row in rows:
        try:
            responses = [int(row[f"Q{i}"]) for i in range(1, 11)]
            score = sus_score(responses)
        except (KeyError, ValueError) as exc:
            print(f"ERROR: {row.get('Participant', '?')}: {exc}", file=sys.stderr)
            return 2
        scores.append(score)
        print(f"{row['Participant']}: SUS = {score:.1f}")

    mean_score = sum(scores) / len(scores)
    print(f"Mean SUS across {len(scores)} participant(s): {mean_score:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
