import os
import markdown
from playwright.sync_api import sync_playwright

DOCS = [
    (
        "docs/assignments/HW06/deliverables/report/23127404_HW06_API_Testing_Report.md",
        "docs/assignments/HW06/deliverables/report/23127404_HW06_API_Testing_Report.pdf"
    ),
    (
        "docs/assignments/HW06/deliverables/ai/23127404_HW06_AI_Critique.md",
        "docs/assignments/HW06/deliverables/ai/23127404_HW06_AI_Critique.pdf"
    ),
    (
        "docs/assignments/HW06/deliverables/ai/23127404_HW06_AI_Audit_Report.md",
        "docs/assignments/HW06/deliverables/ai/23127404_HW06_AI_Audit_Report.pdf"
    ),
    (
        "docs/assignments/HW06/deliverables/cicd/23127404_HW06_CICD_Report.md",
        "docs/assignments/HW06/deliverables/cicd/23127404_HW06_CICD_Report.pdf"
    ),
]

CSS_STYLE = """
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.6;
    color: #24292e;
    padding: 20px;
    font-size: 13px;
}
h1 { color: #0366d6; font-size: 24px; border-bottom: 2px solid #eaecef; padding-bottom: 8px; margin-top: 0; }
h2 { color: #0366d6; font-size: 18px; border-bottom: 1px solid #eaecef; padding-bottom: 6px; margin-top: 24px; }
h3 { color: #1f2328; font-size: 15px; margin-top: 16px; }
table { border-collapse: collapse; width: 100%; margin: 15px 0; font-size: 12px; }
th, td { border: 1px solid #dfe2e5; padding: 7px 12px; text-align: left; }
th { background-color: #f6f8fa; font-weight: 600; color: #24292e; }
tr:nth-child(even) { background-color: #fcfcfc; }
code { background-color: #f6f8fa; padding: 2px 5px; border-radius: 4px; font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; font-size: 11.5px; color: #cf222e; }
pre { background-color: #f6f8fa; padding: 12px; border-radius: 6px; overflow-x: auto; border: 1px solid #e1e4e8; }
pre code { background-color: transparent; padding: 0; color: #24292e; }
blockquote { border-left: 4px solid #0969da; padding: 4px 15px; color: #57606a; margin: 15px 0; background-color: #f6f8fa; border-radius: 0 4px 4px 0; }
hr { border: 0; height: 1px; background: #e1e4e8; margin: 20px 0; }
"""

def render_all():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for md_path, pdf_path in DOCS:
            if not os.path.exists(md_path):
                print(f"Skipping missing file: {md_path}")
                continue
            with open(md_path, "r", encoding="utf-8") as f:
                md_text = f.read()
            html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "nl2br"])
            full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS_STYLE}</style>
</head>
<body>{html_body}</body>
</html>"""
            page = browser.new_page()
            page.set_content(full_html)
            page.pdf(
                path=pdf_path,
                format="A4",
                margin={"top": "18mm", "bottom": "18mm", "left": "15mm", "right": "15mm"},
                print_background=True
            )
            page.close()
            print(f"[OK] Rendered {os.path.basename(pdf_path)} ({os.path.getsize(pdf_path):,} bytes)")
        browser.close()

if __name__ == "__main__":
    render_all()
