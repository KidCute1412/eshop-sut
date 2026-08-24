# HW06 completion tracker — 23127404

This tracker is derived from `2026.HW06.API Testing_En.pdf`. It records only verified progress and does not treat placeholders as completed evidence.

## Completed and locally verifiable

- [x] Selected three distinct-pool APIs: `POST /api/login`, `POST /api/checkout`, and `PUT /api/admin/orders/:id/status`.
- [x] Created 120 test cases: 35 AI-generated and 5 human-extended cases per API.
- [x] Audited every AI-generated row with a label and technical rationale in the JSON data and Excel workbook.
- [x] Included Postman collections, environment, data-driven runs, pre-request header injection, Chai assertions, raw Newman JSON, and HTML reports.
- [x] Executed the isolated local suite: 320 requests, 688 assertions, and 0 runner failures; see `deliverables/evidence/execution-manifest.json`.
- [x] Documented six distinct reproducible root-cause bugs in `deliverables/bugs/bug-report.md`.
- [x] Added the GitHub Actions workflow and mirrored it in the deliverables folder.
- [x] Added the generator source, pseudocode, Mermaid sources, PNG diagrams, OpenAPI audit, Excel matrix, reports, PDFs, and package archive.
- [x] Created real granular local Git commits for HW06 work.

## Required before submission — student/account evidence

1. [x] Confirmed the selected API triple is not duplicated within the group and confirmed the Moodle deadline.
2. [x] Pushed `23127404-LeTuanLoc` to the public GitHub repository. The workflow is configured for `23127404-LeTuanLoc`, `main`, and `master`.
3. [x] Ran `POST /api/login` in Postman and saved `deliverables/postman/screenshots/postman_console_23127404.png`; it shows the expanded request headers, `X-Student-Id: 23127404`, and HTTP `200`.
4. [x] Created six GitHub Issues (#162–#167), linked them in `bug-report.md`, and saved their real browser captures as `bugs/screenshots/bug_01.png` through `bug_06.png`.
5. [x] Recorded the authentic all-pass GitHub Actions capture for `d07a9b1` in `cicd/screenshots/ci-pass.png` and its Action URL in the CI report.
6. [x] Created and captured the intentional failure for `aa32d91` (`TC-LOGIN-01` expected `999`, received `200`), then restored the correct `200` expectation on the current branch.
7. [x] Reviewed the Mermaid designs, accepted the architecture decisions, and exported the final `architecture_diagram.png` and `flow_diagram.png`.
8. [x] Recorded the Unlisted YouTube agent-skill demonstration and linked [https://youtu.be/RjtRRfqsz7s](https://youtu.be/RjtRRfqsz7s) in the README, main report, and agent-skill README.
9. [x] Finalized the AI Audit Report using all recoverable evidence. No platform-native transcript export exists, and no missing interaction was invented.
10. [ ] Regenerate the Git log and ZIP after the final documentation commit, inspect the archive, commit the package, then upload that ZIP to Moodle.

## Notes

- The official PDF requires a real commit for each procedural step and a text commit log. It does **not** require commits across four calendar days; never fabricate dates or hashes.
- `BUG DETECTED` appears on every test that reproduces a known root cause. It does not mean every such test is a separate bug. There are six root-cause issues in this submission.
- The workflow must run against the current branch or a PR. It does not need to run on `main` specifically.
