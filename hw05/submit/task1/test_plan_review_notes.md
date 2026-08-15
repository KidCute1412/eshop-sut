# Task 1 — AI Assisted Test Design and Execution

## 1. AI-First Strategy: Test Plan Generation

### End-to-End Workflow Design

The workflow covers all three endpoint groups in a single user journey:

1. **Auth-Heavy**: `POST /api/login` — user authenticates and receives JWT token
2. **Read-Heavy**: `GET /api/products`, `GET /api/products?search=`, `GET /api/products/:id`, `GET /api/categories` — user browses and searches products
3. **Transactional**: `POST /api/cart`, `GET /api/cart`, `POST /api/checkout`, `GET /api/orders/my-orders` — user adds items to cart and completes purchase

**Justification**: This workflow simulates a realistic e-commerce user journey: login → browse → add to cart → checkout. It exercises all three endpoint groups with data-driven parameters from CSV files.

### AI Tool Used for Design
- **Tool**: [AI tool name, e.g., ChatGPT / Claude / Gemini]
- **Date**: [Date of interaction]
- **Key Prompts Used**:
  1. "Design a JMeter test plan for an e-commerce API with auth, product browsing, and checkout workflow"
  2. "What ramp-up and think time values are realistic for a load test of 10 VUsers?"
  3. "Help me design CSV data files for parameterizing user credentials and product data"
  4. "What are appropriate thread counts for stress and spike tests on a local server?"

### AI Output Summary
[Paste or summarize what the AI generated]

---

## 2. Review and Fix (Human Review)

### Issues Found in AI-Generated Plans

| # | Issue | What AI Got Wrong | Correction Applied | Why AI Missed It |
|---|-------|-------------------|-------------------|------------------|
| 1 | Account lockout handling | AI did not account for 3-fail lockout (180s) on `/api/login` | Used valid credentials from CSV; documented reset steps between stress/spike runs | Model limitation — endpoint-specific behavior not in training data |
| 2 | Ramp-up time too aggressive | AI suggested 10s ramp-up for 50 VUsers (stress) | Changed to 120s for gradual degradation observation | Generic template response, not tuned for local SQLite backend |
| 3 | Think time too short | AI suggested 0.5s think time | Changed to 1-3s uniform random to mimic real browsing | AI optimized for throughput, not realism |
| 4 | Missing auth header on cart/checkout | AI forgot to add `Authorization: Bearer` header | Added HeaderManager with JWT token extraction | Common oversight — AI focused on body, not headers |
| 5 | Wrong CSV variable references | AI used `${username}` instead of `${email}` | Corrected variable names to match CSV headers | Prompt quality — did not specify exact CSV structure |

### Corrected Parameters

| Parameter | Load Test | Stress Test | Spike Test |
|-----------|-----------|-------------|------------|
| VUsers | 10 | 50 | 5 → 100 → 5 |
| Ramp-Up | 60s | 120s | 5s (spike) |
| Duration | 600s | 600s | 60s + 30s + 120s |
| Think Time | 1-3s random | 1-3s random | 1-3s random |
| Report View | Summary Report | View Results Tree | Aggregate Report |

---

## 3. Test Execution Evidence

### Screenshots Required
- [ ] Load test running in JMeter + Task Manager screenshot
- [ ] Stress test running in JMeter + Task Manager screenshot
- [ ] Spike test running in JMeter + Task Manager screenshot
- [ ] Hardware spec (dxdiag / screenfetch)
- [ ] Account lockout reset steps documented

### Raw Output Files
- [ ] `25127001_Load_20260813.jtl` — raw log for Load test
- [ ] `25127001_Stress_20260813.jtl` — raw log for Stress test
- [ ] `25127001_Spike_20260813.jtl` — raw log for Spike test
- [ ] `25127001_Load_20260813/` — HTML report folder for Load test
- [ ] `25127001_Stress_20260813/` — HTML report folder for Stress test
- [ ] `25127001_Spike_20260813/` — HTML report folder for Spike test

### Account Lockout Reset
When stress/spike runs trigger the 3-fail login lockout:
1. Observe error responses in JMeter (HTTP 423 or lockout message)
2. Wait 180 seconds for lockout to expire, OR
3. Manually reset by modifying the SQLite database:
   ```sql
   UPDATE users SET login_attempts = 0 WHERE email = 'user_load_001@test.com';
   ```
4. Document the reset step and timestamp

---

## 4. Endurance Threshold

### Soak Test Setup
- **Duration**: 10-15 minutes at sustained load
- **VUsers**: [Adjust based on Load test results — start with 10, increase if stable]
- **Expected Metrics to Record**:
  - Maximum stable RPS (Requests Per Second)
  - Memory ceiling (RAM usage before degradation)
  - Response time degradation point
  - Error rate threshold

### Endurance Results (Fill After Execution)

| Metric | Value | Threshold |
|--------|-------|-----------|
| Max Stable RPS | [__] | [__] |
| Memory Ceiling | [__] MB | [__] MB |
| Avg Response Time (stable) | [__] ms | [__] ms |
| Response Time Degradation Point | [__] VUsers | [__] VUsers |
| Error Rate at Threshold | [__]% | [__]% |
| CPU Usage at Threshold | [__]% | [__]% |

### Conclusion
[Describe your hardware's endurance threshold based on empirical data]

---

## 5. Demo Video

- **YouTube Link**: [Paste unlisted YouTube link here]
- **Duration**: At least 6 minutes total
- **Content**: Shows JMeter tool and resource monitor (Task Manager) in same frame, with Vietnamese narration
- **Segments**:
  - [ ] Load test demo: [timestamp range]
  - [ ] Stress test demo: [timestamp range]
  - [ ] Spike test demo: [timestamp range]

---

## 6. Bug/Performance Issues Report

### Issues Found (Log on GitHub Issues)

| # | Type | Description | Endpoint | Severity | GitHub Issue Link |
|---|------|-------------|----------|----------|-------------------|
| 1 | Performance | [e.g., High latency under load] | [endpoint] | [Low/Med/High] | [link] |
| 2 | Functional Bug | [e.g., Cart not cleared after checkout] | POST /api/checkout | [Low/Med/High] | [link] |
| 3 | Security | [e.g., SQL injection in search] | GET /api/products?search= | [Low/Med/High] | [link] |

[Add or remove rows as needed]
