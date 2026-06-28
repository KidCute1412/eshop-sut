# FR-20 Login and Account Lockout Mobile - Reconstructed Design, Execution, and Gap Prompt

Reconstruction note: this prompt artifact was recreated after the fact from the current FR-20 reports and audit context. It is not represented as the original verbatim prompt.

Interpreted task:

- Use the `domain-testing-bva` skill for FR-20 Login and Account Lockout (Mobile).
- Complete black-box Phase 1 through Phase 8.
- Treat FR-20 as a Pool D mobile feature scoped to Login and Account Lockout.
- Use FR-02 login/lockout requirements as the functional login basis where FR-20 requires the mobile login feature.
- Use `api_specification.md` for `POST /api/login`.
- Use FR-22 shared form requirements where they apply to mobile login fields and error presentation.
- Use only black-box requirements, public API behaviour, observable mobile UI behaviour, setup guidance, and real evidence.
- Do not inspect implementation source, database schema, internal tests, controllers, services, routes, middleware, or models.

Required outputs:

- `reports/FR-20/requirement-analysis.md`
- `reports/FR-20/domain-testing.md`
- `reports/FR-20/boundary-value-analysis.md`
- `reports/FR-20/test-cases.md`
- `reports/FR-20/bug-report.md`
- `reports/FR-20/ai-gap-analysis.md`
- mobile/API evidence under `reports/FR-20/evidence/`

Execution expectations:

- Execute API login cases through the public backend API when available.
- Execute mobile UI checks only through observable Expo/device/emulator evidence.
- Record real Pass, Fail, or Blocked statuses only.
- Keep API login success separate from mobile authenticated-state success.
- Record BVA lockout cases as Blocked if clean account state or controlled lockout timing is unavailable.

Audit expectations:

- Preserve prompt and output artifacts under `evidence/ai-audit-artifacts/FR-20/`.
- Compare earlier AI assumptions with current human-reviewed reports in Phase 8.
- Clearly distinguish AI-missed tests, human improvements, runtime bugs, and environment/state blockers.
