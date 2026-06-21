# Human Review Checklist

Before submission, a human reviewer must verify:

- Feature ID, name, pool, role, and module are correct.
- Assignment allocation inconsistency is documented when present.
- Requirement, API, UI, backend, and database evidence are separated.
- Each rule has a source reference or is marked as an assumption.
- Contradictions are explicit and not silently resolved by the AI.
- Domain partitions include valid and invalid cases.
- Cross-field dependencies are covered.
- BVA is applied only to ordered or bounded domains.
- Test case IDs are unique and correctly formatted.
- Expected results are observable.
- Test data is concrete and reproducible.
- Actual results and statuses are not fabricated.
- Evidence links or screenshots exist for executed tests.
- AI gap analysis includes missed cases or states that no gaps were found after review.
- Bug reports are created only for executed or otherwise verified failures.
- Final reports are understandable without reading the AI chat.
