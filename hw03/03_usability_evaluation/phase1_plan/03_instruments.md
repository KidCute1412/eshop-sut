# Phase 1 — Instruments

## Standard scale: System Usability Scale (SUS)

**Choice justification:** SUS was chosen over UEQ-S because the study's primary objective is task-completion confidence and friction on a single transactional flow (register→cart→checkout), which is exactly what SUS's 10 items target (ease of use, need for support, consistency, learnability). UEQ-S is stronger for capturing *hedonic/pragmatic emotional quality* across a whole product, which is a secondary concern here. If time allows, UEQ-S may be added as a bonus instrument (both are short, ~2 minutes each), but SUS alone satisfies the requirement.

Administer immediately after the session ends (after the participant reaches success or gives up), before the probe questions. Use the standard 10 SUS items, 5-point Likert (1 = Strongly Disagree, 5 = Strongly Agree):

1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need the support of a technical person to be able to use this system.
5. I found the various functions in this system were well integrated.
6. I thought there was too much inconsistency in this system.
7. I would imagine that most people would learn to use this system very quickly.
8. I found the system very cumbersome/awkward to use.
9. I felt very confident using the system.
10. I needed to learn a lot of things before I could get going with this system.

**Scoring:** For odd items (1,3,5,7,9): score = rating − 1. For even items (2,4,6,8,10): score = 5 − rating. Sum all 10 scores × 2.5 → SUS score out of 100. Record raw ratings + computed score per participant in `03_phase3_analysis/01_sus_scoring_template.md`.

## Open-ended probe questions (asked after the SUS, minimum required set)

1. **Clarity** — "At any point, was it unclear what you were supposed to do or where to click next? Where?"
2. **Error recovery** — "Did anything go wrong or not work as you expected? How did you try to fix it, and did that work?"
3. **Speed** — "Did the process feel fast or slow? Was there any point where you felt like you were waiting or repeating steps?"
4. **Trust** — "How confident are you that the final amount you were charged was correct? Why?" (directly probes the editable-total finding, BUG-14, without leading the participant toward it)

Add any follow-up probes driven by what you personally observed during that specific session (e.g., if they hesitated on the coupon field, ask about it directly).

## Recording & consent

- Ask verbal or written consent to record screen (+ audio if available) before starting. If declined, rely on structured live notes only (see `03_usability_evaluation/phase2_sessions/SESSION_TEMPLATE.md`).
- Store recordings under `03_usability_evaluation/phase2_sessions/recordings/P0X.mp4` (not committed to git if large — reference by filename/local path instead, per participant privacy).
