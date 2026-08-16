# HW05 - Performance Testing - Submission README

- Student: Nguyen Thanh Tien, Student ID 23127539
- SUT: EShop (`https://github.com/ttbhanh/eshop-sut`)
- Working repository / branch: [KidCute1412/eshop-sut - 23127539-NguyenThanhTien](https://github.com/KidCute1412/eshop-sut/tree/23127539-NguyenThanhTien)
- Workflow: Login -> Search Product -> View Detail -> Add to Cart -> Checkout
- Tooling: JMeter test plans with raw `.jtl` logs and generated HTML reports.
- Demo video: Pending real recording
- Agent Skill demo video: Pending real recording

## Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
|---:|---|---:|---:|
| 1 | Task 1 - Load testing | 20 | 20 |
| 2 | Task 1 - Stress testing | 20 | 20 |
| 3 | Task 1 - Spike testing | 20 | 20 |
| 4 | Task 2 - AI analysis + misinterpretation hunt | 10 | 10 |
| 5 | Task 3 - Continuous Performance Testing proposal | 10 | 10 |
| 6 | Agent Skills | 10 | 5 |
|  | **Total** | **100** | **95** |

## Test Summary Report

- Scenarios executed: Load, Stress, Spike, plus Endurance / Soak threshold run.
- Endpoint groups covered:
  - Auth-heavy: `POST /api/login`
  - Read-heavy: `GET /api/products?search=...`, `GET /api/products/:id`
  - Transactional: `POST /api/cart`, `POST /api/checkout`
- CSV data: [data/workflow-users.csv](data/workflow-users.csv)
- JMeter plans:
  - [plans/23127539_Load_20260815.jmx](plans/23127539_Load_20260815.jmx)
  - [plans/23127539_Stress_20260815.jmx](plans/23127539_Stress_20260815.jmx)
  - [plans/23127539_Spike_20260815.jmx](plans/23127539_Spike_20260815.jmx)
  - [plans/endurance/23127539_Soak_20260815.jmx](plans/endurance/23127539_Soak_20260815.jmx)
- Execution status: Real JMeter results are available for all four runs.
- Endurance threshold: 150 virtual users sustained for approximately 599.57s with 0.00% error rate, 70.04ms average, 512ms p95, 756ms p99, and approximately 387.83 samples/s.
- Task 2 AI analysis: [task2-ai-analysis.md](task2-ai-analysis.md)
- Bugs / performance issues: No failed samples were observed. Checkout is the slowest endpoint under Spike and Endurance / Soak.

## Results Index

| Scenario | Raw Log | HTML Report | Evidence |
|---|---|---|---|
| Load | [results/load/load.jtl](results/load/load.jtl) | [results/load/html/index.html](results/load/html/index.html) | [evidence/load/load-run-resource-monitor.png](evidence/load/load-run-resource-monitor.png) |
| Stress | [results/stress/stress.jtl](results/stress/stress.jtl) | [results/stress/html/index.html](results/stress/html/index.html) | [evidence/stress/stress-run-resource-monitor.png](evidence/stress/stress-run-resource-monitor.png) |
| Spike | [results/spike/spike.jtl](results/spike/spike.jtl) | [results/spike/html/index.html](results/spike/html/index.html) | [evidence/spike/spike-run-resource-monitor.png](evidence/spike/spike-run-resource-monitor.png) |
| Endurance / Soak | [results/soak/soak.jtl](results/soak/soak.jtl) | [results/soak/html/index.html](results/soak/html/index.html) | [evidence/endurance/endurance-run-resource-monitor.png](evidence/endurance/endurance-run-resource-monitor.png) |

## Deliverables Index

- Main report: [main-report.md](main-report.md)
- Task 2 AI analysis and human review: [task2-ai-analysis.md](task2-ai-analysis.md)
- AI audit: [ai-audit.md](ai-audit.md)
- AI critique: [ai-critique.md](ai-critique.md)
- Bug/performance issue report: [bug-report.md](bug-report.md)
- Continuous performance-testing proposal: [proposal/continuous-performance-testing.md](proposal/continuous-performance-testing.md)
- Data: [data/workflow-users.csv](data/workflow-users.csv)
- Plans: [plans/](plans/)
- Scripts: [scripts/](scripts/)
- Hardware evidence: [evidence/hardware/hardware-spec.md](evidence/hardware/hardware-spec.md)
- Agent Skill: `.agents/skills/performance-testing/`
