# HW04 Manual Completion Guide — 23127404

This guide separates work that requires the student's direct action from documentation that can be prepared safely. It is based on the eight-page `2026.HW04.Automation Testing_En.pdf`, the repository's HW04 completion checklist, and the HW02 selection record.

## Verified assignment identity and scope

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc |
| Student ID | 23127404 |
| Class | `CSC15003` (student-confirmed) |
| Public repository | https://github.com/KidCute1412/eshop-sut (student-confirmed public repository) |
| Pool A | FR-06 — Product detail view |
| Pool B | FR-10 — Order state machine |
| Pool C | FR-12 — Access control |
| Automation framework currently present | Playwright 1.55.0 with TypeScript; Node.js 22.17.0; npm 10.9.2 |

FR-06, FR-10, and FR-12 are the same three web features recorded in the HW02 implementation plan. FR-20/FR-23 mobile work is not part of HW04.

## Current readiness snapshot (9 August 2026)

The repository preserves one historical automated logical case, `FR06-DT-01`, and a combined Playwright report representing that case on Chromium, Firefox, and WebKit. This is pre-existing evidence, not part of the selected final run set.

A new suite under `deliverables/automation/` defines 51 data-driven cases: FR-06 has 16 external JSON rows, FR-10 has 16, and FR-12 has 19. The final selected matrix contains nine complete HTML/JSON/metadata report directories and has passed structural identity, timestamp, case-count, and totals validation. Across 153 scheduled browser attempts, all 153 reached assertions: 96 passed and 57 failed across 19 unique logical cases. No selected run has a Firefox fixture failure.

Firefox was rerun headless with an option-free Playwright context after isolating incompatible `Desktop Firefox` device options that caused the earlier `newPage()` failures. All 51 Firefox cases reached assertions; the final run ledger and evidence paths are in `deliverables/supporting-materials/`.

No public HW04 Issue URL, main demo URL, or Agent Skill demo URL has been verified. Those items must remain `Not Collected` or `PENDING`. The Markdown/PDF report set has been generated and text-validated; the Firefox rerun is pinned to `a390bc125713a1759443a4e84929641d432a45dc`, while each selected report records its own revision. Agent triage has now classified the 19 candidates as 17 confirmed defects and 2 rejected oracle gaps. The existing archive is provisional and must be regenerated after student-only evidence or the self-score changes.

The full HW04 Git history contains nine qualifying commits that change `.spec.ts` files: the legacy `f905546` commit dated 27 July 2026 plus eight deliverables-suite commits dated 9 August 2026 through `aa316e0bdb75ef27e2af1cf05e37570ee403bcf7`. The eight-commit count is exceeded, but the work spans only two calendar days. Therefore, the separate four-day requirement remains **noncompliant**. Documentation-only commits do not count. Do not backdate, amend dates, or otherwise fabricate the missing span.

Chromium and WebKit reports retain their own exact revisions in metadata; the final Firefox reports use `a390bc125713a1759443a4e84929641d432a45dc`. Do not attribute all nine runs to one revision unless they are rerun together.

## Student-only actions before submission

1. Confirm the Moodle deadline, submission link, class code, and that FR-06/FR-10/FR-12 do not duplicate another member's HW02 choices.
2. Keep the GitHub repository public. Do not replace the honest pre-`aa316e0` execution-revision qualification with the latest commit unless the nine runs are genuinely repeated at that revision.
3. Review and approve at least 12 distinct cases for each feature in `deliverables/supporting-materials/test_case_matrix.md`.
4. Review the completed FR-06, FR-10, and FR-12 source, external data, locators, waits, and assertion patterns. The suite is implemented; remaining work is evidence/defect reconciliation, not case generation.
5. Preserve the exported nine-commit log. The commit count is met; retain the explicit two-day/noncompliant disclosure.
6. Preserve the nine structurally validated final report directories identified in `deliverables/supporting-materials/execution_manifest.md`; do not substitute superseded diagnostic/rerun directories in the totals.
7. Manually open every selected HTML report and visually confirm `Run by: 23127404`, ISO timestamp, browser, cases, outcomes, and linked assets. Automated validation has passed, but the assignment also expects human inspection.
8. Use the agent-generated triage and Issue packets. File the 17 confirmed packets, attach their screenshots, and send the resulting URLs to the agent; the two rejected candidates must not be filed. The superseded Firefox `newPage()` diagnosis is not a final SUT bug.
9. Record the 5+ minute unlisted YouTube demo in Vietnamese. Show one script end to end, the multi-browser run, an HTML report, one human correction to AI output, and either face-cam or terminal output from both `whoami` and `hostname`.
10. If claiming Agent Skills points, review the current reusable source under `deliverables/agent-skill/playwright-data-driven-multibrowser/`, validate it end to end, and record a separate unlisted demonstration. Source presence without a qualifying demo is not enough to claim the category.
11. Replace every `PENDING` marker only with verified data. Reconcile all totals against the run manifests and reports.
12. Visually open the generated PDFs, test external links while logged out where practical, choose the final self-assessed grade, and create `<StudentID>_HW04_AI_Automation_<000-100>.zip` only after replacing student-controlled placeholders.

## Evidence-state rules

- `Planned`: designed but not run.
- `Executed`: directly observed in the named environment and supported by evidence.
- `Blocked`: execution began but a prerequisite prevented the expected observation.
- `Not Executed`: no qualifying run occurred.
- `PENDING`: a student-supplied identity, URL, date, or decision has not been supplied.

Never convert a HW02/HW03 observation, static source inspection, or a legacy report statement into a new HW04 execution result. Keep the exact source and evidence date visible.

## Final integrity gate

- [x] All 51 logical cases are traceable to external data objects and scripts; final run evidence covers each case on three browsers.
- [x] Nine selected browser runs have complete, attributable HTML/JSON/metadata assets and passed automated validation.
- [x] Counts in README, main report, run manifest, reports, and bug register agree: 153 = 96 + 57.
- [x] The 57 recorded failures are assertion failures; no selected Firefox environment failures remain.
- [ ] Every assertion failure maps to a fully triaged defect or an explicit non-SUT classification.
- [ ] Every defect has authentic evidence and a public Issue URL, or the report explicitly says no genuine defect was found.
- [ ] AI prompts and outputs are reproduced exactly where available; missing history remains disclosed.
- [x] AI Critique is one paragraph and contains 246 words under the documented counting method.
- [ ] Demo authorship and Vietnamese narration are visible/audible.
- [x] Nine qualifying test-script commits are documented across two calendar days.
- [ ] Four qualifying calendar days are not present; the submission must retain the noncompliance disclosure.
- [x] Three report PDFs were generated and text-validated (main 8, critique 1, audit 5 pages).
- [ ] Final `<StudentID>_HW04_AI_Automation_<000-100>.zip` is created only after manual evidence and grade updates.
- [ ] Final ZIP name/grade, external links, visual PDF inspection, and Moodle upload have been manually verified.
