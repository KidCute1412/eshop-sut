---
name: automation-test-generation
description: "Generates Playwright test suites and data-driven artifacts from functional requirements."
---

# Automation Test Generation Skill

## Purpose
This skill generates data-driven Playwright test suites from given functional requirements. The user may specify how many test cases to generate. The skill produces paired artifacts for each test case: a `TCXX.spec.js` script and a `TCXX.json` data file placed in `auto-tests/`, plus a traceability matrix and a human-readable report under `setup/report/`.

## Automatic file access
- Read from: `setup/info/` (requirements, API docs, run notes).
- Read from: `setup/logs/logs.md` (session logging rules and previous logs).
- Read/write templates from: `setup/templates/` when available.
- Write to: `auto-tests/` (generated `TCXX.spec.js` and `TCXX.json`).
- Write to: `setup/report/` (test-suite report `FR-XX-report.md`).
- Append to: `setup/logs/logs.md` for session log entries.

## Preconditions & Safety
- This skill only *generates* automated test artifacts; it does not execute them unless explicitly requested by the user.
- The skill must not assume internal implementation details beyond what is supplied in `setup/info/` or by the user.
- The user must provide the functional requirement identifier (e.g., `FR-05`) and the desired number of test cases.

## Output format
- For each test case N (1..count):
  - `auto-tests/TCNN.spec.js` — Playwright test script (ES module) that imports runtime data.
  - `auto-tests/TCNN.json` — JSON object containing the data used by the script (inputs, expected values, metadata).
- A traceability matrix `setup/report/FR-XX-traceability.md` mapping each `TCNN` to the original requirement.
- A human-readable report `setup/report/FR-XX-report.md` listing each test case objective, preconditions, input summary, and an empty `Verdict:` field.

## Playwright integration notes
- Generated specs conform to Playwright's test runner conventions and import `test` and `expect` from `@playwright/test`.
- Data-driven loading uses a portable ESM-friendly pattern that works in Playwright test files:

  const fs = await import('fs');
  const data = JSON.parse(await fs.promises.readFile(new URL('./TC01.json', import.meta.url)));

- Each generated spec contains a single `test()` using data from the corresponding JSON file.

- When writing generated test scripts, the `test()` title must be the `TCXX` identifier only (for example: `test('TC01', async (...) => { ... })`). This ensures stable, traceable test names that map directly to the traceability matrix.

## Assertion techniques (at least three distinct patterns)
The generated scripts will include a mix of these assertion styles across the suite:

1. Accessibility / Role-based assertions
   - Example: `await expect(page.getByRole('heading', { name: data.heading })).toBeVisible()`
   - Rationale: verifies UI semantics and visibility using ARIA roles.

2. Content equality / partial match
   - Example: `await expect(locator).toHaveText(data.expectedText)` or `toContainText` for partial checks.
   - Rationale: asserts exact or partial textual content.

3. Structural/assert count and attribute checks
   - Example: `await expect(page.getByRole('listitem')).toHaveCount(data.expectedCount)` or `toHaveAttribute('alt', data.expectedAlt)`.
   - Rationale: verifies DOM structure, counts, and attributes (image alt text, links).

The skill will distribute these patterns across generated cases to ensure variety and resiliency.

## Traceability matrix
- The skill creates `setup/report/FR-XX-traceability.md` with a simple table:

| Test Case | Requirement ID | Objective Summary |
| --- | --- | --- |
| TC01 | FR-XX | ... |

- Each generated test row must include the input data filename and a short mapping back to the specific requirement clause it addresses.

## Workflow

1. Receive inputs: requirement identifier (e.g., `FR-05`), concise requirement text (if not available in `setup/info/`), and desired number of test cases (N).
2. Validate: confirm `setup/info/` contains the requirement; if absent, request the requirement text from the user.
3. Analyze requirement: extract testable behaviors, preconditions, expected outputs, and edge/value ranges where applicable.
4. Partition behaviors into N test objectives, balancing happy path, edge cases, and negative flows (where applicable). Do not create actual test executions at this stage; only generate artifact files.
5. Generate artifacts for each test objective:
   - Create `auto-tests/TCNN.json` with a structured schema: { id, requirement, objective, preconditions, inputs, expected, metadata }
   - Create `auto-tests/TCNN.spec.js` that loads the JSON, drives Playwright interactions, and applies at least one of the assertion patterns described above.
6. Create traceability matrix in `setup/report/FR-XX-traceability.md`.
7. Create `setup/report/FR-XX-report.md` listing each test case objective and an empty `Verdict:` placeholder.
8. Append a session log to `setup/logs/logs.md` describing the generated artifacts and the exact inputs used.

## File and naming conventions
- Test case numbers use two digits with leading zeros (`TC01`, `TC02`, ...).
- Spec filenames: `TCNN.spec.js` (example: `TC01.spec.js`).
- Data filenames: `TCNN.json` (example: `TC01.json`).

## JSON schema recommendation for each `TCNN.json`

{
  "id": "TC01",
  "requirement": "FR-05",
  "objective": "Verify product listing default view",
  "preconditions": ["server running", "no search term"],
  "inputs": { "url": "http://localhost:5173/", "search": "" },
  "expected": { "visibleCount": 5, "hasImages": true },
  "metadata": { "assertions": ["role-visibility","text-equality"] }
}

## Templates
- The skill will use a spec template similar to `auto-tests/examples.spec.js`:

import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC01.json', import.meta.url)));

test(data.id, async ({ page }) => {
  await page.goto(data.inputs.url);
  // interactions derived from data.inputs
  // sample assertions (choose per-case):
  // await expect(page.getByRole('heading', { name: data.expected.heading })).toBeVisible();
});

Note: actual generated specs will contain full step-by-step actions derived from `inputs` and corresponding assertions from `expected`.

## Reporting
- The generated `setup/report/FR-XX-report.md` contains a table with the following columns: Test Case, Objective, Preconditions, Input Summary, Expected, Verdict.
- Verdict is intentionally left blank until the test run is executed.

## Logging
- Every run of this skill appends a log entry to `setup/logs/logs.md` following the repository's existing format. Each log entry includes:
  - Name of the AI tool
  - Date and time (DD/MM/YYYY HH:mm)
  - Full text of the given prompt (user's request)
  - Attached/created file names
  - Text output summary
  - File outputs (paths)
  - Separator line `------`

## Limitations & Notes
- The skill generates artifacts compatible with Playwright, but the user must ensure local servers and required test fixtures (sample CSVs, images, etc.) are available when running tests.
- The skill will not execute tests or modify other unrelated files.
- When importing JSON in ESM test files the generated code uses `fs.promises.readFile(new URL(..., import.meta.url))` to remain portable.

## Example invocation
- Input: requirement=`FR-05`, count=`6`.
- Output: `auto-tests/TC01.spec.js`..`TC06.spec.js`, `auto-tests/TC01.json`..`TC06.json`, `setup/report/FR-05-report.md`, `setup/report/FR-05-traceability.md`.
