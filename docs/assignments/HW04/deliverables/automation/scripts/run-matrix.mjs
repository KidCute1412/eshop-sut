import { spawnSync } from "node:child_process";
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";

const features = {
  fr06: "tests/fr06-product-detail.spec.ts",
  fr10: "tests/fr10-order-state-machine.spec.ts",
  fr12: "tests/fr12-access-control.spec.ts",
};
const browsers = ["chromium", "firefox", "webkit"];

function valuesAfter(flag) {
  const index = process.argv.indexOf(flag);
  return index === -1 ? undefined : process.argv[index + 1]?.split(",").filter(Boolean);
}

const selectedFeatures = valuesAfter("--feature") ?? Object.keys(features);
const selectedBrowsers = valuesAfter("--browser") ?? browsers;

for (const feature of selectedFeatures) {
  if (!(feature in features)) throw new Error(`Unknown feature '${feature}'`);
}
for (const browser of selectedBrowsers) {
  if (!browsers.includes(browser)) throw new Error(`Unknown browser '${browser}'`);
}

const executable = process.execPath;
const playwrightCli = path.resolve("node_modules", "@playwright", "test", "cli.js");
const results = [];

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function stampHtmlReport(reportKey, feature, browser, runTimestamp, status) {
  const indexPath = path.resolve("reports", reportKey, "index.html");
  if (!existsSync(indexPath)) return;
  const banner = `<aside id="hw04-run-attribution" style="position:fixed;right:12px;bottom:12px;z-index:2147483647;padding:10px 14px;border:2px solid #1d4ed8;border-radius:8px;background:#eff6ff;color:#172554;font:600 12px/1.5 system-ui;box-shadow:0 4px 14px #0003">Run by: 23127404 | ${escapeHtml(runTimestamp)} | ${escapeHtml(feature)} | ${escapeHtml(browser)} | ${escapeHtml(status)}</aside>`;
  const html = readFileSync(indexPath, "utf8");
  writeFileSync(indexPath, html.replace("</body>", `${banner}</body>`), "utf8");
}

for (const feature of selectedFeatures) {
  for (const browser of selectedBrowsers) {
    const runTimestamp = new Date().toISOString();
    const safeTimestamp = runTimestamp.replace(/[:.]/g, "-");
    const reportKey = `${feature}-${browser}-${safeTimestamp}`;
    console.log(`\nRUN ${feature} / ${browser} / ${runTimestamp}`);

    const result = spawnSync(
      executable,
      [playwrightCli, "test", features[feature], `--project=${browser}`],
      {
        cwd: process.cwd(),
        env: {
          ...process.env,
          FEATURE_KEY: feature,
          BROWSER_KEY: browser,
          RUN_TIMESTAMP: runTimestamp,
          REPORT_KEY: reportKey,
        },
        stdio: "inherit",
        shell: false,
      },
    );
    if (result.error) {
      console.error(`Could not launch Playwright for ${feature}/${browser}: ${result.error.message}`);
    }
    const status = result.status ?? 1;
    stampHtmlReport(reportKey, feature, browser, runTimestamp, status === 0 ? "passed" : "failed");
    results.push({ feature, browser, reportKey, status });
  }
}

console.log("\nMATRIX SUMMARY");
for (const result of results) {
  console.log(`${result.status === 0 ? "PASS" : "FAIL"} ${result.feature}/${result.browser} -> reports/${result.reportKey}`);
}
if (results.some((result) => result.status !== 0)) process.exitCode = 1;
