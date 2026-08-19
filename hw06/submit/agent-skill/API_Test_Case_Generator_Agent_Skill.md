# API Test Case Generator Agent Skill

## Skill Name

`API_Test_Case_Generator`

## Objective

Given a single API specification file, automatically analyze every API endpoint and generate a comprehensive set of API test cases.

The agent must generate **at least 35 unique test cases for each endpoint**.

The agent must work step-by-step. It must not generate all test cases from one generic prompt.

## Input

Exactly one input:

`api_specification_file`

The file may contain the API specification in any readable structured or unstructured format, including OpenAPI, Swagger, JSON, YAML, text, Markdown, PDF, or document format.

The agent must first extract and normalize the API specification before generating tests.

If the specification cannot be interpreted reliably, the agent must report the issue instead of inventing API behavior.

## Output

Generate one Excel workbook for every API endpoint.

Filename convention:

`<HTTP_METHOD>_<ENDPOINT>.xlsx`

Examples:

- `POST_users.xlsx`
- `GET_users_{id}.xlsx`
- `PATCH_orders_{id}_status.xlsx`

Each workbook must contain at least 35 unique test cases unless generating 35 meaningful cases is impossible without inventing requirements. In such a case, explicitly identify the specification gap.

## Required Test Case Fields

Each generated test case must contain:

- TC_ID
- Requirement_ID
- HTTP Method
- Endpoint
- Test Technique
- Test Category
- Test Scenario
- Preconditions
- Test Data
- Test Steps
- Expected HTTP Status
- Expected Result
- Schema Validation
- Priority

## Execution Procedure

### Step 1 — Understand the API Specification

Read the entire specification.

Extract:

- endpoints
- HTTP methods
- path parameters
- query parameters
- headers
- request bodies
- datatypes
- required and optional fields
- formats
- enum values
- minimum and maximum values
- length constraints
- regular expressions
- authentication requirements
- authorization requirements
- response codes
- response schemas
- functional requirements
- security requirements
- business rules
- state transitions

Do not generate test cases yet.

### Step 2 — Analyze Every Parameter

For every endpoint, build a parameter-domain model.

For every parameter determine:

- valid domain
- invalid domain
- datatype
- required/optional
- format constraints
- numerical boundaries
- string-length boundaries
- enumeration values
- business constraints

Every parameter must receive test coverage.

### Step 3 — Equivalence Partitioning

Apply Equivalence Partitioning to every applicable parameter.

Create tests representing:

- valid equivalence classes
- invalid equivalence classes
- null values
- missing values where applicable
- wrong datatypes
- invalid formats

For example:

Email:

- valid email
- malformed email
- missing local part
- missing domain
- empty
- null

Price > 0:

- positive
- zero
- negative

Do not invent constraints that are not present in the specification.

### Step 4 — Boundary Value Analysis

Apply Boundary Value Analysis whenever the specification defines minimum, maximum, length, range, or similar limits.

For range `[min, max]`, consider:

- min - 1
- min
- min + 1
- max - 1
- max
- max + 1

Adapt the boundary values to the datatype.

For an exclusive condition such as `price > 0`, test values immediately below, at, and immediately above the boundary when the datatype permits it.

### Step 5 — State Transition Testing

Identify state machines and lifecycle rules from the specification.

For FR-10 or equivalent order lifecycle rules, cover:

`pending → confirmed → shipping → delivered`

Generate tests for:

- every permitted transition
- every prohibited transition
- skipped states
- backward transitions
- repeated transitions
- terminal states
- cancellation transitions

Cancellation behavior must come from the specification.

Do not assume cancellation rules that are not documented.

### Step 6 — Security Testing

Locate SEC-01 through SEC-07 in the specification and generate tests for every requirement.

Security scenarios should include relevant cases such as:

- missing authentication
- invalid or expired authentication
- SQL injection
- IDOR
- unauthorized resource access
- role escalation
- unauthorized field modification
- mass assignment
- malicious input
- information leakage

If SEC-01–SEC-07 are explicitly defined, use their exact definitions.

If they are not defined, use a generic security baseline but mark it as fallback security coverage.

### Step 7 — Schema Validation

For every documented response, generate validation cases ensuring that the response matches the specification exactly.

Validate:

- required properties
- property datatypes
- nested objects
- arrays
- enums
- formats
- nullability
- additional properties
- documented HTTP response codes

Create schema-validation tests for both successful and documented error responses.

### Step 8 — Fuzz Testing

Generate representative fuzz inputs where appropriate.

Examples:

- very long strings
- Unicode characters
- control characters
- zero-width characters
- malformed JSON
- extreme numeric values
- unexpected arrays or objects
- deeply nested input
- unexpected additional fields

The API must not crash or produce uncontrolled server errors.

### Step 9 — Error Guessing

Generate tester-inspired error scenarios such as:

- empty strings
- whitespace-only input
- duplicate requests
- non-existing identifiers
- invalid Content-Type
- missing Content-Type
- malformed request body
- extra fields
- casing differences
- leading/trailing whitespace
- duplicate parameters
- oversized payload

### Step 10 — Decision Table Testing

When endpoint behavior depends on combinations such as:

- role
- resource ownership
- current state
- requested action
- authentication status

build a decision table and generate representative tests for the decision rules.

### Step 11 — Deduplicate Test Cases

Remove cases that exercise the same condition with equivalent input and expected behavior.

Do not artificially duplicate tests merely to reach the minimum count.

### Step 12 — Validate Coverage

Before exporting an endpoint, verify:

- every parameter has domain-partition coverage
- every applicable boundary has BVA coverage
- valid state transitions are covered
- invalid state transitions are covered
- cancellation rules are covered
- SEC-01–SEC-07 are covered
- successful response schema is covered
- documented error schemas are covered
- fuzz/error-guessing scenarios are included

### Step 13 — Reach Minimum Test Count

Count the unique test cases for the endpoint.

If fewer than 35 cases exist, generate additional meaningful cases using:

1. uncovered equivalence classes
2. additional boundary combinations
3. negative parameter combinations
4. security scenarios
5. schema validations
6. fuzz testing
7. error guessing
8. decision-table combinations

Continue until at least 35 unique test cases exist.

Never invent an undocumented business rule only to increase the number of tests.

### Step 14 — Export to Excel

Create one Excel workbook for the endpoint.

Use one row per testcase.

Recommended filename:

`<METHOD>_<NORMALIZED_ENDPOINT>.xlsx`

Examples:

- `POST_orders.xlsx`
- `GET_orders_{id}.xlsx`
- `PATCH_orders_{id}_status.xlsx`

Repeat this procedure independently for every endpoint in the API specification.

---

## High-Level Flow

```text
API Specification File
        |
        v
[1. Read & Normalize Specification]
        |
        v
[2. Extract Endpoints & Parameters]
        |
        v
[3. Equivalence Partitioning]
        |
        v
[4. Boundary Value Analysis]
        |
        v
[5. State Transition Testing]
        |
        v
[6. Security Testing]
        |
        v
[7. Schema Validation]
        |
        v
[8. Fuzz Testing + Error Guessing]
        |
        v
[9. Decision Table Testing]
        |
        v
[10. Deduplicate + Coverage Check]
        |
        v
[11. Ensure >= 35 Tests / Endpoint]
        |
        v
[12. Export Excel]
```

---

## Pseudocode

```text
FUNCTION API_TEST_CASE_GENERATOR(api_spec_file):

    raw_content =
        READ_FILE(api_spec_file)

    normalized_spec =
        NORMALIZE_SPECIFICATION(raw_content)

    IF normalized_spec cannot be parsed:

        RETURN ERROR(
            "API specification cannot be reliably interpreted"
        )

    endpoints =
        EXTRACT_ENDPOINTS(normalized_spec)

    requirements =
        EXTRACT_REQUIREMENTS(normalized_spec)

    security_requirements =
        EXTRACT_SECURITY_REQUIREMENTS(
            normalized_spec
        )

    state_rules =
        EXTRACT_STATE_TRANSITIONS(
            normalized_spec
        )

    FOR endpoint IN endpoints:

        test_cases = []

        parameters =
            EXTRACT_PARAMETERS(endpoint)

        parameter_domains =
            ANALYZE_PARAMETER_DOMAINS(
                parameters,
                requirements
            )

        FOR parameter IN parameters:

            partitions =
                GENERATE_EQUIVALENCE_PARTITIONS(
                    parameter
                )

            test_cases.ADD_ALL(
                CREATE_TESTS_FROM_PARTITIONS(
                    endpoint,
                    parameter,
                    partitions
                )
            )

        FOR parameter IN parameters:

            IF parameter has boundary:

                boundary_values =
                    GENERATE_BOUNDARY_VALUES(
                        parameter
                    )

                test_cases.ADD_ALL(
                    CREATE_BVA_TESTS(
                        endpoint,
                        parameter,
                        boundary_values
                    )
                )

        related_states =
            GET_RELATED_STATE_RULES(
                endpoint,
                state_rules
            )

        IF related_states exist:

            valid_transitions =
                GET_VALID_TRANSITIONS(
                    related_states
                )

            invalid_transitions =
                GET_INVALID_TRANSITIONS(
                    related_states
                )

            cancellation_rules =
                GET_CANCELLATION_RULES(
                    related_states
                )

            test_cases.ADD_ALL(
                CREATE_STATE_TESTS(
                    valid_transitions,
                    invalid_transitions,
                    cancellation_rules
                )
            )

        security_tests =
            GENERATE_SECURITY_TESTS(
                endpoint,
                security_requirements
            )

        test_cases.ADD_ALL(
            security_tests
        )

        schema_tests =
            GENERATE_SCHEMA_TESTS(
                endpoint.request_schema,
                endpoint.response_schemas
            )

        test_cases.ADD_ALL(
            schema_tests
        )

        fuzz_tests =
            GENERATE_FUZZ_TESTS(
                endpoint,
                parameters
            )

        test_cases.ADD_ALL(
            fuzz_tests
        )

        error_guessing_tests =
            GENERATE_ERROR_GUESSING_TESTS(
                endpoint,
                parameters
            )

        test_cases.ADD_ALL(
            error_guessing_tests
        )

        decision_rules =
            IDENTIFY_DECISION_RULES(
                endpoint,
                requirements,
                security_requirements,
                state_rules
            )

        IF decision_rules exist:

            test_cases.ADD_ALL(
                GENERATE_DECISION_TABLE_TESTS(
                    decision_rules
                )
            )

        test_cases =
            REMOVE_DUPLICATE_TESTS(
                test_cases
            )

        coverage =
            CHECK_COVERAGE(
                endpoint,
                parameters,
                test_cases
            )

        VERIFY:

            every parameter has
                equivalence partition coverage

            every boundary has
                BVA coverage

            state rules have
                valid + invalid transitions

            SEC-01 to SEC-07 covered

            documented response schemas covered

        WHILE COUNT(test_cases) < 35:

            additional_tests =
                GENERATE_ADDITIONAL_TESTS(
                    endpoint,
                    uncovered_domains,
                    uncovered_combinations,
                    fuzzing,
                    error_guessing,
                    decision_tables
                )

            test_cases.ADD_ALL(
                additional_tests
            )

            test_cases =
                REMOVE_DUPLICATE_TESTS(
                    test_cases
                )

        filename =
            CREATE_FILENAME(
                endpoint.method,
                endpoint.path
            )

        EXPORT_TO_EXCEL(
            filename,
            test_cases
        )

    RETURN all_generated_excel_files
```
