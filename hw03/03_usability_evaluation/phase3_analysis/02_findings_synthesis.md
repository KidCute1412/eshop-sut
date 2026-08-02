# Phase 3 — Findings Synthesis

Instructions: after all 7 sessions, pull every row from each `phase2_sessions/P*.md` observation table into this file, then group similar pain points together. Separate **isolated bugs** (a one-off technical defect, e.g. a typo or console error only one participant's specific input triggered) from **systemic design issues** (a pattern most/all participants struggled with, e.g. "nobody found the coupon field unprompted").

## Candidate clusters to watch for (seeded from Task 1's code-level findings — confirm or refute with real observation data)

### Cluster A: Checkout total trust
- **Hypothesis (from BUG-14):** participants may not notice, or may be confused by, the editable total field at checkout.
- Participants who showed this: 
- Isolated or systemic: 
- Supporting quotes: 

### Cluster B: Coupon discoverability
- **Hypothesis:** the coupon field is positioned as an optional secondary block; participants who don't scroll or aren't told a discount exists may complete checkout without ever finding it.
- Participants who showed this: 
- Isolated or systemic: 
- Supporting quotes: 

### Cluster C: Password policy comprehension (Register)
- **Hypothesis (from BUG-12):** the hint text and the actual accepted characters diverge; participants may retry several times or give up interpreting the error message.
- Participants who showed this: 
- Isolated or systemic: 
- Supporting quotes: 

### Cluster D: (add your own — anything observed that wasn't hypothesized above)

## Severity prioritization

| Finding | Cluster | # participants affected | Severity (Blocker/Major/Minor) | Recommended fix |
|---|---|---|---|---|
| | | /7 | | |

Blockers = prevented task completion entirely. Major = completed only with a nudge/extra time. Minor = cosmetic/verbal complaint only, no behavioral impact.

## Genuine bugs discovered during sessions (report these in `../../02_bug_reports/Bug_Report.md` too, with a GitHub Issue + screenshot each)

- 
