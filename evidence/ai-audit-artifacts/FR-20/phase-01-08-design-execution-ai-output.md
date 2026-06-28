# FR-20 Phase 1-8 Reconstructed AI Output Summary

## Phase Summary

### Phase 1-2: Feature Intake and Test Basis

FR-20 was scoped to Login and Account Lockout on the mobile app. The basis combined FR-20 mobile coverage, FR-02 login/lockout behaviour, FR-22 form expectations, `POST /api/login`, setup guidance, and observable API/mobile results. The reports explicitly kept API success separate from mobile UI success.

### Phase 3: Domain Modeling

The current domain model includes email and password inputs, registered account state, failed-attempt state, lockout timer, successful API login response, mobile post-login state, invalid-login rejection, lockout safe-error behaviour, mobile login screen presence, required markers, mobile email semantics, password masking, and error placement.

Human-reviewed corrections added negative mobile UI partitions such as missing required markers, misplaced error messages, visible password text, missing mobile login screen, and mobile valid-login failure.

### Phase 4: Boundary Value Analysis

BVA focuses on ordered lockout domains:

- failed attempt count around the threshold: 2, 3, and 4;
- lockout duration values: 29s, 30s, 31s, and nominal active 10s.

Email format, password masking, labels, and error placement remain Domain Testing partitions.

### Phase 5-7: Test Cases and Execution

The current FR-20 test suite contains 19 cases:

- Pass: 9
- Fail: 3
- Blocked: 7

Current failing cases:

- `FR20-DT-008`: required-field marker is missing on mobile login.
- `FR20-DT-010`: mobile login error appears below the submit button.
- `FR20-DT-012`: valid mobile credentials do not reach authenticated mobile state.

Current blocked cases:

- `FR20-BVA-001` through `FR20-BVA-007`, because clean account state and controlled lockout timing were unavailable.

### Phase 8: AI Gap Analysis

The current gap analysis compares earlier AI assumptions with human-reviewed reports and later execution evidence. It highlights missed mobile-specific partitions/cases, improved BVA traceability, stale mobile-runtime blocker assumptions, mobile UI runtime failures, and the need to reconcile the older lockout-duration bug report with current blocked BVA statuses.

## Integrity Notes

- No implementation source, database schema, internal tests, controllers, services, routes, middleware, or models were used as oracle.
- Mobile evidence is represented by current screenshots under `reports/FR-20/evidence/`.
- BVA blockers are retained instead of inventing timing results.
