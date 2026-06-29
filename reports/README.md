# HW02 AI Domain Testing - Submission README

## Submission Contents

- Main report: [main-report.md](main-report.md)
- Feature reports: [FR-01](FR-01/), [FR-02](FR-02/), [FR-07](FR-07/), [FR-17](FR-17/), [FR-20](FR-20/)
- AI audit logs: [../ai-audit/](../ai-audit/)
- Preserved AI prompt/output artifacts: [../evidence/ai-audit-artifacts/](../evidence/ai-audit-artifacts/)
- Agent skill: [../.agents/skills/domain-testing-bva/](../.agents/skills/domain-testing-bva/)
- Demo video: [HW02 Domain Testing Video Demonstration](https://www.youtube.com/watch?v=q7ZQzRcub8Q)

## Selected Features

| Pool | Feature | Feature Name                     | Note                                                              |
| ---- | ------- | -------------------------------- | ----------------------------------------------------------------- |
| A    | FR-02   | Login and account lockout        | Selected Pool A feature for the four-pool requirement.            |
| B    | FR-07   | Shopping cart                    | Selected Pool B feature.                                          |
| C    | FR-17   | Coupon management CRUD           | Selected Pool C feature.                                          |
| D    | FR-20   | Login and account lockout mobile | Selected Pool D mobile feature.                                   |
| A    | FR-01   | Account registration             | Additional completed Pool A artifact included as supporting work. |

## Self-Assessment

| No.   | Criteria                              | Grade | Self-Assessed Grade |
| ----- | ------------------------------------- | ----: | ------------------: |
| 1     | Feature A (Domain + Boundary)         |    25 |                  25 |
| 2     | Feature B (Domain + Boundary)         |    25 |                  25 |
| 3     | Feature C (Domain + Boundary)         |    25 |                  25 |
| 4     | Feature D (Mobile, Domain + Boundary) |    15 |                  15 |
| 5     | Agent Skills                          |    10 |                  10 |
| Total |                                       |   100 |                 100 |

## Test Summary

| Feature | Test Cases Designed | Executed | Passed | Failed | Blocked | Not Yet Executed | Bugs | Evidence Files |
| ------- | ------------------: | -------: | -----: | -----: | ------: | ---------------: | ---: | -------------: |
| FR-01   |                  37 |       37 |      5 |     14 |      18 |                0 |    7 |             37 |
| FR-02   |                  34 |       34 |     22 |      9 |       0 |                0 |    6 |             38 |
| FR-07   |                  20 |       20 |      6 |     14 |       0 |                0 |   10 |             11 |
| FR-17   |                  22 |       22 |     13 |      9 |       0 |                0 |    4 |             22 |
| FR-20   |                  19 |       19 |      9 |      3 |       7 |                0 |    3 |             11 |
| Total   |                 132 |      132 |     55 |     49 |      25 |                0 |   30 |            119 |

## Bug Reports

Detailed bug reports and GitHub Issue links are recorded in:

- [FR-01/bug-report.md](FR-01/bug-report.md)
- [FR-02/bug-report.md](FR-02/bug-report.md)
- [FR-07/bug-report.md](FR-07/bug-report.md)
- [FR-17/bug-report.md](FR-17/bug-report.md)
- [FR-20/bug-report.md](FR-20/bug-report.md)

## Demo Video

- [HW02 Domain Testing Video Demonstration](https://www.youtube.com/watch?v=q7ZQzRcub8Q)
