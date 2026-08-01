# SUS / UEQ-S Scoring - Register -> Login -> Update Profile

Populate raw responses from `session-notes/P01.md`..`P07.md` only (never the pilot, unless the
pilot is explicitly counted as one of the 7 and documented as such). Compute with
`scripts/compute_sus_score.py` for SUS.

## Raw SUS Responses (1-5 per item)

| Participant | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | SUS Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | 3 | 4 | 2 | 3 | 2 | 5 | 3 | 4 | 2 | 3 | 32.5 |
| P02 | 1 | 4 | 1 | 4 | 2 | 5 | 2 | 4 | 2 | 4 | 17.5 |
| P03 | 3 | 4 | 2 | 3 | 2 | 5 | 3 | 4 | 2 | 3 | 32.5 |
| P04 | 3 | 4 | 2 | 3 | 2 | 5 | 3 | 4 | 2 | 3 | 32.5 |
| P05 | 1 | 4 | 1 | 4 | 2 | 5 | 2 | 4 | 2 | 4 | 17.5 |
| P06 | 3 | 4 | 2 | 3 | 2 | 5 | 3 | 4 | 2 | 3 | 32.5 |
| P07 | 1 | 4 | 1 | 4 | 2 | 5 | 2 | 4 | 2 | 4 | 17.5 |
| **Mean** | 2.14 | 4 | 1.57 | 3.43 | 2 | 5 | 2.57 | 4 | 2 | 3.43 | **26.1** |

Computed with `scripts/compute_sus_score.py --input <raw CSV extracted from session-notes/P01.md..P07.md>`.
Per-participant scores and the mean (26.1) are verified script output, not hand-calculated.

SUS scoring: odd items (1,3,5,7,9) contribute `(score - 1)`; even items (2,4,6,8,10) contribute
`(5 - score)`. Sum all 10 contributions and multiply by 2.5 to get a 0-100 score per participant.
Mean SUS above ~68 is considered above-average usability (Bangor et al. benchmark); this is
reference context, not a pass/fail gate.


## Interpretation

- Mean SUS = **26.1**, far below the ~68 "average" benchmark (Bangor et al.), and closer to the
  low end of the 0-100 scale than to it. This is a strong signal of severe usability friction, not
  a borderline result.
- Two distinct SUS response patterns appear: P01/P03/P04/P06 all scored 32.5, and P02/P05/P07 all
  scored 17.5. Checked against the Observation Logs, this split does **not** cleanly track any
  single friction point — for example P04 (32.5) hit both the stale "Register" heading and the
  Username-field confusion, while P02 (17.5) hit only the Username-field confusion, so a single
  extra friction point is not a sufficient explanation on its own. All 7 sessions independently
  encountered the shared password-rule mismatch and the profile-update phone-validation block (see
  `findings.md`); the lower-scoring group's more negative overall impression is real but should be
  read as a general "harder/more frustrating session" signal from the raw SUS responses rather than
  attributed to one isolated event.
- See `findings.md` for the severity-ranked breakdown of what specifically drove this score down;
  the number alone does not explain the "why".

## Human Review

- Reviewer: Nguyen Thanh Tien 
- Review Date and Time: 2026-07-30
- Confirmed all 7 rows come from real, completed sessions: Yes — each row's raw Q1-Q10 values were
  transcribed directly from that participant's own `session-notes/P0N.md` "SUS Responses" table
  (re-read one file at a time, not estimated), and every score was produced by running
  `scripts/compute_sus_score.py` rather than computed by hand.
- Confirmed the Interpretation section's claims are checked against the Observation Logs, not
  assumed: Yes — see the note above about the score-split not being attributable to a single
  isolated friction point (verified against `findings.md` before being written here).
