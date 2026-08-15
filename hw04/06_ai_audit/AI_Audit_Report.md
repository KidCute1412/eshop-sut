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
- **Prompt:** "Dựa vào đề bài `2026.HW04.Automation Testing_En.md` hãy thực hiện tạo một thư mục nộp bài có cấu trúc rõ ràng, những kiến thức bị thiếu hãy hỏi tôi trong quá trình thực hiện."
- **AI output:** Read the assignment spec, discovered the HW02 submission folder (`.../submit/23KTPM3-23127296-HW02`) contained only an empty `.git` (no actual content), and found that the SUT's own `README.md` already contains a "Test Summary Report" section referencing FR-03/FR-09/FR-13 from an earlier manual test-design pass, complete with a known-bug backlog and existing GitHub issues (#25–#35, #50–#51). Proposed candidate features per pool (Pool A: FR-02/FR-05/FR-01; Pool B: FR-09/FR-07/FR-08; Pool C: FR-14/FR-17/FR-19) and asked the student to choose one per pool via a structured question, per the assignment's requirement to self-declare features when HW02 is unavailable.
- **Human review performed:** Student chose FR-03 (Pool A), FR-09 (Pool B, as recommended), and FR-13 (Pool C) — all three matching the pre-existing manual test-design backlog already in the README.

### Entry 2 — Test case design (≥12 cases per feature)
- **Prompt:** "Hãy thiết kế các test case cho 3 tính năng tôi đề cập theo hướng data driven."
- **AI output:** Read the actual route handlers (`backend/server.js`) and UI components (`ForgotPassword.jsx`, admin `App.jsx`) for all three features side by side with the spec (`README.md` FR-03/FR-08/FR-09/FR-12/FR-13), producing 17 (FR-03), 14 (FR-09), and 12 (FR-13) test cases each — mixing positive/negative/boundary/edge/E2E — with expectations written against the **spec**, explicitly flagging where the real implementation is known to diverge.
- **Human review performed:** Review, added 2 tests for each of the functionality.

### Entry 3 — First script draft, config, and report-stamping tooling
- **Prompt:** "Tạo playwright file để automate việc chạy các test."
- **AI output:** Wrote three Playwright spec files (`tests/fr03-forgot-password.spec.js`, `fr09-coupon.spec.js`, `fr13-dashboard.spec.js`), three JSON fixtures (`tests/data/`), a `playwright.config.js` rewrite (3-browser projects, 3 auto-started `webServer`s for backend/frontend-web/frontend-admin, HTML reporter), and a report-stamping script (`scripts/stamp-report.mjs`) to inject "Run by: 23127296 | ISO timestamp" into the generated HTML report per the anti-cheat requirement.
- **Human review performed:** The scripts are correct.
