# Prompt Templates For The AI-Driven API Test Generator

## 1. Endpoint Contract Extraction Prompt

```text
You are an API testing assistant for the EShop SUT.
Read the following source-of-truth excerpts and extract the API contract for one selected feature.

Feature ID: {feature_id}
Selected endpoint(s): {endpoints}
Source documents:
- README.md excerpt: {readme_excerpt}
- api_specification.md excerpt: {api_spec_excerpt}
- setup_guide.md excerpt: {setup_excerpt}

Return a structured contract with:
- method and path;
- actor;
- authentication and role requirement;
- request headers;
- path/query/body parameters;
- required/optional fields;
- valid values and boundaries;
- success status and schema;
- error cases implied by the source of truth;
- side effects;
- ambiguities between README and API specification.

Do not use implementation source code as the oracle.
```

## 2. Domain And Boundary Generation Prompt

```text
Using this endpoint contract, generate domain partitions and boundary values.

Endpoint contract:
{endpoint_contract}

Feature rules:
{feature_rules}

Generate candidate test ideas for:
- valid representative values;
- missing required fields;
- empty values;
- null values;
- wrong types;
- invalid format;
- duplicate values;
- enum invalid values;
- numeric/date/length boundaries.

Return a Markdown table with category, objective, request data, expected status, and expected oracle.
```

## 3. Security And State Generation Prompt

```text
Generate API security and state-transition test cases for this endpoint.

Endpoint contract:
{endpoint_contract}

Security rules:
{security_rules}

State model:
{state_model}

Cover only cases relevant to this endpoint:
- missing token;
- malformed token;
- wrong role;
- body identity injection;
- role escalation;
- SQL injection-looking input;
- XSS-like input;
- sensitive-data leakage;
- duplicate/create/delete state changes;
- repeated GET/read-only stability.

Return expected results from the source of truth, not from current observed bugs.
```

## 4. Final Candidate Suite Prompt

```text
Combine the contract, domain, boundary, security, state, and schema ideas into one candidate suite.

Requirements:
- At least {minimum_cases} cases if the endpoint is broad enough.
- Keep categories clear: Domain, Boundary, Security, State, Schema, Data-driven.
- Include preconditions and request data.
- Include expected status and expected response/schema.
- Mark assumptions or ambiguities explicitly.
- Do not add execution results.

Return a Markdown table with:
ID, Category, Objective, Requirement/Security Ref, Preconditions, Request Data,
Expected Status, Expected Response/Schema, AI Review Label, Review Reason.
```
