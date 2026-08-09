# HW04 — Automation Testing: Completion Checklist

> Source: `2026.HW04.Automation Testing_En.pdf` (8 pages).
> Submission workspace: `docs/assignments/HW04/deliverables/`.
> Replace every placeholder in angle brackets before submitting.

> Status updated 2026-08-09. `[x]` means verified in the workspace; `[ ]` means student-controlled, incomplete, or noncompliant. Current automation: 51 logical cases, 153 browser attempts, 131 reaching assertions, nine selected report directories, three report PDFs, and nine qualifying test-script commits across two days.

## 0. Non-negotiable requirements

- [ ] Confirm the Moodle deadline and the required submission link.
- [ ] Work individually and do not reuse another student's scripts **or prompts**.
- [x] Select exactly three **web** features: one from Pool A, one from Pool B, and one from Pool C.
- [x] Use the same three features as HW02: FR-06, FR-10, and FR-12. Pool D/mobile (FR-20) is out of scope for HW04.
- [ ] Confirm that the selected features are not duplicated with other members in the HW02 group.
- [x] Use Playwright (recommended) or Selenium 4, and declare all AI tools used.
- [ ] Keep the GitHub repository public before submission.
- [x] Keep every submission artefact under `docs/assignments/HW04/deliverables/` while preparing the assignment.
- [ ] Do not fabricate execution evidence: HTML reports need the student identifier and ISO timestamp; the video needs the student's own Vietnamese narration and authorship evidence.

## 1. Record assignment identity and scope

- [ ] Fill in `<StudentID>`, `<Full name>`, `<Class>`, repository URL, and submission date/time.
- [ ] Record the SUT revision/commit, setup instructions, frontend URL(s), API/backend dependencies, and test environment/OS.
- [x] Record the three selected features, their functional-requirement IDs, and the reason for each selection.

| Slot | Pool | Selected FR / feature | HW02 source or self-declaration | Test owner |
| --- | --- | --- | --- | --- |
| A | A — Authentication, Categories, Products | **FR-06 — Product detail view** | Selected in HW02 implementation plan | `23127404` |
| B | B — Cart and Checkout | **FR-10 — Order state machine** | Selected in HW02 implementation plan | `23127404` |
| C | C — Web Admin | **FR-12 — Access control** | Selected in HW02 implementation plan | `23127404` |

- [x] Confirmed scope: FR-06 is Pool A, FR-10 is Pool B, FR-12 is Pool C; do not select Pool D/mobile.

## 2. Plan test cases before automating

For **each** feature (A, B, and C):

- [x] Create at least **12 distinct test cases** (51 total: FR-06 16, FR-10 16, FR-12 19) with stable IDs.
- [x] Include an appropriate mix of positive, negative, boundary, and edge cases.
- [x] Define preconditions, test data, expected results, and test priority for every case in the JSON/design/matrix artifacts.
- [x] Mark all 51 cases as automated; document current oracle/cleanup limitations.
- [x] Map every automated case to the spec, external row, three browser outcomes, and selected reports.
- [x] Prepare valid seed roles/data and case setup; FR-12 cleanup postcondition remains a documented limitation.
- [x] Execute serially with explicit setup so cases do not depend on unspecified order.

Suggested test-case matrix to place in the main report:

| Feature | Case ID | Scenario/type | Preconditions | Data ID | Expected result | Automated? | Script |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `<A/B/C>` | `<ID>` | `<positive/negative/edge>` | `<...>` | `<...>` | `<...>` | `<Yes/No + reason>` | `<path>` |

## 3. Use AI with a reviewable, step-by-step workflow

- [ ] Start the AI Audit Report before the first AI interaction.
- [ ] Ask AI in several focused steps, e.g. analyse the selected requirement, propose cases, design locators, generate one feature's data-driven script, then improve assertions and reliability.
- [x] Do **not** use one generic “write all automation scripts” prompt as the whole workflow.
- [ ] Save, for every interaction: AI tool name, date/time, exact prompt, and AI output.
- [ ] Student performs and signs off the final personal review before submission (agent audits are already preserved).
- [x] Record what was accepted, changed, rejected, or added manually, with the reason and evidence/reference to the final code.
- [ ] Preserve enough of the AI output to make the audit report complete; do not replace it with a summary only.
- [ ] If no AI was used, include the exact required declaration: `I do not use any AI help in this exercise.`
- [ ] If AI was used, include the exact lead-in declaration: `I use AI tools for the following tasks,` followed by the required interaction records.

## 4. Implement reliable data-driven automation

For **each** selected feature:

- [ ] Generate the initial automation with AI, then retain an attributable prompt/output record.
- [x] Place test data in three separate JSON files; no inline case arrays are used.
- [x] Make each spec load and use external data at runtime.
- [x] Implement at least three distinct assertion patterns across the suite.
- [x] Use resilient, meaningful locators and document locator limitations.
- [x] Replace fixed sleeps with condition-based Playwright waits/assertions.
- [x] Isolate setup as far as supported; document FR-10 no-delete and FR-12 cleanup-verification limitations.
- [x] Include feature/case IDs in all test names and reports.
- [x] Preserve screenshots/traces/error context in the selected reports.
- [x] Run all nine feature/browser cells; 22 Firefox fixture failures remain pending a successful rerun.

Suggested implementation inventory:

| Feature | Spec file(s) | Data file(s) | Data-driven proof | Assertion patterns used | Setup/cleanup |
| --- | --- | --- | --- | --- | --- |
| FR-06 — Product detail view | `<path>` | `<path>` | `<case/data mapping>` | `<patterns>` | `<description>` |
| FR-10 — Order state machine | `<path>` | `<path>` | `<case/data mapping>` | `<patterns>` | `<description>` |
| FR-12 — Access control | `<path>` | `<path>` | `<case/data mapping>` | `<patterns>` | `<description>` |

## 5. Human review, corrections, and AI critique

For every feature:

- [x] Compare AI-generated code with the final code and list concrete corrections.
- [ ] Identify fragile selectors, weak/missing assertions, omitted cases, flaky waits, invalid test data, wrong assumptions, or other AI gaps that occurred.
- [ ] Explain why each gap likely occurred (for example: insufficient prompt context, model limitation, incomplete UI/requirement information, or feature-specific state).
- [ ] Explain the correction and how it improves trustworthiness of the test.
- [ ] Document any test case that remains unautomated and why.

- [x] Write the mandatory **AI Critique** as one 246-word paragraph.
- [x] Answer what AI got wrong/incomplete, why, and the collaboration principle learned.
- [x] Verify the word count is within 200–300 words.

Suggested review table:

| Feature/case | AI proposal/problem | Why it was insufficient | Human correction | Final evidence |
| --- | --- | --- | --- | --- |
| `<ID>` | `<...>` | `<...>` | `<...>` | `<commit/path/report>` |

## 6. Execute and preserve multi-browser evidence

- [x] Configure exactly Chromium, Firefox, and WebKit.
- [x] Attempt each feature on each browser: 9 runs, 153 scheduled cases.
- [x] Generate a complete HTML/JSON/metadata directory for every run.
- [x] Embed `Run by: 23127404` visibly in every HTML report.
- [x] Embed an ISO 8601 timestamp in every report.
- [ ] Open each report and visually verify the identifier, timestamp, browser, executed cases, and pass/fail status.
- [x] Preserve the complete selected report directories, including their retained `data/` diagnostics.
- [x] Distinguish expected negative-test passes, assertion failures, and 22 pre-test Firefox fixture failures.
- [ ] Record exact run commands, date/time, SUT URL/version, browser/version, totals, and report location.

| Feature | Browser | Command | ISO timestamp | HTML report path | Executed | Passed | Failed | Verified |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| FR-06 | Chromium | `<command>` | `<ISO>` | `<path>` | `<n>` | `<n>` | `<n>` | `[ ]` |
| FR-06 | Firefox | `<command>` | `<ISO>` | `<path>` | `<n>` | `<n>` | `<n>` | `[ ]` |
| FR-06 | WebKit | `<command>` | `<ISO>` | `<path>` | `<n>` | `<n>` | `<n>` | `[ ]` |
| FR-10 | Chromium | `<command>` | `<ISO>` | `<path>` | `<n>` | `<n>` | `<n>` | `[ ]` |
| FR-10 | Firefox | `<command>` | `<ISO>` | `<path>` | `<n>` | `<n>` | `<n>` | `[ ]` |
| FR-10 | WebKit | `<command>` | `<ISO>` | `<path>` | `<n>` | `<n>` | `<n>` | `[ ]` |
| FR-12 | Chromium | `<command>` | `<ISO>` | `<path>` | `<n>` | `<n>` | `<n>` | `[ ]` |
| FR-12 | Firefox | `<command>` | `<ISO>` | `<path>` | `<n>` | `<n>` | `<n>` | `[ ]` |
| FR-12 | WebKit | `<command>` | `<ISO>` | `<path>` | `<n>` | `<n>` | `<n>` | `[ ]` |

## 7. Report genuine defects

- [ ] Treat a failing assertion as a possible SUT defect only after ruling out script/data/environment errors.
- [ ] For every genuine defect found, create a GitHub Issue in the public repository.
- [ ] Include reproduction steps, actual and expected results, environment, severity/priority, and evidence in the GitHub Issue.
- [ ] Attach a screenshot to each GitHub Issue.
- [ ] Add the issue URL and matching screenshot(s) to the Markdown bug report.
- [ ] Link the affected test case, browser run, and HTML report in the bug report.
- [ ] If no genuine bugs are found, state this explicitly in the main report and README test summary.

## 8. Maintain the required Git history

- [x] Preserve **9 meaningful qualifying commits** that modify HW04 `.spec.ts` files.
- [ ] Spread those qualifying commits across at least **4 different calendar days**.
- [x] Ensure each qualifying commit represents meaningful test progress.
- [x] Exclude documentation-only commits from the qualifying count.
- [x] Export hash, author, ISO date/time, subject, and changed files.
- [ ] Verify the exported log demonstrates the 8 qualifying test-script commits and 4-day span.

## 9. Create the demo video

- [ ] Record an **unlisted YouTube** video of at least **5 minutes**.
- [ ] Narrate in Vietnamese.
- [ ] Demonstrate one selected automation script running end to end.
- [ ] Show the multi-browser execution and the generated HTML report.
- [ ] Explain at least one human fix made to an AI-generated script.
- [ ] Prove authorship by showing either face-cam **or** a terminal running both `whoami` and `hostname`.
- [ ] Open the uploaded link while logged out/incognito if practical to confirm viewers can access it without it being public-listed.
- [ ] Add the video URL to the main report and README summary.

## 10. Agent Skill (recommended; assessment category worth 10 points)

- [x] Submit a reusable Agent Skill for the data-driven, multi-browser workflow.
- [x] Include complete skill source, usage instructions, validator, and contract reference.
- [ ] Record a separate unlisted YouTube demonstration showing the skill applied end to end to one complete feature.
- [ ] Include the skill path and demo URL in the main report/README.
- [ ] If not submitting, record that the 10-point Agent Skill assessment category is intentionally not claimed.

## 11. Assemble deliverables

Use this suggested layout inside `docs/assignments/HW04/deliverables/` (names may be adjusted, but retain all required content):

```text
deliverables/
├── README.md
├── report/
│   ├── <StudentID>_HW04_Automation_Report.md
│   └── <StudentID>_HW04_Automation_Report.pdf
├── ai/
│   ├── <StudentID>_HW04_AI_Critique.md
│   ├── <StudentID>_HW04_AI_Critique.pdf
│   ├── <StudentID>_HW04_AI_Audit_Report.md
│   └── <StudentID>_HW04_AI_Audit_Report.pdf
├── reports/
│   └── <feature>-<browser>-<ISO-timestamp>/  # complete HTML-report assets
├── git/
│   └── <StudentID>_HW04_git_commit_log.txt
├── bugs/
│   ├── bug-report.md
│   └── screenshots/
├── skills/                                   # if submitting Agent Skill
└── supporting-materials/
```

- [x] Write the main report in Markdown and export an equivalent PDF.
- [ ] Include in the main report: scope, selected features, test design/mapping, implementation, data-driven approach, assertion patterns, run commands/results, report links/paths, AI review/gap analysis, bugs, unautomated cases, repository URL, and YouTube URL(s).
- [x] Write the AI Audit Report in Markdown and export an equivalent PDF appendix; retain its honest transcript-gap warning.
- [x] Write the AI Critique in Markdown and export an equivalent PDF appendix.
- [x] Store all nine HTML report directories completely under `deliverables/automation/reports/`.
- [x] Store the qualifying text Git log under `deliverables/git/`.
- [ ] Store bug report/screenshot evidence under `deliverables/bugs/` whenever bugs exist.
- [ ] Include source scripts and external data files in the public GitHub repository; link the exact repository in the reports/README.

## 12. Complete `README.md` and self-assessment

- [ ] Add the public GitHub repository URL.
- [ ] Add the unlisted YouTube demo video URL.
- [ ] Add the Agent Skill path and demo URL if applicable.
- [x] Include a summary of features, logical cases, attempts, assertion outcomes, fixture failures, runs, and candidates.
- [x] Reconcile totals with every selected JSON report and the 51-row matrix.
- [ ] Add this self-assessment table and fill every score:

| No. | Criterion | Maximum | Self-assessed grade | Evidence |
| ---: | --- | ---: | ---: | --- |
| 1 | Task 1 — Feature A | 25 | `<0–25>` | `<links/paths>` |
| 2 | Task 1 — Feature B | 25 | `<0–25>` | `<links/paths>` |
| 3 | Task 1 — Feature C | 25 | `<0–25>` | `<links/paths>` |
| 4 | Task 2 — Demo video | 15 | `<0–15>` | `<URL>` |
| 5 | Agent Skills | 10 | `<0–10>` | `<path/URL or N/A>` |
|  | **Total** | **100** | **`<000–100>`** |  |

## 13. Final validation and packaging

- [ ] Re-run the entire suite from a clean/restarted test environment where feasible.
- [ ] Re-open all nine (or more) HTML reports and verify `Run by: <StudentID>` and an ISO timestamp are visible.
- [x] Structurally validate all selected report directories, identity, timestamps, case counts, completion, and totals; interactive manual opening remains pending.
- [x] Regenerate report PDFs from the final Markdown and text-validate them; visual student review remains pending.
- [ ] Verify AI Audit Report includes every interaction's tool, timestamp, prompt, and output.
- [x] Verify AI Critique is 246 words.
- [ ] Verify GitHub repository is public and its commit history meets both numerical constraints.
- [ ] Verify each GitHub Issue screenshot is attached and also represented in the submitted bug evidence.
- [ ] Verify the YouTube video is unlisted, at least 5 minutes, narrated in Vietnamese, shows multi-browser/report evidence, an AI fix, and face-cam or `whoami` + `hostname`.
- [ ] Ensure no required document is missing; the specification states that missing any required document results in a score of 0.
- [x] Set the current evidence-based provisional self-assessment to `063`; recalculate after adding student-controlled evidence.
- [x] Create `23127404_HW04_AI_Automation_063.zip` inside `deliverables/`; regenerate if the grade/evidence changes.
- [x] Inspect the ZIP: required documents/source/skill are present, nine report triplets exist, and `node_modules`, `test-results`, and `dist` are absent.
- [ ] Submit the ZIP to Moodle before the stated deadline.

## Final evidence count (minimum)

- [x] 3 selected web features, one each from Pools A, B, and C: FR-06, FR-10, and FR-12.
- [ ] 12+ test cases per selected feature (36+ planned cases total).
- [ ] 3 external data files or equivalent external CSV/JSON datasets used by scripts.
- [ ] 3+ assertion patterns.
- [ ] 9+ browser runs and an HTML report for every run.
- [ ] 8+ qualifying test-script commits spanning 4+ days.
- [ ] 1 unlisted Vietnamese demo video, 5+ minutes.
- [x] Markdown and PDF forms of the main report, AI Audit Report, and AI Critique.
