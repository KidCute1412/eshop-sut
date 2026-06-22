# EShop Black-box Analysis Guide

## Approved Test Bases

- Official assignment PDF: `2026.HW02.Domain Testing_En.pdf`.
- Requirements: `README.md`.
- Public API contract: `api_specification.md`.
- Setup guidance: `setup_guide.md`.
- Observable UI labels, controls, messages, navigation, and states.
- Observable public API requests, responses, status codes, and documented state changes.
- Real execution evidence.

Do not inspect frontend or backend implementation, database schema, internal middleware/services/controllers/models, or existing implementation tests. They cannot establish expected results.

## Startup Safety

`run_servers.sh` may be inspected only to understand safe startup. Review it for process-killing commands, hard-coded paths, prerequisites, and ports before execution. Prefer documented manual startup when the script is unsafe. Do not derive requirements or expected results from it.

## Observation Rules

- A UI/API observation made during exploration is `Observable UI behaviour` or `Observable API behaviour`.
- A recorded result from an executed test is `Execution evidence`.
- If observation conflicts with a documented expected result, record an `Observed contradiction`; do not rewrite the expected result to match the application.
- Authentication and authorization expectations must come from requirements or the API specification, then be verified through public interfaces.
