# AI Audit - FR-01

| Time | Tool | Prompt / Task | Output Reference | Human Review |
| --- | --- | --- | --- | --- |
| 2026-08-06T14:03:05Z | Codex | Convert selected FR-01 HW02 registration cases into Playwright data-driven automation. | `data/register-cases.json`, `tests/fr-01-register.spec.js` | Reviewed selectors, fixed POST response wait, retained duplicate-email failure as real bug. |
| 2026-08-07T15:40:00Z | Codex | Re-check registration password validation for documented special characters `!`, `@`, and a 20-character password. | `data/register-cases.json`, `tests/fr-01-register.spec.js`, `bug-report.md` | Corrected `FR01-DT-006` oracle to requirement-based success, added `FR01-BVA-009`, `FR01-BVA-010`, and `FR01-BVA-011`; confirmed `BUG-HW04-FR01-002`. |
