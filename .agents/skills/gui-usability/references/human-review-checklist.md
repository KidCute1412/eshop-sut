# Human Review Gate

## Before Checklist Execution (Task 1 / Task 3)

- Screen(s)/flow selection and IA mapping are accurate and not duplicated with a groupmate (see
  `instructor-clarifications.md` item 11).
- Every `Template-Provided` item's generic wording has been adapted to the concrete EShop screen,
  and every AI-generated item (Sections 1.6/2.3 and any other additions) has been read and
  confirmed or corrected by the human; none is left as an unreviewed AI black box or a leftover
  `TODO` placeholder.
- `Item`-row count is strictly greater than 40, and all four IA categories (IA-01..IA-04) are
  represented among `Item` rows.
- Every `Human-Added` item has a specific, non-generic `AI-Miss Reason`.
- Every item is actually checkable by looking at or interacting with the real, running SUT (no
  item requires source-code or database inspection).
- `scripts/validate_checklist.py` passes with no errors.
- `Approved for Test Execution: Yes/No` is recorded.

Do not execute while approval is `No` or missing.

## Before Usability Sessions (Task 2)

- Objectives, task scenario (goal-oriented, not step-by-step), and instrument (SUS/UEQ-S or
  justified custom scale) are finalized.
- Probe questions cover clarity, error recovery, speed, and trust at minimum.
- The 7-participant table is populated with real names and real, appropriately masked contact
  details, and each participant is confirmed to be outside this class.
- A pilot session has actually been run and its lessons applied to the plan.
- Recording/consent process is defined.
- `Approved to Begin Sessions: Yes/No` is recorded in `usability-plan.md`.

Do not run the 7 real sessions while approval is `No` or missing.

## Before Reporting Usability Findings

- Every SUS/UEQ-S score and every quoted observation traces to an actual session-notes file.
- `scripts/validate_usability_session.py` passes for all 7 session files plus the pilot.
- Pain points are grouped, isolated bugs are separated from systemic issues, and severity ranking
  is justified by observed frequency/impact, not guessed.
- No participant, response, or finding was fabricated to reach a target count.

## Before Cross-Platform Reporting

- At least 3 platforms are covered, with Chrome/Firefox/Safari(-or-Android-Chrome) satisfied,
  optionally substituting Expo Go for one.
- Every screenshot shows the SUT state, the browser/OS/device name, the localhost (or documented
  LAN-IP substitute) URL, and the required identity overlay in the same frame.
- `reports/cross-platform/matrix.md` accurately reflects each platform's checklist results.

## General

- No status, result, evidence, screenshot, bug, participant, or GitHub Issue link is fabricated.
- Initial AI output, human corrections, and human-added items/findings remain auditable in their
  preserved form.
- The AI Audit Report has an entry for every distinct AI interaction actually used.

Record reviewer, date/time, corrections made, and the relevant `Approved: Yes/No` field in the
corresponding file before moving to the next phase.
