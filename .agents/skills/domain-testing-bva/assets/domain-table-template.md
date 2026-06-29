# Domain Testing - {{FEATURE_ID}} {{FEATURE_NAME}}

## Step 1. Identify Input & Output Variables

| Type | Variable or Output | Description | Related Rule IDs | Applies To |
| --- | --- | --- | --- | --- |
| Input | TODO | TODO | TODO | UI/API/TODO |

## Step 2. Identify Equivalence Classes

### Normative Partitions

Only approved rules produce Valid/Invalid classes. Keep UI control existence, value presence, cross-field relationships, output contracts, actor state, and public state as separate partitions when they have different observability or dependencies.

| Partition ID | Type | Variable or Condition | Equivalence Class Description | Validity | Representative Value | Dependencies | Rule IDs | Test Basis Reference | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PARTITION-TODO-V01 | TODO | TODO | TODO | Valid | TODO | TODO | TODO | TODO | TODO |
| PARTITION-TODO-I01 | TODO | TODO | TODO | Invalid | TODO | TODO | TODO | TODO | TODO |

### Ambiguous or Exploratory Partitions

Record unsupported behaviours here. Do not turn them into expected Pass/Fail oracles.

| Candidate ID | Type | Variable or Condition | Candidate Class | Why It Is Ambiguous or Exploratory | Representative Value | Dependencies | Test Basis Reference |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Step 3. Representative Value Summary

| Partition ID | Representative Value | Why This Representative Was Chosen | Required Nominal Values for Other Variables | Applies To |
| --- | --- | --- | --- | --- |

## Partition Derivation

For every Partition ID, explain the source rule, classification, representative rationale, nominal dependencies, and public surface. Separate broad invalid equivalence partitions from BVA boundary values.

## Coverage Decisions

List covered partitions and justify every intentionally omitted partition, surface, or dependency. State which exploratory candidates are excluded from normative coverage and why.

## Human Review

- Reviewer: TODO
- Review Date and Time: TODO
- Review Scope: Domain Modeling for {{FEATURE_ID}} {{FEATURE_NAME}}
- Corrections Made: TODO
- Missing Partitions Added: TODO
- Duplicate or Incorrect Partitions Removed: TODO
- Status: Pending
