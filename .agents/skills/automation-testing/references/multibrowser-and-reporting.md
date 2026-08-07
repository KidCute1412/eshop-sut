# Multi-Browser Execution and the "Run by: {StudentID}" Report Requirement

## Playwright `projects` Config (3 Browsers, One Config)

```ts
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

const STUDENT_ID = '23127539';

export default defineConfig({
  testDir: './tests',
  reporter: [
    ['html', { outputFolder: `reports/html-${STUDENT_ID}`, open: 'never' }],
    ['list'],
  ],
  use: {
    baseURL: 'http://localhost:5173',
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit', use: { ...devices['Desktop Safari'] } },
  ],
});
```

Run all 3 projects for a feature in one invocation: `npx playwright test tests/fr-01-register.spec.ts`
(runs every configured project by default), or target one project at a time with `--project=firefox`
if browsers must be run separately. Either way, every feature must be exercised on all 3 projects —
at least 9 total (feature × browser) runs across the 3 features.

## Injecting "Run by: {StudentID}" + ISO Timestamp

The Playwright HTML reporter supports a custom report title via the `title` reporter option, and a
global setup can stamp a metadata annotation onto every test. Two complementary approaches — use
both, since the assignment allows the tag to live in "title, header, footer, or report metadata":

**1. Report title (visible in the browser tab and header of the generated HTML report):**

```ts
reporter: [
  ['html', {
    outputFolder: `reports/html-${STUDENT_ID}`,
    open: 'never',
  }],
],
// Playwright does not have a single built-in "title" option pre-v1.45 for the HTML reporter;
// if the installed version lacks it, stamp the same string via a global annotation instead (below),
// or post-process reports/html-<id>/index.html's <title> tag as part of the same test run's
// teardown script -- not as a manual hand-edit after the fact.
```

**2. Global annotation on every test (always works, any Playwright version), in
`playwright.config.ts` or a `global-setup.ts`:**

```ts
import { test as base } from '@playwright/test';

export const test = base.extend({});
test.beforeEach(async ({}, testInfo) => {
  testInfo.annotations.push({
    type: 'Run by',
    description: `${STUDENT_ID} - ${new Date().toISOString()}`,
  });
});
```

This makes `Run by: 23127539 - 2026-08-03T09:15:00.123Z` appear in every test's metadata section of
the HTML report, satisfying the requirement without hand-editing generated output. If using Allure
instead, use `allure.label('Run by', STUDENT_ID)` plus `allure.parameter('Timestamp', new
Date().toISOString())` in the same `beforeEach`.

## Why This Must Come From a Real Run

§11 of the assignment names this field as one of two things TAs specifically verify are not
fabricated. A report whose "Run by" tag was typed into the HTML file by hand, rather than emitted by
the actual test run, is distinguishable from a real one (timestamp granularity, surrounding report
structure, absence of the corresponding raw JSON/trace artifacts) — treat `validate_html_report.py`
passing as a minimum bar, not proof of authenticity; the real safeguard is simply never doing this.

## Reporting the Run Matrix

Record every (feature × browser) run's pass/fail counts in `automation-report.md`
(`assets/automation-report-template.md`) — this is what Phase 6 of `SKILL.md` and the submission
`README.md`'s "number of browser runs" figure are built from.
