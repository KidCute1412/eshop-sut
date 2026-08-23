# API Test Design Method

## Contract Extraction

For each selected API, extract:

- Method, path, path/query/body parameters, headers, auth requirements, actor/role.
- Valid and invalid data domains for every parameter.
- Preconditions and dependent setup calls.
- Expected status code, response schema, and side effects.
- Security, state, and idempotency risks.

## Coverage Categories

Use these categories in `test-cases.md`:

- `Domain`: missing, empty, null, wrong type, format, range, length, enumeration, uniqueness, and
  cross-field relationships.
- `Boundary`: values just below/on/above numeric, length, count, date, attempt, and quantity limits.
- `State`: allowed transitions, forbidden transitions, final states, dependency setup, and repeated
  operations.
- `Security`: missing token, malformed token, expired token if available, wrong role, IDOR, role
  escalation, SQL injection, stored/reflected XSS payloads, sensitive data leakage.
- `Schema`: required fields, field types, arrays/objects, no unexpected sensitive fields, error
  body consistency.
- `Data-driven`: repeated cases whose values should come from CSV/JSON rather than one request.

## Test Case Fields

Every final case should include:

- Test Case ID, API ID, Feature, Category, Objective.
- Method and endpoint.
- Requirement/security reference.
- Preconditions.
- Headers, path/query/body data.
- Steps.
- Expected status and expected response/schema.
- AI Review Label: `VALID`, `INVALID`, `INCOMPLETE`, or `Human-Added`.
- Review Reason / AI Miss Reason.
- Actual Result, Status, Evidence, Bug ID.

Use concrete data. Keep unrelated fields nominally valid when testing one invalid condition.

## Human Review Rules

- Remove or merge duplicates only when they test the same condition through the same observable
  path.
- Keep different actor/token/state/schema variants separate even if the endpoint is the same.
- Do not accept vague expected results such as "should work" or "should fail"; specify status,
  body field, and side effect.
- Flag undocumented expected status codes as assumptions unless observed after execution.
- If setup data may mutate between runs, document reset or setup calls.

## AI Miss Reasons

Classify missed cases as:

- Prompt quality: the prompt omitted a rule, actor, state, or output expectation.
- Model limitation: the model produced generic API tests but missed cross-field, state, security,
  or schema strictness.
- SUT-specific behavior: seeded data, token flow, coupon usage count, order state setup, or local
  deployment behavior was not visible from the initial prompt.
