---
name: performance-testing
description: Guides an AI testing agent through auditable HW05 Performance Testing for EShop using JMeter or k6. Use when designing, reviewing, executing, analysing, and reporting Load, Stress, Spike, and Endurance tests for backend API workflows such as Login to Search Product to View Detail to Add to Cart to Checkout, with CSV data, real JTL/raw logs, HTML reports, resource evidence, AI audit, AI critique, Git log, and no-fabrication safeguards.
---

# AI-Assisted Performance Testing

Use this skill for HW05 Performance Testing. It guides an AI testing agent through the complete
EShop performance workflow: selecting backend endpoint groups, designing Load/Stress/Spike plans,
making the workflow CSV-driven, executing real runs, collecting evidence, analysing `.jtl` logs,
reviewing AI misinterpretations, and packaging the final report.

The default workflow for this repository is:

`Login -> Search Product -> View Detail -> Add to Cart -> Checkout`

## Required References

Read these first, in this order, because they are the assignment and SUT source of truth:

- `HW05_Performance_Testing_En.md`
- `README.md`
- `setup_guide.md`
- `api_specification.md`

Then read the skill references as needed:

- `references/instructor-clarifications.md` before deciding what can be claimed as complete.
- `references/assignment-requirements.md` for HW05 scope, required artifacts, grading, and
  anti-cheat constraints.
- `references/eshop-analysis-guide.md` for ports, accounts, endpoint mapping, seed-data risk, and
  workflow-specific SUT notes.
- `references/performance-method.md` before designing Load/Stress/Spike/Endurance workloads.
- `references/jmeter-k6-guidance.md` before creating or running JMeter/k6 plans.
- `references/data-driven-workflow.md` before writing CSV data or request variables.
- `references/reporting-and-evidence.md` before claiming final execution evidence.
- `references/ai-analysis-review.md` before writing AI analysis, misinterpretation review, and the
  continuous performance-testing proposal.
- Use `assets/` and `scripts/` to scaffold and validate HW05 artifacts.

## Integrity Rules

- Never fabricate a test-plan execution, `.jtl` row, HTML report, screenshot, hardware spec, demo
  video link, GitHub Issue URL, performance threshold, resource-monitor value, or Git commit.
- A Load/Stress/Spike/Endurance result only counts if it came from a real JMeter/k6 run against the
  real backend, or is explicitly labelled as a non-submission dry run. Generated plans alone are not
  execution evidence.
- Preserve raw `.jtl` files in full. Do not replace them with screenshots or summaries.
- Expected functional success for the workflow must come from `README.md` and `api_specification.md`,
  not from current buggy behavior. Performance conclusions must come from raw logs.
- `backend/database.js` drops and recreates local data. Treat database reset as deliberate test
  setup; document it and do not hide it.
- The demo video must show the performance tool and resource monitor in the same frame with the
  student's own Vietnamese narration. The hardware report hostname must match previous deployments.

## Phase 0: Scope, Tooling, and Environment

Record in the report before implementation:

- Student ID and test-plan date used in filenames.
- Workflow selected; for this repo use `Login -> Search Product -> View Detail -> Add to Cart ->
  Checkout` unless the human explicitly changes it.
- Confirmation that the workflow is not duplicated with a groupmate, if that class rule is enforced.
- Tool choice: JMeter by default, k6 only if intentionally chosen.
- Backend base URL: `http://localhost:3000`.
- Startup/reset procedure from `setup_guide.md`: run `node database.js` only when a clean seed is
  needed; run `node server.js` for the backend.
- Hardware evidence plan: dxdiag/screenfetch/systeminfo plus resource monitor.

## Phase 1: Map the Workflow to Endpoint Groups

Map the end-to-end workflow to the three required backend groups:

- Auth-heavy: `POST /api/login`, extract JWT token.
- Read-heavy: `GET /api/products?search=<keyword>` and `GET /api/products/:id`.
- Transactional: `POST /api/cart` and `POST /api/checkout`.

Document why this single workflow covers all three groups. Include SUT risks from
`references/eshop-analysis-guide.md`: login lockout, token handling, SQLite writes, cart state, and
client-provided checkout total.

## Phase 2: AI-Assisted Test-Plan Design

Drive the AI step by step, never with one generic prompt:

1. Prompt for endpoint mapping and workload goals.
2. Prompt for Load parameters: virtual users, ramp-up, duration/loops, think time.
3. Prompt for Stress parameters: increasing load and stop/degradation criteria.
4. Prompt for Spike parameters: sudden jump, hold, and recovery period.
5. Prompt for assertions/extractors/correlation: token extraction, status checks, checkout `orderId`.
6. Prompt for report views/listeners and evidence plan.

Preserve prompts and raw outputs in `ai-audit.md` before human corrections.

## Phase 3: Make the Workflow Data-Driven

Use CSV files for runtime input. At minimum:

```csv
email,password,search,product_id,product_name,price,quantity,shipping_address
```

Use seeded credentials from the SUT:

- User: `test@eshop.com` / `Test1234!`
- Admin only when needed: `admin@eshop.com` / `Admin123!`

Avoid invalid-login rows in normal Load/Stress/Spike plans. The backend lockout behavior can distort
performance numbers unless the test is specifically measuring lockout.

Run `scripts/validate_hw5_workspace.py reports/HW5` before final packaging.

## Phase 4: Generate Plans

Create three plans named exactly:

```text
<StudentID>_Load_<YYYYMMDD>.jmx
<StudentID>_Stress_<YYYYMMDD>.jmx
<StudentID>_Spike_<YYYYMMDD>.jmx
```

Each plan must execute the same request chain and include:

- CSV Data Set Config.
- HTTP Request Defaults for `localhost:3000`.
- Login request with JSON token extractor.
- Authorization header for cart and checkout.
- Response assertions for HTTP success and key response fields where possible.
- Think time/timers.
- A distinct listener/report view across the three plans: Summary Report, Aggregate Report, View
  Results Tree, or justified equivalents.

## Phase 5: Human Review and Gap Analysis

The human reviews the AI-generated plans before execution. Record corrections such as:

- Unrealistic virtual-user counts, ramp-up, or think time.
- Missing token extractor or missing Authorization header.
- Missing response assertions.
- Missing account-lockout consideration.
- Wrong base URL or stale port.
- Data reset omitted or undocumented.
- Checkout total trusted without noting the SUT requirement that backend should recalculate totals.

For each correction, explain why the AI missed it: prompt quality, model limitation, or SUT-specific
behavior.

## Phase 6: Real Execution and Evidence

Execute all three scenarios against the real backend, as completely as possible:

```powershell
jmeter -n -t reports/HW5/plans/<plan>.jmx -l reports/HW5/results/<scenario>/<scenario>.jtl -e -o reports/HW5/results/<scenario>/html
```

For each run, capture:

- Raw `.jtl` log in full.
- HTML report folder.
- Screenshot showing the performance tool and backend resource usage together.
- Notes about database reset and whether login lockout needed reset.

Run a short Endurance/Soak test for 10-15 minutes at sustained load and report the empirical
threshold with concrete numbers. Do not invent threshold values if the run was not completed.

## Phase 7: Log Analysis and Misinterpretation Hunt

After `.jtl` logs exist:

1. Use AI to analyse raw logs and suggest thresholds.
2. Independently compute/check samples, pass/fail count, error rate, average, p90, p95, p99,
   throughput, and max latency.
3. Identify AI misinterpretations with exact values from raw logs.
4. Classify AI optimization recommendations as feasible or hallucinated.

Use `scripts/summarize_jtl.py` or an equivalent tool to support the human review.

## Phase 8: Bug and Performance Issue Reporting

File a Markdown bug/performance issue report and a real GitHub Issue when execution evidence shows:

- Reproducible error responses, crashes, or functional regressions.
- Sustained high error rate.
- Severe p95/p99 latency regression at a documented load.
- SQLite lock/write contention or checkout instability.

Attach screenshots. Use `Pending` only when the issue has not actually been filed.

## Phase 9: Demo Video

Record an unlisted YouTube video of at least 6 minutes. It must show:

- Student authorship evidence or face-cam.
- JMeter/k6 and resource monitor in the same frame.
- One scenario run or a clear walkthrough of collected real results.
- Raw `.jtl` and HTML report.
- At least one human correction to the AI-generated plan.
- Vietnamese narration by the student.

## Phase 10: AI Audit, AI Critique, and Continuous Testing

- Maintain `ai-audit.md` with AI tool name, date/time, prompt, raw output, and human corrections.
- Write `ai-critique.md` in 200-300 words.
- Write a continuous performance-testing proposal that watches commits, decides whether to run
  smoke/full performance tests, compares p95/error rate to baseline, flags regressions, and
  discusses cost/false alarms.

## Phase 11: Final Assembly

Final `reports/HW5/` should include:

```text
README.md
main-report.md
ai-audit.md
ai-critique.md
git-commit-log.txt
bug-report.md
data/*.csv
plans/*_Load_*.jmx
plans/*_Stress_*.jmx
plans/*_Spike_*.jmx
results/<scenario>/*.jtl
results/<scenario>/html/
evidence/<scenario>/
evidence/hardware/
proposal/continuous-performance-testing.md
demo-video-script.md
```

Export Markdown/PDF versions when required by Moodle packaging. The final README must contain the
self-assessment table and test summary: scenarios run, endpoint groups covered, endurance threshold,
number of bugs/performance issues, and demo video link.
