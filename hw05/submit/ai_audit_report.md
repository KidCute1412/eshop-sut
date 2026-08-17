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
Read the HW05 assignment, review the current submission artifacts, identify missing evidence, and help complete the performance-testing tasks.
```

- AI Output:

```text
Identified that the submission already had JMeter plans, CSV files, agent skills, and report templates, then listed the execution evidence that had to be produced before submission.
```

- Your Action: Reviewed the findings, ran the missing executions, and completed the final evidence package.

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

- Your Action: Added `task1/seed_performance_data.js` and documented the seed step in `task1/test_plan_review.md`.

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
Initial terminal checks showed PATH differences for Node.js and JMeter. After confirming the installed paths, the backend and JMeter CLI runs were executed successfully.
```

- Your Action: Used verified local tool paths, fixed JMeter runtime issues, and generated real `.jtl` plus HTML dashboard evidence.

### Interaction #5

- AI Tool: Codex
- Date and Time: 2026-08-15 22:55 +07:00
- Purpose: Prepare final report structure and next-run tooling.
- Prompt:

```text
Replace draft report values with verified information and add commands/scripts for reproducible performance evidence.
```

- AI Output:

```text
Renamed JMX files to StudentID format, added a JTL analyzer script, refreshed README, and rewrote the AI critique with concrete issues found during review.
```

- Your Action: Executed Load, Stress, and Spike scenarios; captured screenshots; analyzed raw JTL logs; and filled final metrics from the generated reports.

## Summary

| # | Task | AI Tool | Corrections Made |
|---|------|---------|------------------|
| 1 | Requirement audit | Codex | Separated completed artifacts from evidence required for final submission |
| 2 | JMX review | Codex | Verified endpoint coverage and listener diversity |
| 3 | CSV review | Codex | Added seed script for performance users/products |
| 4 | Environment check | Codex | Confirmed working Node.js and JMeter execution paths |
| 5 | Documentation cleanup | Codex | Replaced draft values with measured Load/Stress/Spike results |
