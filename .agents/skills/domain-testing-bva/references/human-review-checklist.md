# Human Review Gate

Before execution, a human must verify and explicitly confirm:

- Feature, pool, actor, surface, requirements, and API/UI location are accurate.
- Only approved black-box test bases were used and every rule has a Test Basis Reference.
- Requirement ambiguities, assumptions, and observed contradictions are explicit.
- Valid/invalid partitions are complete and their derivations explained.
- Public control/property existence, value presence, and cross-field relationships are separated when they are different domains.
- Every normative partition and selected boundary is checked against every applicable public surface, such as UI and API.
- BVA is limited to ordered/bounded domains; boundaries and adjacent values are correct.
- BVA coverage does not accidentally replace required non-boundary DT partition coverage.
- Dependencies, concrete test data, and observable expected results are complete.
- Technique labels, IDs, partition/boundary references, and traceability are correct.
- Probable duplicates are removed or justified and missing cases are added.
- Cases that may block many other cases are identifiable as conformance or dependency cases.
- No status, result, evidence, screenshot, bug, or Issue link is fabricated.
- Initial AI output, human corrections, and human-added cases remain auditable.

Record reviewer, date/time, corrections, missing cases, and `Approved for execution: Yes/No`. Reports remain non-final and execution remains prohibited until approval is Yes.
