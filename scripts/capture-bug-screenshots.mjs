// One-off helper: opens the stamped Chromium HTML report, finds each known-bug
// test row, expands it, and screenshots it as evidence for the GitHub bug reports.
// Usage: node scripts/capture-bug-screenshots.mjs <reportDir> <outDir>
import { chromium } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

const [, , reportDir, outDir] = process.argv;
fs.mkdirSync(outDir, { recursive: true });

const targets = [
  { file: 'BUG-FR09-002_percent_formula.png', text: 'FR09-TC01' },
  { file: 'BUG-FR09-001_min_order_boundary.png', text: 'FR09-TC02' },
  { file: 'BUG-FR09-003_apply_without_login.png', text: 'FR09-TC08' },
  { file: 'BUG-FR09-006_checkout_cart_not_cleared.png', text: 'FR09-TC13' },
  { file: 'BUG-FR13-002a_admin_orders_access_control.png', text: 'FR13-TC03' },
  { file: 'BUG-FR13-002b_admin_users_access_control.png', text: 'FR13-TC05' },
  { file: 'BUG-FR13-001_revenue_doubled.png', text: 'FR13-TC01' },
];

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
const indexUrl = `file://${path.resolve(reportDir, 'index.html')}`;

for (const t of targets) {
  try {
    await page.goto(indexUrl);
    await page.waitForTimeout(500);
    const row = page.getByText(t.text, { exact: false }).first();
    await row.scrollIntoViewIfNeeded({ timeout: 5000 });
    await row.click({ timeout: 5000 });
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(outDir, t.file), fullPage: true });
    console.log(`Captured ${t.file}`);
  } catch (e) {
    console.error(`Failed to capture ${t.text}: ${e.message}`);
  }
}

await browser.close();
