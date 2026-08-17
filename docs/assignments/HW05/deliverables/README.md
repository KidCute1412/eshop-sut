# HW05 — AI-Assisted Performance Testing

| Field | Value |
| --- | --- |
| Student ID | 23127404 |
| Self-assessment target | 100 / 100 |
| Repository | https://github.com/KidCute1412/eshop-sut |
| SUT / tool | Local Express + SQLite / Apache JMeter 5.6.3 |
| Required workflow | `POST /api/login` → `GET /api/products/:id` → `POST /api/cart` → `POST /api/checkout` |

## Verified execution summary

| Scenario | Samples | Errors | p95 | Duration | Raw evidence |
| --- | ---: | ---: | ---: | ---: | --- |
| Load | 200 | 0 | 14 ms | 38.817 s | `raw-results/load/23127404_Load_20260817.jtl` |
| Stress | 800 | 0 | 13 ms | 56.712 s | `raw-results/stress/23127404_Stress_20260817.jtl` |
| Spike | 500 | 0 | 14 ms | 15.733 s | `raw-results/spike/23127404_Spike_20260817.jtl` |
| Endurance | 4,400 | 0 | 12 ms | 640.194 s | `raw-results/endurance/23127404_Endurance_20260817.jtl` |

The report, AI audit, critique, JMX plans, CSV, raw JTL files, HTML dashboards, hardware evidence, execution screenshots, lockout evidence, reusable skill, continuous-testing proposal, issue packet, and Git history are included in this directory. `supporting-materials/evidence_register.md` provides the claim-to-artifact map.

## External links to complete before submission

- Unlisted Vietnamese demo video: **[STUDENT_TO_PASTE_YOUTUBE_URL]**
- GitHub Issue BUG-HW05-LOCKOUT-001: **[STUDENT_TO_PASTE_GITHUB_ISSUE_URL]**
