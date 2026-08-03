// Stamps a generated Playwright HTML report with "Run by: <StudentID>" and an
// ISO timestamp, per HW04's anti-cheat requirement (report must visibly show
// authorship + when it was actually executed).
//
// Usage: node scripts/stamp-report.mjs <reportDir> <studentId> [browserLabel]
import fs from 'node:fs';
import path from 'node:path';

const [, , reportDir, studentId, browserLabel] = process.argv;

if (!reportDir || !studentId) {
  console.error('Usage: node scripts/stamp-report.mjs <reportDir> <studentId> [browserLabel]');
  process.exit(1);
}

const indexPath = path.resolve(reportDir, 'index.html');
if (!fs.existsSync(indexPath)) {
  console.error(`Report not found at ${indexPath}. Run the suite first.`);
  process.exit(1);
}

const timestamp = new Date().toISOString();
const label = browserLabel ? ` — ${browserLabel}` : '';
const stampText = `Run by: ${studentId} | ${timestamp}${label}`;

let html = fs.readFileSync(indexPath, 'utf8');

// Title (shown in the browser tab / window title).
html = html.replace(/<title>.*?<\/title>/i, `<title>HW04 Report — Run by: ${studentId}${label}</title>`);

const bannerId = 'hw04-run-by-banner';
if (!html.includes(bannerId)) {
  const banner = `
<div id="${bannerId}" style="position:fixed;bottom:0;left:0;right:0;z-index:99999;background:#111827;color:#f9fafb;font:13px/1.6 monospace;padding:6px 12px;text-align:center;">
  ${stampText}
</div>
<style>body{padding-bottom:32px !important;}</style>
`;
  html = html.replace('</body>', `${banner}</body>`);
}

fs.writeFileSync(indexPath, html, 'utf8');
console.log(`Stamped ${indexPath} -> "${stampText}"`);
