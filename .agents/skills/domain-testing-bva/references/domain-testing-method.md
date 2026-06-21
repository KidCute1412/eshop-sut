# Domain Testing Method

## Purpose

Use Domain Testing to model the input and state space of a feature, partition it into equivalent classes, then design representative tests for valid and invalid partitions.

## Procedure

1. Identify feature scope and actor.
2. Extract all inputs, state variables, environmental conditions, and dependent entities.
3. For each variable, collect constraints from requirements, API docs, UI code, backend code, and database schema.
4. Classify each variable into valid and invalid equivalence partitions.
5. Identify cross-variable dependencies and state-dependent rules.
6. Select representative values for each partition.
7. Combine variables using risk-based reasoning; avoid testing every Cartesian product unless interactions require it.
8. Remove duplicates only when they cover the same rule, same partition, and same observable outcome.
9. Record assumptions, contradictions, and gaps.

## Evidence Classes

Use separate notes for:

- Requirement rule.
- API contract.
- Frontend implementation.
- Backend implementation.
- Database enforcement.
- Assumption.
- Contradiction.

## Typical Partitions

Use only when relevant:

- Required value present, missing, empty string, whitespace-only, null.
- Valid and invalid format.
- Valid and invalid length.
- Valid and invalid numeric range.
- Existing and non-existing entity.
- Duplicate and unique entity.
- Authenticated, unauthenticated, wrong role.
- Allowed and disallowed state transition.
- Temporal before, at, after cutoff.
- Collection empty, one item, multiple items.

## Expected Results

Expected results must describe observable behavior: UI message, HTTP status, database state, redirect, token presence, state transition, or unchanged state. Do not write "works correctly" as an expected result.
