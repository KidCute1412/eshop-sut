# README.md

## HW05 — Performance Testing

### Student Information
- **Student ID**: [Your Student ID]
- **Name**: [Your Name]
- **Self-Assessed Grade**: [000-100]

---

### Self-Assessment Table

| No. | Criteria | Grade | Self-Assessed Grade |
|-----|----------|-------|---------------------|
| 1 | Task 1 — Load Testing | 20 | [__] |
| 2 | Task 1 — Stress Testing | 20 | [__] |
| 3 | Task 1 — Spike Testing | 20 | [__] |
| 4 | Task 2 — AI Analysis + Misinterpretation Hunt | 10 | [__] |
| 5 | Task 3 — Continuous Performance Testing Proposal (G9.6) | 10 | [__] |
| 6 | Agent Skills | 10 | [__] |
| | **Total** | **100** | **[__]** |

---

### Test Summary Report

#### Scenarios Run
| Scenario | VUsers | Duration | Status |
|----------|--------|----------|--------|
| Load Test | 10 | 10 min | [Pass/Fail] |
| Stress Test | 50 | 10 min | [Pass/Fail] |
| Spike Test | 5→100→5 | 3.5 min | [Pass/Fail] |

#### Endpoint Groups Covered
- [x] **Auth-Heavy**: POST /api/login
- [x] **Read-Heavy**: GET /api/products, GET /api/products/:id, GET /api/categories
- [x] **Transactional**: POST /api/cart, POST /api/checkout, GET /api/orders/my-orders

#### Endurance Threshold
| Metric | Value |
|--------|-------|
| Maximum Stable RPS | [__] |
| Memory Ceiling | [__] MB |
| Response Time Degradation Point | [__] VUsers |

#### Bugs / Performance Issues
- **Number of bugs found**: [__]
- **Number of performance issues found**: [__]
- **GitHub Issues link**: [Link to GitHub Issues page]

#### Demo Video
- **YouTube Link**: [Unlisted YouTube link]
- **Duration**: [__] minutes

---

### File Structure

```
submit/
├── README.md                          (this file)
├── ai_audit_report.md                 (AI interaction log)
├── ai_critique.md                     (200-300 word critique)
├── task1/
│   ├── 25127001_Load_20260813.jmx     (Load test plan)
│   ├── 25127001_Stress_20260813.jmx   (Stress test plan)
│   ├── 25127001_Spike_20260813.jmx    (Spike test plan)
│   ├── test_data_users.csv            (user credentials)
│   ├── test_data_products.csv         (product data)
│   ├── test_data_checkout.csv         (checkout data)
│   └── test_plan_review_notes.md      (review and corrections)
├── task2/
│   └── ai_analysis_and_review.md      (analysis + misinterpretation hunt)
├── task3/
│   └── continuous_testing_proposal.md (continuous testing proposal)
└── screenshots/
    ├── load_test_screenshot.png
    ├── stress_test_screenshot.png
    ├── spike_test_screenshot.png
    └── hardware_spec.png
```

### Additional Files (to be added after execution)
- `.jtl` log files (3 files)
- HTML report folders (3 folders)
- Demo video link
- Git commit log
- Bug report screenshots (if any)
