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

1. [ ] Confirm the API triple is not duplicated by another member of the group and confirm the Moodle deadline.
2. [ ] Push this branch to the public GitHub repository. The workflow is configured for `23127404-LeTuanLoc`, `main`, and `master`.
3. [ ] Run one collection in Postman and save an authentic Console screenshot with expanded request headers showing `X-Student-Id: 23127404`.
4. [x] Created six GitHub Issues (#162–#167), linked them in `bug-report.md`, and saved their real browser captures as `bugs/screenshots/bug_01.png` through `bug_06.png`.
5. [ ] Obtain a green GitHub Actions run. Record its commit hash and URL and capture `cicd/screenshots/ci-pass.png`.
6. [ ] Create one temporary, intentional-failure commit, capture its red GitHub Actions run as `cicd/screenshots/ci-fail.png`, record its hash/URL, then revert the intentional change and obtain a final green run.
7. [ ] Review the Mermaid designs yourself, make any needed design changes, and export the final `architecture_diagram.png` and `flow_diagram.png`. Do not present an AI-generated image as self-drawn.
8. [ ] Record one 5–8 minute Unlisted YouTube demo of the generator and a real test run; add its URL to the README, main report, and agent-skill README.
9. [ ] Complete the AI Audit Report with the exact tool/model, timestamp, prompt, and output for every AI interaction that is not already recoverable in the workspace. Do not invent missing transcripts.
10. [ ] After all changes, regenerate the real Git log, update Markdown/PDF links, rebuild the ZIP, inspect it, commit the final evidence, and upload that ZIP to Moodle.

## Notes

- The official PDF requires a real commit for each procedural step and a text commit log. It does **not** require commits across four calendar days; never fabricate dates or hashes.
- `BUG DETECTED` appears on every test that reproduces a known root cause. It does not mean every such test is a separate bug. There are six root-cause issues in this submission.
- The workflow must run against the current branch or a PR. It does not need to run on `main` specifically.
