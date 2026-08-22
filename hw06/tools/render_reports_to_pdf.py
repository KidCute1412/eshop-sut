from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak


ROOT = Path(__file__).resolve().parents[2]
SUBMIT = ROOT / "hw06" / "submit"


def clean(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("`", "")
    )


def markdown_to_story(md_text: str, title: str):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="CodeBlockSmall", parent=styles["BodyText"], fontName="Courier", fontSize=8, leading=10))
    story = [Paragraph(clean(title), styles["Title"]), Spacer(1, 6 * mm)]
    in_code = False
    table_rows = []

    def flush_table():
        nonlocal table_rows
        if not table_rows:
            return
        table = Table(table_rows, repeatRows=1)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF7")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#111827")),
            ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#CBD5E1")),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 7),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 3),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ]))
        story.append(table)
        story.append(Spacer(1, 4 * mm))
        table_rows = []

    for raw in md_text.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            flush_table()
            in_code = not in_code
            continue
        if in_code:
            if line:
                story.append(Paragraph(clean(line), styles["CodeBlockSmall"]))
            continue
        if line.startswith("|") and line.endswith("|"):
            cells = [Paragraph(clean(c.strip()), styles["BodyText"]) for c in line.strip("|").split("|")]
            if not all(set(c.getPlainText()) <= {"-", ":"} for c in cells):
                table_rows.append(cells)
            continue
        flush_table()
        if not line:
            story.append(Spacer(1, 2 * mm))
        elif line.startswith("# "):
            story.append(Paragraph(clean(line[2:]), styles["Heading1"]))
        elif line.startswith("## "):
            story.append(Paragraph(clean(line[3:]), styles["Heading2"]))
        elif line.startswith("### "):
            story.append(Paragraph(clean(line[4:]), styles["Heading3"]))
        elif line.startswith("- "):
            story.append(Paragraph("• " + clean(line[2:]), styles["BodyText"]))
        else:
            story.append(Paragraph(clean(line), styles["BodyText"]))
    flush_table()
    return story


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(18 * mm, 10 * mm, "HW06 API Testing - 23127296")
    canvas.drawRightString(192 * mm, 10 * mm, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf(md_path: Path, pdf_path: Path, title: str):
    story = markdown_to_story(md_path.read_text(encoding="utf-8"), title)
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=16 * mm,
        bottomMargin=16 * mm,
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build_pdf(SUBMIT / "main_report.md", SUBMIT / "main_report.pdf", "HW06 API Testing Main Report")
    build_pdf(SUBMIT / "ai_audit_report.md", SUBMIT / "ai_audit_report.pdf", "HW06 AI Audit Report")
    build_pdf(SUBMIT / "ai_critique.md", SUBMIT / "ai_critique.pdf", "HW06 AI Critique")
    print("Generated report PDFs.")
