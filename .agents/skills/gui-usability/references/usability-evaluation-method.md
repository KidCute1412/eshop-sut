# Usability Evaluation Method (Task 2)

Moderated, small-sample (n=7) usability evaluation of one end-to-end flow. The AI assists with
drafting instruments and organizing notes; the human recruits, runs, observes, and records.

## Phase 1: Plan & Prepare

- **Objectives**: 2–4 concrete questions, e.g. "Where do users hesitate during coupon entry?", "Do
  users trust the payment confirmation screen?", "Can users recover from an invalid coupon code
  without help?".
- **Task scenario**: goal-oriented, never step-by-step. Good: "Find a winter coat under 500,000 ₫
  and check out using a discount coupon." Bad: "Click Home, then click the third product, then
  click Add to Cart..." — the latter removes the very navigation/discoverability signal the
  evaluation exists to measure.
- **Instrument**: choose one.
  - **SUS (System Usability Scale)**: 10 items, 5-point Likert (Strongly Disagree=1 .. Strongly
    Agree=5), odd items positively worded, even items negatively worded. See
    `scripts/compute_sus_score.py` for scoring.
  - **UEQ-S (User Experience Questionnaire — Short)**: 8 bipolar item pairs (e.g.
    obstructive/supportive), 7-point scale from -3 to +3, split into Pragmatic Quality (items
    1,2,3,4) and Hedonic Quality (items 5,6,7,8) subscales. Average each subscale separately.
  - **Custom scale**: only with a written justification (why SUS/UEQ-S do not fit this flow) in
    `usability-plan.md`.
- **Probe questions**: at minimum one open-ended question each on clarity, error recovery, speed,
  and trust, e.g.:
  - Clarity: "Was it ever unclear what to do next? Where?"
  - Error recovery: "If something went wrong, how did you figure out what happened?"
  - Speed: "Did any step feel slower or more tedious than expected?"
  - Trust: "At checkout, did you feel confident the order/payment would go through correctly?"
- **Recruitment**: 7 real participants outside this class, target-user-profile-matched, with
  verifiable contact (Zalo/email/phone, middle 4 digits masked, e.g. `090****678`). Non-IT/non-
  tester participants preferred. Record in `assets/participant-table-template.md`. This step is
  never AI-assisted in substance — the AI must not generate names, contacts, or "represent" a
  participant.
- **Pilot**: run one full session with one person first specifically to catch an unclear scenario,
  a broken flow step, or bad timing assumptions; record what changed before the real 7 in
  `usability-plan.md`.

## Phase 2: Conduct (per participant)

1. **Set the stage**: tell the participant you are testing the *product*, not them; ask them to
   think aloud.
2. **Observe neutrally**: no leading hints, no explaining the interface; intervene only if the
   participant is completely stuck (record the intervention as a friction point, not a success).
3. **Capture evidence**: screen recording (audio with consent) plus structured notes — timestamped
   friction points, errors, hesitations, verbalized frustration/confusion, and any workaround the
   participant invents.
4. **Close**: administer the SUS/UEQ-S scale, then ask the probe questions to dig into whatever was
   actually observed as difficult.

Use `assets/session-notes-template.md` per participant (`P01`..`P07`, plus `PILOT`).

## Phase 3: Analyse & Report

1. **Score**: compute SUS (0–100 per participant, then mean) or UEQ-S (per-subscale mean, -3..+3)
   across all 7 real sessions. Never average in a placeholder or an assumed score for a session
   that did not happen.
2. **Synthesize**: cluster session notes into named pain points. For each pain point, note how many
   of the 7 participants hit it, and classify it as:
   - **Isolated bug**: a concrete, reproducible defect (broken button, wrong label, crash).
   - **Systemic design issue**: a pattern that is not a "bug" per se but a design choice that
     confuses users (e.g. no visible way back from checkout, ambiguous coupon-field placement).
3. **Prioritize by severity**:
   - **Blocker**: prevents task completion for most/all participants.
   - **Major**: causes significant friction/hesitation or requires an intervention, but the task is
     eventually completed.
   - **Minor**: noticed and mildly annoying, does not block completion.
   - **Cosmetic**: purely visual/wording, no functional impact.
4. **Report bugs**: any isolated bug found during a session follows the same bug-reporting
   discipline as Task 1 (Markdown + GitHub Issue + screenshot). Systemic design issues go into
   `findings.md` as UX recommendations, not as bugs, unless they violate a documented requirement.

## Integrity Notes

- A TA may call 2 of the 7 participants to verify. Keep contact info genuine and reachable.
- SUS/UEQ-S responses, quotes, and observed friction points must come from the actual session; the
  AI may help you tabulate or phrase the write-up of a note you already collected, but it must not
  originate the observation itself.
