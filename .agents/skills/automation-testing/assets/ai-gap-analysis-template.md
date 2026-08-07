# AI Gap Analysis - {{FEATURE_ID}} {{FEATURE_NAME}}

Covers only what the AI got wrong or missed on its first pass, and why — per the assignment's
requirement to critically review the AI-generated automation. Not a general changelog.

## Gap Findings

| Gap ID | Category | Script / Test | Before (AI-Generated) | After (Human Fix) | Why the AI Missed It |
| --- | --- | --- | --- | --- | --- |
| GAP-{{FEATURE_ID}}-001 | Fragile selector / Weak assertion / Missing edge case / Flaky wait | | | | |

## Categories Reference

- **Fragile selector**: relied on a raw CSS class or hardcoded copy string where a role/accessible-
  name locator would survive a styling or copy change. The app has no `data-testid`/`id` anywhere
  (see `references/eshop-analysis-guide.md`), so this is expected to be the most common category.
- **Weak or missing assertion**: checked something true-but-insufficient (e.g. only a URL change)
  instead of the actual expected content/state.
- **Missing edge case**: a documented boundary or negative condition from `test-cases.md` that the
  AI's script never covered.
- **Flaky wait**: a hardcoded timeout or an assumption about auto-waiting where a deterministic wait
  on a specific element/response would be reliable.

## Human Review

- Reviewer: TODO
- Review Date and Time: TODO
- Confirmed every gap traces to a real diff between AI output (`ai-audit.md`) and the final script:
  Yes/No
- Approved: Yes/No
