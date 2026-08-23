# AI-Driven API Test Generator Design

## Goal

Design an AI-driven API test generator for the EShop SUT. Given the API specification and
supporting requirement documents, the generator automatically produces API test cases and optional
Postman/Newman artifacts for selected endpoints.

The generator does not replace human review. Its job is to create a broad candidate suite quickly,
then force every expected result through source-of-truth mapping and a human audit gate before
execution.

## Source Inputs

| Input | Example in HW06 | Purpose |
| --- | --- | --- |
| API specification | `api_specification.md` | Extract method, path, request fields, auth headers, response schema, and examples. |
| Requirements | `README.md` | Map endpoints to FR rules and SEC rules. |
| Setup guide | `setup_guide.md` | Identify base URL, seed data, credentials, and reset/startup steps. |
| Assignment | `2026.HW06.API_Testing_En.md` | Enforce required evidence, AI audit, CI/CD, and no-fabrication constraints. |
| Student config | Student ID, selected APIs, output folder | Fill `X-Student-Id`, naming convention, and output locations. |
| Prior execution data | Optional Newman output/report | Update actual result and status after real execution. |

## Output Artifacts

| Output | Description |
| --- | --- |
| Test case table | Markdown or Excel table with ID, category, objective, preconditions, request data, expected status, expected response/schema, review label, actual result, status, and evidence. |
| AI audit file | Prompt and raw AI output before human filtering. |
| Gap analysis | Human-added cases and explanation of why AI missed them. |
| Postman collection | Request folders grouped by API/feature, variables, headers, pre-request scripts, token extraction, and assertions. |
| Newman command/report plan | CLI command, output file paths, and expected CI integration. |
| CI workflow draft | GitHub Actions workflow that starts backend, waits for readiness, runs Newman, and uploads report artifacts. |

## High-Level Pipeline

1. **Source Loader**
   - Reads `api_specification.md`, `README.md`, `setup_guide.md`, assignment instructions, and
     student config.
   - Normalizes Markdown headings, endpoint tables, auth notes, and examples into searchable
     chunks.

2. **Endpoint Contract Parser**
   - Extracts method, path, path/query/body/header parameters, authentication role, success
     status, error status hints, response schema, and example bodies.
   - Produces a structured `EndpointContract`.

3. **Requirement Mapper**
   - Links the endpoint to feature requirements (`FR-*`) and security requirements (`SEC-*`).
   - Marks contradictions or ambiguities, such as UI-only requirements that are not exposed in API
     request fields.

4. **Domain and Boundary Analyzer**
   - Builds equivalence partitions for each field: valid, missing, empty, null, wrong type,
     malformed, duplicate, enum invalid, and business-rule invalid.
   - Builds boundary values for numeric, length, date, quantity, discount, and usage-limit fields.

5. **Security and State Analyzer**
   - Generates missing token, malformed token, wrong role, IDOR/body identity injection, SQL
     injection-looking payload, XSS-like payload, sensitive-data leakage, and tampering cases.
   - Generates state cases for duplicate registration, duplicate add-to-cart, create/delete coupon,
     and repeated GET stability.

6. **AI Candidate Generator**
   - Calls the AI model with a scoped prompt for one endpoint or feature at a time.
   - Requests a candidate suite with categories, expected status, oracle, and required setup.
   - Saves raw output before modification.

7. **Rule-Based Validator**
   - Checks that each case has an ID, objective, source reference, expected status, request data,
     and oracle.
   - Flags unsupported expected behavior and ambiguous cases for human review.

8. **Human Review Gate**
   - Human marks each AI case as `VALID`, `INVALID`, or `INCOMPLETE`.
   - Human adds missing security/state/schema cases.
   - Final table keeps stable IDs; removed rows are not renumbered if auditability requires gaps.

9. **Artifact Emitter**
   - Writes final Markdown test tables, AI audit files, gap analysis, Postman collection,
     environment, optional data file, Newman command, and CI workflow draft.

10. **Execution Evidence Integrator**
    - Parses Newman output/report when available.
    - Updates `Actual Result`, `Status`, and `Evidence` columns only from real execution evidence.

## Core Data Model

```text
EndpointContract
  feature_id
  method
  path
  actor
  auth_required
  required_role
  request_fields[]
  headers[]
  success_status
  response_schema
  side_effects[]
  requirement_refs[]
  security_refs[]
  ambiguities[]

TestCase
  id
  category
  objective
  requirement_ref
  preconditions
  request_data
  expected_status
  expected_oracle
  ai_review_label
  review_reason
  actual_result
  status
  evidence
```

## Generation Rules

- Generate at least one positive case for each endpoint.
- Generate required-field missing, empty, null, and wrong-type cases for every request field.
- Generate boundary cases for fields with numeric, length, enum, date, quantity, or money
  constraints.
- Generate authentication and authorization cases for every protected endpoint.
- Generate at least one schema assertion for each success response.
- Generate state-transition cases for APIs that create, update, delete, or depend on existing
  server state.
- Generate security cases from SEC rules: role escalation, identity tampering, injection payloads,
  XSS-like payloads, and sensitive-data leakage.
- Do not treat current buggy behavior as expected behavior.
- Preserve AI raw output separately from final reviewed cases.

## EShop-Specific Examples

| Feature | Generator Focus |
| --- | --- |
| FR01 Registration | required fields, email format, duplicate email, password complexity, role injection, response schema, password leakage. |
| FR07 Cart | token requirement, quantity partitions, product id/name/price tampering, duplicate add state, cart isolation. |
| FR17 Coupons | admin role, coupon field validation, enum/range/date boundaries, duplicate code, create/delete side effects. |

## Safeguards

- No fabricated Newman results: execution fields remain `Not Executed` until a real run is parsed.
- No fabricated evidence: image/report links are added only when files exist.
- No fabricated CI links: CI report remains TODO until GitHub Actions run links exist.
- Human review is mandatory before final submission.
- Self-drawn diagram must be produced manually by the student.
