# Test oracles and analysis playbook

## Select an oracle

Use the strongest available source for each expected result:

1. explicit requirement or acceptance criterion
2. design system, accessibility standard, or platform convention named by the project
3. invariant derived from domain/data rules
4. consistency with the same control or state elsewhere in the SUT
5. recognized usability heuristic, explicitly identified as heuristic judgment

Do not use current implementation behavior as its own oracle. When sources conflict, record the conflict and avoid claiming a definitive failure until the governing source is established.

## Risk-first checklist design

Prioritize checks by `user impact × likelihood × detectability`. Include happy path, alternate path, invalid input, recovery, interruption, repeated action, refresh/back navigation, slow/loading state, empty state, and permission/state transitions when applicable. Use boundary values for numeric, date, length, and quantity controls.

For every core journey, verify state at three layers when observable:

- immediate control feedback
- destination or summary screen
- persisted state after navigation or reload

## Evidence sufficiency

- A screenshot proves only the visible state at capture time.
- A video can prove sequence and timing when the relevant interval is visible.
- Console/network logs can support causality but do not replace user-visible evidence.
- Source code supports hypotheses and root-cause analysis, not runtime status by itself.
- A participant quotation supports perception, not technical causality.

Capture the smallest evidence set that proves the claim while preserving URL/environment identity and privacy.

## Usability coding

Code observations without mind-reading:

- `Hesitation`: visible pause, repeated scan, or verbal uncertainty before progress.
- `Error`: action that moves away from the goal or creates an incorrect state.
- `Recovery`: participant returns to a viable path without moderator guidance.
- `Intervention`: moderator provides information beyond restating the goal.
- `Failure`: success criteria are not met within the defined stop rule.

Aggregate a finding only when the observation has a session/timestamp trail. Rate severity from frequency, task impact, persistence, and recoverability. Keep SUS as a perceived-usability score; do not treat it as defect count or diagnostic proof.

## Cross-platform comparison

Hold test data, task, checkpoints, and expected results constant. Compare layout, interaction, validation, state persistence, rendering, accessibility input paths, and performance symptoms. Separate browser variation from viewport/device variation and from backend instability.

## Review challenges

Before finalizing, actively try to falsify each important claim:

- Could another requirement justify the observed behavior?
- Does the evidence show the stated sequence, environment, and identity?
- Is one root defect being counted multiple times?
- Is a summary based on all source rows or only memorable examples?
- Would another tester reproduce the result using only the written steps?
