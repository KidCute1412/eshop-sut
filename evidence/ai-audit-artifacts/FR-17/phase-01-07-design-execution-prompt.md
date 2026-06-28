# FR-17 Coupon Management CRUD - Reconstructed Design and Execution Prompt

Reconstruction note: this prompt artifact was recreated after the fact from the current FR-17 reports and audit context. It is not represented as the original verbatim prompt.

Interpreted task:

- Use the `domain-testing-bva` skill for FR-17 Coupon Management CRUD.
- Complete black-box Phase 1 through Phase 7 for the Web Admin coupon feature.
- Use only approved black-box sources: assignment PDF, `README.md`, `api_specification.md`, setup guidance, public API/UI observations, and real execution evidence.
- Do not inspect application implementation source, database schema, internal tests, controllers, services, routes, middleware, or models.
- Create and maintain the standard FR-17 report set under `reports/FR-17/`.
- Preserve requirement analysis, domain partitions, BVA boundaries, test cases, execution evidence, confirmed bug reports, traceability, and AI gap notes.
- Execute approved cases through public API/UI only and record Pass, Fail, or Blocked from real observable results.
- Leave GitHub Issue links as `Pending` unless real issues are created.

Feature scope:

- Feature ID: FR-17
- Feature name: Coupon Management CRUD
- Pool: C - Web Admin
- Actor: Admin user, unauthenticated user, and non-admin authenticated user where access control is relevant.
- Surfaces: Web Admin coupon management area and public/admin coupon APIs.
- API focus: `GET /api/coupons`, `POST /api/admin/coupons`, `DELETE /api/admin/coupons/:id`.

Expected outputs:

- `reports/FR-17/requirement-analysis.md`
- `reports/FR-17/domain-testing.md`
- `reports/FR-17/boundary-value-analysis.md`
- `reports/FR-17/test-cases.md`
- `reports/FR-17/bug-report.md`
- `reports/FR-17/ai-gap-analysis.md`
- evidence files under `reports/FR-17/evidence/`

Integrity constraints:

- Do not fabricate evidence, statuses, screenshots, bugs, or issue links.
- Expected results must come from approved requirements and API specifications, not implementation behaviour.
- Runtime failures must be tied to concrete test cases and evidence.
- Human review and corrections must remain visible in the reports.
