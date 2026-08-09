import { defineConfig, devices } from "@playwright/test";
import path from "node:path";

const studentId = "23127404";
const runTimestamp = process.env.RUN_TIMESTAMP ?? new Date().toISOString();
const feature = process.env.FEATURE_KEY ?? "all-features";
const browser = process.env.BROWSER_KEY ?? "all-browsers";
const safeTimestamp = runTimestamp.replace(/[:.]/g, "-");
const reportKey = process.env.REPORT_KEY ?? `${feature}-${browser}-${safeTimestamp}`;
const reportDir = path.resolve("reports", reportKey);
const listOnly = process.argv.includes("--list");
const title = `HW04 ${feature} ${browser} | Run by: ${studentId} | ${runTimestamp}`;

export default defineConfig({
  testDir: "./tests",
  outputDir: "./test-results",
  fullyParallel: false,
  workers: 1,
  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 1 : 0,
  timeout: 30_000,
  expect: { timeout: 8_000 },
  metadata: {
    "Run by": studentId,
    "Run timestamp": runTimestamp,
    Feature: feature,
    Browser: browser,
  },
  reporter: listOnly
    ? [["list"]]
    : [
        ["line"],
        ["html", { outputFolder: reportDir, open: "never", title }],
        ["json", { outputFile: path.join(reportDir, "results.json") }],
        [
          "./src/reporters/run-metadata-reporter.ts",
          { reportDir, studentId, runTimestamp, feature, browser },
        ],
      ],
  use: {
    baseURL: process.env.WEB_URL ?? "http://localhost:5173",
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
    video: "retain-on-failure",
    actionTimeout: 10_000,
    navigationTimeout: 15_000,
  },
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
    {
      name: "firefox",
      // On the assignment Windows image, Playwright Firefox launches in
      // headless mode but fails before newPage(). A minimal headful smoke
      // check succeeds, although full runs remain intermittently affected by
      // page-fixture timeouts; preserve and classify those outcomes honestly.
      use: { ...devices["Desktop Firefox"], headless: false },
    },
    { name: "webkit", use: { ...devices["Desktop Safari"] } },
  ],
});
