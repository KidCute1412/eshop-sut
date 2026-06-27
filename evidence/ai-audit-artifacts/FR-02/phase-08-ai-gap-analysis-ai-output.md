# AI Gap Analysis - FR-02 Login and Account Lockout

## Scope and Sources

This Phase 8 analysis compares the preserved initial AI artifacts for Domain Modeling, BVA, and test-case generation with the current human-reviewed reports, execution records, evidence, bug report, and AI Audit. It does not inspect implementation source or change any test result.

## Verified Baseline

| Artifact                                      |    Preserved Initial AI Output |        Current Human-reviewed State | Verified Difference                                                          |
| --------------------------------------------- | -----------------------------: | ----------------------------------: | ---------------------------------------------------------------------------- |
| Normative domain partitions                   |                             28 |                                  30 | Two partitions added by human review, net +2                                 |
| Ambiguous/exploratory partitions              |                              4 |                                   4 | No count change                                                              |
| Lockout/threshold boundary values             |                              4 |                                   4 | No boundary added or removed                                                 |
| DT test cases                                 |                             20 |                                  28 | Eight human-added cases                                                      |
| BVA test cases                                |                              8 |                                   8 | No count change                                                              |
| Total test cases                              |                             28 |                                  36 | Eight added; none removed or reclassified                                    |
| Retained initial cases rewritten or corrected |                             28 |                                  28 | Every retained case received at least one documented design-field correction |
| Execution results                             | Not executed in initial output |        Not applicable in this phase | No runtime data is claimed here                                              |
| Confirmed bug records                         |             0 before execution | 0 in this preserved output snapshot | No bug claims are introduced                                                 |
| Evidence files currently present              |             0 in design output | 0 in this preserved output snapshot | No execution evidence is claimed                                             |
| GitHub Issue links                            |                              0 |                                   0 | No Issue link is claimed as created                                          |

## Gap Register

| Gap ID       | Category                            | Initial AI Output                                                                                                                       | Human Correction or Runtime Finding                                                                                           | Why AI Missed or Mishandled It                                                                  | Corrective Action                                                                                                     | Related requirement, partition, boundary, test case, evidence, or bug |
| ------------ | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| GAP-FR02-001 | Domain-model reasoning correction   | Modeled Email and Password presence but did not separate UI-required markers from input presence.                                       | Human review split the form rule into required-field markers, control type, and masking outputs.                              | The AI collapsed visible form structure with input-data presence.                               | Separate form presentation rules from input domain rules.                                                             | FR02-SF01/FR02-SF02/FR02-SF03; current `domain-testing.md`.           |
| GAP-FR02-002 | Domain-model reasoning correction   | Treated account-lockout behaviour as a single partition without isolating active and expired lockout states.                            | Human review distinguished unlocked, locked, and post-expiry states and kept the 30-second duration as the only BVA boundary. | The AI under-modeled state transition and elapsed-time behaviour.                               | Model lockout as a state machine with time-dependent transitions.                                                     | FR02-R06/FR02-R07/FR02-R08; current `boundary-value-analysis.md`.     |
| GAP-FR02-003 | AI-missed test cases                | Initial DT suite covered valid login and missing fields but lacked public API coverage for lockout-active and lockout-expired outcomes. | Human added dedicated API-facing cases for the lockout state and expiry timing.                                               | The AI stopped after nominal login and input-validation coverage.                               | Project every normative lockout partition onto each applicable surface.                                               | FR02-R06/FR02-R07; added DT cases in `test-cases.md`.                 |
| GAP-FR02-004 | AI-missed test cases                | Initial suite did not include a dedicated case for non-existing account rejection on the public API.                                    | Human added a case to preserve the non-enumeration requirement.                                                               | The AI assumed the existing-account path was sufficient for invalid credentials.                | Add a separate invalid-identity partition whenever the requirement distinguishes existing from non-existing accounts. | FR02-R04/FR02-R09; added DT case in `test-cases.md`.                  |
| GAP-FR02-005 | Human improvement to existing tests | Initial cases used generic login values and unclear dependency wording.                                                                 | Human rewrote retained cases with controlled credentials, clearer preconditions, and explicit lockout setup steps.            | The AI optimized for breadth, not execution-ready specificity.                                  | Use a field-by-field executable-test checklist before approval.                                                       | Current `test-cases.md`; human review section.                        |
| GAP-FR02-006 | Unsupported AI assumption           | The AI treated email normalization and whitespace handling as normative outcomes.                                                       | Human review reclassified these as ambiguous unless the approved basis explicitly defines trimming or case rules.             | The AI inferred behaviour from common login conventions rather than approved black-box sources. | Keep ambiguous inputs in exploratory candidates until a public oracle exists.                                         | Ambiguous candidates in `domain-testing.md`; requirement ambiguities. |

## Classification of Findings

### AI-missed test cases

Four cases were genuinely absent from the initial suite and added by the human. They cover public API projection of lockout states, lockout expiry, and explicit non-existing account rejection.

### Human improvements to existing tests

All retained cases were clarified or rewritten in at least one field. The most significant improvements were in data specificity, preconditions, and surface mapping.

### Runtime bugs exposed by AI-generated tests

No runtime execution is recorded in this preserved phase-8 artifact. Any later bug findings must be classified only after execution evidence exists.

## AI Gap Summary

- Phase 3: human review separated form presentation rules from input presence and refined lockout state modeling.
- Phase 4: no boundary values were added or removed; the main work was keeping lockout timing and threshold traceability precise.
- Phase 5: 8 cases were added, 0 removed, and 0 reclassified; all 28 retained cases received documented corrections.
- Execution: no runtime status is asserted in this preserved AI-output snapshot.
- Bug reporting: no confirmed bugs are claimed here.
- The strongest AI weakness was incomplete projection of a correct concept onto every applicable surface.

## Lessons Learned

1. Hidden state such as lockout counters should be tested only through observable state transitions and public responses.
2. Form presentation rules and input-value rules should not be merged into one partition.
3. Ambiguous behaviour should remain exploratory until the approved basis resolves it.
4. A good domain model needs both valid and invalid partitions for each relevant public surface.
5. The AI should not infer lockout or normalization behaviour from common product expectations without a documented oracle.

## Human Review

- Reviewer: Pending
- Review Date and Time: Pending
- Human Review Status: Pending
- Human Corrections: Pending
