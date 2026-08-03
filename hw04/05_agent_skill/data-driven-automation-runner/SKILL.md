---
name: data-driven-automation-runner
description: Turn a set of manually-designed test cases for a web feature into a data-driven, multi-browser Playwright suite (spec-correct assertions, JSON/CSV fixtures, HTML report with authorship stamp), against a SUT whose backend resets its state on every boot. Use when asked to "automate this feature with Playwright", "convert these test cases into scripts", or "set up data-driven multi-browser tests" for a given feature/spec.
---

# Data-Driven, Multi-Browser Automation Runner

Reproduces the disciplined HW04 (Automation Testing) workflow, so it can be reapplied to any additional feature without re-deriving the method from scratch: read the spec and the real implementation side by side, write assertions against the **spec**, drive the AI step by step rather than with one generic prompt, and produce a genuinely runnable, multi-browser, data-driven suite.

## When to use this skill

Invoke it whenever the user wants a real feature automated end-to-end with Playwright (or Selenium) against a real codebase they have read access to — not a request to "just write some example tests." It assumes: a written spec (README/FR list or equivalent), the actual frontend + backend source, and the ability to run the app locally (or a `webServer` config that can start it).

## Process (follow every step — do not collapse into one prompt)

### Step 1 — Read the spec AND the implementation, side by side
Before writing a single test, read the feature's spec section and the actual route handlers / components that implement it. Note every place they **diverge** — that divergence is where the real bugs (and the most valuable test cases) live. Do not write tests only from the spec (you'll miss implementation quirks) or only from the code (you'll just be testing the bugs as if they were correct behavior).

### Step 2 — Design ≥12 test cases before writing scripts
Produce a test-case table (ID, type — positive/negative/boundary/edge/E2E, input, **spec-correct** expected result, notes on any known/suspected defect). Mix positive, negative, and boundary-value cases; boundary cases around every numeric threshold in the spec (`>=` vs `>`, min/max lengths, off-by-one) are disproportionately likely to catch real bugs. Save this as a standalone Markdown table before touching code.

### Step 3 — Externalize test data
Every parameterized input/expected-output row goes into a `.json` (or `.csv`) fixture file next to the spec — never as an inline array/object in the test file. Write **one** parameterized `test()` (or loop) that iterates the fixture, plus separate `test()`s for cases that need multi-step setup (login, prior state) that don't fit the flat data-driven shape.

### Step 4 — Assert against the spec, not the implementation
Every assertion's expected value must come from step 1's spec reading, even when you already know (from reading the code) that the implementation will produce something different. A test that's expected to fail against a real defect is not a broken test — it's the deliverable. Never quietly encode the buggy behavior as the "expected" value just to make the suite green.

### Step 5 — Account for shared, resettable backend state
Before choosing a concurrency model, check: does the backend reset/reseed its database on boot? Do multiple tests mutate the same server-side counters (login attempts, usage limits, in-memory carts)? If yes:
- Set `fullyParallel: false` and `workers: 1` globally so execution order is deterministic.
- Do **not** reach for `test.describe.configure({ mode: 'serial' })` as a substitute — it causes Playwright to skip every remaining test in the block after the first failure, which silently hides every other bug-revealing assertion after the first one. Use it only when later tests should genuinely never run after an earlier one fails.
- Set `reuseExistingServer: false` on every `webServer` entry if the run needs a clean, comparable dataset each time (e.g. running the same suite once per browser) — reusing a server across separate CLI invocations carries mutated state forward invisibly.

### Step 6 — Multi-browser execution + report authorship stamp
Run the suite once per required browser/engine (e.g. `--project=chromium|firefox|webkit`), each against a fresh server, each into its own HTML report output folder. Then post-process each generated report to inject a visible "Run by: `<identifier>` | `<ISO timestamp>`" banner (title + a fixed footer div) — do not rely on the reporter's built-in metadata alone, since most HTML reporters don't surface it visibly by default.

### Step 7 — Human review pass (mandatory, not decoration)
For every locator/config/wait that fails on first real run, record: what broke, why the first draft got it wrong (e.g. "assumed `<label>`+`<input>` are auto-associated without `htmlFor`", "used a one-shot `innerText()` read that raced an async fetch", "copied a starter-template default without checking this SUT's stateful backend"), and the fix applied. This is the deliverable the "human review" requirement is actually checking for — a generic "AI made some mistakes, I fixed them" is not sufficient.

### Step 8 — Bug reporting
For every assertion that fails against a genuine spec violation (not a test-authoring bug), that's a candidate bug report: title, spec citation, actual behavior with file:line, repro steps, and a screenshot. For UI tests, screenshot the page. For API-only tests, screenshot the relevant row of the generated HTML report (it already shows expected/received + file:line) — a small headless-browser script that opens the report and screenshots the expanded test row works for any number of bugs without manual work.

## Output format

Produce:
1. A test-case design doc per feature (Markdown table, ≥12 rows).
2. One or more `.json`/`.csv` fixture files per feature.
3. Spec files that assert spec-correct expectations, organized so a known-bug failure never hides other tests in the same file.
4. One stamped HTML report per browser run.
5. A review/gap-analysis doc (per Step 7) that the human must read and confirm before submission.
6. A bug report doc linking each failing assertion to a filed issue (or explaining why it wasn't filed).

## Known limitations to always disclose

- If the SUT can't be run locally (no access to start backend/frontend), state this explicitly and describe what would need to run live before the suite could be trusted.
- Never claim a browser run happened, or fabricate pass/fail counts, HTML report contents, or screenshots, if they weren't actually produced by a real `playwright test` invocation.
- The AI can draft the review-and-fix narrative, but the actual human (the student) must read it and confirm agreement before submission — this skill produces a draft for review, not a finished, unreviewed deliverable.
