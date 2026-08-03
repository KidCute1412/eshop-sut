// @ts-check
import { defineConfig, devices } from '@playwright/test';

/**
 * Read environment variables from file.
 * https://github.com/motdotla/dotenv
 */
// import dotenv from 'dotenv';
// import path from 'path';
// dotenv.config({ path: path.resolve(__dirname, '.env') });

const STUDENT_ID = process.env.HW04_STUDENT_ID || '23127296';

/**
 * @see https://playwright.dev/docs/test-configuration
 */
export default defineConfig({
  testDir: './tests',
  /*
   * backend/server.js drops and reseeds its SQLite database on every start, and
   * mutates shared server-side state across requests (login-attempt counters,
   * coupon usage, in-memory carts keyed by user id). Running spec files/tests in
   * parallel against the same backend instance would make data-driven assertions
   * non-deterministic, so the whole HW04 suite runs single-threaded.
   */
  fullyParallel: false,
  workers: 1,
  /* Fail the build on CI if you accidentally left test.only in the source code. */
  forbidOnly: !!process.env.CI,
  /* Retry on CI only */
  retries: process.env.CI ? 2 : 0,
  /* Reporter to use. See https://playwright.dev/docs/test-reporters */
  reporter: [
    ['html', { outputFolder: process.env.HW04_REPORT_DIR || 'playwright-report', open: 'never' }],
  ],
  /* Shared settings for all the projects below. See https://playwright.dev/docs/api/class-testoptions. */
  use: {
    /* Base URL to use in actions like `await page.goto('')`. */
    // baseURL: 'http://localhost:3000',

    /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
    trace: 'on-first-retry',
    /* Screenshots of failing assertions, used as evidence in the GitHub bug reports. */
    screenshot: 'only-on-failure',
  },

  /* Stamped into the HTML report by scripts/stamp-report.js after each run (HW04 anti-cheat requirement). */
  metadata: {
    'Run by': STUDENT_ID,
    'Run at': new Date().toISOString(),
  },

  /* Configure projects for major browsers */
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },

    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },

    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },

    /* Test against mobile viewports. */
    // {
    //   name: 'Mobile Chrome',
    //   use: { ...devices['Pixel 5'] },
    // },
    // {
    //   name: 'Mobile Safari',
    //   use: { ...devices['iPhone 12'] },
    // },

    /* Test against branded browsers. */
    // {
    //   name: 'Microsoft Edge',
    //   use: { ...devices['Desktop Edge'], channel: 'msedge' },
    // },
    // {
    //   name: 'Google Chrome',
    //   use: { ...devices['Desktop Chrome'], channel: 'chrome' },
    // },
  ],

  /* Auto-start the SUT (backend + web + admin) before the suite runs. */
  webServer: [
    {
      command: 'node server.js',
      cwd: './backend',
      url: 'http://localhost:3000/api/products',
      // Always start a fresh backend: server.js drops/reseeds the whole DB on
      // boot, and several tests (coupon usage limits, revenue math) depend on
      // that clean state. Reusing a server left running from a previous browser
      // run would silently carry over mutated data between runs.
      reuseExistingServer: false,
      timeout: 30_000,
    },
    {
      command: 'npx vite --port 5173 --strictPort',
      cwd: './frontend-web',
      url: 'http://localhost:5173',
      reuseExistingServer: false,
      timeout: 30_000,
    },
    {
      command: 'npx vite --port 5174 --strictPort',
      cwd: './frontend-admin',
      url: 'http://localhost:5174',
      reuseExistingServer: false,
      timeout: 30_000,
    },
  ],
});
