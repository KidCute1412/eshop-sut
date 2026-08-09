---
name: playwright-data-driven-multibrowser
description: Build, review, and validate Playwright test suites that load JSON or CSV cases at runtime and execute the same traceable scenarios across multiple browser projects. Use when creating external test-data contracts, converting manual cases into Playwright tests, configuring Chromium/Firefox/WebKit or other browser matrices, reducing UI-test flakiness, or auditing JSON and HTML execution evidence.
---

# Playwright Data-Driven Multibrowser

## Establish the contract

1. Inspect the requirement, current UI, existing test conventions, and environment setup.
2. Define stable case IDs, preconditions, inputs, expected outcomes, cleanup needs, and supported browsers before writing selectors.
3. Separate SUT defects from unavailable dependencies, invalid fixtures, and automation defects. Never fabricate a pass, timestamp, browser result, or report.

Read [references/contracts.md](references/contracts.md) when selecting a dataset schema, project configuration, or reporter layout.

## Build the suite

1. Store executable cases in external JSON or CSV. Validate required fields and reject duplicate case IDs before tests start.
2. Generate one independently named Playwright test per data row. Include the case ID in the title so reports remain traceable.
3. Keep setup and cleanup isolated by case, worker, and browser. Create unique mutable records and remove only records created by that case.
4. Prefer role, label, accessible name, and test-ID locators. Scope ambiguous locators and assert the user-visible outcome.
5. Use web-first assertions and event- or response-based waits. Remove `waitForTimeout` and other fixed sleeps.
6. Cover distinct observable outcomes with appropriate URL, visibility, text/value, count, state, or response assertions. Do not add assertions merely to increase a count.

## Configure and execute browsers

1. Declare explicit Playwright projects for every required browser. Keep locale, viewport, authentication, and feature flags consistent unless the requirement calls for a difference.
2. Enable failure diagnostics such as screenshots and traces. Configure an HTML reporter for human review and a JSON reporter for deterministic auditing.
3. Run a focused case in one project first, then the feature in one project, then the complete browser matrix.
4. Preserve the exact command, environment or SUT revision, ISO 8601 start time, project, totals, and complete report directory for each required run.
5. Treat browser-specific failures as findings only after reproducing them and ruling out stale state, unsupported browser binaries, data collisions, and locator timing.

## Validate artifacts

Run the bundled validator from any directory:

```text
python <skill-dir>/scripts/validate_playwright_artifacts.py \
  --suite-root <playwright-project> \
  --expected-project chromium \
  --expected-project firefox \
  --expected-project webkit
```

Add one or more `--report <playwright-json-report>` arguments and `--require-case-matrix` to prove that every external case ID appears under every expected project. Add `--fail-on-unexpected` when an unexpected, flaky, or skipped result must fail the audit. Use `--json` for machine-readable validator output.

Fix every reported error or document why the checked contract does not apply. Do not weaken the validator to make incomplete evidence pass; change the suite contract explicitly when the project has a justified variation.

## Review the evidence

1. Confirm report case IDs map back to the external dataset and requirement.
2. Inspect retained diagnostics for unexpected failures and distinguish expected negative scenarios from failed tests.
3. Open HTML reports and verify visible run metadata, browser identity, totals, and linked assets.
4. Report automation limitations and unresolved environmental blockers separately from product defects.
