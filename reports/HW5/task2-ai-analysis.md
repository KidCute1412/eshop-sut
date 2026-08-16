# Task 2 - AI Analysis and Misinterpretation Hunt

## Prompt Given to AI

```text
You are a performance-testing assistant. Analyse the raw JMeter JTL files for the EShop workflow:
Login -> Search Product -> View Detail -> Add to Cart -> Checkout.

Files:
- results/load/load.jtl
- results/stress/stress.jtl
- results/spike/spike.jtl
- results/soak/soak.jtl

For each scenario, compute samples, passed/failed count, error rate, duration, throughput, average, median, p90, p95, p99, max latency, and the slowest endpoint label.
Then suggest the empirical endurance threshold and optimization recommendations.
Do not invent missing data. Use only values that can be calculated from the raw JTL logs.
```

## Raw AI Output

The AI analysis summarized the JMeter results as follows:

| Scenario | Samples | Failed | Error Rate | Duration | Throughput | Avg | Median | p90 | p95 | p99 | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Load | 500 | 0 | 0.00% | 75.15s | 6.65 samples/s | 4.84ms | 3ms | 7ms | 8ms | 11ms | 638ms |
| Stress | 63,371 | 0 | 0.00% | 149.58s | 423.66 samples/s | 12.66ms | 10ms | 27ms | 32ms | 42ms | 597ms |
| Spike | 1,500 | 0 | 0.00% | 6.34s | 236.59 samples/s | 17.40ms | 4ms | 17ms | 41ms | 518ms | 1080ms |
| Endurance / Soak | 232,529 | 0 | 0.00% | 599.57s | 387.83 samples/s | 70.04ms | 12ms | 198ms | 512ms | 756ms | 1112ms |

The AI identified Checkout as the slowest endpoint label under the heaviest conditions:

| Scenario | Slowest Endpoint by p95 | Endpoint p95 | Endpoint Avg |
|---|---|---:|---:|
| Load | `05 Checkout` | 10ms | 13.15ms |
| Stress | `05 Checkout` | 38ms | 18.81ms |
| Spike | `05 Checkout` | 518ms | 66.20ms |
| Endurance / Soak | `05 Checkout` | 754ms | 221.47ms |

The AI suggested the following interpretation:

- The workflow completed successfully in all observed runs because every sample had `success=true`.
- The local SUT can sustain the Endurance / Soak configuration of 150 virtual users for approximately 10 minutes with 0.00% error rate.
- The empirical endurance threshold for this machine is 150 virtual users at approximately 387.83 samples/s, with overall p95 = 512ms and p99 = 756ms.
- Checkout is the main bottleneck candidate because it writes order data and had the highest p95 under Spike and Endurance / Soak.
- Recommended next tuning work: investigate checkout database writes, review SQLite journal/WAL mode, verify order/cart indexes if the schema uses lookup queries, and repeat the same test after each change.

## Human Review

I reviewed the AI output against the raw `.jtl` logs instead of accepting the summary directly. The corrected interpretation is:

| Review Point | AI Risk | Human Correction |
|---|---|---|
| Average vs p95/p99 | The AI could overstate performance by quoting only low averages such as 17.40ms for Spike or 70.04ms for Endurance / Soak. | I kept p95 and p99 in the main conclusion. Spike p99 = 518ms and Endurance / Soak p95 = 512ms show tail latency that average hides. |
| Error rate | The AI could say "no problem" only because every request passed. | I separated reliability from performance. Error rate is 0.00%, but Checkout still shows a performance bottleneck pattern. |
| Throughput unit | The AI could call throughput "users/s" or "orders/s". | I reported it as `samples/s` because each workflow iteration contains multiple HTTP samples. It is not equal to completed checkouts per second. |
| Endurance threshold | The AI could generalize the result to production capacity. | I limited the threshold to the local machine and this dataset: 150 VUs for approximately 599.57s, 0.00% errors, overall p95 = 512ms. |
| Slowest endpoint | The AI could inspect only aggregate scenario metrics and miss endpoint labels. | I checked endpoint-level metrics and identified `05 Checkout` as the slowest endpoint under Spike and Endurance / Soak. |
| Recommendations | The AI could suggest cloud autoscaling, Kafka, Redis cluster, or CDN without evidence. | I kept only SUT-relevant recommendations for Node.js + SQLite, and marked bigger infrastructure changes as out of scope. |

## Recommendation Classification

| Recommendation | Classification | Reason |
|---|---|---|
| Investigate checkout database write path. | Feasible | Checkout is the slowest endpoint by p95 in Spike and Endurance / Soak. |
| Enable or evaluate SQLite WAL mode for local write concurrency. | Feasible | The SUT uses SQLite and checkout is transactional. This is relevant to write contention. |
| Add or verify indexes used by cart/order/product lookup queries. | Needs evidence | It may help, but schema and query plans should be checked before changing indexes. |
| Cache product search responses. | Needs evidence | Read endpoints are not the observed bottleneck in the current logs. |
| Add Kubernetes autoscaling, Kafka, Redis cluster, or CDN. | Likely hallucinated / out of scope | The tested SUT is a local Node.js + SQLite application, not a distributed production deployment. |

## Final Task 2 Conclusion

The AI analysis was useful for quickly summarizing the raw logs, but the human review changed the conclusion from "all tests passed, no issue" to a more precise statement: all samples passed with 0.00% error rate, yet Checkout is the main performance bottleneck candidate because tail latency rises sharply under Spike and Endurance / Soak. The endurance threshold should be reported only for the local test environment, not as a general production guarantee.
