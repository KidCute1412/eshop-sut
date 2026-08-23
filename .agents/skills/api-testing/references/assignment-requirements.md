# HW6 Assignment Requirements

Use `2026.HW6.API_Testing_En.md` as the primary authority. This reference summarizes the parts
that affect agent behavior.

## Scope

- Select three APIs: one implementing a feature from Pool A, one from Pool B, and one from Pool C.
- Pool D/mobile is out of scope for HW6 because the homework targets backend APIs.
- Consult `api_specification.md` for available endpoints and `README.md` for correct business and
  security requirements.

## Per-API Pipeline

For each of the three selected APIs:

- Generate test cases with AI step by step, not through one generic prompt.
- Target at least 35 AI-generated cases per API.
- Cover domain partitions for every parameter.
- Cover state transitions where relevant, especially order states in FR-10.
- Cover security requirements SEC-01 through SEC-07 where applicable.
- Cover exact response schema validation against the API contract.
- Human-review every AI case and label it `VALID`, `INVALID`, or `INCOMPLETE` with reasoning.
- Correct invalid/incomplete cases.
- Add at least five human-designed cases missed by AI, and explain why AI missed them.
- Execute with Postman + Newman by default, or Karate/RestAssured if intentionally chosen.
- Send `X-Student-Id: {StudentID}` on every request.
- Preserve Newman/HTML report or equivalent real execution report.
- Report genuine bugs in Markdown and on GitHub Issues with screenshots/evidence.

## Cross-Suite Requirements

- Use and list as many relevant Postman features as practical: collections, variables,
  environments, data-driven runs, monitors, mock servers, pre-request scripts, test scripts.
- Integrate tests into CI/CD, normally GitHub Actions running Newman.
- Provide two sample CI commits/runs: one all-passing and one with one intentionally failing test.
- Provide Excel test cases and test summary.
- Provide the AI test-generator diagram and pseudocode.
- Provide AI Audit Report, AI Critique, Git commit log, main report, README, collections, scripts,
  reports, and supporting evidence.

## Grading Template

| No. | Criteria                                | Grade |
| --: | --------------------------------------- | ----: |
|   1 | API 1 full pipeline                     |    30 |
|   2 | API 2 full pipeline                     |    30 |
|   3 | API 3 full pipeline                     |    30 |
|   4 | Agent Skills / AI-driven test generator |    10 |
|     | Total                                   |   100 |

## Anti-Fabrication Constraints

Do not fabricate:

- `X-Student-Id` evidence.
- Newman output.
- Hostname/base URL evidence.
- GitHub Issue links.
- CI run links.
- Student self-drawn diagram.
- Commit log entries.

If a required artifact cannot be produced, document the exact blocker and mark it incomplete.
