# HW06 — AI Audit Report

Student: **Lê Tuấn Lộc** (`23127404`)
AI usage declaration: **AI tools were used to assist test design, artifact generation, review, and documentation.**

## Evidence basis and fidelity

This audit records AI-assisted work that is recoverable from version-controlled artifacts, Git history, and retained execution evidence. A platform-native export of every chat turn is not available. Accordingly, the report identifies the tool, time period, task request, retained output, and human review decision for each recoverable interaction; it does not invent missing prompts, timestamps, or model responses.

| Field | Value |
|---|---|
| AI tool/model | Codex (GPT-5) |
| Work period | 2026-08-23 to 2026-08-24 (UTC+07) |
| SUT | EShop backend at `http://127.0.0.1:3000` |
| Human responsibility | Select scope, approve contract oracles, audit generated cases, reproduce defects, create account-owned evidence, and approve the final diagrams and report. |

## Recoverable interaction register

### R1 — Requirement review and scope

- **Date/evidence:** 2026-08-23; commit `ef27f9a`.
- **Task request:** Review the official HW06 specification and prepare a compliant API-testing scope.
- **AI output:** Selected three APIs from distinct pools: `POST /api/login`, `POST /api/checkout`, and `PUT /api/admin/orders/:id/status`.
- **Retained evidence:** `specs/2026.HW06.API Testing_En.pdf`, `specs/manual.md`, `specs/HW06_submission_checklist.md`, and commit `ef27f9a`.
- **Human decision:** Approved the three-API scope.

### R2 — Test-case generation and audit matrix

- **Date/evidence:** 2026-08-23; commits `662c2b4` and `105610e`.
- **Task request:** Produce broad candidate API tests and retain a reviewable data-driven matrix.
- **AI output:** Created 35 candidate cases per API, Postman collections, iteration data, and audit fields: `source`, `audit_label`, `audit_reason`, `contract_status`, and `expected_status`.
- **Retained evidence:** `postman/data/*.json`, `postman/collections/*.json`, and `excel/23127404_HW06_API_Test_Cases.xlsx`.
- **Human decision:** Added five extension cases per API and separated the contract oracle from observed SUT behavior. Final total: 105 AI-generated and 15 human-extended cases.

### R3 — Newman execution evidence

- **Date/evidence:** 2026-08-23T15:23:46.653Z.
- **Task request:** Execute the suite against the local SUT and preserve verifiable raw evidence rather than simulated screenshots.
- **AI output:** Implemented isolated fixture handling and an evidence-preserving runner.
- **Retained evidence:** `scripts/run_hw06_verified_evidence.js`, `evidence/execution-manifest.json`, and `newman-reports/`.
- **Observed result:** 120 primary cases, 320 HTTP requests, 688 assertions, and 0 runner failures.
- **Human decision:** Accepted raw Newman JSON as the source for numeric claims.

### R4 — Defect analysis and reporting

- **Date/evidence:** 2026-08-23 to 2026-08-24; commits `dc362ec` and `272f1a6`.
- **Task request:** Investigate observed deviations and distinguish independent root causes from repeated manifestations.
- **AI output:** Consolidated the selected scope into six root-cause defects: login counter behavior, lock duration, plaintext password exposure, cart-rule bypass, missing admin-role authorization, and an invalid terminal-state transition.
- **Retained evidence:** `bugs/bug-report.md`, raw Newman evidence, GitHub Issues [#162](https://github.com/KidCute1412/eshop-sut/issues/162)–[#167](https://github.com/KidCute1412/eshop-sut/issues/167), and `bugs/screenshots/`.
- **Human decision:** Created the Issues and captured authentic issue pages.

### R5 — CI/CD evidence

- **Date/evidence:** 2026-08-23 to 2026-08-24; commits `57a8474`, `f15130e`, `d07a9b1`, and `aa32d91`.
- **Task request:** Run the API evidence suite in GitHub Actions on the working branch and retain both all-pass and intentional-failure evidence.
- **AI output:** Added the workflow and delivery copy at `.github/workflows/api-tests.yml` and `cicd/workflows/api-tests.yml`.
- **Retained evidence:** [all-pass run](https://github.com/KidCute1412/eshop-sut/actions/runs/32665200965/job/97257113623), [intentional-failure run](https://github.com/KidCute1412/eshop-sut/actions/runs/32665781240/job/97258816558), and `cicd/screenshots/`.
- **Human decision:** Confirmed both account-owned captures and restored the test expectation to `200`.

### R6 — Agent-skill design and correction

- **Date/evidence:** 2026-08-23 to 2026-08-24; commits `f18b53c` and `03ca938`.
- **Task request:** Build a reusable API-test-generator skill for the selected APIs, then address execution defects found in review.
- **AI output:** Created the generator, skill instructions, pseudocode, Mermaid sources, and test-artifact synthesis. The reviewed implementation bootstraps real protected-suite tokens and binds admin requests to iteration-specific `orderId` values.
- **Retained evidence:** `agent-skills/api-test-generator/`, `agent-skills/diagrams/`, and commit `03ca938`.
- **Human decision:** Reviewed and approved the final Mermaid design sources and exported PNG diagrams.

### R7 — Submission evidence and documentation

- **Date/evidence:** 2026-08-24; commits `272f1a6`, `3faa5ba`, and `bb9056d`.
- **Task request:** Link account-owned evidence and complete submission documentation.
- **AI output:** Connected GitHub Issues, CI captures, the Postman Console capture, and the Unlisted video to the delivery artifacts.
- **Retained evidence:** `README.md`, `report/23127404_HW06_API_Testing_Report.md/.pdf`, `cicd/`, `postman/screenshots/postman_console_23127404.png`, and [video demonstration](https://youtu.be/RjtRRfqsz7s).
- **Human decision:** Confirmed evidence authenticity, video availability, group scope, deadline, and final submission readiness.

## Review conclusions

1. A `BUG DETECTED` result documents an observed defect reproduction; it is not a claim that the SUT conforms to its contract.
2. Stateful flows require controlled fixtures. Pool A isolates account state; Pool B exercises login, cart, checkout, and cart query; Pool C seeds each required order state.
3. Repeated manifestations are reported as six root causes rather than inflated into independent bugs.
4. GitHub Issue, CI, and Postman Console screenshots are account-owned tool captures, not generated images.
5. The final artifact set includes the public evidence links, Postman header capture, diagrams, AI audit, reports, and Unlisted video link.

## Audit closure

All recoverable AI-assisted work is documented above. No additional platform-native chat export exists, and no missing interaction content has been reconstructed from memory.
