# Test Case Schema

Write test cases in Markdown using one heading per case.

## Required Fields

- Test Case ID
- Technique
- Objective
- Requirement or Rule Reference
- Preconditions
- Test Data
- Steps
- Expected Result
- Actual Result
- Status
- Evidence
- Partition or Boundary Covered
- Source Code Reference
- Notes and Assumptions

## ID Format

Use `FRNN-DT-###` or `FRNN-BVA-###`, where `NN` is two digits and `###` is a three-digit sequence.

Examples:

- `FR01-DT-001`
- `FR17-BVA-004`

## Execution Integrity

For unexecuted tests, use exactly:

- `Actual Result: Not Executed`
- `Status: Not Executed`
- `Evidence: None`

Use Pass or Fail only when the test has been executed and evidence is recorded.

## Traceability

Every test case must trace to at least one requirement or rule and at least one source reference. Domain tests must name the covered partition. BVA tests must name the covered boundary.
