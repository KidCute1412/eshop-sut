# HW05 Performance Testing Report

## 1. Executive summary

This report evaluates the local EShop backend with one data-driven API workflow: login, product detail, add cart, and checkout. Apache JMeter 5.6.3 executed Load, Stress, Spike, and Endurance scenarios against `http://localhost:3000`. The three required scenarios completed with zero JTL-recorded errors. The ten-minute endurance run completed 4,400 successful samples. A separate controlled security check confirmed an account-lockout defect: after two invalid passwords, a valid password was rejected with HTTP 403.

All performance values below are reproduced from raw JTL files by `agent-skill/jmeter-performance-evidence/scripts/summarize_jtl.py`; screenshots are used only for attributable GUI, monitor, hardware, and reset evidence.

## 2. Scope, traceability, and environment

| Workflow order | API request | Endpoint group | Functional traceability | Verification in plan |
| ---: | --- | --- | --- | --- |
| 1 | `POST /api/login` | Auth-heavy | FR-02 | CSV credentials, HTTP 200 assertion, JSON token extraction |
| 2 | `GET /api/products/:id` | Read-heavy | FR-06 | CSV product ID and HTTP 200 assertion |
| 3 | `POST /api/cart` | Transactional | FR-07 | Bearer-token correlation, CSV payload, HTTP 200 assertion |
| 4 | `POST /api/checkout` | Transactional | FR-08 | Bearer-token correlation, shipping payload, HTTP 200 assertion |

The same sequence is present in every required JMX plan. `workflow.csv` contains only the local seeded test account and local product/order inputs; no production credential, token, or personal data is reported.

| Environment field | Observed value | Evidence |
| --- | --- | --- |
| SUT | Local Node.js Express backend with SQLite | `supporting-materials/execution_manifest.md` |
| Base URL | `http://localhost:3000` | JMX plans |
| Tool | Apache JMeter 5.6.3 | JMX plans and EV-RUN screenshots |
| Host | LOKMIRACLE; Windows 11 Home Single Language 64-bit, build 26200 | EV-HW-001 |
| CPU / RAM | AMD Ryzen 5 6600HS Creator Edition, 12 logical CPUs, 16 GB RAM | EV-HW-001 |
| Storage / monitor | NVMe SSD; Windows Task Manager | EV-HW-002 |

The captured monitor baseline showed 25% CPU and 12.3/13.7 GB memory in use. It is an attributable point-in-time observation, not a per-process peak claim; the submission does not invent a backend CPU/RAM peak that was not recorded.

## 3. Test design and execution integrity

| Scenario | Configuration | Listener/report view | Intent and stop condition |
| --- | --- | --- | --- |
| Load | 5 users, 15 s ramp-up, 10 loops | Summary Report | Expected local workload; stop on assertion failure or backend crash. |
| Stress | 20 users, 30 s ramp-up, 10 loops | Aggregate Report | Higher concurrent pressure; stop on material error/degradation. |
| Spike | 25 users, 2 s ramp-up, 5 loops | View Results Tree | Abrupt demand increase and recovery check. |
| Endurance | 5 users, 15 s ramp-up, 220 loops | HTML report + raw JTL | Sustained workload for at least ten minutes. |

Each plan has a CSV Data Set Config, token extraction, bearer authorization, response-code assertions, and a randomized think time. The first Load preflight is retained at `raw-results/preflight/` because its header row was consumed as test data, causing 75 failed authentications. It is excluded from final metrics; removing that header produced successful final runs. This correction is documented in the AI audit rather than concealed.

## 4. Reproducible results

| Scenario | Samples | Errors | Mean | p95 | Min / Max | Duration | Throughput |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| Load | 200 | 0 (0.00%) | 5.79 ms | 14 ms | 2 / 75 ms | 38.817 s | 5.152 RPS |
| Stress | 800 | 0 (0.00%) | 5.21 ms | 13 ms | 1 / 71 ms | 56.712 s | 14.106 RPS |
| Spike | 500 | 0 (0.00%) | 6.42 ms | 14 ms | 2 / 76 ms | 15.733 s | 31.780 RPS |
| Endurance (validated JMX) | 4,400 | 0 (0.00%) | 3.84 ms | 12 ms | 1 / 44 ms | 632.403 s | 6.958 RPS |

Raw sources are `raw-results/{load,stress,spike,endurance}/`; the validated endurance source is `raw-results/endurance/23127404_Endurance_VALIDATED_20260817.jtl`, with dashboard `html-reports/endurance-validated/`. The evidence register maps required GUI/Task Manager frames to EV-RUN-LOAD, EV-RUN-STRESS, and EV-RUN-SPIKE. The completed 20-VU stepped profile achieved 24.014 RPS, p95 10 ms, and zero errors over 133.256 seconds; it is the highest completed stepped level. It is reported as a tested stable level, not a fabricated saturation capacity.

## 5. Defect, recovery, and limitations

The lockout/reset screenshot pair records two invalid requests returning HTTP 401 and a third returning HTTP 403; a fresh controlled follow-up was then executed with two invalid logins followed by a valid password, yielding 401, 401, and 403. The valid login should remain permitted until the configured third failed attempt has occurred. The implementation instead records two attempts per invalid password, so it locks early. The issue packet is `bugs/BUG-HW05-LOCKOUT-001.md`; only its public GitHub URL remains to be added by the student.

Restarting the local backend rebuilt seeded SQLite state; the valid-login reset evidence returned HTTP 200. Results are specific to one laptop, local loopback networking, seeded data, and the selected workflow. They cannot be generalized to production capacity or cloud deployment. No backend CPU/RAM peak is asserted because the captured Task Manager evidence is an observation frame rather than a time-series profiler.

## 6. AI review and continuous testing

The AI Audit Report records design, plan, execution-review, and analysis interactions. The key AI-assisted defect was the initial CSV-header configuration; human review retained the failed preflight, corrected the data contract, and used only the final JTL runs for conclusions. The 200–300 word critique is in `reports/ai_critique.md`.

`reports/continuous_performance_proposal.md` defines a commit-aware pipeline, baseline and regression gates, retry/triage route, retention policy, and trade-offs. Optimization suggestions are conditional: migrate from local SQLite only after production evidence shows write contention; profile database query plans before adding indexes; and treat connection-pool changes as inapplicable to the present SQLite process unless the architecture changes.

### AI optimization recommendation review

| AI-proposed optimization | Classification | Evidence-based review |
| --- | --- | --- |
| Add indexes for order/cart access paths | Conditional | SQLite supports indexes, but no slow-query plan or endpoint-specific query evidence was captured. Profile the production-like query plan before adding an index. |
| Enable SQLite WAL or migrate to a server database | Conditional | Final JTLs recorded zero errors, so current evidence does not establish SQLite write contention. Reconsider only if sustained concurrent writes reproduce locking or p95 degradation. |
| Increase a database connection pool | Not applicable | The SUT uses local SQLite through `sqlite3`, not a client-server pool. A pool setting would not address the observed architecture. |
| Raise JMeter virtual-user count as an application optimization | Not applicable | Virtual users change test pressure rather than EShop behavior. They are a measurement control, not a product remediation. |

## 7. External submission links

- Unlisted Vietnamese demo video (at least six minutes):
- Confirmed GitHub Issue BUG-HW05-LOCKOUT-001:
