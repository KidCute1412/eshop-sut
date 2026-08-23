# Human Review Checklist for HW6

Use this before finalizing generated tests, execution results, and reports.

## Scope and Source of Truth

- Three APIs are selected: one Pool A, one Pool B, one Pool C.
- Endpoint method/path matches `api_specification.md`.
- Business rules and expected results trace to `README.md`.
- Security cases map to SEC-01 through SEC-07 where applicable.
- State cases map to FR-10 when order status is involved.
- Contradictions or assumptions are documented.

## Test Case Quality

- At least 35 AI-generated cases exist per selected API before human extension.
- Every AI-generated case is labelled `VALID`, `INVALID`, or `INCOMPLETE`.
- Every invalid/incomplete case has a reason and correction or removal decision.
- At least five human-added cases exist per API.
- Every human-added case has an AI-miss reason.
- Expected results specify status, response schema/body, and side effect where observable.
- Negative cases isolate one invalid condition when practical.
- Security tests include missing token, wrong role, IDOR/role escalation, injection, or leakage as
  relevant to the selected API.

## Postman/Newman

- Every request sends `X-Student-Id: {StudentID}`.
- Protected endpoints obtain and use a real JWT.
- Admin endpoints are tested with admin token, user token, and no token where relevant.
- Variables/environments/data-driven files are used instead of duplicating brittle literal values.
- Newman CLI output and HTML report are real generated artifacts.

## Evidence and Bugs

- No executed case has `Evidence: None`.
- Failures are triaged as SUT bug, test bug, data/setup issue, or blocked.
- Bug reports include reproduction steps, expected/actual result, evidence, and real GitHub Issue
  link when filed.
- CI/CD screenshots and links point to real runs.

## Final Packaging

- Main report, README, AI audit, AI critique, bug report, CI/CD report, generator design,
  collection/environment/data, Newman report, Excel test cases, Git log, and supporting evidence
  are present.
- The AI test-generator diagram is self-drawn by the student.
- The README summary counts match the final test cases and Newman output.
