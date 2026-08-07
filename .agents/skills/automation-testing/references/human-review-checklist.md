# Human Review Gate

## Before Converting Test Cases to Scripts (Phase 1/2)

- The 3 features match HW02's selection exactly (or a documented, justified self-declaration if
  HW02 is unavailable).
- At least 12 test cases per feature are selected, with a real mix of positive/negative/edge (not
  padded with near-duplicates to hit the number).
- The AI was driven step by step (scaffold, then per test-case group), not with one generic prompt —
  confirm this against the `ai-audit.md` entries for this feature.

## Before Reporting a Script as Data-Driven (Phase 3)

- Every literal test-data value lives in an external `.csv`/`.json` file, not inline in the script.
- `scripts/validate_test_data.py` passes for this feature's directory.
- The script actually loops over the external data (not just imports it once and ignores most of
  it).

## Before Reporting Assertion Coverage (Phase 4)

- At least 3 genuinely distinct assertion patterns are used across the feature's suite (see
  `references/data-driven-and-assertions.md`'s table) — not 3 different matcher names checking
  functionally the same thing.

## Before Reporting the Human Review / Gap Analysis Complete (Phase 5)

- Every AI-generated script has actually been read line by line, not spot-checked.
- Every fragile selector, weak assertion, missing edge case, and flaky wait that was fixed is
  recorded in `ai-gap-analysis.md` with a concrete "why the AI missed it" reason — not a generic
  restatement of the category name.
- The pre-fix AI output is still recoverable from `ai-audit.md` for each fix claimed.

## Before Reporting a Multi-Browser Run Complete (Phase 6)

- All 3 configured browsers actually ran for this feature (check the HTML report's project/browser
  breakdown, not just that the command exited 0).
- The report visibly shows `Run by: {StudentID}` + an ISO timestamp.
- `scripts/validate_html_report.py` passes for the generated report.
- Pass/fail counts recorded in `automation-report.md` match what the report itself shows.

## Before Filing a Bug (Phase 7)

- The failing assertion reflects a genuine SUT defect against a documented expected result
  (`README.md`/`api_specification.md`), not a wrong expectation written into the script itself, and
  not a flaky/non-deterministic failure.
- A real screenshot (from the actual failing run, e.g. Playwright's `screenshot: 'only-on-failure'`
  artifact) is attached, both in the Markdown bug report and on the filed GitHub Issue.

## Before Final Submission

- `scripts/check_commit_rule.py` confirms ≥8 spec-touching commits spanning ≥4 distinct days.
- `scripts/compute_test_summary.py` output matches what's written in `README.md`'s test summary —
  do not hand-type different numbers than what the tooling actually counted.
- The demo video shows real narration in Vietnamese, a real multi-browser run and HTML report, at
  least one narrated real fix, and face-cam or `whoami`/`hostname` authorship evidence.
- No status, result, HTML report content, bug, GitHub Issue link, or commit was fabricated or
  backdated.

Record reviewer, date/time, corrections made, and an `Approved: Yes/No` field in the relevant report
file before moving to the next phase.
