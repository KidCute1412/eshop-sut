# SUS / UEQ-S Scoring - {{FLOW_NAME}}

Populate raw responses from `session-notes/P01.md`..`P07.md` only (never the pilot, unless the
pilot is explicitly counted as one of the 7 and documented as such). Compute with
`scripts/compute_sus_score.py` for SUS.

## Raw SUS Responses (1-5 per item)

| Participant | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | SUS Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | | | | | | | | | | | |
| P02 | | | | | | | | | | | |
| P03 | | | | | | | | | | | |
| P04 | | | | | | | | | | | |
| P05 | | | | | | | | | | | |
| P06 | | | | | | | | | | | |
| P07 | | | | | | | | | | | |
| **Mean** | | | | | | | | | | | |

SUS scoring: odd items (1,3,5,7,9) contribute `(score - 1)`; even items (2,4,6,8,10) contribute
`(5 - score)`. Sum all 10 contributions and multiply by 2.5 to get a 0-100 score per participant.
Mean SUS above ~68 is considered above-average usability (Bangor et al. benchmark); this is
reference context, not a pass/fail gate.

## Raw UEQ-S Responses (-3..+3 per item), if used instead

| Participant | I1 | I2 | I3 | I4 | I5 | I6 | I7 | I8 | Pragmatic Mean (I1-4) | Hedonic Mean (I5-8) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | | | | | | | | | | |
| P02 | | | | | | | | | | |
| P03 | | | | | | | | | | |
| P04 | | | | | | | | | | |
| P05 | | | | | | | | | | |
| P06 | | | | | | | | | | |
| P07 | | | | | | | | | | |
| **Mean** | | | | | | | | | | |

## Interpretation

- TODO: summarize what the score range means for this flow, referencing the actual pain points
  from `findings.md` rather than the number alone.

## Human Review

- Reviewer: TODO
- Review Date and Time: TODO
- Confirmed all 7 rows come from real, completed sessions: Yes/No
