# Black-box Test Case Schema

Use one level-two heading per case and these fields: Test Case ID, Technique, Objective, Requirement or Rule Reference, Preconditions, Test Data, Steps, Expected Result, Actual Result, Status, Evidence, Partition or Boundary Covered, Test Basis Reference, and Notes and Assumptions.

Use `FRNN-DT-###`, `FRNN-BVA-###`, `DNN-DT-###`, or `DNN-BVA-###`. The prefix must match the workspace feature, such as `FR-01` -> `FR01-DT-001` and `D-01` -> `D01-BVA-001`.

## Derivation and Traceability

After each case, explain the derivation: originating rule, partition or Boundary ID, why the data is representative, and how the expected result follows from an approved black-box test basis. DT cases name a partition ID; BVA cases name a Boundary ID. `Test Basis Reference` points to a requirement, specification section, or recorded observable behaviour, not implementation source. Do not include `Source Code Reference` in black-box test cases.

Before human review, include a coverage summary that maps each normative partition and boundary to the test cases that cover it. The summary must show the applicable surface (`UI`, `API`, or both), the coverage status, and the reason for any omission.

Do not rely on BVA cases as the only evidence that a broad invalid equivalence class is covered when a non-boundary representative is meaningful. Keep DT partition coverage and BVA boundary coverage traceable as separate design decisions.

For invalid cases, choose concrete data that isolates the target invalid condition while unrelated fields remain nominally valid. If isolation depends on a public control, property, or state that might be absent, record the dependency explicitly.

## Execution Integrity

Allowed statuses are `Not Executed`, `Pass`, `Fail`, and `Blocked`. Before execution use exactly `Actual Result: Not Executed`, `Status: Not Executed`, and `Evidence: None`. Pass and Fail require a concrete observed `Actual Result` and real evidence. Blocked requires a `Blocking Reason` field plus evidence showing the blocker. Do not use Blocked when the target behaviour was actually observable. Not Executed must not cite execution evidence.

Before handoff and after execution updates, run the provided validation script when available. Fix missing partition or boundary references, missing evidence, invalid statuses, duplicate IDs, and missing `Blocking Reason` fields before reporting completion.
