# Task 1 - AI Assisted Test Design and Execution

## 1. Workflow Design

The three JMeter plans exercise the same end-to-end e-commerce workflow:

1. Auth-heavy: `POST /api/login`
2. Read-heavy: `GET /api/products`, `GET /api/products?search=`, `GET /api/products/:id`, `GET /api/categories`
3. Transactional: `POST /api/cart`, `GET /api/cart`, `POST /api/checkout`, `GET /api/orders/my-orders`

This simulates a realistic user journey: login, browse products, add an item to cart, checkout, then view orders.

## 2. Final Test Plans

| Scenario | File | VUsers | Ramp-up | Duration | Listener |
|----------|------|--------|---------|----------|----------|
| Load | `23127296_Load_20260815.jmx` | 10 | 60s | 600s | Summary Report |
| Stress | `23127296_Stress_20260815.jmx` | 50 | 120s | 600s | View Results Tree |
| Spike | `23127296_Spike_20260815.jmx` | 5 -> 100 -> 5 | 10s / 5s / 10s | 60s + 30s + 120s | Aggregate Report |

The plans use CSV files for credentials, products, and checkout data:

- `test_data_users.csv`
- `test_data_products.csv`
- `test_data_checkout.csv`

## 3. Human Review and Fixes

| # | Issue Found | Correction Applied | Reason |
|---|-------------|--------------------|--------|
| 1 | Original file names used sample ID `25127001` and old date. | Renamed plans to `23127296_*_20260815.jmx`. | Required format is `{StudentID}_{ScenarioType}_{YYYYMMDD}`. |
| 2 | CSV users were not present in the default SQLite seed data. | Added `seed_performance_data.js`. | Without seeding, `/api/login` returns 401 and all protected requests fail. |
| 3 | Generic lockout wording assumed three wrong passwords. | Documented backend behavior: failed attempts increase by 2, so two wrong passwords can lock an account for 180s. | This was verified in `backend/server.js`. |
| 4 | AI-style plan review did not mention real environment blockers. | Added `runbook.md` and marked real-run evidence as pending. | `jmeter` and `node` are not on PATH in this terminal. |
| 5 | Report tables contained placeholders that looked final. | Replaced placeholders with `PENDING_REAL_RUN`, `PENDING_JTL_LOGS`, or verified values. | Avoids fabricated metrics. |

## 4. Assertions and Auth Handling

Verified from the JMX files:

- Login response assertion checks HTTP 200.
- JWT token is extracted using a JSON post-processor at `$.token`.
- Protected cart, checkout, and order requests send `Authorization: Bearer ${auth_token}`.
- Read endpoints use CSV-driven `product_id` and `search_keyword`.

## 5. Account Lockout Reset

The backend locks users for 180 seconds after enough failed login attempts. In this implementation, each wrong password adds 2 attempts:

```js
const newAttempts = user.login_attempts + 2;
```

Before each Stress or Spike run, reset performance accounts:

```sql
UPDATE users
SET login_attempts = 0, locked_until = NULL
WHERE email LIKE 'user_load_%@test.com';
```

The included seed script performs this reset by recreating the performance users.

## 6. Execution Evidence Status

| Required Evidence | Status |
|-------------------|--------|
| Load `.jtl` raw log | PENDING_REAL_RUN |
| Stress `.jtl` raw log | PENDING_REAL_RUN |
| Spike `.jtl` raw log | PENDING_REAL_RUN |
| Load HTML report folder | PENDING_REAL_RUN |
| Stress HTML report folder | PENDING_REAL_RUN |
| Spike HTML report folder | PENDING_REAL_RUN |
| JMeter + Task Manager screenshots | PENDING_REAL_RUN |
| Hardware spec screenshot | PENDING_REAL_RUN |
| Demo video >= 6 minutes | PENDING_USER_INPUT |

## 7. Endurance Threshold

Use the Load plan as a 10-minute soak test after seeding data. Fill these values only from the generated `.jtl` and resource screenshots:

| Metric | Value | Source |
|--------|-------|--------|
| Max Stable RPS | PENDING_JTL_LOGS | JMeter dashboard / `.jtl` |
| Memory Ceiling | PENDING_SCREENSHOT | Task Manager |
| Avg Response Time | PENDING_JTL_LOGS | `.jtl` |
| p95 Response Time | PENDING_JTL_LOGS | `.jtl` |
| Error Rate | PENDING_JTL_LOGS | `.jtl` |
| CPU Usage at Threshold | PENDING_SCREENSHOT | Task Manager |

## 8. How To Run

Follow `runbook.md`:

1. Start backend on `localhost:3000`.
2. Run `node hw05\submit\task1\seed_performance_data.js`.
3. Run the three JMeter CLI commands.
4. Generate screenshots and video evidence.
5. Analyze `.jtl` files with `node hw05\submit\task2\analyze_jtl.mjs <jtl files>`.

## 9. Bugs and Performance Issues

No GitHub Issues can be filed until the real runs produce evidence. Candidate issues to watch:

- High p95 or p99 latency during Stress or Spike.
- Any non-2xx responses in protected endpoints after successful login.
- Backend crash or sustained memory growth.
- Product search performance degradation because `/api/products?search=` builds SQL using string interpolation.
