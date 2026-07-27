import { defineConfig, devices } from "@playwright/test";

const runTimestamp = new Date().toISOString();

export default defineConfig({
  testDir: "./tests",
  outputDir: "test-results",
  fullyParallel: false,
  retries: 0,
  workers: 1,
  metadata: {
    "Run by": "23127404",
    "Run timestamp": runTimestamp,
  },
  reporter: [
    ["list"],
    [
      "html",
      {
        outputFolder: "playwright-report",
        open: "never",
        title: `Run by: 23127404 | ${runTimestamp}`,
      },
    ],
  ],
  use: {
    baseURL: process.env.BASE_URL ?? "http://localhost:5173",
    locale: "en-US",
    screenshot: "only-on-failure",
    trace: "retain-on-failure",
  },
  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
    {
      name: "firefox",
      use: { ...devices["Desktop Firefox"] },
    },
    {
      name: "webkit",
      use: { ...devices["Desktop Safari"] },
    },
  ],
});
