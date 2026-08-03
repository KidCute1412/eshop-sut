"""Generate submission PDFs and workbooks from canonical Markdown/CSV sources."""

from __future__ import annotations

import csv
import re
from pathlib import Path
from xml.sax.saxutils import escape

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation
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
DATA = HW03_ROOT / "workbench/data"
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
    status_fills = {"Pass": "E2F0D9", "Passed": "E2F0D9", "Fail": "FCE4D6", "Failed": "FCE4D6", "Not Executed": "FFF2CC"}
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


def checklist_to_xlsx(source: Path, target: Path) -> None:
    csv_to_xlsx(source, target, "GUI Checklist", True)
    workbook = load_workbook(target)
    checklist = workbook["GUI Checklist"]
    summary = workbook.create_sheet("Test Summary", 0)
    last_row = checklist.max_row
    summary_rows = [
        ("HW03 GUI Checklist Summary", "Current classified result"),
        ("Designed", f"=COUNTA('GUI Checklist'!A2:A{last_row})"),
        ("Executed", f'=COUNTIF(\'GUI Checklist\'!I2:I{last_row},"Passed")+COUNTIF(\'GUI Checklist\'!I2:I{last_row},"Failed")'),
        ("Passed", f'=COUNTIF(\'GUI Checklist\'!I2:I{last_row},"Passed")'),
        ("Failed", f'=COUNTIF(\'GUI Checklist\'!I2:I{last_row},"Failed")'),
        ("Not Executed", f'=COUNTIF(\'GUI Checklist\'!I2:I{last_row},"Not Executed")'),
        ("Unique defects", 19),
        ("", ""),
        ("Requirement coverage", "Items"),
        ("FR-07", f'=COUNTIF(\'GUI Checklist\'!B2:B{last_row},"FR-07")'),
        ("FR-10", f'=COUNTIF(\'GUI Checklist\'!B2:B{last_row},"FR-10")'),
        ("FR-11", f'=COUNTIF(\'GUI Checklist\'!B2:B{last_row},"FR-11")'),
        ("FR-18", f'=COUNTIF(\'GUI Checklist\'!B2:B{last_row},"FR-18")'),
        ("FR-23", f'=COUNTIF(\'GUI Checklist\'!B2:B{last_row},"FR-23")'),
        ("", ""),
        ("Interface-aspect coverage", "Items"),
        ("IA-01 General UI", f'=COUNTIF(\'GUI Checklist\'!C2:C{last_row},"IA-01 General UI")'),
        ("IA-02 Forms & Validation", f'=COUNTIF(\'GUI Checklist\'!C2:C{last_row},"IA-02 Forms & Validation")'),
        ("IA-03 Navigation", f'=COUNTIF(\'GUI Checklist\'!C2:C{last_row},"IA-03 Navigation")'),
        ("IA-04 Feedback & State", f'=COUNTIF(\'GUI Checklist\'!C2:C{last_row},"IA-04 Feedback & State")'),
        ("", ""),
        ("Design provenance", "Items"),
        ("AI", f'=COUNTIF(\'GUI Checklist\'!L2:L{last_row},"AI")'),
        ("Human-added", f'=COUNTIF(\'GUI Checklist\'!L2:L{last_row},"Human-added")'),
        ("Hybrid", f'=COUNTIF(\'GUI Checklist\'!L2:L{last_row},"Hybrid")'),
        ("", ""),
        ("Evidence note", "PDF requires screenshots for Failed items; all 20 Failed rows have evidence and Bug IDs."),
        ("Desktop execution", "Google Chrome 151.0.7922.72 / Windows 11 / two clean runs / 2 August 2026"),
        ("Mobile evidence", "Four authentic 1284×2778 captures; exact device metadata and required identity overlay remain to be supplied."),
    ]
    for row in summary_rows:
        summary.append(row)

    navy = "1F4E78"
    section_fill = "D9EAF7"
    thin = Side(style="thin", color="CBD5E1")
    for row in summary.iter_rows():
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            cell.border = Border(bottom=thin)
    for row_number in (1, 9, 16, 22):
        for cell in summary[row_number]:
            cell.font = Font(color="FFFFFF" if row_number == 1 else "1F2937", bold=True)
            cell.fill = PatternFill("solid", fgColor=navy if row_number == 1 else section_fill)
    summary.freeze_panes = "A2"
    summary.auto_filter.ref = summary.dimensions
    summary.column_dimensions["A"].width = 30
    summary.column_dimensions["B"].width = 88
    summary.row_dimensions[1].height = 26
    summary.sheet_view.showGridLines = False
    summary.sheet_view.zoomScale = 90

    checklist.row_dimensions[1].height = 36
    checklist.sheet_view.showGridLines = False
    checklist.sheet_view.zoomScale = 80
    checklist.auto_filter.ref = checklist.dimensions
    checklist.print_title_rows = "1:1"
    checklist.sheet_properties.pageSetUpPr.fitToPage = True
    checklist.page_setup.fitToWidth = 1
    checklist.page_setup.fitToHeight = 0
    checklist.page_margins.left = 0.25
    checklist.page_margins.right = 0.25
    checklist.page_margins.top = 0.5
    checklist.page_margins.bottom = 0.5

    status_validation = DataValidation(type="list", formula1='"Passed,Failed,Not Executed"', allow_blank=False)
    fr_validation = DataValidation(type="list", formula1='"FR-07,FR-10,FR-11,FR-18,FR-23"', allow_blank=False)
    origin_validation = DataValidation(type="list", formula1='"AI,Human-added,Hybrid"', allow_blank=False)
    for validation in (status_validation, fr_validation, origin_validation):
        checklist.add_data_validation(validation)
    status_validation.add(f"I2:I{last_row}")
    fr_validation.add(f"B2:B{last_row}")
    origin_validation.add(f"L2:L{last_row}")

    for row_number in range(2, last_row + 1):
        evidence = checklist.cell(row=row_number, column=15)
        raw = str(evidence.value or "").strip()
        if raw and ";" not in raw and "://" not in raw:
            evidence.hyperlink = "../" + raw.replace("\\", "/")
            evidence.style = "Hyperlink"
        checklist.row_dimensions[row_number].height = 72

    workbook.calculation.calcMode = "auto"
    workbook.calculation.fullCalcOnLoad = True
    workbook.calculation.forceFullCalc = True
    workbook.save(target)


def sus_csv_to_xlsx(source: Path, target: Path) -> None:
    csv_to_xlsx(source, target, "SUS Results", True)
    workbook = load_workbook(target)
    sheet = workbook.active
    validation = DataValidation(type="whole", operator="between", formula1="1", formula2="5", allow_blank=True)
    validation.error = "Enter a whole-number SUS response from 1 to 5."
    validation.errorTitle = "Invalid SUS response"
    validation.prompt = "Enter 1 (strongly disagree) through 5 (strongly agree)."
    validation.promptTitle = "SUS response"
    validation.showErrorMessage = True
    validation.showInputMessage = True
    sheet.add_data_validation(validation)
    validation.add("B2:K8")

    for row in range(2, 9):
        contributions = []
        for question, column in enumerate(range(2, 12), start=1):
            reference = f"{get_column_letter(column)}{row}"
            contributions.append(f"{reference}-1" if question % 2 else f"5-{reference}")
        sheet[f"L{row}"] = f'=IF(COUNTA(B{row}:K{row})=0,"",IF(COUNTA(B{row}:K{row})<10,"INCOMPLETE",SUM({",".join(contributions)})))'
        sheet[f"M{row}"] = f'=IF(ISNUMBER(L{row}),L{row}*2.5,"")'
        sheet[f"R{row}"] = f'=IF(COUNTA(B{row}:K{row})=0,"Not collected",IF(COUNTA(B{row}:K{row})<10,"Incomplete","Calculated"))'

    sheet["M9"] = '=IF(COUNT(M2:M8)=7,AVERAGE(M2:M8),"")'
    sheet["R9"] = '=IF(COUNT(M2:M8)=7,"Calculated","Not calculated")'
    sheet.freeze_panes = "A2"
    workbook.calculation.fullCalcOnLoad = True
    workbook.calculation.forceFullCalc = True
    workbook.save(target)


def usability_results_to_xlsx(target: Path) -> None:
    """Build one submission workbook containing every usability data table."""
    shared_recording_url = "https://drive.google.com/drive/u/0/folders/1_3wIHUVqJGG-mPwcZotoAStgRjd6X9x_"
    session_source = DATA / "session_results.csv"
    sus_source = DATA / "sus_survey_results.csv"
    workbook = Workbook()

    def add_csv_sheet(source: Path, name: str):
        sheet = workbook.active if len(workbook.sheetnames) == 1 and workbook.active.max_row == 1 and workbook.active["A1"].value is None else workbook.create_sheet()
        sheet.title = name
        if sheet.max_row == 1 and sheet["A1"].value is None:
            sheet.delete_rows(1)
        with source.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.reader(handle):
                sheet.append(row)
        return sheet

    sessions = add_csv_sheet(session_source, "Sessions")
    observations = workbook.create_sheet("Observations")
    observations.append(["session_id", "checkpoint", "timestamp", "outcome", "observed_action_or_quote", "error", "hesitation", "intervention", "evidence_status"])
    checkpoints = ["Product List", "Product Detail", "Add to Cart", "Cart", "Checkout", "Order submission", "Post-checkout cart", "Order History"]
    for session_id in ["Pilot", "P1", "P2", "P3", "P4", "P5", "P6", "P7"]:
        for checkpoint in checkpoints:
            observations.append([session_id, checkpoint, "", "To be coded from video", "", "", "", "", "Awaiting video"])

    sus = add_csv_sheet(sus_source, "SUS")
    recordings = workbook.create_sheet("Recordings")
    recordings.append([
        "session_id", "filename", "drive_folder_url", "duration_seconds",
        "file_size_bytes", "sha256", "resolution", "local_verified",
        "drive_access_verified", "status",
    ])
    recording_manifest = [
        ("Pilot", "Pilot.mp4", 73.600, 1205683, "B34A705CB99820C43741C6595391D2715479783160AFE2AEB76067E17CD65C3A"),
        ("P1", "P1.mp4", 96.467, 1051696, "373372F85253EC6C783A1501A760E65E39EF0E11C937F71E0A67C4C22A6D04AB"),
        ("P2", "P2.mp4", 72.100, 968087, "FD92D109F10C2FDF5E1C6F8263A4EB3462DA4AB3D4EA60BE3F813A1B8C9C5BC9"),
        ("P3", "P3.mp4", 67.767, 891790, "DAA85393B6BACB5370D57E1086562BF7907EC3BEFFB2580C38F9EC1FEA75BA55"),
        ("P4", "P4.mp4", 63.467, 1452706, "D1089B51D4BB25E0981A85BA9D79F5040078D4240B42B28FBDF78302BEEF50EE"),
        ("P5", "P5.mp4", 108.433, 1506431, "B5F850BF0A2FBDC191481C18E42DE9144B213BDB34789EBEA4A0DD6BAFB63CE9"),
        ("P6", "P6.mp4", 63.633, 715887, "E41A12B239754E8864234442D56B1E7F20320D83C662B3CB32AFBC30D1AC5C60"),
        ("P7", "P7.mp4", 82.200, 1014487, "E4712473D8A3E2A4DF4CAE61F4835A653FE5B8D621210C0E92654AB23FF8CA95"),
    ]
    for session_id, filename, duration, size, sha256 in recording_manifest:
        recordings.append([session_id, filename, shared_recording_url, duration, size, sha256, "1920x1080", "Yes", "Yes - publicly listed", "Local file and public Drive listing verified on 3 August 2026"])

    for session_row, sus_row in zip(range(3, 10), range(2, 9)):
        sessions[f"J{session_row}"] = f"=SUS!M{sus_row}"

    header_fill = PatternFill("solid", fgColor="1F4E78")
    for sheet in workbook.worksheets:
        for cell in sheet[1]:
            cell.font = Font(color="FFFFFF", bold=True)
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        for row in sheet.iter_rows(min_row=2):
            for cell in row:
                cell.alignment = Alignment(vertical="top", wrap_text=True)
        for number, column in enumerate(sheet.columns, 1):
            maximum = max(len(str(cell.value or "")) for cell in column)
            sheet.column_dimensions[get_column_letter(number)].width = min(max(maximum + 2, 11), 42)
        sheet.freeze_panes = "A2"
        sheet.auto_filter.ref = sheet.dimensions
        sheet.print_title_rows = "1:1"
        sheet.print_area = sheet.dimensions
        sheet.page_setup.orientation = "landscape"
        sheet.page_setup.fitToWidth = 1
        sheet.sheet_properties.pageSetUpPr.fitToPage = True

    validation = DataValidation(type="whole", operator="between", formula1="1", formula2="5", allow_blank=True)
    validation.error = "Enter a whole-number SUS response from 1 to 5."
    validation.errorTitle = "Invalid SUS response"
    validation.showErrorMessage = True
    sus.add_data_validation(validation)
    validation.add("B2:K8")
    for row in range(2, 9):
        contributions = []
        for question, column in enumerate(range(2, 12), start=1):
            reference = f"{get_column_letter(column)}{row}"
            contributions.append(f"{reference}-1" if question % 2 else f"5-{reference}")
        sus[f"L{row}"] = f'=IF(COUNTA(B{row}:K{row})=0,"",IF(COUNTA(B{row}:K{row})<10,"INCOMPLETE",SUM({",".join(contributions)})))'
        sus[f"M{row}"] = f'=IF(ISNUMBER(L{row}),L{row}*2.5,"")'
        sus[f"R{row}"] = f'=IF(COUNTA(B{row}:K{row})=0,"Not collected",IF(COUNTA(B{row}:K{row})<10,"Incomplete","Calculated"))'
    sus["M9"] = '=IF(COUNT(M2:M8)=7,AVERAGE(M2:M8),"")'
    sus["R9"] = '=IF(COUNT(M2:M8)=7,"Calculated","Not calculated")'
    workbook.calculation.fullCalcOnLoad = True
    workbook.calculation.forceFullCalc = True
    workbook.save(target)


def main() -> None:
    checklist_to_xlsx(DATA / "gui_checklist.csv", DELIVERABLES / "checklist/gui_checklist.xlsx")
    # The submission workbook contains reviewed observation coding and recording
    # metadata that are not fully represented by the compact CSV sources. Preserve
    # the reviewed workbook during routine PDF/checklist regeneration.
    usability_target = DELIVERABLES / "usability/usability_results.xlsx"
    if not usability_target.exists():
        usability_results_to_xlsx(usability_target)
    markdown_to_pdf(DELIVERABLES / "main_report.md", DELIVERABLES / "main_report.pdf", "HW03 — GUI and Usability Testing")
    markdown_to_pdf(DELIVERABLES / "ai_reports/ai_audit_report.md", DELIVERABLES / "ai_reports/ai_audit_report.pdf", "HW03 — AI Audit Report")
    markdown_to_pdf(DELIVERABLES / "ai_reports/ai_critique.md", DELIVERABLES / "ai_reports/ai_critique.pdf", "HW03 — AI Critique")
    print("Generated two workbooks and three PDFs.")


if __name__ == "__main__":
    main()
