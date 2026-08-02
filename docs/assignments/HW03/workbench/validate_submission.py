"""Validate internal consistency of the current HW03 deliverables."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

from openpyxl import load_workbook
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[4]
DELIVERABLES = ROOT / "docs/assignments/HW03/deliverables"
errors: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


with (DELIVERABLES / "checklist/gui_checklist.csv").open(
    encoding="utf-8-sig", newline=""
) as source:
    rows = list(csv.DictReader(source))

require(len(rows) == 45, f"Checklist must contain 45 rows; found {len(rows)}")
counts = Counter(row["Status"] for row in rows)
require(counts == {"Passed": 16, "Failed": 15, "Not Executed": 14}, f"Unexpected status counts: {counts}")
require(all(row["Actual Result"].strip() for row in rows), "Every checklist row needs an actual result")
require(all(row["Notes"].strip() for row in rows), "Every checklist row needs execution or non-execution notes")
require(not any(row["FR ID"] == "FR-23" for row in rows), "Unsupported FR-23 remains in checklist")
require(sum(row["FR ID"] == "Pool D" for row in rows) == 8, "Expected eight Pool D rows")

failed_ids: set[str] = set()
for row in rows:
    item_id = row["Item ID"]
    if row["Status"] == "Failed":
        require(row["Bug ID"].startswith("BUG-"), f"{item_id} lacks Bug ID")
        require(bool(row["Evidence Reference"]), f"{item_id} lacks evidence reference")
        if row["Evidence Reference"]:
            require((DELIVERABLES / row["Evidence Reference"]).is_file(), f"Missing evidence for {item_id}")
        failed_ids.add(row["Bug ID"])
    elif row["Status"] == "Passed":
        require(row["Bug ID"] == "N/A", f"Passed {item_id} must not map to a bug")
        require(not row["Evidence Reference"], f"Passed {item_id} must not include failed-item evidence")
    else:
        require("physical device" in row["Notes"] or "Mobile app" in row["Notes"], f"{item_id} lacks a qualifying Mobile reason")

bug_report = (DELIVERABLES / "bugs/bug_report.md").read_text(encoding="utf-8")
verified_headings = set(re.findall(r"^### (BUG-\d{3}) —", bug_report, flags=re.MULTILINE))
require(verified_headings == failed_ids, f"Bug headings differ from failed rows: {verified_headings ^ failed_ids}")
require("Verified defects | 15" in bug_report, "Bug summary count missing")

bug_pngs = sorted((DELIVERABLES / "bugs/evidence_images").glob("*.png"))
chrome_pngs = sorted((DELIVERABLES / "cross_platform/chrome_desktop").glob("*.png"))
firefox_pngs = sorted((DELIVERABLES / "cross_platform/firefox_desktop").glob("*.png"))
mobile_pngs = sorted((DELIVERABLES / "cross_platform/mobile_real_device").glob("*.png"))
require(len(bug_pngs) == 15, f"Expected 15 bug PNGs; found {len(bug_pngs)}")
require(len(chrome_pngs) == 5, f"Expected 5 Chrome PNGs; found {len(chrome_pngs)}")
require(not firefox_pngs, "Firefox screenshots must not be claimed")
require(not mobile_pngs, "Mobile screenshots must not be generated")

readme = (DELIVERABLES / "README.md").read_text(encoding="utf-8")
for expected in ("| Checklist items executed | 31 |", "| Passed | 16 |", "| Failed | 15 |", "| Not executed | 14 Mobile-dependent items |", "| Verified defects | 15"):
    require(expected in readme, f"README missing summary: {expected}")

critique = (DELIVERABLES / "ai_reports/ai_critique.md").read_text(encoding="utf-8")
critique_words = len(re.findall(r"\b[\w’'-]+\b", re.sub(r"^#.*$", "", critique, flags=re.MULTILINE), flags=re.UNICODE))
require(200 <= critique_words <= 300, f"AI Critique has {critique_words} words")

for path in DELIVERABLES.rglob("*"):
    if path.is_file() and path.suffix.lower() in {".md", ".csv", ".txt"}:
        try:
            path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError as exc:
            errors.append(f"UTF-8 error in {path.relative_to(DELIVERABLES)}: {exc}")

for rel, rows_expected, cols_expected in (
    ("checklist/gui_checklist.xlsx", 46, 12),
    ("usability/sus_survey_results.xlsx", 9, 18),
):
    workbook = load_workbook(DELIVERABLES / rel, read_only=False)
    sheet = workbook.active
    require(sheet.max_row == rows_expected, f"{rel} row count is {sheet.max_row}")
    require(sheet.max_column == cols_expected, f"{rel} column count is {sheet.max_column}")
    require(sheet.freeze_panes == "A2", f"{rel} should freeze A2")
    require(bool(sheet.auto_filter.ref), f"{rel} lacks an auto-filter")
    require(bool(sheet.print_area), f"{rel} lacks a print area")

for rel in ("main_report.pdf", "ai_reports/ai_audit_report.pdf", "ai_reports/ai_critique.pdf"):
    reader = PdfReader(DELIVERABLES / rel)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    require("23127404" in text, f"{rel} lacks student ID")
    require("|---" not in text, f"{rel} contains raw Markdown table syntax")
    require(reader.metadata and reader.metadata.title, f"{rel} lacks title metadata")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("VALIDATION PASSED")
print(f"Checklist: {dict(counts)}")
print(f"Verified bugs/screenshots: {len(failed_ids)}/{len(bug_pngs)}")
print(f"Chrome/Firefox/Mobile screenshots: {len(chrome_pngs)}/{len(firefox_pngs)}/{len(mobile_pngs)}")
print(f"AI Critique words: {critique_words}")
