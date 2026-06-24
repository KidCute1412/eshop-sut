# Boundary Value Analysis - FR-01 Account Registration

## Black-box Test Basis Summary

This Phase 4 analysis uses only the approved `reports/FR-01/requirement-analysis.md` and human-reviewed `reports/FR-01/domain-testing.md`, together with the approved skill BVA method. Phase 3 is `Completed` and `Approved for BVA: Yes`. No implementation, database, internal tests, application execution, HTTP request, or observed runtime behaviour was used. Classification below is test design, not execution.

## Step 1: Candidate Domain Assessment

| Domain or Variable                | Rule ID               | Domain Type                 | Documented Constraint                                                                | BVA Applicability | Reason                                                                        | Test Basis Reference                                                        |
| --------------------------------- | --------------------- | --------------------------- | ------------------------------------------------------------------------------------ | ----------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Full-name presence                | FR01-R01              | Categorical presence        | Full name must be provided.                                                          | Not applicable    | Present/absent is categorical, not an ordered magnitude.                      | `requirement-analysis.md` - FR01-R01; `domain-testing.md` - NAME-PRESENCE   |
| Full-name length                  | FR01-R01, API02       | String length               | No minimum or maximum documented.                                                    | Undetermined      | Length is ordered, but no approved numeric boundary exists.                   | `requirement-analysis.md` - ambiguities                                     |
| Email presence                    | FR01-R02              | Categorical presence        | Email must be provided.                                                              | Not applicable    | Present/absent is categorical.                                                | `domain-testing.md` - EMAIL-PRESENCE                                        |
| Email format                      | FR01-R04              | Format category             | Must be valid; example `user@domain.com`.                                            | Not applicable    | Syntax classes are not an ordered numeric scale.                              | `domain-testing.md` - EMAIL-FORMAT                                          |
| Email uniqueness                  | FR01-R05              | State category              | Email is unused or already registered.                                               | Not applicable    | Unique/duplicate is state-based and unordered.                                | `domain-testing.md` - EMAIL-UNIQUENESS                                      |
| Email length                      | FR01-R04, API03       | String length               | No minimum or maximum documented.                                                    | Undetermined      | Possible ordered domain lacks documented limits.                              | `requirement-analysis.md` - ambiguities                                     |
| Password presence                 | FR01-R03              | Categorical presence        | Password must be provided.                                                           | Not applicable    | Present/absent is categorical.                                                | `domain-testing.md` - PASSWORD-PRESENCE                                     |
| Password length                   | FR01-R06              | Lower-bounded string length | Minimum 8 characters, inclusive; no maximum.                                         | Applicable        | Explicit ordered lower boundary supports lower-only BVA.                      | `requirement-analysis.md` - FR01-R06; `domain-testing.md` - PASSWORD-LENGTH |
| Uppercase presence                | FR01-R07              | Character-class category    | At least one uppercase letter.                                                       | Not applicable    | Modeled as categorical presence; no upper count is specified.                 | `domain-testing.md` - PASSWORD-UPPERCASE                                    |
| Lowercase presence                | FR01-R08              | Character-class category    | At least one lowercase letter.                                                       | Not applicable    | Presence/absence is categorical.                                              | `domain-testing.md` - PASSWORD-LOWERCASE                                    |
| Digit presence                    | FR01-R09              | Character-class category    | At least one digit.                                                                  | Not applicable    | Presence/absence is categorical.                                              | `domain-testing.md` - PASSWORD-DIGIT                                        |
| Special-character presence        | FR01-R10              | Character-class category    | At least one documented special character.                                           | Not applicable    | Presence/absence and identity are unordered categories.                       | `domain-testing.md` - PASSWORD-SPECIAL                                      |
| Confirm-password control presence | FR01-R11              | UI structure category       | Confirmation control must exist.                                                     | Not applicable    | Control existence is Boolean.                                                 | `domain-testing.md` - CONFIRM-CONTROL                                       |
| Confirm-password value presence   | FR01-R11              | Categorical presence        | Confirmation value must be provided.                                                 | Not applicable    | Provided/empty is categorical; no length limit is documented.                 | `domain-testing.md` - CONFIRM-VALUE                                         |
| Password-confirmation equality    | FR01-R12              | Relational category         | Values match or mismatch.                                                            | Not applicable    | Equality is relational, not ordered.                                          | `domain-testing.md` - CONFIRM-MATCH                                         |
| API request properties            | API02-API04, R01-R03  | Contract structure          | `name`, `email`, and `password` are documented and required.                         | Not applicable    | Named-property presence is categorical; no property-count range is specified. | `domain-testing.md` - API-REQUEST                                           |
| Guest actor state                 | API01; Feature Intake | State category              | Guest/unauthenticated actor uses public registration.                                | Not applicable    | Actor state is unordered.                                                     | `domain-testing.md` - ACTOR-GUEST                                           |
| Required-field marker             | SF01                  | UI property                 | Required labels show adjacent `*`.                                                   | Not applicable    | Marker presence is Boolean.                                                   | `domain-testing.md` - FORM-REQUIRED-MARKER                                  |
| Email control type                | SF02                  | UI property                 | Email control uses `type="email"`.                                                   | Not applicable    | Control types are unordered.                                                  | `domain-testing.md` - FORM-EMAIL-TYPE                                       |
| Password control type/masking     | SF03                  | UI property                 | Password uses `type="password"` and is masked.                                       | Not applicable    | Type and visibility are categorical.                                          | `domain-testing.md` - FORM-PASSWORD-TYPE                                    |
| Error placement                   | SF04                  | UI spatial category         | Error appears above, not below, Submit.                                              | Not applicable    | Named placement categories have no measurable boundary.                       | `domain-testing.md` - FORM-ERROR-PLACEMENT                                  |
| Registration step indicator       | SF05                  | Conditional UI rule         | Required only for forms with at least two steps; registration step count is unknown. | Undetermined      | Approved basis does not establish registration as multi-step.                 | `domain-testing.md` - FORM-STEP-INDICATOR-A01                               |
| API success response              | API05                 | Contract/output category    | HTTP 200 with documented message and identifier.                                     | Not applicable    | Status and response shape are categorical; identifier bounds are unspecified. | `domain-testing.md` - API-SUCCESS                                           |
| UI successful outcome             | R13                   | Outcome state               | Valid registration completes successfully.                                           | Not applicable    | Success/non-success is state-based.                                           | `domain-testing.md` - REGISTRATION-COMPLETE                                 |
| Validation rejection              | R01-R12               | Outcome state               | Invalid documented input is rejected.                                                | Not applicable    | Rejection is categorical; undocumented statuses cannot form boundaries.       | `domain-testing.md` - VALIDATION-REJECTION                                  |
| Redirect destination              | R14                   | Navigation category         | Successful registration goes to Login page.                                          | Not applicable    | Destination is categorical; timing has no documented limit.                   | `domain-testing.md` - REDIRECT-SUCCESS                                      |

## Step 2: Applicable Boundary Model

| Boundary Model ID        | Variable                 | Rule                 | Test Basis                        | Boundary Type        | Off Point | On Point | In Point | Nominal Internal Value | Expected Classification   | Justification                                                                                          |
| ------------------------ | ------------------------ | -------------------- | --------------------------------- | -------------------- | --------- | -------- | -------- | ---------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------ |
| FR01-PASSWORD-LENGTH-M01 | Password character count | Minimum 8 characters | FR01-R06; PASSWORD-LENGTH-V01/I01 | Inclusive lower-only | 7         | 8        | 9        | 11                     | 7 Invalid; 8, 9, 11 Valid | Integer counts below, at, and inside the inclusive minimum isolate the only approved numeric boundary. |

No upper-bound model is created because the approved test basis documents no maximum password length.

## Step 3: Concrete Boundary Values

| Boundary ID              | Variable        | Rule ID  | Boundary Position      | Concrete Value | Character Count | Expected Classification | Dependencies and Nominal Values                                                                                                                  | Applicable Surface | Test Basis Reference                                                                | Justification                                                                              | Assumptions                        |
| ------------------------ | --------------- | -------- | ---------------------- | -------------- | --------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------- |
| FR01-PASSWORD-LENGTH-B01 | Password length | FR01-R06 | `min-1` / off point    | `Abcd1!x`      | 7               | Invalid                 | Name `Nguyen Van A`; unique valid email; UI confirmation equals password; guest actor. Includes uppercase, lowercase, digit, and documented `!`. | UI and API         | `requirement-analysis.md` - FR01-R06-R10; `domain-testing.md` - PASSWORD-LENGTH-I01 | Exactly one character below the minimum while every other password rule remains satisfied. | Seven displayed ASCII characters.  |
| FR01-PASSWORD-LENGTH-B02 | Password length | FR01-R06 | `min` / on point       | `Abcd1!xy`     | 8               | Valid                   | Same nominal dependencies; confirmation equals password on UI; all character classes satisfied.                                                  | UI and API         | Same as B01                                                                         | Exactly at the inclusive minimum.                                                          | Eight displayed ASCII characters.  |
| FR01-PASSWORD-LENGTH-B03 | Password length | FR01-R06 | `min+1` / in point     | `Abcd1!xyz`    | 9               | Valid                   | Same nominal dependencies; confirmation equals password on UI; all character classes satisfied.                                                  | UI and API         | Same as B01                                                                         | Immediately inside the valid domain.                                                       | Nine displayed ASCII characters.   |
| FR01-PASSWORD-LENGTH-N01 | Password length | FR01-R06 | Nominal internal value | `ValidPass1!`  | 11              | Valid                   | Same nominal dependencies; confirmation equals password on UI; all character classes satisfied.                                                  | UI and API         | Same as B01                                                                         | Clearly internal valid value distinct from adjacent points.                                | Eleven displayed ASCII characters. |

## Boundary Derivation

FR01-R06 states “at least 8 characters,” creating an inclusive lower boundary over integer character counts. Thus 8 is the on point, 7 the adjacent off point, and 9 the adjacent in point; 11 is nominal valid. Every value contains uppercase, lowercase, digit, and explicitly documented `!`, so length alone changes classification. UI confirmation repeats the selected password; full name, email, actor state, and request structure remain nominal.

Verified counts: `Abcd1!x` = 7, `Abcd1!xy` = 8, `Abcd1!xyz` = 9, and `ValidPass1!` = 11. Classification is design-time analysis, not execution.

## Coverage Decisions and Exclusions

- BVA is included only for the documented password minimum.
- No `max-1`, `max`, or `max+1` exists because no password maximum is documented.
- Presence, format, uniqueness, equality, actor, property, UI, placement, response, outcome, and redirect domains remain categorical Domain Testing domains.
- Character-class rules remain presence partitions; no undocumented maximum counts are invented.
- Step-indicator applicability is undetermined because registration step count is unknown.
- Full-name, email, and confirmation lengths have no approved numeric limits.
- Test-case coverage is reserved for Phase 5; no BVA test case is created here.

## Assumptions and Gaps

- Selected ASCII values avoid unspecified Unicode counting semantics.
- Maximum field lengths, full-name numeric limits, email length limits, and confirmation length limits are undocumented.
- Email normalization, invalid API statuses/bodies, duplicate response details, exact redirect URL/timing, and UI success text provide no numeric BVA oracle.
- No public UI observation or execution evidence supplements the reviewed reports.
- Human review must approve this model before Phase 5.

## Human Review - Phase 4

- Reviewer:
- Review Date and Time:
- Corrections Made:
- Missing Boundaries Added:
- Incorrect Boundaries Removed:
- Status: Pending
- Approved for Test-Case Derivation: No
- Approved for Test Execution: No
