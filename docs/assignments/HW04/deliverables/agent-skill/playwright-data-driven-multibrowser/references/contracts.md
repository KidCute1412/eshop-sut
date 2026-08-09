# Data and evidence contracts

## External case data

Use an array when a feature has multiple cases. Keep the schema explicit and stable:

```json
[
  {
    "caseId": "FEATURE-001",
    "description": "A concise observable scenario",
    "preconditions": ["Required state"],
    "input": { "path": "/example" },
    "expected": { "heading": "Example" }
  }
]
```

Accept `caseId`, `case_id`, `testCaseId`, or `test_case_id` consistently within one suite. Parse the file before declaring tests, validate its shape, and reject empty or duplicate IDs. Avoid secrets and environment-specific accounts in committed data.

For CSV, use one header row and one row per case. Parse booleans and numbers deliberately; CSV values are strings by default. Prefer JSON when expected values are nested.

## Test generation

Declare a distinct test for each row so retries, traces, and reports identify the failing case:

```ts
const cases = loadAndValidateCases("test-data/feature.json");

for (const row of cases) {
  test(`${row.caseId}: ${row.description}`, async ({ page }) => {
    await page.goto(row.input.path);
    await expect(page.getByRole("heading", { name: row.expected.heading }))
      .toBeVisible();
  });
}
```

Do not put all rows inside one `test` callback. Do not branch around assertions based on unexpected page state. Encode the expected outcome in the row and make failures visible.

## Browser projects

Declare projects explicitly in `playwright.config.ts`:

```ts
projects: [
  { name: "chromium", use: { ...devices["Desktop Chrome"] } },
  { name: "firefox", use: { ...devices["Desktop Firefox"] } },
  { name: "webkit", use: { ...devices["Desktop Safari"] } },
]
```

Use the project names required by the delivery contract. Run a single project with `playwright test --project=<name>` and the full matrix with `playwright test`.

## Reporter and run metadata

Emit both reviewable and machine-readable evidence:

```ts
const startedAt = new Date().toISOString();

reporter: [
  ["html", { outputFolder: process.env.PW_HTML_REPORT ?? "playwright-report", open: "never" }],
  ["json", { outputFile: process.env.PW_JSON_REPORT ?? "test-results/report.json" }],
],
metadata: {
  runOwner: process.env.RUN_OWNER ?? "unspecified",
  startedAt,
  sutRevision: process.env.SUT_REVISION ?? "unknown",
}
```

Give separate runs separate output paths or archive each complete report before the next run. Supply required identity through environment variables; do not bake a particular person, repository, or deployment into a reusable suite.

The JSON audit contract requires:

- parseable Playwright JSON with `stats` and an ISO-like `startTime`;
- expected project names on test entries;
- external case IDs in test titles;
- one case/project pair for every required matrix cell when full coverage is claimed;
- no unexpected, flaky, or skipped outcomes when a clean pass is claimed.

The HTML review contract requires the complete generated report directory, visible run metadata required by the assignment or organization, readable results, and accessible failure attachments. Validate JSON mechanically, then inspect HTML visually; neither substitutes for the other.
