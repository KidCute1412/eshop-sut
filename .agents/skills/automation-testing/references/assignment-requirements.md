# HW04 Assignment Requirements (Summary)

Full text: `2026.HW04.Automation Testing_En.pdf`. This is a condensed reference, not a replacement —
re-read the PDF if any requirement below seems ambiguous.

## Scope

- SUT: EShop (`https://github.com/ttbhanh/eshop-sut`), same app as HW02/HW03.
- Automate the **same 3 web features selected in HW02**, one each from Pool A (Authentication/
  Categories/Products), Pool B (Cart/Checkout), Pool C (Web Admin). Pool D (Mobile) is not used —
  this homework is web-frontend automation only.

## Task 1 — AI-Generated Automation Scripts

- Per feature: convert **at least 12 test cases** (any mix of positive/negative/edge) into
  automation scripts, driving the AI step by step, not with one generic prompt.
- **Data-driven**: test data in a separate `.csv`/`.json` file; hardcoded inline arrays/objects are
  not accepted.
- **At least 3 distinct assertion patterns** across the suite.
- **At least 3 browsers** (Chromium/Firefox/WebKit, or Chrome/Edge/Firefox); every feature runs on
  all 3 → at least **9 browser runs** total.
- Every run produces an **HTML report** (Allure or Playwright HTML reporter) visibly showing
  `Run by: {StudentID}` (title/header/footer/metadata) plus an ISO timestamp.
- **Human review**: critique and fix the AI-generated scripts; report what the AI got wrong or
  missed (fragile selectors, weak/missing assertions, missing edge cases, flaky waits) and *why* it
  missed each.
- **Bug reporting**: for every failing assertion that reveals a genuine defect, log it in the
  Markdown report and file a real GitHub Issue with a screenshot attached.
- Document any of the 12+ test cases that could not be automated, and why.

## Task 2 — Demo Video

- Unlisted YouTube video, **≥5 minutes**, narrated in **Vietnamese**.
- Demonstrates ONE automation script running end to end: the multi-browser run and the generated
  HTML report.
- Narrates **at least one real fix** made to the AI-generated script during review.
- Must show authorship: **face-cam OR a terminal running `whoami` and `hostname`**.

## Agent Skill (Encouraged, 10 points)

- Build a reusable skill for this data-driven, multi-browser automation workflow.
- Submit with a demonstration video (YouTube) showing end-to-end use on one complete feature.

## AI Audit Report (Mandatory Appendix)

Same schema as HW02/HW03: per AI interaction, record AI tool name, date/time, verbatim prompt, and
the AI output (or a reference to it). Declare explicitly if no AI was used.

## AI Critique (200-300 words, Mandatory)

Address: where the AI was wrong/biased/incomplete; why it failed to catch the issue; what principle
was learned about collaborating with AI.

## Anti-AI-Cheat Constraints

- HTML reports must contain `Run by: {StudentID}` + an ISO timestamp — not fabricated, not
  hand-edited after the fact.
- The demo video must contain the student's own voice narration and show a face-cam or a terminal
  running `whoami`/`hostname`.

## Git Commit Log

- Public GitHub repository, **≥8 commits over ≥4 days**.
- Only commits touching `.spec.js`/`.spec.ts` (or equivalent) count toward the 8-commit minimum.
- Provide the commit log as a text file.

## Submission Regulations

- Filename: `<StudentID>_HW04_AI_Automation_<SelfAssessedGrade>.zip`.
- Required contents: main report (MD+PDF, incl. automation report + gap analysis), public GitHub
  repo link, multi-browser HTML reports, unlisted YouTube demo link, AI Critique + AI Audit Report
  (MD+PDF), git commit log (text), bug report with GitHub Issue screenshots (if any),
  `README.md` with self-assessment table + test summary (number of features; test cases
  automated/executed/passed/failed; browser runs; bugs; demo video link), any other supporting
  materials.

## Assessment Template

| No. | Criteria | Grade |
| --- | --- | ---: |
| 1 | Task 1 - Feature A | 25 |
| 1 | Task 1 - Feature B | 25 |
| 1 | Task 1 - Feature C | 25 |
| 2 | Task 2 - Demo video | 15 |
| 3 | Agent Skills | 10 |
| **Total** | | **100** |
