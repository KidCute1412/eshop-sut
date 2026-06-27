# Black-box Domain Testing Method

Domain Testing is a functional black-box technique. Model the feature's input, output, condition, and public state space from approved test bases, partition it into equivalence classes, and select representative tests.

## Procedure

1. Identify the selected feature, actor, surface, and public interface.
2. Extract variables, conditions, dependencies, and observable outcomes from official requirements, API specifications, and observable UI/API behaviour.
3. Give every rule a Rule ID, evidence class, Test Basis Reference, expected behaviour, ambiguity, and assumption.
4. Define valid and invalid partitions for each relevant variable or condition.
5. Explain how each partition follows from its test basis and choose concrete representative values.
6. Model cross-variable and state dependencies instead of treating all inputs independently.
7. Split public control/property existence, value presence, and value relationship partitions when they can produce different observations or blockers.
8. Combine representatives by risk and interaction; avoid an unjustified Cartesian product.
9. Remove cases only when rule, partition, data intent, surface, and observable outcome are materially identical.
10. Trace every test case back to a partition and rule.

Before deriving cases, create or verify a surface matrix for every normative partition: UI, API, or both. Coverage on one public surface does not automatically cover another. Broad invalid domain partitions remain separate from ordered boundary checks; BVA examples may exercise an invalid value, but they do not replace explicit DT coverage for the invalid partition unless the case is intentionally traced to both.

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

For public forms and API contracts, model these separately when applicable: control/property exists or is absent, value is provided or missing, two values match or mismatch, and output/navigation succeeds or is rejected. Do not collapse a missing public control into an empty value partition.

When a value or relationship can only be evaluated if a public control or API property exists first, record that dependency in the partition and representative. Keep rule and partition IDs stable once human-reviewed; if a rule or partition is split or renamed, update downstream domain, BVA, test-case, traceability, bug, and gap-analysis references together.

## Expected Results

Describe public outcomes such as a UI message, rendered state, HTTP status/body, redirect, token presence, or externally visible state transition. Do not use hidden database state, implementation behaviour, or vague phrases such as "works correctly."

## Surface Coverage Check

For every normative partition, decide whether it applies to UI, API, or both. Coverage on one surface does not cover another public surface unless the requirement or contract says so. Record every excluded surface with a reason, such as no public input on that surface, no oracle, ambiguity, or dependency on a separate conformance condition.

Unsupported behaviours stay ambiguous or exploratory unless an approved black-box basis defines them. Common examples are maximum lengths, exact undocumented messages, exact undocumented status bodies, normalization, case sensitivity, Unicode handling, redirect timing, and storage or internal enforcement details.
