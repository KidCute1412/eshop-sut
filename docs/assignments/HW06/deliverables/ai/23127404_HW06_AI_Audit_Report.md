# HW06 — AI Audit Report

Student ID: `23127404`  
AI usage declaration: **I use AI tools for the following tasks.**

## Fidelity statement

This report records the AI-assisted work that is recoverable from the workspace, the retained task conversation, Git history, and generated artifacts. The repository does not contain a platform-native export of every chat turn; therefore this report does **not** invent missing prompts, timestamps, or model output. For each record below, the output is retained as a versioned file or a real Git commit and can be inspected directly.

| Field | Value |
|---|---|
| AI tool/model | Codex (GPT-5) |
| Work dates | 2026-08-23 and 2026-08-24 (UTC+07) |
| SUT | EShop backend at `http://127.0.0.1:3000` |
| Human responsibility | Review all generated cases, decide contract oracles, reproduce bugs, create account-owned evidence, and approve the final diagrams/report. |

## Recoverable interaction register

### R1 — Requirement review and test scope

- **Date/evidence time:** 2026-08-23; retained in commit `ef27f9a`.
- **Prompt:** “Rà soát kỹ yêu cầu chính ở `docs/assignments/HW06/specs`; chỉ chừa placeholder cho link video, GitHub Issues và ảnh CI.”
- **AI task/output:** Extracted the official HW06 requirements and selected one API from each required pool: `POST /api/login`, `POST /api/checkout`, and `PUT /api/admin/orders/:id/status`.
- **Retained output:** `specs/2026.HW06.API Testing_En.pdf`, `specs/manual.md`, `specs/HW06_submission_checklist.md`, and commit `ef27f9a`.
- **Human review:** Confirmed the three-API scope and that genuine external-account evidence must remain pending.

### R2 — AI-generated cases and human audit matrix

- **Date/evidence time:** 2026-08-23; retained in commits `662c2b4` and `105610e`.
- **Prompt:** “Implement the plan.”
- **AI task/output:** Generated 35 candidate cases per API and structured data-driven collections; retained audit fields `source`, `audit_label`, `audit_reason`, `contract_status`, and `expected_status`.
- **Retained output:** `postman/data/login_data.json`, `checkout_data.json`, `admin_orders_data.json`, `excel/23127404_HW06_API_Test_Cases.xlsx`, and `scripts/generate_hw06_verified_suite.py`.
- **Human review:** Added five extension cases per pool and separated the requirement oracle from observed vulnerable behavior. Final count: 105 AI-generated cases and 15 human-extended cases.

### R3 — Newman execution and evidence preservation

- **Date/evidence time:** 2026-08-23T15:23:46.653Z.
- **Prompt:** “Thực hiện evidence thật, không dựng số liệu hoặc ảnh chạy tool giả.”
- **AI task/output:** Implemented isolated fixtures and a runner that starts the local SUT, executes Newman, preserves raw JSON, and restores the prior SQLite database file.
- **Retained output:** `scripts/run_hw06_verified_evidence.js`, `evidence/execution-manifest.json`, and `newman-reports/`.
- **Observed result:** 120 primary cases, 320 HTTP requests, 688 assertions, and 0 runner failures against `127.0.0.1:3000`.
- **Human review:** Verified that numeric claims point to raw Newman JSON rather than generated screenshots.

### R4 — Defect analysis and reporting

- **Date/evidence time:** 2026-08-23 and 2026-08-24; retained in commits `dc362ec` and `272f1a6`.
- **Prompt:** “Bug chỉ có 6 bug thôi hay có thể tìm thêm và sâu hơn không; deliverables hiện tại chỉ là draft.”
- **AI task/output:** Investigated the selected API scope and deduplicated repeated symptoms into six root causes: two login-state defects, plaintext password exposure, cart-rule bypass, missing admin-role authorization, and a forbidden terminal-state transition.
- **Retained output:** `bugs/bug-report.md`, raw Newman references, six GitHub Issue templates, six public issue links, and `bugs/screenshots/bug_01.png` through `bug_06.png`.
- **Human review:** Created GitHub Issues #162–#167 and captured the authentic issue pages.

### R5 — CI/CD design

- **Date/evidence time:** 2026-08-23 and 2026-08-24; retained in commits `57a8474` and `f15130e`.
- **Prompt:** “Nếu không yêu cầu main thì cứ để CI chạy branch hiện tại.”
- **AI task/output:** Added a GitHub Actions workflow that installs dependencies/Newman, invokes the evidence-preserving runner, uploads reports, and listens on `23127404-LeTuanLoc`, `main`, and `master`.
- **Retained output:** `.github/workflows/api-tests.yml` and `cicd/workflows/api-tests.yml`.
- **Human review still required:** Run the workflow from the student GitHub account, capture one green run and one intentionally failing run, then record the real URLs/hashes and screenshots.

### R6 — Agent-skill design and reviewer correction

- **Date/evidence time:** 2026-08-23 and 2026-08-24; retained in commits `f18b53c` and `03ca938`.
- **Prompt:** “Generate an API test generator for the selected SUT APIs.” Follow-up reviewer prompt: “Generate valid auth tokens for protected suites” and “Bind admin requests to each iteration's order_id.”
- **AI task/output:** Created a reusable generator, skill instructions, pseudocode, Mermaid architecture/flow sources, and collection/data synthesis. Corrected the reviewer findings by adding real login bootstrap requests and dynamic `{{orderId}}` binding.
- **Retained output:** `agent-skills/api-test-generator/generator.py`, `SKILL.md`, `pseudocode.md`, diagrams, and commit `03ca938`.
- **Human review still required:** Make the final architecture decisions in the Mermaid diagrams and export the PNGs personally before submission.

### R7 — Documentation, issue evidence, and package updates

- **Date/evidence time:** 2026-08-24; retained in commits `f15130e`, `fa61cd0`, `272f1a6`, and `3b397c0`.
- **Prompt:** “Tôi đã thêm link GitHub Issues và hình ảnh. Kiểm tra và cập nhật các file liên quan.”
- **AI task/output:** Verified each screenshot against the matching Issue title/number, replaced issue placeholders in the README, bug report, main report, and checklist, rendered PDFs, and rebuilt the archive.
- **Retained output:** `README.md`, `bugs/bug-report.md`, `report/23127404_HW06_API_Testing_Report.md/.pdf`, and `23127404_HW06_AI_API_100.zip`.
- **Human review:** Confirmed screenshots are authentic browser captures and corresponding Issues are publicly accessible.

## Human review decisions and lessons

1. A `BUG DETECTED` row is a reproduction of an observed behavior, not proof that the behavior conforms to the requirement. The matrix therefore stores both the contract status and the observed status.
2. Stateful APIs need explicit fixture setup. Pool A isolates account state; Pool B exercises login → cart → checkout → cart query; Pool C seeds each initial order state.
3. Repeated reproductions are consolidated into root-cause issues. This avoids incorrectly inflating ten checkout manifestations into ten independent bugs.
4. Generated or simulated screenshots were removed. GitHub Issue, CI, and Postman Console evidence must be created from the student's account/tool session.
5. The reviewer found two material generator flaws (placeholder authorization tokens and fixed order ID). Both were corrected and verified by generating fresh collections.

## Remaining external evidence

The following must be appended after the student performs them: the exact Postman Console capture/run notes, the all-pass and intentional-fail GitHub Actions URLs/hashes/screenshots, the Unlisted YouTube URL, and any AI conversations that exist only in another platform's chat history. Do not reconstruct them from memory; attach/export the original text if available.
