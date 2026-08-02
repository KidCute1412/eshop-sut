"""Apply verified runtime results to the canonical HW03 checklist CSV."""

from __future__ import annotations

import csv
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
CHECKLIST = REPO / "docs/assignments/HW03/deliverables/checklist/gui_checklist.csv"
RESULTS = HERE / "results/execution_results.json"


def main() -> None:
    payload = json.loads(RESULTS.read_text(encoding="utf-8"))
    runtime_results = {item["id"]: item for item in payload["results"]}

    with CHECKLIST.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        fieldnames = reader.fieldnames
        rows = list(reader)

    if not fieldnames:
        raise SystemExit("Checklist has no header")
    if len(rows) != 45 or len(runtime_results) != 45:
        raise SystemExit(
            f"Expected 45 checklist and runtime rows; got {len(rows)} and {len(runtime_results)}"
        )

    for row in rows:
        item_id = row["Item ID"]
        result = runtime_results[item_id]
        if row["FR ID"] == "FR-23":
            row["FR ID"] = "Pool D"
        row["Actual Result"] = result["actual"]
        row["Status"] = result["status"]
        row["Bug ID"] = result["bugId"] or "N/A"
        if result["status"] == "Not Executed":
            row["Notes"] = result["notes"]
        else:
            detail = result["notes"].strip()
            row["Notes"] = "Executed twice on Google Chrome 151 / Windows." + (
                f" {detail}" if detail else ""
            )
        row["Evidence Reference"] = result["evidence"]

    with CHECKLIST.open("w", encoding="utf-8-sig", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)

    counts: dict[str, int] = {}
    for row in rows:
        counts[row["Status"]] = counts.get(row["Status"], 0) + 1
    print(json.dumps(counts, ensure_ascii=False))


if __name__ == "__main__":
    main()
