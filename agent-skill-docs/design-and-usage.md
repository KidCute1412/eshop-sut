# Design and Usage

## Reusable Skill Choice

One reusable skill was selected because Domain Testing and BVA share the same evidence-gathering foundation across all EShop features. Feature-specific details belong in generated reports, not in the skill instructions.

## Progressive Disclosure

`SKILL.md` contains the activation contract and workflow. Detailed methods are split into `references/`, and output shapes live in `assets/`. Agents only load deeper material when needed.

## Role of Files

- `SKILL.md`: concise procedure, phases, required outputs, and integrity rules.
- `references/`: assignment summary, EShop inspection guide, Domain Testing method, BVA method, schema, and human review checklist.
- `assets/`: Markdown templates for reports and audit entries.
- `scripts/`: deterministic helpers for workspace creation, validation, and audit logging.

## Human Review Gates

The skill explicitly requires human review after evidence collection, after test design, after validation, and before submission. It marks unreviewed work as pending.

## Repository Evidence

The workflow requires agents to separate documented requirements, API contracts, frontend behavior, backend behavior, database enforcement, assumptions, and contradictions. This prevents source code from silently overriding the assignment.

## No Fabricated Results

The skill requires `Actual Result: Not Executed`, `Status: Not Executed`, and `Evidence: None` until a test is actually executed. Bug reports and screenshots may only be claimed when real evidence exists.

