# Task 2 — Usability Evaluation: Plan (Execution Pending Real Sessions)

**Student ID:** 23127296
**Flow selected (§5):** Register → browse/search a product → add to cart → checkout with a discount coupon.

## Status of this deliverable

Task 2 requires 7 real, moderated sessions with human participants recruited from outside the class, verifiable by the TA calling two of them, plus genuine screen recordings/notes. **These cannot be produced inside this Claude Code session** — there is no way to recruit or interview real people from here, and fabricating any part of this (participant identities, quotes, SUS scores) would violate §11's anti-cheat rule and zero out this task. What follows is therefore the complete **Phase 1 plan** (fully usable as-is) plus **ready-to-fill Phase 2/3 templates** — the student must run the actual sessions.

## Phase 1 — Plan & prepare (complete, see `03_usability_evaluation/phase1_plan/`)

| File | Contents |
|---|---|
| `01_objectives.md` | 5 concrete research questions, each tied to a specific Task-1 code finding (BUG-12, BUG-14, coupon flow) so the study isn't a generic "is it usable" fishing expedition. |
| `02_task_scenario.md` | Participant-facing goal-oriented script + moderator-only notes (what not to reveal, timing/nudge rules). |
| `03_instruments.md` | SUS chosen (with justification over UEQ-S) + scoring formula + the 4 required probe question categories (clarity, error recovery, speed, trust). |
| `04_participants.md` | Empty 7+1(pilot) participant table with eligibility rules, contact-masking format, and a recruitment script — to be filled with real people only. |

## Phase 2 — Conduct sessions (template ready, not yet executed)

`03_usability_evaluation/phase2_sessions/SESSION_TEMPLATE.md` — one copy per participant (P0 pilot + P1..P7), capturing timing, a structured friction-observation table, verbatim think-aloud quotes, the 10 SUS items, and the 4+ probe answers.

## Phase 3 — Analyse & report (template ready, not yet executed)

- `03_usability_evaluation/phase3_analysis/01_sus_scoring.md` — per-participant SUS computation + mean vs. the 68-point industry benchmark.
- `03_usability_evaluation/phase3_analysis/02_findings_synthesis.md` — pre-seeded with 3 hypothesis clusters derived from Task 1's code review (checkout-total trust, coupon discoverability, password-policy comprehension) to confirm/refute with real data, plus space for anything unhypothesized that comes up, and a severity-ranked findings table (Blocker/Major/Minor).

## What the student must still do

1. Recruit 7 eligible participants + 1 pilot (real people, outside the class); fill `04_participants.md` with masked contact info.
2. Run the pilot, adjust the scenario/timing if needed, log the outcome in `04_participants.md`.
3. Run all 7 real sessions using `SESSION_TEMPLATE.md`, recording screen (+audio with consent) where possible.
4. Score SUS in `01_sus_scoring.md`, synthesize findings in `02_findings_synthesis.md`, prioritize by severity.
5. File any genuine bugs discovered during sessions as GitHub Issues with screenshots (same process as Task 1, see `../02_bug_reports/HOWTO_create_github_issues.md`).
6. Replace this report's "Status" section with an actual results summary once data exists.
