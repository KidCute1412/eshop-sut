"""Generate submission PDFs and workbooks from canonical Markdown/CSV sources."""

from __future__ import annotations

import csv
import re
from pathlib import Path
from xml.sax.saxutils import escape

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


HW03_ROOT = Path(__file__).resolve().parents[1]
DELIVERABLES = HW03_ROOT / "deliverables"
AUTHOR = "Lê Tuấn Lộc (23127404)"


def register_font() -> str:
    for path in (
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/calibri.ttf"),
        Path("C:/Windows/Fonts/segoeui.ttf"),
    ):
        if path.exists():
            pdfmetrics.registerFont(TTFont("SubmissionFont", str(path)))
            return "SubmissionFont"
    return "Helvetica"


def inline_markdown(value: str) -> str:
    value = escape(value.strip())
    value = re.sub(r"`([^`]*)`", r"<font name='Courier'>\1</font>", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", value)
    value = re.sub(r"\[([^]]+)]\(([^)]+)\)", r"<link href='\2'>\1</link>", value)
    return value


def page_footer(canvas, document) -> None:
    canvas.saveState()
    canvas.setFont("SubmissionFont", 8)
    canvas.setFillColor(colors.HexColor("#475569"))
    canvas.drawString(16 * mm, 10 * mm, AUTHOR)
    canvas.drawRightString(A4[0] - 16 * mm, 10 * mm, f"Page {document.page}")
    canvas.restoreState()


def markdown_to_pdf(source: Path, target: Path, title: str) -> None:
    font = register_font()
    styles = getSampleStyleSheet()
    body = ParagraphStyle("Body", parent=styles["BodyText"], fontName=font, fontSize=9.5, leading=13, spaceAfter=5)
    quote = ParagraphStyle("Quote", parent=body, leftIndent=7 * mm, textColor=colors.HexColor("#475569"), borderColor=colors.HexColor("#CBD5E1"), borderWidth=0.5, borderPadding=5)
    table_cell = ParagraphStyle("TableCell", parent=body, fontSize=7.5, leading=9, spaceAfter=0)
    headings = {
        1: ParagraphStyle("H1", parent=styles["Heading1"], fontName=font, fontSize=18, leading=22, alignment=TA_CENTER, textColor=colors.HexColor("#0F172A"), spaceAfter=12),
        2: ParagraphStyle("H2", parent=styles["Heading2"], fontName=font, fontSize=13, leading=16, textColor=colors.HexColor("#1D4ED8"), spaceBefore=10, spaceAfter=6),
        3: ParagraphStyle("H3", parent=styles["Heading3"], fontName=font, fontSize=11, leading=14, textColor=colors.HexColor("#334155"), spaceBefore=7, spaceAfter=4),
    }
    lines = source.read_text(encoding="utf-8").splitlines()
    story = []
    index = 0
    while index < len(lines):
        line = lines[index].rstrip()
        if not line or re.fullmatch(r"---+", line):
            story.append(Spacer(1, 2 * mm)); index += 1; continue
        heading = re.match(r"^(#{1,3})\s+(.*)$", line)
        if heading:
            story.append(Paragraph(inline_markdown(heading.group(2)), headings[len(heading.group(1))])); index += 1; continue
        if line.startswith("|"):
            rows = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                    rows.append([Paragraph(inline_markdown(cell), table_cell) for cell in cells])
                index += 1
            if rows:
                table = Table(rows, repeatRows=1, hAlign="LEFT")
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E78")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, -1), font),
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CBD5E1")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]))
                story.append(table)
            continue
        if re.match(r"^[-*]\s+", line):
            items = []
            while index < len(lines) and re.match(r"^[-*]\s+", lines[index].strip()):
                items.append(ListItem(Paragraph(inline_markdown(re.sub(r"^[-*]\s+", "", lines[index].strip())), body)))
                index += 1
            story.append(ListFlowable(items, bulletType="bullet", leftIndent=14)); continue
        if line.startswith(">"):
            story.append(Paragraph(inline_markdown(line.lstrip("> ")), quote)); index += 1; continue
        story.append(Paragraph(inline_markdown(line), body)); index += 1

    document = SimpleDocTemplate(
        str(target), pagesize=A4, title=title, author=AUTHOR,
        rightMargin=16 * mm, leftMargin=16 * mm, topMargin=16 * mm, bottomMargin=16 * mm,
    )
    document.build(story, onFirstPage=page_footer, onLaterPages=page_footer)


def csv_to_xlsx(source: Path, target: Path, sheet_name: str, landscape_mode: bool = False) -> None:
    with source.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.reader(handle))
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for row in rows:
        sheet.append(row)
    header_fill = PatternFill("solid", fgColor="1F4E78")
    status_fills = {"Pass": "E2F0D9", "Fail": "FCE4D6", "Not Executed": "FFF2CC"}
    for cell in sheet[1]:
        cell.font = Font(color="FFFFFF", bold=True)
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    headers = {cell.value: cell.column for cell in sheet[1]}
    status_column = headers.get("Status") or headers.get("Status (Pass/Fail)")
    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True)
        if status_column:
            status_cell = sheet.cell(row=row[0].row, column=status_column)
            if status_cell.value in status_fills:
                status_cell.fill = PatternFill("solid", fgColor=status_fills[status_cell.value])
    for number, column in enumerate(sheet.columns, 1):
        maximum = max(len(str(cell.value or "")) for cell in column)
        sheet.column_dimensions[get_column_letter(number)].width = min(max(maximum + 2, 11), 42)
    sheet.freeze_panes = "A2"
    sheet.auto_filter.ref = sheet.dimensions
    sheet.print_title_rows = "1:1"
    sheet.print_area = sheet.dimensions
    sheet.page_setup.orientation = "landscape" if landscape_mode else "portrait"
    sheet.page_setup.fitToWidth = 1
    sheet.sheet_properties.pageSetUpPr.fitToPage = True
    workbook.save(target)


def main() -> None:
    csv_to_xlsx(DELIVERABLES / "checklist/gui_checklist.csv", DELIVERABLES / "checklist/gui_checklist.xlsx", "GUI Checklist", True)
    csv_to_xlsx(DELIVERABLES / "usability/sus_survey_results.csv", DELIVERABLES / "usability/sus_survey_results.xlsx", "SUS Results", True)
    markdown_to_pdf(DELIVERABLES / "main_report.md", DELIVERABLES / "main_report.pdf", "HW03 — GUI and Usability Testing")
    markdown_to_pdf(DELIVERABLES / "ai_reports/ai_audit_report.md", DELIVERABLES / "ai_reports/ai_audit_report.pdf", "HW03 — AI Audit Report")
    markdown_to_pdf(DELIVERABLES / "ai_reports/ai_critique.md", DELIVERABLES / "ai_reports/ai_critique.pdf", "HW03 — AI Critique")
    print("Generated two workbooks and three PDFs.")


if __name__ == "__main__":
    main()

