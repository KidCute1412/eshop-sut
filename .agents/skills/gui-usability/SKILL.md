---
name: gui-usability
description: Guides an AI testing agent through auditable GUI-checklist design/execution, moderated usability evaluation with real participants, and cross-browser/cross-platform re-testing for HW03 (GUI & Usability). Use when designing, reviewing, executing, or reporting a GUI checklist, a usability evaluation (SUS/UEQ-S), or cross-platform coverage without fabricating participants, results, or evidence.
---

# GUI Checklist and Usability Evaluation

Use this skill for HW03 — GUI & Usability. It covers three tasks against the EShop SUT: a GUI checklist
(Task 1), a moderated usability evaluation with 7 real participants (Task 2), and cross-browser /
cross-platform re-testing (Task 3), plus the mandatory AI Audit Report, AI Critique, and Git commit log.

## Required References

- Read `references/instructor-clarifications.md` first.
- Read `references/assignment-requirements.md` for HW03 scope, minimums, and submission rules.
- Read `references/eshop-analysis-guide.md` for approved test bases, safe startup, and the
  cross-platform localhost-tunneling note.
- Read `references/gui-checklist-method.md` before designing Task 1 items.
- Read `references/checklist-item-schema.md` before writing or validating checklist rows.
- Read `references/usability-evaluation-method.md` before planning or running Task 2 sessions.
- Read `references/cross-platform-method.md` before Task 3 execution.
- Use `references/human-review-checklist.md` before any execution phase (checklist execution,
  usability sessions, cross-platform runs) is marked approved.
- Use `assets/` and `scripts/` to create workspaces, generate templates, and validate artifacts.

## Integrity Rules

- Never invent a checklist Yes/No result, a Remarks reason, a screenshot, a bug, a GitHub Issue
  link, a participant, a participant's contact detail, a SUS/UEQ-S response, a session observation,
  or a quote. If it was not actually observed or actually collected, it does not go in a report.
- The AI may draft checklist items, scenarios, probe questions, and synthesis groupings. The human
  must review every AI output, correct it, and is responsible for its correctness. Submitting raw
  AI output without review is not acceptable per the assignment's Human Review principle.
- Task 2 participants must be real people outside this class, with verifiable contact details
  (middle four digits of phone/Zalo masked). Do not generate, simulate, or "represent" a participant
  with AI. A TA may call two participants to verify; impersonation scores 0 for Task 2.
- Treat implementation source code, database schema, and internal tests as off-limits oracles for
  expected UI behaviour. The oracle is `README.md` (FR-21..FR-24 and general FRs), `api_specification.md`,
  observable UI behaviour, general usability heuristics (Nielsen's 10 heuristics, WCAG basics), and
  real execution evidence.
- Preserve the initial AI-generated checklist/scenario/questions before human edits so the gap
  analysis stays auditable. Record every human-added checklist item's "why the AI missed it" reason.
- Encourage one Git commit per demonstrated step (see `references/assignment-requirements.md` §Git
  Commit Log). This is normally individual work; do not assume or copy another student's screen,
  flow, or prompts — copying (including prompts) is a zero for both parties.
- Every screenshot used as evidence (Task 1 failures, Task 3 platform runs, Task 2 bug evidence)
  must be real, must show the actual failure/state, and Task 3 screenshots must overlay the
  required identity text (see `references/cross-platform-method.md`).

## Phase 0: Scope Selection

Ask the human to state, and record verbatim:

- The screen(s) selected for the Task 1 / Task 3 checklist (e.g. Home, Cart, Checkout, Admin
  Dashboard, a Mobile screen), each assigned a `GUI ID` (e.g. `01`, `02`) matching the professor's
  `Web GUI checklist Template.xlsx` "GUI list" sheet convention. Minimum one screen; recommend
  several since one screen rarely yields 40 non-repetitive items (see §5 of the HW03 PDF) — though
  the base template alone (~100 items, see Phase 1) already exceeds 40, so the real coverage goal
  is genuine EShop-specific depth, not just hitting the count.
- The single end-to-end flow selected for Task 2 (e.g. Sign-up → Add to cart → Checkout with a
  coupon).
- Confirmation that this screen selection and this flow are not duplicated with any groupmate, if
  the course cohort enforces that rule (the official PDF states this under "Within each group",
  even though the assignment `Form` is listed as Individual — flag this to the human as an
  instructor-clarification point rather than silently resolving it).

Never pick the screen or flow automatically. Initialize workspaces only after the human confirms
scope with `scripts/create_checklist_workspace.py --gui-id <ID> --gui-name <name>` (one call per
screen) and `scripts/create_usability_workspace.py`.

## Phase 1: Task 1 — Start From the Template, Then AI-Assisted Generation

1. `scripts/create_checklist_workspace.py` seeds each screen's `checklist.md` from
   `assets/checklist-template.md`, which is a verbatim transcription of the professor's
   `Web GUI checklist Template.xlsx` taxonomy (`Source: Template-Provided`; Section 1 General UI,
   Section 1.5 Forms, Section 2.1 Navigation, Section 2.2 general usability, Section 3
   Compatibility — see `references/checklist-item-schema.md` for the full IA mapping). Adapt the
   generic Vietnamese wording to the concrete screen (e.g. point "Phần tìm kiếm được hiển thị nổi
   bật" at the actual EShop search bar).
2. The template reserves two placeholder subsections the base xlsx does not cover:
   `1.6 KHẢ NĂNG TIẾP CẬN...` (accessibility/dark-mode/RTL) and `2.3 PHẢN HỒI / TRẠNG THÁI`
   (IA-04 Feedback/State). Collect black-box test bases per `references/eshop-analysis-guide.md`
   (`README.md` FR-21..FR-24) for these, then prompt the AI — one prompt per gap subsection, not
   one generic prompt — to replace every `TODO -- generate via AI` `Checkpoint` with a real item,
   with `Source: AI-Generated`.
3. Preserve this initial AI prompt and output verbatim (e.g.
   `reports/gui-checklist/GUI-<ID>/ai-initial-output.md`) before any edit — this is the baseline
   for the mandatory AI-gap analysis.
4. Also prompt the AI to propose additional EShop-specific `AI-Generated` items anywhere in
   Sections 1-2 the generic template wording doesn't quite capture.

## Phase 2: Human Critique and Gap-Filling

The human critically reviews the AI's checklist and adds missed items. For every added item:

- Set `Source: Human-Added`.
- Fill `AI-Miss Reason` with a concrete explanation: prompt quality (what the prompt omitted),
  model limitation (what class of issue the model tends to skip, e.g. accessibility, RTL layout,
  dark mode, keyboard-only operation, screen-reader semantics, locale/number formatting), or a
  characteristic of the chosen interface the AI could not see (only observable by actually using
  the screen, e.g. a specific truncation, a specific inconsistent color, a specific missing focus
  ring).
- Do not simply relabel an AI item as human-added to inflate the "found more than AI" count —
  `AI-Miss Reason` must describe a genuine, specific gap.

Run `scripts/validate_checklist.py <checklist-file>` to confirm: `Item`-row count > 40, all four IA
categories represented, no leftover `TODO` placeholders, every `Human-Added` item has a
non-placeholder `AI-Miss Reason`, and `No.` values are unique. Fix reported problems before
execution.

## Phase 3: Human Review Gate (Checklist)

Before execution, the human confirms via `references/human-review-checklist.md`:

- Screen/flow selection and requirement mapping are accurate.
- No AI-generated item is left unreviewed; every item is either confirmed or corrected.
- Every checklist item is actually executable by looking at or interacting with the real SUT.
- `Approved for Test Execution: Yes/No` is recorded in the checklist file.

Do not execute while approval is `No` or missing.

## Phase 4: Checklist Execution (Task 1 baseline platform)

Execute every `Item`-type row against the running SUT on the primary/baseline platform (`Section`
rows are category headings and are never marked themselves):

- Mark exactly one of `Yes`/`No` with `X` (never fabricate; leave both blank — `Not Executed` —
  only transiently).
- For every item marked `No`, fill `Remarks` with the concrete failure reason and attach a real
  screenshot under `reports/gui-checklist/GUI-<ID>/evidence/<No.>.png`. Do not attach screenshots
  for items marked `Yes` — the assignment only requires evidence for failures.
- Run `scripts/validate_checklist.py` again after execution; it enforces that every item marked
  `No` has non-empty `Remarks` and an existing evidence file, and that `Yes`/unexecuted items do not
  claim evidence they do not have.

## Phase 5: Bug Reporting (Task 1)

For every item marked `No` that represents a genuine, reproducible bug (not a documentation
ambiguity), create an entry in `reports/gui-checklist/bug-report.md` using
`assets/bug-report-template.md`, then file the same bug on GitHub Issues with the screenshot
attached. Replace `Pending` with the real Issue URL only after the Issue exists — never fabricate a
URL.

## Phase 6: Task 2 — Usability Evaluation Planning

Follow `references/usability-evaluation-method.md`. Populate `assets/usability-plan-template.md`
with:

- Objectives (what you want to learn from the chosen flow).
- The task scenario: goal-oriented, not step-by-step (e.g. "Find a winter coat under 500,000 ₫ and
  check out using a discount coupon").
- Chosen instrument: SUS or UEQ-S (or a justified custom scale) plus probe questions covering at
  minimum clarity, error recovery, speed, and trust.
- The human recruits and records 7 real participants outside the class in
  `assets/participant-table-template.md` (masked contact info) — the AI must not generate or
  stand in for this list.
- Plan and run one pilot session first; record what was refined before the real 7 sessions in the
  plan file.

## Phase 7: Usability Session Execution

For each of the 7 sessions (plus the pilot), the human runs the session; the AI may help prepare
the script, take structured notes dictated by the human, or organize evidence — the AI does not
observe the participant itself. Use `assets/session-notes-template.md` per participant:

- Set the stage (testing the product, not the participant) and enable think-aloud.
- Record friction points, errors, hesitations, and verbalized frustration as they are actually
  reported by the human running the session.
- Record the completed SUS/UEQ-S responses and the probe-question answers verbatim.

Run `scripts/validate_usability_session.py reports/usability-evaluation/` after each session to
catch missing required fields before moving to the next participant.

## Phase 8: Usability Analysis and Reporting

1. Score SUS/UEQ-S with `scripts/compute_sus_score.py` (SUS) or manually per the UEQ-S scoring
   guide in `references/usability-evaluation-method.md`, across all 7 participants.
2. Synthesize notes in `assets/findings-severity-template.md`: group similar pain points, separate
   isolated bugs from systemic design issues, and rank by severity (Blocker / Major / Minor /
   Cosmetic).
3. File genuine bugs found during sessions the same way as Phase 5 (Markdown + GitHub Issue +
   screenshot).

## Phase 9: Task 3 — Cross-Browser / Cross-Platform Execution

Follow `references/cross-platform-method.md`. For each of at least 3 platforms (e.g. Chrome,
Firefox, Safari-or-Android-Chrome, optionally replacing one with Expo Go on a real phone):

1. Copy the human-reviewed, approved checklist from Task 1 into a per-platform, per-screen file
   with `scripts/create_checklist_workspace.py --gui-id <ID> --gui-name <name> --platform <name>
   --seed-from reports/gui-checklist/GUI-<ID>/checklist.md` (same items, fresh `Yes`/`No`/
   `Remarks`/`Evidence`/`Bug ID`).
2. Re-execute the checklist on that platform (BrowserStack/LambdaTest preferred; real device or
   another cloud tool as fallback). If the SUT runs on localhost, use BrowserStack Local /
   LambdaTest Tunnel (or an equivalent) so the cloud browser can reach it — see the reference for
   the exact setup. Section 3 (`Compatibility`) rows are the ones this task is specifically about;
   give them extra attention on each platform.
3. Every screenshot must overlay the identity text required by the assignment (student email, and
   for the cross-platform set specifically, also student ID + full name — see
   `references/cross-platform-method.md`), plus be visibly labeled with the browser/OS/device name
   and the localhost URL.
4. Record results in `reports/cross-platform/<platform>/GUI-<ID>/checklist.md` and summarize all
   platforms in `reports/cross-platform/matrix.md` using `assets/cross-platform-matrix-template.md`.

## Phase 10: AI Audit Report and AI Critique

- After every distinct AI interaction across Tasks 1–3 (checklist generation, scenario drafting,
  probe-question drafting, note synthesis assistance, etc.), append an entry with
  `scripts/append_ai_audit.py` — never overwrite prior entries, always record the verbatim prompt,
  the AI output reference, and the human review/corrections.
- Write the mandatory 200–300 word AI Critique using `assets/ai-critique-template.md`: cite a
  concrete instance where the AI was wrong, biased, or incomplete (the checklist gaps from Phase 2
  are good source material), explain why it failed to catch the issue, and state the collaboration
  principle learned.

## Phase 11: Git Commit Log and Final Assembly

- Commit each demonstrated step separately (checklist design, checklist execution, bug logging,
  each usability session, the analysis, each cross-platform run) rather than one giant commit.
- Export the commit log to a text file, e.g. `git log --stat > git-commit-log.txt`, per
  `references/assignment-requirements.md`.
- Assemble the main report with `assets/main-report-template.md`, and the submission `README.md`
  self-assessment/summary with `assets/readme-self-assessment-template.md`.

## Workspace Layout

```text
reports/
|-- gui-checklist/
|   |-- gui-list.md                     (assets/gui-list-template.md, one row per screen)
|   |-- bug-report.md                   (shared across all screens)
|   |-- ai-gap-analysis.md              (shared across all screens)
|   `-- GUI-<ID>/
|       |-- ai-initial-output.md        (preserved, pre-human-review AI output for 1.6/2.3)
|       |-- checklist.md                (assets/checklist-template.md, executed)
|       `-- evidence/<No.>.png          (items marked No only)
|-- usability-evaluation/
|   |-- usability-plan.md
|   |-- participants.md
|   |-- session-notes/
|   |   |-- PILOT.md
|   |   `-- P01.md .. P07.md
|   |-- sus-scoring.md
|   |-- findings.md
|   |-- bug-report.md
|   `-- evidence/
`-- cross-platform/
    |-- matrix.md
    |-- <platform-1>/GUI-<ID>/checklist.md + evidence/
    |-- <platform-2>/GUI-<ID>/checklist.md + evidence/
    `-- <platform-3>/GUI-<ID>/checklist.md + evidence/
ai-audit.md
ai-critique.md
git-commit-log.txt
README.md
```

Demonstrate end-to-end use on one complete screen (Task 1/3) and one complete flow (Task 2). A
demonstration video may use voice-over or captions. Comprehensive, non-repetitive coverage and real
confirmed findings improve the assessment; volume never permits fabrication.
