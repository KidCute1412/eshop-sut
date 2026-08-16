# AI Audit - HW05 Performance Testing

## Declaration

I used AI assistance during HW05 to create a reusable performance-testing Agent Skill, design JMeter plans, review the generated plans, analyse real JMeter logs, and write the final performance interpretation. I did not use AI to fabricate execution results. All performance metrics reported in this submission are based on real `.jtl` files generated from JMeter runs.

## Interaction 1 - Create a Reusable Agent Skill

- AI tool: Codex
- Date/time: 2026-08-15, Asia/Saigon

### Prompt

```text
Read the HW05 Performance Testing assignment carefully before doing any implementation.

You must first create a reusable Agent Skill for this homework, similar in style to the skills used in my previous homework submissions. The skill should help an AI testing agent perform HW05 correctly and audibly. It must cover:

1. The exact assignment scope for performance testing.
2. The selected EShop workflow: Login -> Search Product -> View Detail -> Add to Cart -> Checkout.
3. How to map the workflow to auth-heavy, read-heavy, and transactional endpoint groups.
4. How to design JMeter Load, Stress, Spike, and Endurance / Soak tests.
5. How to keep the workflow data-driven with CSV data.
6. How to generate correctly named JMeter plans using my student ID and date.
7. How to collect real evidence: raw JTL files, HTML reports, screenshots, hardware evidence, and Git log.
8. How to prevent fabricated results.
9. How to perform AI analysis and human misinterpretation review for Task 2.
10. How to package the final report, README, AI audit, AI critique, bug report, and proposal.

Before creating the skill, read these project files as source of truth:
- HW05_Performance_Testing_En.md
- README.md
- setup_guide.md
- api_specification.md

After reading, create the skill under `.agents/skills/performance-testing/` with a complete `SKILL.md` and supporting references. Keep the instructions specific to this EShop backend and do not invent any test execution evidence.
```

### Raw Output

```text
Created a reusable HW05 Agent Skill at `.agents/skills/performance-testing/`.

The skill is named `performance-testing` and its description is:
"Guides an AI testing agent through auditable HW05 Performance Testing for EShop using JMeter or k6. Use when designing, reviewing, executing, analysing, and reporting Load, Stress, Spike, and Endurance tests for backend API workflows such as Login to Search Product to View Detail to Add to Cart to Checkout, with CSV data, real JTL/raw logs, HTML reports, resource evidence, AI audit, AI critique, Git log, and no-fabrication safeguards."

The skill defines the default workflow:
Login -> Search Product -> View Detail -> Add to Cart -> Checkout

The skill requires the AI agent to read:
- HW05_Performance_Testing_En.md
- README.md
- setup_guide.md
- api_specification.md

The skill includes integrity rules:
- Do not fabricate JMeter/k6 runs.
- Do not fabricate `.jtl` rows, HTML reports, screenshots, hardware specs, video links, GitHub issues, or Git commits.
- Use raw logs for performance conclusions.
- Treat database reset as deliberate test setup.
- Preserve raw evidence.

The skill defines the HW05 phases:
1. Scope, tooling, and environment.
2. Workflow mapping to endpoint groups.
3. AI-assisted test-plan design.
4. CSV-driven data setup.
5. JMeter plan generation.
6. Human review and gap analysis.
7. Real execution and evidence collection.
8. Log analysis and misinterpretation hunt.
9. Bug/performance issue reporting.
10. Demo video.
11. AI audit, AI critique, and continuous testing.
12. Final assembly.

The skill also explains the endpoint mapping:
- Auth-heavy: POST /api/login
- Read-heavy: GET /api/products?search=<keyword>, GET /api/products/:id
- Transactional: POST /api/cart, POST /api/checkout

The skill requires generated plans named:
- <StudentID>_Load_<YYYYMMDD>.jmx
- <StudentID>_Stress_<YYYYMMDD>.jmx
- <StudentID>_Spike_<YYYYMMDD>.jmx

The skill instructs the agent to collect:
- Raw `.jtl` logs.
- HTML report folders.
- Tool/resource-monitor screenshots.
- Hardware evidence.
- AI audit and critique.
- Bug report.
- Continuous performance-testing proposal.
- Git commit log.

The skill was validated and is ready to guide HW05 work.
```

### Human Review / Correction

The initial skill structure was acceptable because it captured the assignment workflow, evidence requirements, and no-fabrication safeguards. I later refined the workflow references to make the EShop-specific risks explicit: login lockout, JWT extraction, SQLite checkout writes, and the need to distinguish samples/s from completed orders/s.

## Interaction 2 - Generate the Initial Performance-Test Design and JMeter Plans

- AI tool: Codex
- Date/time: 2026-08-15, Asia/Saigon

### Prompt

```text
Use the new `performance-testing` Agent Skill to design HW05 performance tests for the EShop backend.

The required workflow is:
Login -> Search Product -> View Detail -> Add to Cart -> Checkout

Use JMeter as the main tool. The test design must satisfy these conditions:

1. All plans must exercise the same end-to-end workflow.
2. The workflow must cover all three required endpoint groups:
   - Auth-heavy: login.
   - Read-heavy: product search and product detail.
   - Transactional: cart mutation and checkout.
3. Use CSV-driven test data for credentials, product ID, product name, price, quantity, and shipping address.
4. Use seeded valid user credentials only for normal performance runs to avoid account lockout distorting the result.
5. Generate JMeter plans with the required naming convention:
   - 23127539_Load_20260815.jmx
   - 23127539_Stress_20260815.jmx
   - 23127539_Spike_20260815.jmx
6. Use three distinct JMeter listener/report views across the three main plans.
7. Include token extraction after Login and use the token in Authorization headers for Add to Cart and Checkout.
8. Include response assertions so failed functional requests are visible in the JTL output.
9. Do not claim that any plan has been executed unless real JMeter JTL logs exist.

After generating the draft plans, review them against the assignment and explain what still needs human correction before final execution.
```

### Raw Output

```text
Generated the initial HW05 performance-testing structure under `reports/HW5/`.

Created data file:
- reports/HW5/data/workflow-users.csv

The CSV columns are:
email,password,search,product_id,product_name,price,quantity,shipping_address

The CSV uses seeded valid credentials:
test@eshop.com / Test1234!

Mapped workflow:
1. Login:
   POST http://localhost:3000/api/login
   Body contains email and password from CSV.
   A JSON extractor reads the JWT token from the response.

2. Search Product:
   GET http://localhost:3000/api/products?search=${search}
   This is the first read-heavy endpoint.

3. View Detail:
   GET http://localhost:3000/api/products/${product_id}
   This is the second read-heavy endpoint.

4. Add to Cart:
   POST http://localhost:3000/api/cart
   Uses Authorization: Bearer ${token}
   Body contains product_id and quantity.

5. Checkout:
   POST http://localhost:3000/api/checkout
   Uses Authorization: Bearer ${token}
   Body contains shipping_address and total_amount.

Created JMeter plans:
- reports/HW5/plans/23127539_Load_20260815.jmx
- reports/HW5/plans/23127539_Stress_20260815.jmx
- reports/HW5/plans/23127539_Spike_20260815.jmx

Initial workload design:
- Load: 20 users, 60-second ramp-up, 5 loops, moderate think time.
- Stress: initial draft used 80 users, 120-second ramp-up, 5 loops.
- Spike: 100 users, 5-second ramp-up, abrupt traffic burst.

Initial listener/report-view design:
- Load used Summary Report.
- Stress was intended to use Aggregate Report.
- Spike used a View Results Tree style listener for detailed request inspection.

Created helper scripts:
- reports/HW5/scripts/generate-jmeter-plans.js
- reports/HW5/scripts/analyze-jtl.js
- reports/HW5/scripts/perf-runner.js

Created report scaffolding:
- reports/HW5/README.md
- reports/HW5/main-report.md
- reports/HW5/ai-audit.md
- reports/HW5/ai-critique.md
- reports/HW5/bug-report.md
- reports/HW5/proposal/continuous-performance-testing.md
- reports/HW5/demo-video-script.md

Important warning:
The generated plans are not execution evidence. Real `.jtl` files, HTML reports, and screenshots must be produced by running JMeter against the real backend.
```

### Human Review / Correction

The first generated plan was only a draft. I reviewed it against `README.md`, `setup_guide.md`, `api_specification.md`, and the actual `.jmx` structure, then corrected the following issues:

| AI / Draft Issue | Why It Was Wrong | Human Correction |
|---|---|---|
| Login did not consistently include `Content-Type: application/json`. | The backend expects JSON request bodies. If the header is missing, login may fail and all later authenticated requests become invalid. | Added `Content-Type: application/json` to JSON POST requests. |
| Authorization header appeared as `Bearer \${token}` in one draft. | The backslash escapes the JMeter variable and sends a literal string instead of the JWT. | Corrected it to `Authorization: Bearer ${token}`. |
| Checkout body could generate invalid JSON such as `"total_amount":,`. | Invalid JSON would test request construction failure, not checkout performance. | Computed `total_amount` using a JMeter expression based on CSV price and quantity. |
| Listener was sometimes only renamed by label. | Renaming a listener is not the same as using a distinct listener/report view. | Used distinct JMeter listener types/views for Load, Stress, and Spike. |
| Stress draft used `80 users / 120s ramp-up / 5 loops`. | That behaves more like a finite larger load test, not sustained stress. | Changed Stress to `150 users / 30s ramp-up / continuous looping`. |
| Account lockout risk was not explicit. | Invalid credentials can lock accounts and distort performance results. | Kept normal performance CSV rows valid and documented lockout risk. |
| Checkout was treated as just another POST. | Checkout writes to SQLite and is likely the transactional bottleneck. | Marked Checkout as the key endpoint to inspect in Stress, Spike, and Endurance / Soak. |

## Interaction 3 - Execution Integrity Check Before Real Runs

- AI tool: Codex
- Date/time: 2026-08-15, Asia/Saigon

### Prompt

```text
Check whether this workspace can execute the HW05 performance tests directly.

Please verify:
1. Whether JMeter is installed and available from PATH.
2. Whether k6 is installed and available from PATH.
3. Whether the backend can be safely started from this Codex session.
4. Whether real `.jtl` result logs or HTML reports already exist.

Important constraints:
- Do not fabricate execution results.
- If JMeter/k6 is unavailable, say exactly what is missing.
- If starting the backend may reset or destroy local data, stop and document the risk instead of silently running it.
- The report should clearly distinguish generated test plans from real execution evidence.
```

### Raw Output

```text
Checked local performance tool availability.

Command attempted:
jmeter -v

Result:
JMeter was not available from PATH in the Codex execution environment.

Command attempted:
k6 version

Result:
k6 was not available from PATH in the Codex execution environment.

Backend startup review:
The backend database initialization flow includes destructive reset behavior that drops and recreates local tables. Starting or resetting the backend inside this session could overwrite local data. Because of that, the backend was not started automatically.

Evidence status at that time:
- JMeter plans existed.
- CSV data existed.
- Report scaffolding existed.
- Real `.jtl` logs were not available yet.
- JMeter HTML report folders were not available yet.
- Resource-monitor screenshots were not available yet.
- Endurance threshold could not be claimed yet.

Conclusion:
The report must mark execution evidence as pending until the human runs JMeter locally and provides real results.
```

### Human Review / Correction

This output was correct at the time because the Codex environment could not run JMeter/k6 directly. I later ran the plans manually outside that limitation, saved the real `.jtl` logs and HTML reports, and then updated the report with actual values. This prevents confusing generated plan files with real performance evidence.

## Interaction 4 - Post-Execution Evidence Review and Report Update

- AI tool: Codex
- Date/time: 2026-08-16, Asia/Saigon

### Prompt

```text
I have now run the HW05 JMeter plans manually.

The raw result logs are stored under `reports/HW5/results/`, and the screenshots are stored under `reports/HW5/evidence/`.

Please do the following carefully:

1. Inspect the available result folders and evidence folders.
2. Rename the PNG screenshots so their filenames clearly match their scenarios.
3. Analyse the real `.jtl` files instead of using estimated values.
4. Update the report so it no longer says execution is pending.
5. Include Load, Stress, Spike, and Endurance / Soak results.
6. Do not invent any missing data.
7. If a result folder uses the name `soak` but the assignment calls it Endurance, explain the naming clearly instead of hiding it.
8. If all samples passed, do not create a fake bug report. Instead, report any performance bottleneck as an observation.

Use the workflow Login -> Search Product -> View Detail -> Add to Cart -> Checkout.
```

### Raw Output

```text
Inspected result folders:
- reports/HW5/results/load/load.jtl
- reports/HW5/results/load/html/index.html
- reports/HW5/results/stress/stress.jtl
- reports/HW5/results/stress/html/index.html
- reports/HW5/results/spike/spike.jtl
- reports/HW5/results/spike/html/index.html
- reports/HW5/results/soak/soak.jtl
- reports/HW5/results/soak/html/index.html

Inspected evidence folders and renamed screenshots:
- reports/HW5/evidence/load/load-run-resource-monitor.png
- reports/HW5/evidence/stress/stress-run-resource-monitor.png
- reports/HW5/evidence/spike/spike-run-resource-monitor.png
- reports/HW5/evidence/endurance/endurance-run-resource-monitor.png

Computed JTL metrics:

Load:
- Samples: 500
- Passed: 500
- Failed: 0
- Error rate: 0.00%
- Duration: 75.15s
- Throughput: 6.65 samples/s
- Average: 4.84ms
- Min: 1ms
- Max: 638ms
- p90: 7ms
- p95: 8ms
- p99: 11ms
- Slowest important endpoint: 05 Checkout, average 13.15ms, p95 10ms

Stress:
- Samples: 63,371
- Passed: 63,371
- Failed: 0
- Error rate: 0.00%
- Duration: 149.58s
- Throughput: 423.66 samples/s
- Average: 12.66ms
- Min: 0ms
- Max: 597ms
- p90: 27ms
- p95: 32ms
- p99: 42ms
- Slowest important endpoint: 05 Checkout, average 18.81ms, p95 38ms

Spike:
- Samples: 1,500
- Passed: 1,500
- Failed: 0
- Error rate: 0.00%
- Duration: 6.34s
- Throughput: 236.59 samples/s
- Average: 17.40ms
- Min: 0ms
- Max: 1080ms
- p90: 17ms
- p95: 41ms
- p99: 518ms
- Slowest important endpoint: 05 Checkout, average 66.20ms, p95 518ms

Endurance / Soak:
- Samples: 232,529
- Passed: 232,529
- Failed: 0
- Error rate: 0.00%
- Duration: 599.57s
- Throughput: 387.83 samples/s
- Average: 70.04ms
- Min: 0ms
- Max: 1112ms
- p90: 198ms
- p95: 512ms
- p99: 756ms
- Slowest important endpoint: 05 Checkout, average 221.47ms, p95 754ms

Report updates:
- Updated `main-report.md` with real execution results.
- Updated `README.md` with result links and endurance threshold.
- Updated `bug-report.md` to avoid claiming a fake bug.
- Added the observation that Checkout is the main bottleneck candidate under Spike and Endurance / Soak.
- Kept the actual result folder name `soak` but labelled the scenario as `Endurance / Soak` in the report.

Validation:
The HW05 validator passed after keeping only the three required Load/Stress/Spike plans in the top-level plans folder and moving the Soak plan under `plans/endurance/`.
```

### Human Review / Correction

I accepted the computed values because they came from raw `.jtl` files. I corrected the interpretation in two ways. First, I did not report throughput as completed orders/s because the number is calculated from all JMeter samples, and each workflow iteration contains multiple requests. Second, I did not file a GitHub bug because all samples passed; Checkout was documented as a performance observation rather than a confirmed defect.

## Interaction 5 - Task 2 AI Log Analysis and Misinterpretation Hunt

- AI tool: Codex
- Date/time: 2026-08-16, Asia/Saigon

### Prompt

```text
Act as a performance-testing assistant for Task 2 of HW05.

Analyse the raw JMeter `.jtl` logs for the EShop workflow:
Login -> Search Product -> View Detail -> Add to Cart -> Checkout.

Input files:
- reports/HW5/results/load/load.jtl
- reports/HW5/results/stress/stress.jtl
- reports/HW5/results/spike/spike.jtl
- reports/HW5/results/soak/soak.jtl

For each scenario, compute and report:
1. Total samples.
2. Passed samples.
3. Failed samples.
4. Error rate.
5. Test duration based on JTL timestamps.
6. Throughput in samples per second.
7. Average response time.
8. Median response time.
9. p90 response time.
10. p95 response time.
11. p99 response time.
12. Maximum response time.
13. Slowest endpoint label by p95.

Then provide:
- A suggested empirical endurance threshold.
- A bottleneck hypothesis.
- A list of optimization recommendations.

After that, perform a human-style misinterpretation review. Specifically check whether the AI analysis:
- Confuses average latency with p95/p99.
- Treats 0.00% error rate as proof that there is no performance problem.
- Uses the wrong throughput unit.
- Generalizes local-machine results to production capacity.
- Misses the fact that Checkout writes to SQLite.
- Suggests infrastructure that does not exist in this local Node.js + SQLite SUT.

Do not fabricate missing evidence. Use only numbers that can be computed from the raw JTL files.
```

### Raw Output

```text
Analysed raw JTL logs for Load, Stress, Spike, and Endurance / Soak.

Scenario summary:

| Scenario | Samples | Passed | Failed | Error Rate | Duration | Throughput | Avg | Median | p90 | p95 | p99 | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Load | 500 | 500 | 0 | 0.00% | 75.15s | 6.65 samples/s | 4.84ms | 3ms | 7ms | 8ms | 11ms | 638ms |
| Stress | 63,371 | 63,371 | 0 | 0.00% | 149.58s | 423.66 samples/s | 12.66ms | 10ms | 27ms | 32ms | 42ms | 597ms |
| Spike | 1,500 | 1,500 | 0 | 0.00% | 6.34s | 236.59 samples/s | 17.40ms | 4ms | 17ms | 41ms | 518ms | 1080ms |
| Endurance / Soak | 232,529 | 232,529 | 0 | 0.00% | 599.57s | 387.83 samples/s | 70.04ms | 12ms | 198ms | 512ms | 756ms | 1112ms |

Endpoint-level bottleneck:

| Scenario | Slowest Endpoint by p95 | Endpoint Average | Endpoint p95 |
|---|---|---:|---:|
| Load | 05 Checkout | 13.15ms | 10ms |
| Stress | 05 Checkout | 18.81ms | 38ms |
| Spike | 05 Checkout | 66.20ms | 518ms |
| Endurance / Soak | 05 Checkout | 221.47ms | 754ms |

Interpretation:
- All scenarios completed with 0 failed samples and 0.00% error rate.
- Load is stable and suitable as a baseline.
- Stress stayed functionally stable at high sample volume.
- Spike exposed tail-latency risk: average was only 17.40ms, but p99 rose to 518ms and max reached 1080ms.
- Endurance / Soak sustained 150 virtual users for about 599.57 seconds with 0.00% error rate.
- Checkout is the main bottleneck candidate because it has the highest p95 under Spike and Endurance / Soak.

Suggested empirical endurance threshold:
- Local threshold: 150 virtual users for approximately 599.57 seconds.
- Reliability at threshold: 0.00% error rate.
- Overall latency at threshold: average 70.04ms, p95 512ms, p99 756ms.
- Throughput at threshold: 387.83 samples/s.
- Important limitation: this is a local-machine threshold, not a production guarantee.

Bottleneck hypothesis:
Checkout likely becomes slower under burst and sustained pressure because it is the transactional path. It performs authenticated cart/order work and writes checkout/order data to SQLite. Read-heavy endpoints stay much faster than Checkout in the observed runs.

Optimization recommendations:
1. Investigate the checkout database write path.
2. Review SQLite journal mode and consider WAL mode for local write concurrency.
3. Check whether cart/order/product lookup queries need indexes.
4. Repeat Spike and Endurance / Soak after any database or checkout change.
5. Avoid production-scale recommendations such as Kubernetes autoscaling, Kafka, Redis cluster, or CDN unless the SUT architecture actually changes.

Misinterpretation review:
- Do not rely on average latency alone. Spike average is 17.40ms, but p99 is 518ms.
- Do not say there is no performance risk only because error rate is 0.00%.
- Throughput is samples/s, not users/s and not orders/s.
- The Endurance / Soak threshold only applies to this local environment.
- Checkout should be analysed separately because it is the SQLite write path.
- Infrastructure recommendations must match the actual Node.js + SQLite SUT.
```

### Human Review / Correction

The raw AI analysis was useful, but I corrected the conclusion before putting it into the final report:

| AI Analysis Risk | Human Review Correction |
|---|---|
| "All samples passed" could be misread as "no performance concern." | I reported 0.00% error rate separately from bottleneck risk. Checkout still has high p95/p99 under Spike and Endurance / Soak. |
| Average latency can hide tail latency. | I emphasized p95 and p99 in Task 2. Spike average is 17.40ms, but p99 is 518ms. |
| Throughput can be mislabeled. | I used `samples/s`, not orders/s, because each user workflow creates multiple HTTP samples. |
| Endurance result can be overgeneralized. | I described the threshold as local and empirical only. |
| AI could recommend unrelated infrastructure. | I kept feasible recommendations to Node.js + SQLite: checkout write path, WAL mode evaluation, and query/index review. |

Final Task 2 conclusion: the SUT passed all observed requests with 0.00% error rate, but Checkout is the clearest performance bottleneck candidate because its p95 increases sharply during Spike and Endurance / Soak.

## Interaction 6 - Hardware Evidence Completion

- AI tool: Codex
- Date/time: 2026-08-16, Asia/Saigon

### Prompt

```text
I have added a hardware evidence screenshot under `reports/HW5/evidence/hardware/`.

Please inspect the image, rename the PNG file to a meaningful name, and rewrite `hardware-spec.md`.

Use only information visible in the screenshot or available from safe local commands. Do not guess missing hardware details. If a value is truncated in the screenshot, say that it is truncated.

The hardware evidence should include:
- Screenshot filename.
- Hostname and user.
- CPU.
- RAM.
- Memory speed.
- Storage type.
- GPU information visible in the screenshot.
- OS version if it can be obtained locally.
- A short note explaining the source of each value.
```

### Raw Output

```text
Inspected hardware evidence folder.

Found screenshot:
- Screenshot 2026-08-16 134535.png

Renamed screenshot to:
- reports/HW5/evidence/hardware/hardware-task-manager-performance.png

Read visible information from Task Manager screenshot:
- RAM: 16.0 GB installed, 15.8 GB usable.
- Memory speed: 2933 MT/s.
- Memory form factor: SODIMM.
- Memory slots used: 2 of 8.
- Storage: Disk 0 (C:, E:) - SSD (NVMe).
- GPU 0: Intel(R) UHD Graphics.
- GPU 1: NVIDIA GeForce GTX series, exact suffix truncated in screenshot.

Collected safe local command information:
- hostname: DESKTOP-QMOKU4T
- whoami: desktop-qmoku4t\acer
- CPU: 11th Gen Intel(R) Core(TM) i5-11400H @ 2.70GHz
- OS: Microsoft Windows 10.0.22631, X64

Rewrote `reports/HW5/evidence/hardware/hardware-spec.md` with:
- Evidence file link.
- Machine identity.
- Hardware / environment summary table.
- Notes explaining that the screenshot is from Task Manager Performance view and that CPU/OS were collected from safe local commands because the screenshot did not show the full CPU model.
```

### Human Review / Correction

The screenshot showed the Memory panel, not the full CPU details. Therefore, I did not infer the CPU model from the screenshot. I accepted CPU and OS values only because they were collected from safe local commands, and I marked the truncated NVIDIA GPU suffix as truncated instead of inventing the exact model.
