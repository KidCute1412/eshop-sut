# HW6 - API Testing - Submission README

- Student: TODO
- Student ID: TODO_STUDENT_ID
- SUT: EShop backend API
- Repository link: TODO
- Base URL: http://localhost:3000
- Tool: Postman + Newman
- Selected APIs: FR01 (POST /api/register), FR07 (GET /api/cart, POST /api/cart), FR17 (GET /api/coupons, POST /api/admin/coupons, DELETE /api/admin/coupons/:id)
- Agent Skill: .agents/skills/api-testing

## Self-Assessment

| No. | Criteria                                    |   Grade | Self-Assessed Grade |
| --: | ------------------------------------------- | ------: | ------------------: |
|   1 | API 1 - FR01 full pipeline                  |      30 |                     |
|   2 | API 2 - FR07 full pipeline                  |      30 |                     |
|   3 | API 3 - FR17 full pipeline                  |      30 |                     |
|   4 | Agent Skills / AI-driven API test generator |      10 |                     |
|     | **Total**                                   | **100** |                     |

## Test Summary

| Metric               |                                          Count / Link |
| -------------------- | ----------------------------------------------------: |
| APIs selected        |                                                     3 |
| AI-generated cases   |                                                   105 |
| Human-added cases    |                                                    15 |
| Total designed cases |                                                   120 |
| Executed cases       |                      127 Newman requests in draft run |
| Passed               |                                        173 assertions |
| Failed               |                                         80 assertions |
| Blocked              |                                                   TBD |
| Newman report        |                                    newman/report.html |
| CI passing run       |                         TODO real GitHub Actions link |
| CI failing run       |                         TODO real GitHub Actions link |

## Postman Features Used

- Collections: yes
- Variables: yes, collection and environment variables
- Environments: yes, HW6 local environment
- Data-driven runs: CSV file included for runner compatibility; core coverage is itemized in the collection
- Pre-request scripts: yes, collection-level X-Student-Id injection and console log
- Test scripts: yes, status, schema, token, security, and state assertions
- Monitors / mock servers: not used in local submission draft

## Required Manual Finalization

Replace TODO fields, especially Student ID, before final Newman execution. The current local run used `00000000`, so it is useful execution evidence for debugging but not final anti-cheat evidence. Capture a real Postman console screenshot showing X-Student-Id.
