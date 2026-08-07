# Automation Test-Case Selection Schema

Used in Phase 1 when selecting/documenting the ≥12 cases per feature before conversion to scripts.
Mirrors HW02's DT/BVA test-case schema so a case can be traced back to its original design.

| Field | Meaning |
| --- | --- |
| ID | The original HW02 test-case ID if reused (e.g. `FR01-DT-012`), or a new ID prefixed `AUTO-` if added in this pass. |
| Type | Positive / Negative / Edge. |
| Steps | The user actions, same as HW02's version — this is what the AI converts into Playwright actions. |
| Test Data | Reference to the row/object in the external data file this case uses (by `id`), not the literal values inline in this table. |
| Expected Result | Same as HW02's version, traced to `README.md`/`api_specification.md`. |
| Assertion Pattern(s) | Which of the patterns in `references/data-driven-and-assertions.md` this case's script uses — filled in after Phase 2, used to check Phase 4's diversity requirement. |
| Automatable | Yes / No. If No, the reason (Phase 7 requires documenting these). |
| Spec File | Path to the `.spec.ts`/`.spec.js` file and test name once converted. |

Keep this table in each feature's `test-cases.md` (seeded from the HW02 file, trimmed/extended per
Phase 1) — it is the bridge between the design-time case and the automation artifact, and is what
the human review in Phase 5 checks line by line.
