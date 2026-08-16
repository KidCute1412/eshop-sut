# HW05 - Performance Testing Main Report

- Student: Nguyen Thanh Tien, Student ID 23127539
- SUT: EShop (`https://github.com/ttbhanh/eshop-sut`)
- Repository branch: [KidCute1412/eshop-sut - 23127539-NguyenThanhTien](https://github.com/KidCute1412/eshop-sut/tree/23127539-NguyenThanhTien)
- Workflow: Login -> Search Product -> View Detail -> Add to Cart -> Checkout
- Date used in plan names: 20260815

## Scope

The selected end-to-end workflow exercises all three required backend endpoint groups:

| Group | Endpoint(s) | Purpose in Workflow |
|---|---|---|
| Auth-heavy | `POST /api/login` | Authenticates the virtual user and extracts the JWT token. |
| Read-heavy | `GET /api/products?search=...`, `GET /api/products/:id` | Simulates product search and detail viewing. |
| Transactional | `POST /api/cart`, `POST /api/checkout` | Simulates cart mutation and order creation. |

The workflow is data-driven through [data/workflow-users.csv](data/workflow-users.csv). Each row supplies credentials, search keyword, product ID/name/price, quantity, and shipping address.

## Task 1 - Test Design and Execution

### Generated Test Plans

| Scenario | File | Design Intent | Listener / Report View |
|---|---|---|---|
| Load | [plans/23127539_Load_20260815.jmx](plans/23127539_Load_20260815.jmx) | 20 users, 60s ramp-up, 5 loops, moderate think time. | Summary Report |
| Stress | [plans/23127539_Stress_20260815.jmx](plans/23127539_Stress_20260815.jmx) | 150 users, 30s ramp-up, continuous looping to create sustained pressure until the run is stopped. | Aggregate Report |
| Spike | [plans/23127539_Spike_20260815.jmx](plans/23127539_Spike_20260815.jmx) | 100 users, 5s ramp-up, abrupt burst traffic. | View Results Tree |
| Endurance / Soak | [plans/endurance/23127539_Soak_20260815.jmx](plans/endurance/23127539_Soak_20260815.jmx) | 150 users, sustained run for approximately 10 minutes to estimate an empirical endurance threshold. | Aggregate Report |

The plans include CSV data, HTTP requests for the full workflow, token extraction after login, Authorization header usage for cart and checkout, and response-code assertions.

### Execution Results

The plans were executed with JMeter against the real local backend. Raw `.jtl` logs, generated HTML reports, and resource-monitor screenshots are stored under `reports/HW5/results/` and `reports/HW5/evidence/`.

| Scenario | Raw Log | HTML Report | Evidence Screenshot | Samples | Passed | Failed | Error Rate | Duration | Throughput | Avg | p95 | p99 | Max |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Load | [results/load/load.jtl](results/load/load.jtl) | [results/load/html/index.html](results/load/html/index.html) | [evidence/load/load-run-resource-monitor.png](evidence/load/load-run-resource-monitor.png) | 500 | 500 | 0 | 0.00% | 75.15s | 6.65 samples/s | 4.84ms | 8ms | 11ms | 638ms |
| Stress | [results/stress/stress.jtl](results/stress/stress.jtl) | [results/stress/html/index.html](results/stress/html/index.html) | [evidence/stress/stress-run-resource-monitor.png](evidence/stress/stress-run-resource-monitor.png) | 63,371 | 63,371 | 0 | 0.00% | 149.58s | 423.66 samples/s | 12.66ms | 32ms | 42ms | 597ms |
| Spike | [results/spike/spike.jtl](results/spike/spike.jtl) | [results/spike/html/index.html](results/spike/html/index.html) | [evidence/spike/spike-run-resource-monitor.png](evidence/spike/spike-run-resource-monitor.png) | 1,500 | 1,500 | 0 | 0.00% | 6.34s | 236.59 samples/s | 17.40ms | 41ms | 518ms | 1080ms |
| Endurance / Soak | [results/soak/soak.jtl](results/soak/soak.jtl) | [results/soak/html/index.html](results/soak/html/index.html) | [evidence/endurance/endurance-run-resource-monitor.png](evidence/endurance/endurance-run-resource-monitor.png) | 232,529 | 232,529 | 0 | 0.00% | 599.57s | 387.83 samples/s | 70.04ms | 512ms | 756ms | 1112ms |

Endpoint-level review shows that Checkout is the slowest step under burst and sustained pressure. In the Spike run, Checkout reached p95 = 518ms while the overall p95 was 41ms. In the Endurance / Soak run, Checkout reached p95 = 754ms while the overall p95 was 512ms. This matches the SUT risk that checkout is the transactional SQLite write path.

### Human Review of AI-Generated Design

The first AI-generated JMeter design was useful as a draft, but it was not acceptable for final submission without human review. I reviewed the generated workflow against `README.md`, `setup_guide.md`, `api_specification.md`, and the actual `.jmx` structure, then corrected the following issues:

| Issue in AI / first-pass plan | Why it was wrong or risky | Human correction |
|---|---|---|
| `POST /api/login` did not include `Content-Type: application/json`. | The backend expects JSON request bodies. Without this header, login can fail or be parsed inconsistently, making every later authenticated request invalid. | Added a Header Manager to Login with `Content-Type: application/json`. |
| The Authorization header was generated as `Bearer \${token}` in one draft. | The backslash escapes the JMeter variable and sends the literal string instead of the JWT. Cart and checkout would then return authentication errors, so the test would measure 401 failures instead of performance. | Corrected the header to `Authorization: Bearer ${token}` for Add to Cart and Checkout. |
| Checkout body initially produced invalid JSON such as `"total_amount":,` when the expression was not evaluated correctly. | Invalid JSON would make checkout fail before the backend order-writing path is measured. That would invalidate the transactional part of the workflow. | Replaced it with a JMeter Groovy expression that computes `price * quantity` from CSV values. |
| The report listener was initially renamed only by display text, without changing the real listener type. | HW05 requires three distinct report/listener views. Renaming the label is not equivalent to using a different JMeter listener implementation. | Kept Load as `SummaryReport`, changed Stress to `StatVisualizer` for Aggregate Report, and kept Spike as the View Results Tree style report view. |
| Stress was initially `80 users / 120s ramp-up / 5 loops`. | That setup behaves more like a larger load test than a stress test. It ramps slowly and finishes after a small fixed number of loops, so it may not create sustained backend pressure. | Changed Stress to `150 users / 30s ramp-up / loops = -1`, so it generates sustained pressure until the run is stopped. |
| The AI draft did not explicitly handle account lockout risk. | The SUT locks accounts after repeated failed logins. If invalid credentials are mixed into the performance CSV, later samples can fail because of lockout instead of backend capacity. | Kept normal performance data to valid seeded credentials only and documented lockout as a risk to reset only when intentionally tested. |
| The first design treated checkout as just another POST request. | Checkout is the transactional bottleneck because it writes orders into SQLite. Stress/spike conclusions must consider SQLite write contention and not only read endpoint latency. | Marked checkout as the key transactional step and planned analysis by endpoint label after `.jtl` logs are collected. |

These corrections make the test plans measure the intended end-to-end workflow instead of measuring avoidable scripting errors. The final execution results above are based on raw JMeter `.jtl` logs, not inferred from screenshots.

## Endurance Threshold

The Endurance / Soak test ran for approximately 599.57 seconds, which satisfies the 10-minute lower bound. Based on this run, the empirical threshold observed on the local machine is:

- Sustained load: 150 virtual users.
- Workflow throughput: approximately 387.83 samples/s across all request labels.
- Overall latency: average 70.04ms, p95 512ms, p99 756ms.
- Reliability: 232,529 / 232,529 samples passed, 0.00% error rate.
- Bottleneck: Checkout, with average 221.47ms and p95 754ms.

This threshold is empirical for the local test environment only. It should not be generalized to production hardware without rerunning the same plan in that environment.

## Task 2 - AI Analysis and Misinterpretation Hunt

See the full Task 2 analysis in [task2-ai-analysis.md](task2-ai-analysis.md).

The raw `.jtl` logs were analysed with AI, then independently reviewed against computed metrics. The main AI-generated conclusion was that all scenarios completed successfully with 0.00% error rate. Human review refined that conclusion because "success=true" does not mean there is no performance risk.

Key reviewed values:

| Scenario | Samples | Error Rate | Avg | Median | p95 | p99 | Human Interpretation |
|---|---:|---:|---:|---:|---:|---:|---|
| Load | 500 | 0.00% | 4.84ms | 3ms | 8ms | 11ms | Stable baseline. |
| Stress | 63,371 | 0.00% | 12.66ms | 10ms | 32ms | 42ms | Stable sustained pressure. |
| Spike | 1,500 | 0.00% | 17.40ms | 4ms | 41ms | 518ms | Tail latency appears during burst traffic. |
| Endurance / Soak | 232,529 | 0.00% | 70.04ms | 12ms | 512ms | 756ms | Sustained run passed, but checkout tail latency is visible. |

Human misinterpretation fixes:

- Do not confuse low average latency with p95/p99 tail latency.
- Do not treat 0.00% error rate as proof that there is no bottleneck.
- Report throughput as `samples/s`, not `users/s` or completed orders/s.
- Limit the endurance threshold to the local environment: 150 VUs for approximately 599.57s, 0.00% errors, overall p95 = 512ms.
- Keep recommendations grounded in Node.js + SQLite; avoid unrelated production-scale architecture suggestions.

## Task 3 - Continuous Performance Testing Proposal

See [proposal/continuous-performance-testing.md](task3-continuous-performance-testing.md).

## Agent Skill

A reusable Agent Skill was created at `.agents/skills/performance-testing/`. It captures the HW05 workflow, integrity rules, endpoint mapping, JMeter guidance, analysis checklist, and continuous-testing proposal guidance.

The purpose of this skill is to make the AI assistant follow an auditable performance-testing workflow instead of generating a generic test report. It requires the agent to read the assignment and EShop documentation first, then map the selected workflow to the required endpoint groups: `POST /api/login` for auth-heavy traffic, product search/detail endpoints for read-heavy traffic, and cart/checkout endpoints for transactional traffic.

The skill also defines the evidence rules used in this submission. It explicitly prevents the AI from claiming p95, throughput, endurance thresholds, screenshots, HTML reports, or GitHub Issues unless those artifacts exist. This was important because the first generated JMeter plans were only scripts, not execution evidence. Real conclusions were written only after `.jtl` logs, HTML reports, and resource screenshots were available.

In practice, the skill helped guide three parts of the work:

- Test design: choosing JMeter, CSV-driven data, token extraction, Authorization headers, response assertions, and distinct report views for Load, Stress, and Spike.
- Human review: checking AI mistakes such as missing `Content-Type`, escaped `Bearer \${token}`, invalid checkout JSON, weak stress configuration, and missing account-lockout consideration.
- Result analysis: analysing raw JTL metrics, separating average latency from p95/p99 tail latency, reporting throughput as `samples/s`, and keeping optimization recommendations grounded in the local Node.js + SQLite SUT.

This made the AI useful as a structured assistant while keeping the final testing judgment under human review.

## AI Audit and Critique

- AI audit: [ai-audit.md](ai-audit.md)
- AI critique: [ai-critique.md](ai-critique.md)
