import { readFileSync } from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath, pathToFileURL } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.resolve(here, "../../../HW04/deliverables/automation/package.json"));
const { chromium } = require("playwright");
const { marked } = require("marked");
const reportDir = path.resolve(here, "../reports");
const documents = ["main_report.md", "ai_audit_report.md"];
const css = `@page{size:A4;margin:17mm 15mm 19mm}body{font:10pt 'Segoe UI',Arial;color:#172033;line-height:1.45}h1,h2,h3{color:#12355b;break-after:avoid}h1{font-size:23pt;border-bottom:3px solid #2f75b5;padding-bottom:8px}h2{font-size:15pt;border-bottom:1px solid #a9bdd2;padding-bottom:3px;margin-top:24px}h3{font-size:12pt;margin-top:18px}table{border-collapse:collapse;width:100%;font-size:8pt;margin:10px 0 16px}th,td{border:1px solid #aeb9c6;padding:5px;vertical-align:top}th{background:#dce8f4;color:#12355b}tr{break-inside:avoid}code{font:8pt Consolas;background:#eef2f6;padding:1px 3px;border-radius:3px}pre{white-space:pre-wrap;background:#172033;color:#f4f7fa;padding:9px}a{color:#165f9f}`;
const browser = await chromium.launch({ headless: true });
try {
  for (const name of documents) {
    const markdownPath = path.join(reportDir, name);
    const html = await marked.parse(readFileSync(markdownPath, "utf8"), { gfm: true });
    const page = await browser.newPage();
    await page.setContent(`<!doctype html><html><head><meta charset="utf-8"><base href="${pathToFileURL(`${reportDir}${path.sep}`).href}"><style>${css}</style></head><body>${html}</body></html>`, { waitUntil: "load" });
    await page.pdf({ path: markdownPath.replace(/\.md$/i, ".pdf"), format: "A4", printBackground: true, displayHeaderFooter: true, headerTemplate: "<span></span>", footerTemplate: "<div style=\"font:8px Segoe UI;color:#607080;width:100%;padding:0 15mm;display:flex;justify-content:space-between\"><span>23127404 · HW05 Performance Testing</span><span><span class=\"pageNumber\"></span> / <span class=\"totalPages\"></span></span></div>", margin: { top: "17mm", right: "15mm", bottom: "19mm", left: "15mm" } });
    await page.close();
    console.log(`Rendered ${name}`);
  }
} finally { await browser.close(); }
