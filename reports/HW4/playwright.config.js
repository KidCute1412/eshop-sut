const { defineConfig, devices } = require("@playwright/test");
const path = require("path");

const STUDENT_ID = process.env.STUDENT_ID || "23127539";
const runStamp = new Date().toISOString();

const webServers = [
  {
    command: "node server.js",
    cwd: path.join(__dirname, "..", "..", "backend"),
    url: "http://localhost:3000",
    reuseExistingServer: true,
    timeout: 120000
  },
  {
    command: "npm run dev",
    cwd: path.join(__dirname, "..", "..", "frontend-web"),
    url: "http://localhost:5173",
    reuseExistingServer: true,
    timeout: 120000
  },
  {
    command: "npm run dev",
    cwd: path.join(__dirname, "..", "..", "frontend-admin"),
    url: "http://localhost:5174",
    reuseExistingServer: true,
    timeout: 120000
  }
];

module.exports = defineConfig({
  testDir: ".",
  testMatch: ["**/tests/*.spec.js"],
  timeout: 45000,
  expect: { timeout: 8000 },
  fullyParallel: false,
  workers: 1,
  reporter: [
    ["list"],
    [
      "html",
      {
        outputFolder: `reports/html-${STUDENT_ID}`,
        open: "never",
        title: `Run by: ${STUDENT_ID} - ${runStamp}`
      }
    ]
  ],
  use: {
    baseURL: process.env.WEB_BASE_URL || "http://localhost:5173",
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
    video: "retain-on-failure"
  },
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
    { name: "firefox", use: { ...devices["Desktop Firefox"] } },
    { name: "webkit", use: { ...devices["Desktop Safari"] } }
  ],
  webServer: process.env.HW4_SKIP_WEBSERVER === "1" ? undefined : webServers
});
