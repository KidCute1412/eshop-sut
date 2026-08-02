"""Validate and calculate the canonical HW03 SUS CSV without inventing responses."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "deliverables/usability/sus_survey_results.csv"
QUESTION_FIELDS = [f"q{number}" for number in range(1, 11)]


def calculate(responses: list[int]) -> tuple[int, float]:
    contributions = [
        response - 1 if index % 2 == 1 else 5 - response
        for index, response in enumerate(responses, start=1)
    ]
    adjusted = sum(contributions)
    return adjusted, adjusted * 2.5


def process(source: Path, write: bool) -> None:
    with source.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    expected = {"participant_id", *QUESTION_FIELDS, "adjusted_sum", "sus_score", "status"}
    missing = expected - set(fieldnames)
    if missing:
        raise ValueError(f"Missing SUS columns: {sorted(missing)}")

    scores: list[float] = []
    for row in rows:
        participant = row["participant_id"]
        if participant == "AVERAGE":
            continue
        raw = [row[field].strip() for field in QUESTION_FIELDS]
        if not any(raw):
            row["adjusted_sum"] = ""
            row["sus_score"] = ""
            row["status"] = "Not collected"
            continue
        if not all(raw):
            raise ValueError(f"{participant}: SUS response is incomplete")
        responses = [int(value) for value in raw]
        if any(value < 1 or value > 5 for value in responses):
            raise ValueError(f"{participant}: every SUS response must be from 1 to 5")
        adjusted, score = calculate(responses)
        row["adjusted_sum"] = str(adjusted)
        row["sus_score"] = f"{score:.1f}"
        row["status"] = "Calculated"
        scores.append(score)

    average = next((row for row in rows if row["participant_id"] == "AVERAGE"), None)
    if average is None:
        raise ValueError("AVERAGE row is missing")
    average["sus_score"] = f"{sum(scores) / len(scores):.1f}" if scores else ""
    average["status"] = "Calculated" if len(scores) == 7 else "Not calculated"

    if write:
        with source.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    print(f"Valid completed SUS responses: {len(scores)}/7")
    print(f"Official average: {average['sus_score'] or 'Not calculated'}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--write", action="store_true", help="Write calculated fields to the source CSV")
    arguments = parser.parse_args()
    process(arguments.source, arguments.write)


if __name__ == "__main__":
    main()
