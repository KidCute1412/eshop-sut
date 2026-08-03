# AI Audit Report (Mandatory Appendix) — HW04 Automation Testing

**Student ID:** 23127296
**Declaration:** "I use AI tools for the following tasks."

## Tools declared

- **Claude Code** (Anthropic), model Claude Sonnet 5, running as a CLI/VSCode-extension agent with file read/write/bash access to the local `eshop-sut` repository (backend, frontend-web, frontend-admin) and the `hw04` submission folder.
- **Playwright** (`@playwright/test` 1.62.1) — automation framework, run across Chromium, Firefox, and WebKit projects.
- **GitHub CLI (`gh`)** — used, at the student's explicit direction, to file GitHub Issues for defects the automation surfaced.

## Interaction log

> Produced across one continuous Claude Code session on 2026-08-03. Entries are grouped by deliverable/decision rather than by exact timestamp.

### Entry 1 — Scoping and feature self-declaration
- **Prompt:** "Dựa vào đề bài `2026.HW04.Automation Testing_En.md` hãy thực hiện tạo một thư mục nộp bài có cấu trúc rõ ràng và thực hiện những phần bạn có thể làm, những kiến thức bị thiếu hãy hỏi tôi trong quá trình thực hiện."
- **AI output:** Read the assignment spec, discovered the HW02 submission folder (`.../submit/23KTPM3-23127296-HW02`) contained only an empty `.git` (no actual content), and found that the SUT's own `README.md` already contains a "Test Summary Report" section referencing FR-03/FR-09/FR-13 from an earlier manual test-design pass, complete with a known-bug backlog and existing GitHub issues (#25–#35, #50–#51). Proposed candidate features per pool (Pool A: FR-02/FR-05/FR-01; Pool B: FR-09/FR-07/FR-08; Pool C: FR-14/FR-17/FR-19) and asked the student to choose one per pool via a structured question, per the assignment's requirement to self-declare features when HW02 is unavailable.
- **Human review performed:** Student chose FR-03 (Pool A), FR-09 (Pool B, as recommended), and FR-13 (Pool C) — all three matching the pre-existing manual test-design backlog already in the README, rather than the AI's other suggested options.

### Entry 2 — Test case design (≥12 cases per feature)
- **Prompt:** implicit continuation, applied to designing test cases for the three chosen features.
- **AI output:** Read the actual route handlers (`backend/server.js`) and UI components (`ForgotPassword.jsx`, admin `App.jsx`) for all three features side by side with the spec (`README.md` FR-03/FR-08/FR-09/FR-12/FR-13), producing 17 (FR-03), 14 (FR-09), and 12 (FR-13) test cases each — mixing positive/negative/boundary/edge/E2E — with expectations written against the **spec**, explicitly flagging where the real implementation is known to diverge.
- **Human review performed:** Not yet — flagged in `00_report/Review_And_GapAnalysis.md` as one of the things the student must personally confirm before submission.

### Entry 3 — First script draft, config, and report-stamping tooling
- **AI output:** Wrote three Playwright spec files (`tests/fr03-forgot-password.spec.js`, `fr09-coupon.spec.js`, `fr13-dashboard.spec.js`), three JSON fixtures (`tests/data/`), a `playwright.config.js` rewrite (3-browser projects, 3 auto-started `webServer`s for backend/frontend-web/frontend-admin, HTML reporter), and a report-stamping script (`scripts/stamp-report.mjs`) to inject "Run by: 23127296 | ISO timestamp" into the generated HTML report per the anti-cheat requirement.
- **Human review performed:** None yet at this point — the first real run (Entry 4) is what actually exposed the problems.

### Entry 4 — First real run, failures, and fixes (the actual "human review" step)
- **AI output / self-correction:** Ran the suite on Chromium. First result: 12 passed / 3 failed / **22 not run**. Diagnosed and fixed, in order:
  1. `test.describe.configure({ mode: 'serial' })` in all three spec files caused Playwright to skip every remaining test in a block after the first failure — since several tests are *designed* to fail (they assert spec-correct behavior against a known bug), this silently hid 22 other tests. Removed it; ordering is instead guaranteed by global `fullyParallel: false` / `workers: 1`.
  2. `page.getByLabel(...)` locators in the FR-03 UI tests timed out, because `ForgotPassword.jsx`'s `<label>` elements aren't associated with their `<input>` via `htmlFor`/`id`. Replaced with structural locators (`page.locator('form input[type="text"]').first()`).
  3. The FR-13 dashboard revenue-card UI test read `innerText` immediately after the heading became visible, racing the page's own async `fetchData()` call — first fixed-config run still showed `Received: 0`. Replaced the one-shot read with a self-retrying `expect(locator).not.toHaveText('0 ₫')` before reading the value.
  4. The original `webServer` config (copied from the Playwright starter template) set `reuseExistingServer: !process.env.CI`, which let state (coupon usage counts, delivered-order totals) leak between separate `--project=<browser>` invocations since this SUT's backend resets its entire SQLite DB only on a fresh boot. Set `reuseExistingServer: false` unconditionally.
- **Human review performed:** This entire fix cycle is documented, with the "why the AI draft got it wrong" reasoning, in `00_report/Review_And_GapAnalysis.md` §1 — **the student must read this section and confirm agreement before final submission**, since the AI both wrote the bug and diagnosed/fixed it in the same session.

### Entry 5 — Multi-browser execution and evidence collection
- **AI output:** Re-ran the full suite on Chromium, Firefox, and WebKit (fresh backend/frontend servers each time). All three runs produced identical results: 29 passed / 8 failed / 0 skipped, with the 8 failures mapping 1:1 to genuine spec violations (confirmed numerically, e.g. displayed revenue = exactly 2× the correct sum). Stamped all three HTML reports and captured evidence screenshots (a headless-Chromium script that opens each report and screenshots the expanded failing-test row) for the 7 bug-worthy failures.
- **Human review performed:** Student should personally open all three HTML reports and spot-check at least the failing rows before submission (see checklist in the top-level `README.md`).

### Entry 6 — Bug filing
- **Prompt:** Asked the student whether to reuse the existing GitHub issues (#25–#35, #50–#51) or file new ones for HW04; student chose to file new issues for all findings.
- **AI output:** Filed 6 new GitHub issues (#135–#140) on `KidCute1412/eshop-sut`, each linked back to the relevant earlier issue for traceability, each with a screenshot evidence link and exact repro steps/file:line citations. One additional defect found while writing the E2E checkout test (client-controlled `total_amount`, no server-side recomputation) was **not** filed as an issue, since it wasn't caught by a failing automated assertion — documented as a manual-review finding only, to avoid overstating what automation actually detected.
- **Human review performed:** Student approved the push-to-remote and issue-filing actions before they were executed (see the AskUserQuestion prompts in this session); still recommended the student skim each filed issue for accuracy.

## Note on method

Every "known bug" claim in this submission was reproduced by an actual `npx playwright test` run against a locally running instance of the SUT (backend + frontend-web + frontend-admin, freshly started each time) — not inferred from reading the code alone. The exact failure numbers (e.g. "Received: 5000000", "Received: 2100000") are copy-pasted from real Playwright output captured in this session, not fabricated. What the AI could not do — record a narrated demo video, or perform the actual final human sign-off on the review document — is left explicitly open in `README.md` and `00_report/Review_And_GapAnalysis.md`.
