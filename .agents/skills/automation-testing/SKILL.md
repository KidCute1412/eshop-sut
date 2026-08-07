---
name: automation-testing
description: Guides an AI testing agent through auditable, data-driven, multi-browser test automation with Playwright (or Selenium) for HW04 (Automation Testing). Use when generating automation scripts with AI, converting DT/BVA test cases from HW02 into data-driven Playwright specs, reviewing AI-generated automation for fragile selectors/weak assertions, running multi-browser suites with an HTML report, or filing bugs found by failing assertions, without fabricating results, reports, or commits.
---

# AI-Assisted Data-Driven Automation Testing

Use this skill for HW04 — Automation Testing. It automates the same three EShop features selected
in HW02 (one each from Pools A, B, C), converting at least 12 reviewed test cases per feature into
data-driven, multi-browser Playwright (or Selenium) scripts, plus the mandatory AI Audit Report, AI
Critique, demo video, and Git commit log.

## Required References

- Read `references/instructor-clarifications.md` first.
- Read `references/assignment-requirements.md` for HW04 scope, minimums, and submission rules.
- Read `references/eshop-analysis-guide.md` for the SUT's real ports, page structure, and known
  selector risks (the app has **no `data-testid`/`id` attributes anywhere** — every selector is
  text/class/role-based, which is the single biggest source of fragile-selector risk this
  assignment asks you to review for).
- Read `references/automation-method.md` before generating scripts.
- Read `references/data-driven-and-assertions.md` before writing test data files or assertions.
- Read `references/multibrowser-and-reporting.md` before running the suite or producing HTML
  reports.
- Use `references/human-review-checklist.md` before any run is reported as final.
- Use `assets/` and `scripts/` to scaffold feature workspaces, generate templates, and validate
  artifacts.

## Integrity Rules

- Never fabricate a test result (Passed/Failed), an HTML report, a "Run by: {StudentID}" tag, an
  ISO timestamp, a bug, or a GitHub Issue link. An HTML report only counts if it was actually
  produced by a real `npx playwright test` (or Selenium + Allure) invocation against the real SUT —
  never hand-edit a report file to inject the required tag without a real run behind it.
- The AI may draft automation scripts, test data, and assertions. The human must review every
  script, fix fragile selectors and weak assertions, and is fully responsible for the final code.
  Submitting raw AI output without review is not acceptable per the assignment's Human Review
  principle.
- Preserve the initial AI-generated script (before human fixes) per feature so the gap analysis
  stays auditable — see Phase 5.
- Test data belongs in a separate `.csv`/`.json` file. A script with hardcoded inline arrays/objects
  for its test data does not satisfy "data-driven", even if it otherwise works.
- Treat implementation source code as a legitimate reference for *building selectors* (this is
  automation, not black-box GUI testing) but never as the oracle for *expected behavior* — expected
  results must trace to `README.md`, `api_specification.md`, or documented UI copy, the same as
  every other assignment in this course.
- Only commits that modify test-script files (`.spec.js`, `.spec.ts`, or equivalent) count toward
  the assignment's 8-commit minimum, and they must span at least 4 different days — see
  `references/assignment-requirements.md` §Git Commit Log. Do not batch a week of work into one
  commit the night before the deadline; it will not satisfy this rule even if the diff is correct.
- The demo video must contain the student's own voice narration in Vietnamese and show either a
  face-cam or a terminal running `whoami` and `hostname` — an AI voice-over or a screen recording
  with no narration does not satisfy this requirement.

## Phase 0: Feature and Tooling Selection

Ask the human to confirm, and record verbatim:

- The same three features selected in HW02 (one each from Pools A/B/C). If HW02 is unavailable,
  the human self-declares three features from Pools A-C directly in the report and states why.
- Confirmation the selection is not duplicated with any groupmate, per the same instruction-
  ambiguity note as HW02/HW03 (`Form: Individual Assignment`, but §5 still mentions group
  de-duplication) — record this as an open ambiguity, do not silently resolve it.
- Automation framework: Playwright (recommended) or Selenium 4+. This skill's scripts assume
  Playwright's project/reporter model; adapt paths if Selenium + Allure is chosen instead.
- Browsers: at least 3 (Chromium/Firefox/WebKit if Playwright; Chrome/Edge/Firefox if Selenium).

Never pick the features or framework automatically. Initialize each feature's workspace only after
the human confirms scope, with `scripts/init_feature_workspace.py --feature-id <FR-XX> --feature-
name <name>`.

## Phase 1: Source the Test Cases from HW02

1. For each feature, start from the already-designed, already-human-reviewed test cases in
   `reports/HW2/<FR-XX>/test-cases.md` (Domain Testing + BVA from HW02) — this is real prior work,
   not something to re-invent. Select at least 12 of those cases, covering a mix of positive,
   negative, and edge cases (any mix counts toward the minimum).
2. If HW02's test cases for a feature number fewer than 12, or don't yet cover a case class the
   automation should exercise, add the missing cases directly in this feature's automation test-case
   list, following the same schema as `references/test-case-schema.md` (design-time fields only —
   this list is what you'll convert to scripts next, it is not itself the automation output).

## Phase 2: AI-Assisted Script Generation (Step by Step, Not One Prompt)

Drive the AI through the conversion one deliberate step at a time, never with a single "write all
the automation scripts for this feature" prompt:

1. One prompt to scaffold the Playwright project structure/config for this feature (or confirm the
   shared config from `scripts/init_feature_workspace.py` if already scaffolded).
2. One prompt per test-case *group* (e.g. "convert these 4 positive registration cases," then "these
   3 negative cases," then "these edge cases") to generate the actual `.spec.ts`/`.spec.js` code,
   explicitly instructing the AI to read test data from an external file rather than hardcoding it.
3. Preserve the raw AI output for each prompt, before any human edit, in this feature's
   `ai-audit.md` via `scripts/append_ai_audit.py` — this is the baseline the gap analysis in Phase 5
   is measured against.

## Phase 3: Make It Data-Driven

- Move every literal test-data value (usernames, emails, passwords, product names, coupon codes,
  expected messages, etc.) out of the script and into a `.csv` or `.json` file per feature — see
  `assets/test-data-template.json` and `assets/test-data-template.csv`. Hardcoded inline
  arrays/objects in the script itself do not satisfy this requirement, even if the values happen to
  be stored in a constant at the top of the file.
- The script should load this file at runtime (e.g. Playwright's `test.describe.parametrize`-style
  loop over a JSON import, or a CSV-parsing fixture) and iterate over it, not just reference it once.
- Run `scripts/validate_test_data.py <feature-dir>` — it fails if it finds an external data file
  missing, or finds a spec file with a suspicious inline literal array/object of test-data shape.

## Phase 4: Assertion Pattern Diversity

Ensure the suite as a whole uses **at least three distinct assertion patterns**, for example:

- Visibility/existence assertions (`expect(locator).toBeVisible()`).
- Text/value content assertions (`expect(locator).toHaveText(...)`, `toHaveValue(...)`).
- URL/navigation assertions (`expect(page).toHaveURL(...)`).
- Count assertions (`expect(locator).toHaveCount(n)`), useful for cart rows / coupon list rows.
- Element-state assertions (`toBeEnabled()`/`toBeDisabled()`, useful for a disabled submit button
  during a pending request).
- API/network response assertions (via `page.waitForResponse` or a direct API check), useful for
  confirming a backend rejection the UI doesn't clearly surface.

Do not satisfy this by writing the same pattern three times with different matcher names — the
point is genuinely different *kinds* of check, because the assignment is testing whether the
automation would actually catch different classes of regression.

## Phase 5: Human Review and Gap Analysis

The human critically reviews every AI-generated script and fixes it. For `ai-gap-analysis.md`
(`assets/ai-gap-analysis-template.md`), record concretely, per fix:

- **Fragile selectors**: the app has no `data-testid`/`id` anywhere (see
  `references/eshop-analysis-guide.md`), so an AI's first-pass selector is often a raw CSS class or
  a hardcoded Vietnamese text string that will break the moment copy changes. Note which selectors
  were replaced with a more resilient locator (role + accessible name, or a stable structural path)
  and why the original was fragile.
- **Weak or missing assertions**: e.g. a script that only checks `page.url()` changed but never
  checks the actual success/error message content.
- **Missing edge cases**: e.g. the AI's first pass covered the happy path and one negative case but
  skipped a documented boundary (password length, coupon expiry date, quantity limits).
- **Flaky waits**: e.g. a hardcoded `page.waitForTimeout(2000)` instead of waiting on a specific
  element/response — note where these were replaced with a deterministic wait.

For each, explain *why* the AI missed it (prompt quality, a model limitation, or a characteristic of
this specific feature/page) — this is the same discipline as the AI-Miss Reason column in the
HW02/HW03 skills, just applied to code instead of checklist items or test cases.

## Phase 6: Multi-Browser Execution and Reporting

1. Run the full suite for each feature on all 3 configured browsers/projects (at least 9 browser
   runs total across the 3 features) — see `references/multibrowser-and-reporting.md` for the
   Playwright `projects` config pattern.
2. Every HTML report (Allure or the Playwright HTML reporter) must visibly display
   `Run by: {StudentID}` together with an ISO timestamp, in the title, header, footer, or report
   metadata — this is an anti-cheat-verified field, not decorative. Configure it once in the
   reporter config (see the reference) rather than hand-editing generated report HTML.
3. Run `scripts/validate_html_report.py <report-dir-or-file>` after generating each report; it fails
   if the required tag or a plausible ISO timestamp is missing.
4. Record the run matrix (feature x browser x pass/fail counts) in `automation-report.md` using
   `assets/automation-report-template.md`.

## Phase 7: Bug Reporting and Non-Automatable Cases

- For every failing assertion that reveals a genuine SUT defect (not a flaky test or a wrong
  expectation in the script itself), file it in `bug-report.md`
  (`assets/bug-report-template.md`) and as a real GitHub Issue with a screenshot attached. Replace
  `Pending` with the real Issue URL only once it exists.
- For any of the 12+ selected test cases that could not be automated, document which ones and why
  (e.g. requires a manual email-inbox check, requires a payment gateway sandbox not available,
  requires timing precision the UI doesn't expose) in the same report — do not silently drop them.

## Phase 8: AI Audit Report and AI Critique

- After every distinct AI interaction (script generation per group, data-file drafting, assertion
  refinement, etc.), append an entry with `scripts/append_ai_audit.py` — never overwrite prior
  entries, always record the verbatim prompt, the AI output reference, and the human
  review/corrections.
- Write the mandatory 200-300 word AI Critique using `assets/ai-critique-template.md`: cite a
  concrete instance from Phase 5 (a fragile selector, a weak assertion, a missed edge case) where
  the AI was wrong or incomplete, explain why it failed to catch the issue, and state the
  collaboration principle learned.

## Phase 9: Demo Video Script

Draft a narration script (`demo-video-script.md`, Vietnamese, targeting 5+ minutes) that demos ONE
automation script end to end: the multi-browser run, the generated HTML report, and a narrated
walk-through of at least one real fix made during Phase 5's human review. The recording must show
either a face-cam or a terminal running `whoami` and `hostname` for authorship evidence — build this
into the script's opening beat, not as an afterthought.

## Phase 10: Git Commit Log and Final Assembly

- Commit each demonstrated step separately (script generation per feature, data-file addition, each
  review-driven fix, each new browser run) rather than one giant commit — and spread genuine
  progress across at least 4 different days, since only `.spec.*`-touching commits count toward the
  8-commit minimum.
- Run `scripts/check_commit_rule.py` to verify the repository actually satisfies "≥8 commits
  touching test-script files, spanning ≥4 distinct days" before submission.
- Export the commit log to a text file, e.g. `git log --stat > git-commit-log.txt`.
- Run `scripts/compute_test_summary.py` across all 3 features' reports to get the real counts
  (features, test cases automated/executed/passed/failed, browser runs, bugs) for the submission
  `README.md`, then assemble it with `assets/readme-self-assessment-template.md` and the main report
  with `assets/main-report-template.md`.

## Workspace Layout

```text
reports/
`-- HW4/
    |-- <FR-XX>/
    |   |-- test-cases.md              (Phase 1, seeded from reports/HW2/<FR-XX>/test-cases.md)
    |   |-- tests/*.spec.ts            (Playwright specs, one file per feature)
    |   |-- data/*.json or *.csv       (external test data, Phase 3)
    |   |-- ai-audit.md                (Phase 2/8, per-feature prompt+output log)
    |   |-- ai-gap-analysis.md         (Phase 5)
    |   |-- reports/<browser>/         (HTML report per browser run, Phase 6)
    |   `-- bug-report.md              (Phase 7)
    |-- automation-report.md           (Phase 6, cross-feature run matrix)
    |-- main-report.md
    |-- ai-critique.md
    |-- demo-video-script.md
    |-- git-commit-log.txt
    `-- README.md
```

Demonstrate end-to-end use on one complete feature for the Agent Skill's own demo video (separate
from the Task 2 demo video, though they may reuse the same recording if it satisfies both). Real,
reproducible automation and genuine review findings improve the assessment; volume never permits
fabrication.
