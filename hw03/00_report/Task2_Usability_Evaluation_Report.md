# Task 2 — Usability Evaluation: Results

**Student ID:** 23127296
**Flow tested:** Forgot Password → enter email → receive OTP → enter OTP + new password → submit reset.
(Scope narrowed from the originally planned Register→Cart→Checkout flow to fit 4 recruited participants in the available time — see `../03_usability_evaluation/phase1_plan/02_task_scenario.md`, "Deviation note".)

## Summary of results

4 real, moderated sessions were run (P1 Long, P2 Linh, P3 Tiến, P4 Khải — all recruited from outside the class). All 4 sessions were screen-recorded (`../03_usability_evaluation/videos/`) and completed the full SUS + probe-question protocol.

**Headline finding: 0/4 participants completed the task.** Every participant was blocked at the same step — entering a new password — by the same root cause: `ForgotPassword.jsx` (and `Register.jsx`, sharing the same code) validates the new password against a regex requiring a **whitespace character**, while the on-screen hint tells the user a **special character** is required instead. No password that honestly follows the hint can ever pass. Participants made 2–4 attempts each, tried plausible variations (more punctuation, different punctuation, removing the digit requirement), and none discovered the actual (whitespace) requirement unaided.

**Mean SUS score: 34.4 / 100** — well below the 68-point industry benchmark, consistent with a full-task-failure outcome across all participants. See `../03_usability_evaluation/phase3_analysis/01_sus_scoring.md` for per-participant scores and outlier analysis (P3 lowest at 12.5, most visibly frustrated after 4 attempts; P2 highest at 55.0, disengaged analytically after 2 attempts rather than emotionally).

The OTP field's digit-count label ("4 số") matched the actual 4-digit code shown in every session (verified against `backend/server.js`), so it caused no observed confusion this round — this refutes, for the current build, the original BUG-13 hypothesis of a 4-vs-6-digit mismatch (worth re-checking against whichever commit BUG-13 was originally filed against).

Full findings, severity table, and recommended fixes: `../03_usability_evaluation/phase3_analysis/02_findings_synthesis.md`.

## Deliverables index

| File | Contents |
|---|---|
| `01_objectives.md` | Updated research questions for the Forgot Password scope. |
| `02_task_scenario.md` | Participant-facing script + moderator notes + deviation note explaining the scope narrowing. |
| `03_instruments.md` | SUS + probe questions (probe 4 adapted from "checkout total trust" to "account security trust" for this flow). |
| `04_participants.md` | 4 real participants, contact-masked, with session dates. |
| `phase2_sessions/P1.md`–`P4.md` | Full session notes: timing, friction table, verbatim quotes, SUS raw ratings, probe answers, moderator summary. Recordings in `../videos/`. |
| `phase3_analysis/01_sus_scoring.md` | Per-participant SUS computation, mean, benchmark comparison, outlier analysis. |
| `phase3_analysis/02_findings_synthesis.md` | Clusters (password-hint mismatch, generic error message, OTP label, checkout-total-out-of-scope), severity table, genuine-bug callout. |

## Known gap / follow-up

- Only 4 of the originally planned 7 participants were recruited; no separate pilot was run (P1 doubled as the pilot with no script changes needed).
- The checkout-total-trust hypothesis (BUG-14) was not tested this round since the narrowed flow never reaches Checkout — would need a separate short study if pursued.
- The password-reset regex/hint mismatch found here is a genuine, user-confirmed **Blocker** bug distinct in user-facing impact from the original BUG-12 (Register) framing — recommended for its own GitHub Issue with a screenshot/recording excerpt; not yet filed.
