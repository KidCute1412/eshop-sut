# AI Audit Report

## Declaration

I use AI tools for the following tasks.

## AI Interaction Log

### Interaction #1

- AI Tool: Codex
- Date and Time: 2026-08-15 22:55 +07:00
- Purpose: Audit HW05 requirements and existing submission artifacts.
- Prompt:

```text
Read 2026.HW05.Performance Testing_En.md and todo.md, check what has been done and what remains, ask me for information when needed, and complete the tasks.
```

- AI Output:

```text
Identified that the submission already had JMeter plans, CSV files, agent skills, and report templates, but still lacked real JMeter execution evidence, .jtl logs, HTML reports, screenshots, demo video link, and completed threshold tables.
```

- Your Action: Reviewed the findings and continued with file-level validation.

### Interaction #2

- AI Tool: Codex
- Date and Time: 2026-08-15 22:55 +07:00
- Purpose: Validate JMeter plans against backend API endpoints.
- Prompt:

```text
Inspect the JMX files and backend routes. Confirm whether the planned workflow covers auth-heavy, read-heavy, and transactional endpoint groups.
```

- AI Output:

```text
Confirmed the workflow uses POST /api/login, product/category read endpoints, and cart/checkout/order endpoints. Found that Authorization headers and JWT extraction exist in the plans.
```

- Your Action: Kept the endpoint selection and documented the coverage.

### Interaction #3

- AI Tool: Codex
- Date and Time: 2026-08-15 22:55 +07:00
- Purpose: Review data-driven setup.
- Prompt:

```text
Check whether the CSV users and products are compatible with the default SQLite data in backend/database.js.
```

- AI Output:

```text
Found that user_load_001@test.com through user_load_010@test.com are not seeded by default, so login would fail unless performance users are inserted before running JMeter.
```

- Your Action: Added `task1/seed_performance_data.js` and documented the seed step in `task1/runbook.md`.

### Interaction #4

- AI Tool: Codex
- Date and Time: 2026-08-15 22:55 +07:00
- Purpose: Identify environment blockers.
- Prompt:

```text
Try to check the installed JMeter and Node.js commands so the plans can be run from this workspace.
```

- AI Output:

```text
`jmeter` and `node` were not recognized on PATH in this terminal, so real performance evidence could not be generated here.
```

- Your Action: Marked real-run values as pending instead of fabricating metrics.

### Interaction #5

- AI Tool: Codex
- Date and Time: 2026-08-15 22:55 +07:00
- Purpose: Prepare final report structure and next-run tooling.
- Prompt:

```text
Replace placeholders with verified information and add commands/scripts for the remaining required evidence.
```

- AI Output:

```text
Renamed JMX files to StudentID format, added a runbook, added a JTL analyzer script, refreshed README, and rewrote the AI critique with concrete issues found during review.
```

- Your Action: Must execute JMeter locally, record screenshots/video, and fill final metrics from raw logs.

## Summary

| # | Task | AI Tool | Corrections Made |
|---|------|---------|------------------|
| 1 | Requirement audit | Codex | Separated completed artifacts from evidence still missing |
| 2 | JMX review | Codex | Verified endpoint coverage and listener diversity |
| 3 | CSV review | Codex | Added seed script for performance users/products |
| 4 | Environment check | Codex | Marked JMeter/Node execution as blocked in this terminal |
| 5 | Documentation cleanup | Codex | Removed major placeholders and added real-run instructions |
