# Black-box Domain Testing Method

Domain Testing is a functional black-box technique. Model the feature's input, output, condition, and public state space from approved test bases, partition it into equivalence classes, and select representative tests.

## Procedure

1. Identify the selected feature, actor, surface, and public interface.
2. Extract variables, conditions, dependencies, and observable outcomes from official requirements, API specifications, and observable UI/API behaviour.
3. Give every rule a Rule ID, evidence class, Test Basis Reference, expected behaviour, ambiguity, and assumption.
4. Define valid and invalid partitions for each relevant variable or condition.
5. Explain how each partition follows from its test basis and choose concrete representative values.
6. Model cross-variable and state dependencies instead of treating all inputs independently.
7. Combine representatives by risk and interaction; avoid an unjustified Cartesian product.
8. Remove cases only when rule, partition, data intent, and observable outcome are materially identical.
9. Trace every test case back to a partition and rule.

## Approved Evidence Classes

- Official requirement
- API specification
- Observable UI behaviour
- Observable API behaviour
- Execution evidence
- Assumption
- Requirement ambiguity
- Observed contradiction

Implementation source, internal tests, and database constraints are not test bases or oracles.

## Typical Partitions

Use only when relevant: present/missing, empty/whitespace/null, valid/invalid format, valid/invalid length or range, existing/non-existing public identity, duplicate/unique, authenticated/unauthenticated/role, allowed/disallowed state, before/at/after time, and empty/one/many collection states.

## Expected Results

Describe public outcomes such as a UI message, rendered state, HTTP status/body, redirect, token presence, or externally visible state transition. Do not use hidden database state, implementation behaviour, or vague phrases such as "works correctly."
