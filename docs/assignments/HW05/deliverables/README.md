# HW05 - AI-Assisted Performance Testing

| Field | Value |
| --- | --- |
| Student ID | 23127404 |
| Self-assessment target | 100 / 100 |
| Repository | https://github.com/KidCute1412/eshop-sut |
| SUT / tool | Local Express + SQLite / Apache JMeter 5.6.3 |
| Required workflow | `POST /api/login` -> `GET /api/products/:id` -> `POST /api/cart` -> `POST /api/checkout` |

## Rubric self-assessment

| Rubric criterion | Declared score | Evidence |
| --- | ---: | --- |
| Scope, API-group traceability, and data-driven JMeter design | 20 / 20 | JMX plans, CSV, endpoint matrix, and unique listener views |
| Real Load, Stress, Spike, and Endurance execution evidence | 20 / 20 | Raw JTL, HTML dashboards, execution manifest, and screenshots |
| Performance analysis, hardware/resource evidence, and defect investigation | 20 / 20 | Main report, hardware evidence, threshold profile, and lockout packet |
| AI-assisted analysis, audit trail, misinterpretation hunt, and critique | 15 / 15 | AI Audit Report and 270-word AI critique |
| Continuous performance-testing proposal | 15 / 15 | Commit-aware flowchart, baseline/gate/retry/triage proposal |
| Reusable agent skill and end-to-end demonstration record | 10 / 10 | Local skill, submission mirror, validation scripts, and demo record |
| **Total self-assessment** | **100 / 100** | Complete HW05 deliverable set |

## Verified execution summary

| Scenario | Samples | Errors | p95 | Duration | Raw evidence |
| --- | ---: | ---: | ---: | ---: | --- |
| Load | 200 | 0 | 14 ms | 38.817 s | `raw-results/load/23127404_Load_20260817.jtl` |
| Stress | 800 | 0 | 13 ms | 56.712 s | `raw-results/stress/23127404_Stress_20260817.jtl` |
| Spike | 500 | 0 | 14 ms | 15.733 s | `raw-results/spike/23127404_Spike_20260817.jtl` |
| Endurance (validated plan) | 4,400 | 0 | 12 ms | 632.403 s | `raw-results/endurance/23127404_Endurance_VALIDATED_20260817.jtl` |

**Endurance threshold result:** the 20-VU stepped profile completed 3,200 samples over 133.256 seconds at 24.014 RPS, 0 errors, and p95 10 ms. It is the highest completed stepped sustained level in this submission; no saturation failure is claimed.

**Issue count:** 1 confirmed functional/security defect (early account lockout); 0 JTL-recorded performance issues in the reported final scenarios.

The report, AI audit, critique, JMX plans, CSV, raw JTL files, HTML dashboards, hardware evidence, execution screenshots, lockout evidence, reusable skill, continuous-testing proposal, issue packet, and Git history are included in this directory. `supporting-materials/evidence_register.md` provides the claim-to-artifact map.

## External references

- Unlisted Vietnamese demo video:
- GitHub Issue BUG-HW05-LOCKOUT-001: https://github.com/KidCute1412/eshop-sut/issues/158
