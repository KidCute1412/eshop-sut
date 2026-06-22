# Black-box Test Case Schema

Use one level-two heading per case and these fields: Test Case ID, Technique, Objective, Requirement or Rule Reference, Preconditions, Test Data, Steps, Expected Result, Actual Result, Status, Evidence, Partition or Boundary Covered, Test Basis Reference, and Notes and Assumptions.

Use `FRNN-DT-###`, `FRNN-BVA-###`, `DNN-DT-###`, or `DNN-BVA-###`. The prefix must match the workspace feature, such as `FR-01` -> `FR01-DT-001` and `D-01` -> `D01-BVA-001`.

## Derivation and Traceability

After each case, explain the derivation: originating rule, partition or Boundary ID, why the data is representative, and how the expected result follows from an approved black-box test basis. DT cases name a partition ID; BVA cases name a Boundary ID. `Test Basis Reference` points to a requirement, specification section, or recorded observable behaviour—not implementation source.

## Execution Integrity

Allowed statuses are `Not Executed`, `Pass`, `Fail`, and `Blocked`. Before execution use exactly `Actual Result: Not Executed`, `Status: Not Executed`, and `Evidence: None`. Pass and Fail require real evidence. Blocked requires a reason. Not Executed must not cite execution evidence.
