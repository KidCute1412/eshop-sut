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
- Broad invalid DT partitions are not counted as covered only because a BVA boundary touches a nearby invalid value.
- Every applicable public surface, such as UI and API, is covered or explicitly excluded with a reason.
- Blocked cases include a concrete blocker and are not marked Blocked when the target observation was reachable.
- No status, result, evidence, screenshot, bug, or Issue link is fabricated.
- Initial AI output, human corrections, and human-added cases remain auditable.

Record reviewer, date/time, corrections, missing cases, and `Approved for execution: Yes/No`. Reports remain non-final and execution remains prohibited until approval is Yes.

For AI gap analysis, classify differences precisely:

- AI-missed test case: a needed case was absent from the initial AI output and later added by a human.
- Human improvement: a human clarified, split, reclassified, or rewrote an existing AI case without creating a genuinely new coverage obligation.
- Runtime bug from AI-generated test: execution of an AI-generated case exposed a bug; do not claim the AI missed that bug.
- Runtime bug from human-added test: execution of a human-added case exposed a bug and should be traced to the added coverage.

Verify counts from the current files and preserved AI outputs instead of relying on prompts, memory, or summaries.
