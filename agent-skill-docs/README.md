# domain-testing-bva

Purpose: reusable Agent Skill for Domain Testing and Boundary Value Analysis on EShop features.

Folder: `.agents/skills/domain-testing-bva/`

## Requirements

- Python 3 standard library.
- Access to the EShop repository.
- Human review before submission.

## Discovery

Use the skill by referencing `domain-testing-bva` or by asking an agent to design Domain Testing and BVA reports for an EShop feature.

## Example Invocation

```bash
python .agents/skills/domain-testing-bva/scripts/create_feature_workspace.py --feature-id FR-01 --feature-name "Account registration" --pool A --output reports
```

Then ask the agent:

```text
Use domain-testing-bva for FR-01 Account registration in Pool A. Inspect the repository and generate assignment-ready Domain Testing and BVA reports under reports/FR-01.
```

## Inputs

Feature ID, feature name, pool, role, module, requirement source, source paths, API endpoints, database models, auth role, preconditions, test data, output directory, and execution environment if tests will be run.

## Outputs

Feature reports, domain table, BVA table, test cases, traceability matrix, AI gap analysis, evidence directory, and AI audit entries.

## Script Commands

```bash
python .agents/skills/domain-testing-bva/scripts/create_feature_workspace.py --help
python .agents/skills/domain-testing-bva/scripts/validate_test_cases.py --help
python .agents/skills/domain-testing-bva/scripts/append_ai_audit.py --help
```

## Known Limitations

- The skill designs tests; it does not execute application test cases unless the agent deliberately starts the SUT and captures evidence.
- Source inspection is not execution evidence.
- The current allocation has two Pool A features and no Pool D feature.

## YouTube Demo

Placeholder: `<add YouTube demo link here>`

