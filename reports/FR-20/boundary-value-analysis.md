# Boundary Value Analysis - FR-20 Login and Account Lockout (Mobile)

## Scope

BVA is applied only to ordered or bounded FR-20 domains:

- Consecutive failed-login attempt count.
- Lockout duration.

Email format, credential match/mismatch, token presence, mobile UI form labels, keyboard semantics, password masking, and error placement are categorical or structural domains. They remain Domain Testing partitions and are not modeled as BVA.

## Boundary Values

| Boundary ID            | Variable                          | Rule                                                     | Test Basis Reference                                                                | Boundary Type                | On Point         | Off Point        | In Point / Nominal | Selected Value           | Expected Classification                                                                  | Related Partition       | Justification                                                                 |
| ---------------------- | --------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------- | ---------------- | ---------------- | ------------------ | ------------------------ | ---------------------------------------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------------------- |
| FR20-ATTEMPT-LOCK-B01  | Consecutive failed-login attempts | Account locks after 3 or more consecutive failed logins. | `requirement-analysis.md` - FR20-R04; `domain-testing.md` - ATTEMPTS-BELOW-LOCK-V01 | Lower threshold, below point | 3 wrong attempts | 2 wrong attempts | 1 wrong attempt    | 2 wrong attempts         | Valid below-lock state; account should not be locked yet.                                | ATTEMPTS-BELOW-LOCK-V01 | `2` is immediately below the documented lock threshold.                       |
| FR20-ATTEMPT-LOCK-B02  | Consecutive failed-login attempts | Account locks after 3 or more consecutive failed logins. | `requirement-analysis.md` - FR20-R04; `domain-testing.md` - ATTEMPTS-LOCK-I01       | Lower threshold, on point    | 3 wrong attempts | 2 wrong attempts | 1 wrong attempt    | 3 wrong attempts         | Invalid locked state; account should be locked.                                          | ATTEMPTS-LOCK-I01       | `3` is the documented inclusive threshold.                                    |
| FR20-ATTEMPT-LOCK-B03  | Consecutive failed-login attempts | Account locks after 3 or more consecutive failed logins. | `requirement-analysis.md` - FR20-R04; `domain-testing.md` - ATTEMPTS-LOCK-I01       | Lower threshold, above point | 3 wrong attempts | 2 wrong attempts | 1 wrong attempt    | 4 wrong attempts         | Invalid locked state; account should remain locked.                                      | ATTEMPTS-LOCK-I01       | `4` is immediately above the threshold and still belongs to the locked class. |
| FR20-LOCK-DURATION-B01 | Lockout duration                  | Temporary lock lasts 30 seconds in demo environment.     | `requirement-analysis.md` - FR20-R05; `domain-testing.md` - LOCK-ACTIVE-V01         | Duration before boundary     | 30 seconds       | 31 seconds       | 10 seconds         | 29 seconds after lockout | Active lockout; correct login should still be rejected.                                  | LOCK-ACTIVE-V01         | `29s` is immediately before the documented 30-second duration.                |
| FR20-LOCK-DURATION-B02 | Lockout duration                  | Temporary lock lasts 30 seconds in demo environment.     | `requirement-analysis.md` - FR20-R05; `domain-testing.md` - LOCK-EXPIRED-V01        | Duration on point            | 30 seconds       | 31 seconds       | 10 seconds         | 30 seconds after lockout | Expected unlocked or no longer rejected solely due lockout, subject to timing precision. | LOCK-EXPIRED-V01        | `30s` is the documented duration boundary.                                    |
| FR20-LOCK-DURATION-B03 | Lockout duration                  | Temporary lock lasts 30 seconds in demo environment.     | `requirement-analysis.md` - FR20-R05; `domain-testing.md` - LOCK-EXPIRED-V01        | Duration after boundary      | 30 seconds       | 31 seconds       | 10 seconds         | 31 seconds after lockout | Lockout should have expired; correct login should succeed.                               | LOCK-EXPIRED-V01        | `31s` is clearly after the documented duration.                               |
| FR20-LOCK-DURATION-N01 | Lockout duration                  | Temporary lock lasts 30 seconds in demo environment.     | `requirement-analysis.md` - FR20-R05; `domain-testing.md` - LOCK-ACTIVE-V01         | Nominal active-lock value    | 30 seconds       | 31 seconds       | 10 seconds         | 10 seconds after lockout | Active lockout; correct login should still be rejected.                                  | LOCK-ACTIVE-V01         | `10s` is a stable internal value inside the active-lockout interval.          |

## Boundary Derivation

- `FR20-ATTEMPT-LOCK-B01` to `FR20-ATTEMPT-LOCK-B03` come from the rule that an account locks after `3` or more consecutive failed logins.
- `2` wrong attempts is selected as `threshold - 1`.
- `3` wrong attempts is selected as the inclusive threshold.
- `4` wrong attempts is selected as `threshold + 1` and should still be locked.
- `FR20-LOCK-DURATION-B01` to `FR20-LOCK-DURATION-B03` come from the documented 30-second temporary lockout duration.
- `29s` is selected as immediately before the duration boundary.
- `30s` is selected as the documented boundary point.
- `31s` is selected as clearly after the boundary.
- `10s` is retained as a nominal active-lockout internal value.

## Excluded Boundary Candidates

- Email format is categorical/grammar-like and remains Domain Testing.
- Credential match/mismatch is relational and remains Domain Testing.
- Token presence is a response-contract condition and remains Domain Testing.
- Mobile required markers, email keyboard semantics, password masking, and error placement are UI conformance partitions, not numeric/ordered boundaries.
- Password length/complexity is not part of login requirements; it belongs to registration or reset-password features.
- Exact status codes, exact message text, and message length have no documented numeric boundary.

## Coverage Decisions

- Attempt-count BVA can be executed through the public `POST /api/login` surface.
- Lockout-duration BVA can be executed through the public `POST /api/login` surface using controlled disposable accounts.
- Mobile UI execution may reuse the same conceptual boundaries, but evidence requires Expo/device/emulator access.
- Exact behaviour at precisely `30.000` seconds is ambiguous, so test execution should record actual timing and avoid over-claiming precision.

## Human Review - Phase 4

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-27 18:20
- Review Scope: FR-20 Boundary Value Analysis
- Human Review Status: Completed
- Missing Boundaries Added: `threshold + 1` attempt value, `29s`, `30s`, `31s`, and nominal `10s` duration value
- Incorrect Boundaries Removed: None
- Approved for Test-Case Derivation: Yes
- Approved for Test Execution: Yes

## Human Corrections

- Split the original broad boundary rows into separate boundary IDs for traceability.
- Added attempt-count values `2`, `3`, and `4` to cover below, at, and above the documented threshold.
- Added lockout-duration values `29s`, `30s`, `31s`, and nominal `10s`.
- Clarified that email format, token presence, and mobile UI form rules are Domain Testing partitions, not BVA boundaries.
- Clarified that exact timing at `30.000s` is ambiguous and should be handled carefully during execution.
