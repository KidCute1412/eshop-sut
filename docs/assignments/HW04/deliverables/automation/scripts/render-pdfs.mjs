import { readFileSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { chromium } from "@playwright/test";
import { marked } from "marked";

const reportDir = path.resolve("..", "reports");
const documents = ["main_report.md", "ai_critique.md", "ai_audit_report.md"];

const stylesheet = `
  @page { size: A4; margin: 17mm 15mm 19mm; }
  :root { color: #172033; font-family: "Segoe UI", Arial, sans-serif; font-size: 10.2pt; }
  body { line-height: 1.52; margin: 0; }
  h1, h2, h3 { color: #12355b; break-after: avoid; }
  h1 { border-bottom: 3px solid #2f75b5; font-size: 24pt; margin: 0 0 18px; padding-bottom: 9px; }
  h2 { border-bottom: 1px solid #a9bdd2; font-size: 16pt; margin-top: 28px; padding-bottom: 4px; }
  h3 { font-size: 12.5pt; margin-top: 21px; }
  p, li { orphans: 3; widows: 3; }
  table { border-collapse: collapse; font-size: 8.1pt; margin: 11px 0 18px; width: 100%; }
  th, td { border: 1px solid #aeb9c6; padding: 5px 6px; text-align: left; vertical-align: top; }
  th { background: #dce8f4; color: #12355b; font-weight: 650; }
  tr { break-inside: avoid; }
  code { background: #eef2f6; border-radius: 3px; font-family: Consolas, monospace; font-size: 8.7pt; padding: 1px 3px; }
  pre { background: #172033; color: #f4f7fa; overflow-wrap: anywhere; padding: 10px; white-space: pre-wrap; }
  pre code { background: transparent; color: inherit; padding: 0; }
  blockquote { border-left: 4px solid #2f75b5; color: #34485d; margin-left: 0; padding-left: 12px; }
  a { color: #165f9f; text-decoration: none; }
  strong { color: #102d4d; }
`;

const browser = await chromium.launch({ headless: true });
try {
  for (const fileName of documents) {
    const markdownPath = path.join(reportDir, fileName);
    const pdfPath = markdownPath.replace(/\.md$/i, ".pdf");
    const markdown = readFileSync(markdownPath, "utf8");
    const title = markdown.match(/^#\s+(.+)$/m)?.[1] ?? fileName;
    const body = await marked.parse(markdown, { gfm: true });
    const baseHref = pathToFileURL(`${reportDir}${path.sep}`).href;
    const page = await browser.newPage();
    await page.setContent(
      `<!doctype html><html lang="en"><head><meta charset="utf-8"><base href="${baseHref}"><title>${title}</title><style>${stylesheet}</style></head><body>${body}</body></html>`,
      { waitUntil: "load" },
    );
    await page.pdf({
      path: pdfPath,
      format: "A4",
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: "<span></span>",
      footerTemplate: `<div style="font:8px 'Segoe UI',Arial;color:#607080;width:100%;padding:0 15mm;display:flex;justify-content:space-between"><span>23127404 · HW04 Automation Testing</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
      margin: { top: "17mm", right: "15mm", bottom: "19mm", left: "15mm" },
    });
    await page.close();
    console.log(`Rendered ${path.relative(process.cwd(), pdfPath)}`);
  }
} finally {
  await browser.close();
}
