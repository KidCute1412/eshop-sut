# HW06 — API Testing: 100/100 Master Completion Checklist

> **Assignment ID:** `HW06-AI`  
> **Topic:** AI-Driven API Testing, Postman/Newman Data-Driven Automation, CI/CD Integration, and Agent Skill  
> **Source Document:** [`2026.HW06.API Testing_En.pdf`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/specs/2026.HW06.API%20Testing_En.pdf) (8 pages)  
> **Student ID:** `23127404`  
> **Submission Root Folder:** [`docs/assignments/HW06/deliverables/`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/)  
> **Target Archive Name:** `23127404_HW06_AI_API_100.zip`  
> **Self-Assessed Score:** `100 / 100`  

---

## 0. Non-Negotiable Regulations & Anti-0-Point Policy

- [ ] **Moodle Submission Deadline:** Confirm exact submission deadline and upload link on Moodle.
- [ ] **Individual Work:** Completed individually; no sharing or copying of test cases, Postman scripts, Newman reports, or AI prompts (copying results in a grade of 0 for both parties).
- [ ] **Mandatory Non-Overlapping Scope:** Selected exactly three backend APIs across 3 distinct pools (Pool A, Pool B, Pool C).
- [ ] **No Group Duplication:** Confirmed that the combination of 3 selected APIs is unique and not identical to any group member.
- [ ] **Real & Attributable Evidence:** All test runs executed against real local SUT (`http://localhost:3000` or `127.0.0.1:3000`). No fabricated Newman logs or fake AI responses.
- [ ] **Required Request Header:** Every request contains the custom header `X-Student-Id: 23127404` injected via Postman pre-request script.
- [ ] **Public GitHub Repository:** Repository is public and accessible with all collections, environments, data files, CI/CD workflows, and test reports.
- [ ] **Complete Archive Contents:** Every required file exists in `deliverables/` before compressing into `.zip`. Missing any required document results in **0 points**.

---

## 1. Assignment Scope & API Suite Registry

- **System Under Test (SUT):** EShop Backend (`Node.js + Express + SQLite`) at `http://localhost:3000`.
- **API Specification Source:** [`api_specification.md`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/api_specification.md) & [`README.md`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/README.md).

| Pool | Feature ID & Name | Selected API Endpoint | HTTP Method | Auth Required | Key Testing Dimensions |
|---|---|---|---|---|---|
| **Pool A** | **FR-02: Login & Lockout** | `/api/login` | `POST` | No (Public) | Domain/EP on email & password, BVA on 3-attempt lockout threshold, 30s lockout state, JWT response schema, SEC-01 (plaintext), SEC-02 |
| **Pool B** | **FR-08 / FR-10: Checkout & Orders** | `/api/checkout` | `POST` | Yes (Bearer Token) | Cart state dependency, server-side amount re-computation, BVA on total amount, initial `pending` order state, SEC-02 |
| **Pool C** | **FR-18 / FR-10: Order State Machine** | `/api/admin/orders/:id/status` | `PUT` | Yes (Admin Token) | 5-state transition graph (`pending` → `confirmed` → `shipping` → `delivered` / `canceled`), final states rejection, SEC-03 (Admin RBAC), SEC-05 |

---

## 2. Pipeline Execution Checklist: API 1 — Pool A (`POST /api/login`) (30 Points)

### 2.1 Step 1: AI-Driven Generation (≥ 35 Test Cases)
- [ ] Guided AI step-by-step (using structured prompts, not a single generic black-box prompt).
- [ ] Generated **≥ 35 distinct test cases** covering all required testing dimensions:
  - [ ] **Domain Partitions (EP):** Valid email format, invalid email (no `@`, missing domain, leading/trailing spaces, special chars), empty password, valid password, wrong password.
  - [ ] **Boundary Value Analysis (BVA):** Attempt count 1 (counter = 1), Attempt count 2 (counter = 2), Attempt count 3 (lockout triggered, HTTP 403), Attempt count 4+ (lockout persisted).
  - [ ] **State Transitions:** Normal state → 1st failure → 2nd failure → 3rd failure (Locked state) → Expiration of 30s timeout → Normal state reset on successful login.
  - [ ] **Security (SEC-01, SEC-02, SEC-05):** SQL injection payload in email (`' OR 1=1 --`), XSS string in email/password, oversized body (>1MB), password exposure in response payload.
  - [ ] **Response Schema Validation:** JSON response structure containing `token` (valid JWT structure) and `user` object (`id`, `name`, `email`, `role`) on HTTP 200; error payload `{ "error": string }` on HTTP 401/403.

### 2.2 Step 2: Human Audit
- [ ] Audited 100% of AI-generated test cases with explicit labels: `VALID`, `INVALID`, or `INCOMPLETE`.
- [ ] Provided technical reasoning for each audit label.
- [ ] Corrected and refined all `INVALID` and `INCOMPLETE` cases (e.g., corrected wrong status codes, clarified lockout timing, fixed payload schema).

### 2.3 Step 3: Test Suite Extension (≥ 5 Cases AI Missed)
- [ ] Designed at least **5 additional test cases** not discovered by AI:
  1. `EXT-A01`: Concurrent brute-force login requests within lockout race condition window.
  2. `EXT-A02`: Case sensitivity of email address during authentication and lockout increment.
  3. `EXT-A03`: Reset of failure attempt counter upon immediate successful login after 2 failed attempts.
  4. `EXT-A04`: Login attempt with valid credentials while account is currently in active 30s lockout state.
  5. `EXT-A05`: Response header security verification (`Content-Type: application/json; charset=utf-8`, absence of sensitive stack traces on 500).
- [ ] Documented in-depth root cause analysis explaining **why** the AI missed these cases (e.g., lack of state persistence awareness, model token context limit, assumption of stateless REST).

### 2.4 Step 4: Postman & Newman Execution
- [ ] Created Postman collection with dynamic pre-request script injecting `X-Student-Id: 23127404`.
- [ ] Implemented comprehensive Chai test scripts for status code, schema, token format, error message, and response time (< 2000 ms).
- [ ] Executed automated run via Newman with HTML reporter:
  ```powershell
  newman run deliverables/postman/collections/pool_a_login.postman_collection.json -e deliverables/postman/environments/local.postman_environment.json -d deliverables/postman/data/login_data.json -r cli,htmlextra --reporter-htmlextra-export deliverables/newman-reports/pool-a/report.html
  ```
- [ ] Verified Newman execution completed with attributable localhost output and 0 unhandled failures.

### 2.5 Step 5: Bug Reporting
- [ ] Identified and documented all genuine SUT bugs found on `/api/login` (e.g., `BUG-API-01: Login attempt counter increases by +2 instead of +1`, `BUG-API-02: Lockout duration is 180 seconds instead of 30 seconds`).
- [ ] Created official GitHub Issues in the public repository with reproduction steps, expected vs actual behavior, and attached screenshots.
- [ ] Linked GitHub Issues in the Markdown bug report.

---

## 3. Pipeline Execution Checklist: API 2 — Pool B (`POST /api/checkout`) (30 Points)

### 3.1 Step 1: AI-Driven Generation (≥ 35 Test Cases)
- [ ] Guided AI step-by-step through `/api/checkout` specification.
- [ ] Generated **≥ 35 distinct test cases** covering:
  - [ ] **Domain Partitions (EP):** Valid shipping address, empty shipping address, extremely long address, valid total amount, zero total amount, negative total amount.
  - [ ] **Boundary Value Analysis (BVA):** Minimum order total (`1 ₫`), standard total, zero quantity in cart, maximum integer amount.
  - [ ] **State Transitions:** Non-empty cart → Checkout submitted → Order created with state `pending` → Cart emptied → Subsequent checkout fails with empty cart.
  - [ ] **Security (SEC-02, SEC-04, SEC-05):** Request without `Authorization` header (401), invalid/expired JWT token (403), tampering `total_amount` in request body vs server-calculated cart total, SQL injection / XSS payload in `shipping_address`.
  - [ ] **Response Schema Validation:** Response contains `message`, `orderId`, `status: "pending"`, and accurate order details.

### 3.2 Step 2: Human Audit
- [ ] Audited 100% of generated cases (`VALID` / `INVALID` / `INCOMPLETE`) with technical rationale.
- [ ] Fixed missing auth token prerequisites, resolved cart setup preconditions, and corrected client-vs-server amount expectations.

### 3.3 Step 3: Test Suite Extension (≥ 5 Cases AI Missed)
- [ ] Added at least **5 custom test cases**:
  1. `EXT-B01`: Checkout attempt with an empty cart (server must reject with 400 Bad Request).
  2. `EXT-B02`: Price tampering exploit: Client sends `total_amount = 1` for a 500,000 ₫ cart item (verifying server re-computes total).
  3. `EXT-B03`: Verification that cart items are completely cleared from database immediately after successful checkout.
  4. `EXT-B04`: HTML/XSS injection in `shipping_address` (`<script>alert(1)</script>`) stored safely without unescaped persistence.
  5. `EXT-B05`: Idempotency / Double submit test: Sending two identical checkout requests in rapid succession with the same cart.
- [ ] Detailed rationale explaining why AI failed to formulate multi-step stateful cart-to-order dependencies.

### 3.4 Step 4: Postman & Newman Execution
- [ ] Built multi-request Postman workflow (Seed User → Login → Add Item to Cart → Execute Checkout → Verify Order & Cart State).
- [ ] Executed automated suite with Newman:
  ```powershell
  newman run deliverables/postman/collections/pool_b_checkout.postman_collection.json -e deliverables/postman/environments/local.postman_environment.json -d deliverables/postman/data/checkout_data.json -r cli,htmlextra --reporter-htmlextra-export deliverables/newman-reports/pool-b/report.html
  ```
- [ ] Preserved full HTML reports and JSON summary logs.

### 3.5 Step 5: Bug Reporting
- [ ] Reported genuine SUT defects found on `/api/checkout` (e.g., `BUG-API-03: Server trusts client-submitted total_amount without recalculating from cart`).
- [ ] Submitted GitHub Issues with full request/response dumps and screenshots.

---

## 4. Pipeline Execution Checklist: API 3 — Pool C (`PUT /api/admin/orders/:id/status`) (30 Points)

### 4.1 Step 1: AI-Driven Generation (≥ 35 Test Cases)
- [ ] Guided AI step-by-step through Admin Order Management and State Machine specification (FR-10, FR-18, SEC-03).
- [ ] Generated **≥ 35 distinct test cases** covering:
  - [ ] **State Machine Valid Transitions:** `pending` → `confirmed`, `confirmed` → `shipping`, `shipping` → `delivered`, `pending` → `canceled`, `confirmed` → `canceled`.
  - [ ] **State Machine Invalid Transitions (Final & Backwards):** `delivered` → `pending`, `delivered` → `canceled`, `canceled` → `confirmed`, `shipping` → `pending`, `delivered` → `shipping`.
  - [ ] **Domain / Parameter Partitions:** Valid status string, invalid status (`"processing"`, `"completed"`, `""`, numeric `123`), non-existent order ID (`999999`), negative order ID (`-1`), string order ID (`"abc"`).
  - [ ] **Security & RBAC (SEC-03, SEC-05):** Regular customer JWT token attempting admin order update (must return 403 Forbidden), unauthenticated request (401), SQL injection in order ID path parameter (`1 OR 1=1`).
  - [ ] **Response Schema Validation:** Returns updated order object or `{ "message": "Order status updated successfully", "status": string }`.

### 4.2 Step 2: Human Audit
- [ ] Audited each case with `VALID` / `INVALID` / `INCOMPLETE` tags.
- [ ] Corrected AI assumptions about non-standard status values and enforced exact 5-state lifecycle boundaries.

### 4.3 Step 3: Test Suite Extension (≥ 5 Cases AI Missed)
- [ ] Added at least **5 custom test cases**:
  1. `EXT-C01`: RBAC Privilege Escalation: Regular user JWT (`role = 'user'`) attempting to transition order to `delivered` (must be 403).
  2. `EXT-C02`: Transition attempt on terminal state `delivered` back to `shipping` or `canceled` (must reject with 400/422).
  3. `EXT-C03`: Transition attempt on terminal state `canceled` to `confirmed` (must reject with 400/422).
  4. `EXT-C04`: State update with nonexistent enum value (e.g. `status = "refunded"` or `"shipped"`).
  5. `EXT-C05`: SQL injection attack in path parameter `:id` (e.g. `PUT /api/admin/orders/1%20OR%201=1/status`).
- [ ] Analyzed AI's blind spots regarding state immutability on terminal vertices and RBAC role header verification.

### 4.4 Step 4: Postman & Newman Execution
- [ ] Implemented Postman collection with dynamic token switching (Admin Token vs Customer Token vs Guest).
- [ ] Executed automated suite with Newman:
  ```powershell
  newman run deliverables/postman/collections/pool_c_admin_orders.postman_collection.json -e deliverables/postman/environments/local.postman_environment.json -d deliverables/postman/data/admin_orders_data.json -r cli,htmlextra --reporter-htmlextra-export deliverables/newman-reports/pool-c/report.html
  ```
- [ ] Verified complete HTML Newman execution report.

### 4.5 Step 5: Bug Reporting
- [ ] Documented genuine SUT defects found on `/api/admin/orders/:id/status` (e.g., `BUG-API-04: API allows transition from terminal state delivered back to pending`, `BUG-API-05: Missing RBAC verification allowing non-admin users to update order status`).
- [ ] Created GitHub Issues with reproduction steps, payloads, and screenshots.

---

## 5. Postman Technical Suite & Feature Coverage

- [ ] **Workspaces:** Configured dedicated workspace `HW06-API-Testing`.
- [ ] **Collections:** Created modular collections for Pool A, Pool B, and Pool C (or unified master collection with folders).
- [ ] **Environments:** Configured `local.postman_environment.json` containing `baseUrl`, `studentId`, `adminToken`, `userToken`, `testOrderId`.
- [ ] **Variables Hierarchy:** Demonstrated usage of Global, Environment, Collection, and Data variables.
- [ ] **Pre-request Scripts:** Implemented dynamic header injection and payload generation across all requests:
  ```javascript
  // Pre-request Script for X-Student-Id header injection
  pm.request.headers.upsert({
      key: 'X-Student-Id',
      value: pm.environment.get('studentId') || '23127404'
  });
  console.log('[AUDIT] Request initiated by Student ID:', pm.request.headers.get('X-Student-Id'));
  ```
- [ ] **Test Scripts & Assertions:** Utilized comprehensive Chai assertion patterns:
  1. HTTP Status Code validation (`pm.response.to.have.status(...)`)
  2. Header validation (`pm.response.to.have.header('Content-Type')`)
  3. Response Time assertion (`pm.expect(pm.response.responseTime).to.be.below(2000)`)
  4. JSON Schema / Type validation (`pm.expect(jsonData).to.have.property(...)`)
  5. Business Logic & Error Message validation
- [ ] **Data-Driven Runs (Collection Runner):** Created external JSON/CSV data files for multi-iteration parameterized execution.
- [ ] **Newman CLI Runner:** Scripted automated command-line execution with `htmlextra` reporter.
- [ ] **Postman Features Register:** Included full feature checklist table in the main report.

---

## 6. CI/CD Pipeline Integration (GitHub Actions)

- [ ] **Workflow Configuration File:** Created [`.github/workflows/api-tests.yml`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/.github/workflows/api-tests.yml) (and mirrored in `deliverables/cicd/workflows/`).
- [ ] **Pipeline Execution Steps:**
  1. Checkout code repository.
  2. Setup Node.js runtime environment.
  3. Install backend dependencies (`npm install`).
  4. Start backend server in background (`npm start &`).
  5. Wait for backend health check readiness (`http://localhost:3000/api/products`).
  6. Run Newman test collections against running SUT.
  7. Upload Newman HTML test reports as build artifacts.
- [ ] **Sample Commit 1 (All Pass):**
  - Git commit hash recorded.
  - GitHub Actions run shows **all API test cases passing (green build)**.
  - Screenshot captured and saved to `deliverables/cicd/screenshots/ci-pass.png`.
  - Direct live URL to the GitHub Actions run provided in CI/CD report.
- [ ] **Sample Commit 2 (Intentional Fail):**
  - Git commit hash recorded (e.g. modified expected status from 200 to 999 or added assertion verifying bug).
  - GitHub Actions run shows **pipeline failing (red build)** at the exact expected test step.
  - Screenshot captured and saved to `deliverables/cicd/screenshots/ci-fail.png`.
  - Direct live URL to the failing GitHub Actions run provided in CI/CD report.
- [ ] **CI/CD Report:** Authored [`<StudentID>_HW06_CICD_Report.md`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/cicd) and exported PDF.

---

## 7. Agent Skill: AI-Driven API Test Generator (10 Points — Bloom G9.5 Create)

- [ ] **Architecture & Workflow Design:**
  - Designed end-to-end architecture for an autonomous API test generation tool.
  - Input: Markdown API Specification / OpenAPI 3.0 YAML.
  - Engine: Specification parser, Equivalence Partitioning & BVA engine, Security & State machine rule injector, Postman Collection Builder.
  - Output: Executable Postman Collection (`.json`) + Data-driven dataset (`.json`).
- [ ] **Self-Drawn Architecture Diagram:**
  - Authored clear architectural workflow diagram (using Draw.io / Mermaid / PlantUML).
  - Ensured the design and decisions are student-created (Anti-Cheat compliance).
  - Saved as `deliverables/agent-skills/diagrams/architecture_diagram.png` and Mermaid code.
- [ ] **Pseudocode & Implementation:**
  - Wrote comprehensive pseudocode in Markdown (`deliverables/agent-skills/api-test-generator/pseudocode.md`).
  - Implemented working generator script / agent skill (`generator.py` or `.agents/skills/api-test-generator/`).
- [ ] **Demonstration Video (YouTube Link):**
  - Recorded clear walkthrough video demonstrating the test generator taking an API spec endpoint and producing complete test cases and Postman collection.
  - Uploaded as **Unlisted YouTube Video**.
  - Verified link opens without permission errors in incognito mode.
  - Embedded YouTube URL in main report and `README.md`.

---

## 8. AI Audit Report & Prompts History (Mandatory Appendix)

- [ ] Declared exact AI usage statement:
  > *"I use AI tools for the following tasks,"*
- [ ] Logged every single AI interaction chronologically:
  1. **AI Tool Name & Model:** (e.g., Gemini 3.7 Flash, Claude 3.5 Sonnet, ChatGPT-4o).
  2. **Timestamp (ISO / Date & Time):** Recorded exact timestamp for each query.
  3. **Exact Student Prompt:** Full unmodified text of the prompt sent to AI.
  4. **Exact AI Response:** Complete output generated by AI.
- [ ] Demonstrated step-by-step guidance (Specification analysis → Partitioning → BVA → State/Security injection → Postman assertion generation) rather than single generic prompt.
- [ ] Exported as Markdown (`deliverables/ai/23127404_HW06_AI_Audit_Report.md`) and PDF (`23127404_HW06_AI_Audit_Report.pdf`).

---

## 9. Mandatory AI Critique (200–300 Words)

- [ ] Authored rigorous critique paragraph addressing all 3 required questions:
  1. **Where did the AI get something wrong, biased, or incomplete?** (e.g., assuming REST standard 400 status when SUT returns 200 `{}` or 500, missing stateful multi-step cart requirements, overlooking RBAC checks).
  2. **Why did it fail to catch the issue?** (e.g., stateless prompt nature, lack of runtime execution feedback, LLM bias towards idealized RFC specifications).
  3. **What principle have you learned about collaborating with AI during this assignment?** (e.g., AI as an accelerator for test case expansion, human tester as the indispensable verification oracle and security auditor).
- [ ] **Word Count Verification:** Verified word count is strictly between **200 and 300 words**.
- [ ] Exported as Markdown (`deliverables/ai/23127404_HW06_AI_Critique.md`) and PDF (`23127404_HW06_AI_Critique.pdf`).

---

## 10. Anti-Cheat & Authenticity Verification

- [ ] **Header Evidence:** Captured terminal / Postman console screenshot showing `X-Student-Id: 23127404` header logged during runtime execution.
- [ ] **Deployment Hostname Evidence:** Newman HTML report clearly displays requests targeted at `localhost:3000` or `127.0.0.1:3000`.
- [ ] **Authorship of Diagrams:** Diagrams created and structured by the student.
- [ ] **Oral Defense Readiness:** Ready to explain test case design rationale, Postman assertion scripts, Newman execution results, and generator architecture in 5–7 minutes if randomly selected.

---

## 11. Genuine Bug Reporting Register

- [ ] Compiled comprehensive Bug Report in `deliverables/bugs/bug-report.md`.
- [ ] Registered each confirmed defect on public GitHub Issues page with reproduction steps, expected vs actual behavior, severity, and screenshots.

| Bug ID | Endpoint | Description | Severity | GitHub Issue Link | Screenshot |
|---|---|---|---|---|---|
| `BUG-HW06-01` | `POST /api/login` | Login attempt counter increments by +2 instead of +1 on bad password | Major | `#issue-1` | `bugs/screenshots/bug_01.png` |
| `BUG-HW06-02` | `POST /api/login` | Account lockout duration is set to 180s instead of 30s as specified | Medium | `#issue-2` | `bugs/screenshots/bug_02.png` |
| `BUG-HW06-03` | `POST /api/checkout` | Backend accepts client-supplied `total_amount` without server recalculation | Critical | `#issue-3` | `bugs/screenshots/bug_03.png` |
| `BUG-HW06-04` | `PUT /api/admin/orders/:id/status` | Order state machine permits illegal transitions from final state `delivered` | High | `#issue-4` | `bugs/screenshots/bug_04.png` |
| `BUG-HW06-05` | `PUT /api/admin/orders/:id/status` | Non-admin users can update order status due to missing role check | Critical | `#issue-5` | `bugs/screenshots/bug_05.png` |

---

## 12. Excel Test Cases Matrix & Test Summary

- [ ] Created complete test matrix spreadsheet: `deliverables/excel/23127404_HW06_API_Test_Cases.xlsx`.
- [ ] Included all required columns:
  - `Test Case ID`
  - `Pool & Feature`
  - `API Endpoint & Method`
  - `Testing Dimension (EP / BVA / State / Security / Schema)`
  - `Preconditions & Auth Token`
  - `Request Payload / Parameters`
  - `Expected Status & Response Body`
  - `Audit Label (VALID / INVALID / INCOMPLETE)`
  - `Source (AI Generated / Human Extended)`
  - `Execution Status (PASS / FAIL / BUG DETECTED)`
  - `Notes & Traceability`
- [ ] Sheet 1: `Summary & Statistics Dashboard`
- [ ] Sheet 2: `Pool A — POST /api/login (40+ Cases)`
- [ ] Sheet 3: `Pool B — POST /api/checkout (40+ Cases)`
- [ ] Sheet 4: `Pool C — PUT /api/admin/orders/:id/status (40+ Cases)`

---

## 13. Git Commit History & 4-Day Development Span

- [ ] Maintained fine-grained git commits reflecting real step-by-step progress:
  - Step 1: AI test generation for API 1, 2, 3
  - Step 2: Human audit & test correction commits
  - Step 3: Test suite extension commits
  - Step 4: Postman collection & Newman automation scripts
  - Step 5: Bug report commits & CI/CD workflow commits
  - Step 6: Agent skill generator design & implementation
- [ ] Spread qualifying commits over at least **4 distinct calendar days**.
- [ ] Exported complete git log to text file:
  ```powershell
  git log --pretty=format:"%h - %an, %ad : %s" --date=iso > deliverables/git/23127404_HW06_git_commit_log.txt
  ```

---

## 14. Deliverables Folder Layout & Package Manifest

Ensure the contents of [`docs/assignments/HW06/deliverables/`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/) adhere strictly to the following tree structure:

```text
docs/assignments/HW06/deliverables/
├── README.md                                 # Master Summary, Self-Assessment Table, URLs
├── report/
│   ├── 23127404_HW06_API_Testing_Report.md  # Main Markdown Report
│   └── 23127404_HW06_API_Testing_Report.pdf # Rendered PDF Report
├── ai/
│   ├── 23127404_HW06_AI_Critique.md         # 200–300 words AI critique
│   ├── 23127404_HW06_AI_Critique.pdf
│   ├── 23127404_HW06_AI_Audit_Report.md     # Full AI prompt & output history
│   └── 23127404_HW06_AI_Audit_Report.pdf
├── postman/
│   ├── collections/
│   │   ├── pool_a_login.postman_collection.json
│   │   ├── pool_b_checkout.postman_collection.json
│   │   └── pool_c_admin_orders.postman_collection.json
│   ├── environments/
│   │   └── local.postman_environment.json
│   └── data/
│       ├── login_data.json
│       ├── checkout_data.json
│       └── admin_orders_data.json
├── newman-reports/
│   ├── pool-a/
│   │   ├── report.html
│   │   └── report.json
│   ├── pool-b/
│   │   ├── report.html
│   │   └── report.json
│   └── pool-c/
│       ├── report.html
│       └── report.json
├── cicd/
│   ├── 23127404_HW06_CICD_Report.md
│   ├── 23127404_HW06_CICD_Report.pdf
│   ├── workflows/
│   │   └── api-tests.yml
│   └── screenshots/
│       ├── ci-pass.png
│       └── ci-fail.png
├── excel/
│   └── 23127404_HW06_API_Test_Cases.xlsx
├── bugs/
│   ├── bug-report.md
│   └── screenshots/
│       ├── bug_01.png
│       ├── bug_02.png
│       ├── bug_03.png
│       ├── bug_04.png
│       └── bug_05.png
├── agent-skills/
│   ├── api-test-generator/
│   │   ├── SKILL.md
│   │   ├── generator.py
│   │   └── pseudocode.md
│   ├── diagrams/
│   │   ├── architecture_diagram.png
│   │   └── flow_diagram.png
│   └── README.md
├── git/
│   └── 23127404_HW06_git_commit_log.txt
└── openapi/
    ├── eshop-openapi.yaml
    └── openapi_audit.md
```

- [ ] Compressed deliverables into archive:
  ```powershell
  Compress-Archive -Path "docs/assignments/HW06/deliverables/*" -DestinationPath "docs/assignments/HW06/23127404_HW06_AI_API_100.zip" -Force
  ```

---

## 15. Master 100/100 Assessment Matrix

| No. | Criteria | Target Requirement | Maximum Grade | Self-Assessed Grade | Compliance Status |
|---|---|---|:---:|:---:|:---:|
| **1** | **API 1 — Full Pipeline (`POST /api/login`)** | AI Generation (≥ 35 TCs) + Human Audit + Extension (≥ 5 TCs) + Newman Execution (`X-Student-Id`) + Bug Reports | 30 | **30** | `[x]` |
| **2** | **API 2 — Full Pipeline (`POST /api/checkout`)** | AI Generation (≥ 35 TCs) + Human Audit + Extension (≥ 5 TCs) + Newman Execution (`X-Student-Id`) + Bug Reports | 30 | **30** | `[x]` |
| **3** | **API 3 — Full Pipeline (`PUT /api/admin/orders/:id/status`)** | AI Generation (≥ 35 TCs) + Human Audit + Extension (≥ 5 TCs) + Newman Execution (`X-Student-Id`) + Bug Reports | 30 | **30** | `[x]` |
| **4** | **Agent Skills (AI-Driven Test Generator)** | Complete Generator Design (G9.5 Create) + Self-drawn Diagram + Pseudocode/Python script + YouTube Demo Video | 10 | **10** | `[x]` |
| **TOTAL** | **HW06 Overall Evaluation** | **Zero missing items, 100% genuine execution evidence, 2 CI/CD sample commits, Excel matrix, PDF reports** | **100** | **100** | `[x]` |

---

## 16. Quick Execution & Verification Command Reference

```powershell
# 1. Start Local Backend Server
cd "D:\HCMUS\Third Year\Software Testing\eshop-sut\backend"
npm install
node server.js

# 2. Run Postman Collections with Newman CLI
newman run "docs/assignments/HW06/deliverables/postman/collections/pool_a_login.postman_collection.json" `
  -e "docs/assignments/HW06/deliverables/postman/environments/local.postman_environment.json" `
  -d "docs/assignments/HW06/deliverables/postman/data/login_data.json" `
  -r cli,htmlextra `
  --reporter-htmlextra-export "docs/assignments/HW06/deliverables/newman-reports/pool-a/report.html"

# 3. Export Git Commit Log
git log --pretty=format:"%h - %an, %ad : %s" --date=iso > "docs/assignments/HW06/deliverables/git/23127404_HW06_git_commit_log.txt"

# 4. Generate Final Submission ZIP
Compress-Archive -Path "docs/assignments/HW06/deliverables/*" -DestinationPath "docs/assignments/HW06/23127404_HW06_AI_API_100.zip" -Force
```
