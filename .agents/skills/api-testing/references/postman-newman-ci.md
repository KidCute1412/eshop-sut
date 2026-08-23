# Postman, Newman, and CI Guidance

## Collection Design

Use collection/environment variables for:

- `baseUrl`
- `studentId`
- `userEmail`, `userPassword`
- `adminEmail`, `adminPassword`
- `userToken`, `adminToken`
- Entity IDs created during setup, such as `productId`, `orderId`, `couponId`

Every request must include:

```text
X-Student-Id: {{studentId}}
```

Prefer a collection-level header or pre-request script so it is not forgotten in individual
requests.

## Postman Test Script Patterns

Include assertions for:

- HTTP status code.
- Required JSON fields and types.
- Error messages or stable error shape where specified.
- Authorization rejection for missing/wrong token.
- State transition result, then a follow-up GET where the API exposes the new state.
- Sensitive field absence, such as password hashes in user lists.

Use data files when a case template repeats across values. Keep data in `postman/data.csv` or
`postman/data.json`.

## Newman Evidence

Preserve:

- The exact command used.
- CLI output in `newman/newman-output.txt`.
- HTML report in `newman/report.html` or a timestamped equivalent.
- Screenshots of Postman console/pre-request script showing the `X-Student-Id` header when required.

Do not edit a generated Newman HTML report to change results.

## CI/CD

For GitHub Actions, the pipeline commonly needs:

- Node setup.
- Backend dependency install.
- Database seed/reset.
- Backend server start in the background.
- Health check or short wait.
- Newman install or `npx newman`.
- Collection run with environment/data files.
- Upload of Newman report as an artifact.

Document two real runs:

- One all-passing run from a commit where the suite passes.
- One intentionally failing run from a separate commit, with the failing assertion clearly marked
  as demonstration-only and reverted/fixed afterward when appropriate.

If CI cannot be executed, keep the workflow file and local Newman report, but mark the CI run links
as blocked with the exact reason.
