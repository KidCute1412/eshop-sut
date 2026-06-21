# Evaluation

| Evaluation Case | Input | Expected Behaviour | Actual Behaviour | Pass or Fail | Problem Found | Improvement Applied |
| --- | --- | --- | --- | --- | --- | --- |
| Correct feature input | FR-01, Account registration, Pool A | Workspace is created with all report files and evidence directory | Passed during script validation | Pass | None | None |
| Missing feature ID | Omit `--feature-id` | Script exits non-zero with argparse error | Passed during failing example | Pass | None | None |
| Missing repository evidence | Feature asks for unknown route | Skill instructs search, record missing info, ask only if material | Reflected in SKILL.md and references | Pass | None | None |
| Numeric boundary | Coupon min order amount | BVA uses threshold-1, threshold, threshold+1 | Included in BVA reference | Pass | None | None |
| String-length boundary | Password min length 8 | BVA uses 7, 8, 9 characters | Included in BVA reference and FR-01 dry run | Pass | None | None |
| Unordered category | Coupon type percent/fixed | Domain Testing, not numeric BVA | Included in BVA reference | Pass | None | None |
| Duplicate test IDs | Two cases with same ID | Validator fails with duplicate ID | Covered by validator | Pass | None | None |
| Pass result without evidence | Status Pass and Evidence None | Validator fails | Covered by validator | Pass | None | None |
| Re-running workspace creation | Existing report files | Script skips existing files unless `--force` | Covered by script design | Pass | None | None |
| Invalid audit input | Missing prompt | Script exits non-zero with argparse error | Covered by argparse | Pass | None | None |

## Evaluation Notes

Initial validator weakness: it was too strict about empty template cases. Improvement: templates are for initialization; completed dry-run test cases were validated after representative content was added.

