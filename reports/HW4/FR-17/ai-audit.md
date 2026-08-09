# AI Audit - FR-17 Coupon Management (Prompt + Raw AI Output Only)

- AI Tool: Codex (GPT-5)
- Date: 2026-08-06 to 2026-08-09
- Feature: FR-17 Coupon management
- Final reviewed artifacts: [test-cases.md](test-cases.md), [data/coupon-cases.json](data/coupon-cases.json), [tests/fr-17-coupons.spec.js](tests/fr-17-coupons.spec.js), [bug-report.md](bug-report.md)

## Interaction 1 - Generate FR-17 Data-Driven Playwright Automation

- AI Tool: Codex (GPT-5)
- Date: 2026-08-06

### Prompt

```text
Complete HW04 Automation Testing for the EShop SUT.

First, read the repository, the HW04 assignment PDF, the HW02 selected-feature artifacts,
and the existing HW03 report structure. For FR-17 Coupon Management, convert the selected HW02
Domain Testing and Boundary Value Analysis cases into data-driven Playwright automation.

Store all test inputs and expected results in an external JSON data file. Create a Playwright
specification that can run on Chromium, Firefox, and WebKit. Keep the workflow auditable through
test-case documentation, an AI audit, AI gap analysis, bug reporting, and report references.

Use the Admin UI to verify coupon create, list/view, delete, required fields, duplicate code,
type handling, and numeric boundary behavior. Use real network response assertions for create
and delete operations. Do not fabricate execution results. When a real SUT defect is observed,
preserve it as a failing assertion and document the evidence clearly.
```

### AI Output

```text
Created FR-17 automation artifacts under reports/HW4:

- FR-17/data/coupon-cases.json
- FR-17/tests/fr-17-coupons.spec.js
- FR-17/test-cases.md
- FR-17/bug-report.md
- FR-17/ai-gap-analysis.md

Selected initial FR-17 cases:

- FR17-DT-001 create percent coupon
- FR17-DT-002 create fixed coupon
- FR17-DT-003 minimum order amount = 0
- FR17-DT-004 max uses per user = 1
- FR17-DT-005 create then delete coupon
- FR17-DT-006 missing coupon code
- FR17-DT-007 missing discount value
- FR17-DT-008 missing expiry date
- FR17-DT-009 duplicate coupon code
- FR17-BVA-001 expired coupon label
- FR17-BVA-002 large fixed discount
- FR17-BVA-003 lowercase code transformed to uppercase

Generated external test data in FR-17/data/coupon-cases.json:

[
  { "id": "FR17-DT-001", "type": "Positive", "scenario": "create_percent", "codePrefix": "AUTOPCT", "couponType": "percent", "discount": "10", "minimum": "100000", "expiryOffsetDays": 30, "maxUses": "1", "expected": "created" },
  { "id": "FR17-DT-002", "type": "Positive", "scenario": "create_fixed", "codePrefix": "AUTOFIX", "couponType": "fixed", "discount": "50000", "minimum": "200000", "expiryOffsetDays": 30, "maxUses": "2", "expected": "created" },
  { "id": "FR17-DT-009", "type": "Negative", "scenario": "duplicate_code", "codePrefix": "AUTODUP", "couponType": "percent", "discount": "15", "minimum": "1000", "expiryOffsetDays": 20, "maxUses": "1", "expected": "server_error" },
  { "id": "FR17-BVA-001", "type": "Edge", "scenario": "expired_coupon_label", "codePrefix": "AUTOEXP", "couponType": "fixed", "discount": "1000", "minimum": "0", "expiryOffsetDays": -1, "maxUses": "1", "expected": "expired_visible" },
  { "id": "FR17-BVA-002", "type": "Edge", "scenario": "large_discount", "codePrefix": "AUTOBIG", "couponType": "fixed", "discount": "999999", "minimum": "0", "expiryOffsetDays": 20, "maxUses": "1", "expected": "created" },
  { "id": "FR17-BVA-003", "type": "Edge", "scenario": "uppercase_transform", "codePrefix": "autolower", "couponType": "percent", "discount": "7", "minimum": "0", "expiryOffsetDays": 20, "maxUses": "1", "expected": "uppercase_visible" }
]

Generated core Playwright flow in FR-17/tests/fr-17-coupons.spec.js:

const { test, expect, loginAdmin, openCouponsTab } = require("../../fixtures/hw4-test");
const cases = require("../data/coupon-cases.json");

async function fillCouponForm(page, tc, code) {
  const form = page.locator("form").last();
  const inputs = form.locator("input");
  if (tc.codePrefix !== "") {
    await inputs.nth(0).fill(code);
  }
  await form.locator("select").selectOption(tc.couponType);
  if (tc.discount !== "") {
    await inputs.nth(1).fill(tc.discount);
  }
  await inputs.nth(2).fill(tc.minimum);
  if (tc.expiryOffsetDays !== null) {
    await inputs.nth(3).fill(dateWithOffset(tc.expiryOffsetDays));
  }
  await inputs.nth(4).fill(tc.maxUses);
}

async function createCoupon(page, tc, code) {
  await fillCouponForm(page, tc, code);
  const responsePromise = page.waitForResponse((r) =>
    r.url().includes("/api/admin/coupons") && r.request().method() === "POST"
  );
  await page.locator("form").last().locator("button").click();
  return responsePromise;
}

Human review of this first pass found these issues:

- Admin credentials in notes were inconsistent; final fixture uses the actual seeded password `Admin123!`.
- Coupon tab text selectors were brittle because the app has no stable `data-testid` or `id`.
- The feature name suggests CRUD, but the actual Admin UI exposes create/list/delete only; edit was documented as not automated.
- Create/delete tests needed network assertions, not only DOM visibility.
- The initial three BVA cases were observable UI behaviors, but they did not directly target the documented lower-bound constraints.

Initial FR-17 result before the later BVA correction:

- 36 browser executions
- 36 passed
- 0 failed
- This pass result was later judged incomplete because the BVA set did not directly test
  `discount_value > 0`, `min_order_amount >= 0`, and `max_uses_per_user >= 1`.
```

## Interaction 2 - Replace FR-17 BVA With Requirement-Based Lower Bound Cases

- AI Tool: Codex (GPT-5)
- Date: 2026-08-09

### Prompt

```text
Review and fix my FR-17 automation using the requirement below. The requirement is the test
oracle; do not change the Expected Result to match the current SUT behavior just to make tests pass.

FR-17 requirement:
Admin can add, view, and delete coupons.
Fields:
- code is required and unique.
- type is required and only percent or fixed.
- discount_value must be > 0.
- expired_at is required.
- min_order_amount must be >= 0.
- max_uses_per_user must be >= 1.

The actual UI form fields are ordered as:
Coupon code, Type dropdown, Discount value, Minimum order amount, Expiry date, Max uses per user.
The default type is Percent, min_order_amount defaults to 0, and max_uses_per_user defaults to 1.

Keep FR17-DT-001 through FR17-DT-009 unchanged.

Replace the old BVA cases:
- FR17-BVA-001: expired coupon
- FR17-BVA-002: large fixed discount
- FR17-BVA-003: lowercase to uppercase

with these requirement-based boundary tests:

FR17-BVA-001:
Type: Edge / Negative
Scenario: discount_zero
discount_value = 0
Expected: coupon creation is rejected because discount_value must be > 0.

FR17-BVA-002:
Type: Edge / Negative
Scenario: minimum_negative
min_order_amount = -1
Expected: coupon creation is rejected because min_order_amount must be >= 0.

FR17-BVA-003:
Type: Edge / Negative
Scenario: max_uses_zero
max_uses_per_user = 0
Expected: coupon creation is rejected because max_uses_per_user must be >= 1.

Make the three boundary pairs clear:
- min_order_amount: -1 rejects, 0 succeeds.
- max_uses_per_user: 0 rejects, 1 succeeds.
- discount_value: 0 rejects, >0 succeeds.
```

### AI Output

```text
Updated FR-17/data/coupon-cases.json:

- Kept FR17-DT-001 through FR17-DT-009 unchanged.
- Replaced FR17-BVA-001 with scenario discount_zero:
  discount_value = "0", expected = "rejected".
- Replaced FR17-BVA-002 with scenario minimum_negative:
  min_order_amount = "-1", expected = "rejected".
- Replaced FR17-BVA-003 with scenario max_uses_zero:
  max_uses_per_user = "0", expected = "rejected".

Updated final BVA data:

[
  { "id": "FR17-BVA-001", "type": "Edge / Negative", "scenario": "discount_zero", "codePrefix": "AUTOZERODISCOUNT", "couponType": "fixed", "discount": "0", "minimum": "0", "expiryOffsetDays": 20, "maxUses": "1", "expected": "rejected" },
  { "id": "FR17-BVA-002", "type": "Edge / Negative", "scenario": "minimum_negative", "codePrefix": "AUTONEGMIN", "couponType": "fixed", "discount": "50000", "minimum": "-1", "expiryOffsetDays": 20, "maxUses": "1", "expected": "rejected" },
  { "id": "FR17-BVA-003", "type": "Edge / Negative", "scenario": "max_uses_zero", "codePrefix": "AUTOZEROMAX", "couponType": "fixed", "discount": "50000", "minimum": "0", "expiryOffsetDays": 20, "maxUses": "0", "expected": "rejected" }
]

Updated FR-17/tests/fr-17-coupons.spec.js:

- Added attemptCreateCoupon(page, tc, code).
- Added an expected === "rejected" branch.
- If no POST request is sent, the test checks native HTML validation through checkValidity().
- If a POST request is sent, the test requires HTTP status >= 400.
- The coupon code must not appear in the table after a rejected creation attempt.
- Removed obsolete expired_visible and uppercase_visible expected branches because the old BVA
  cases were replaced.

Generated corrected negative-boundary assertion:

async function attemptCreateCoupon(page, tc, code) {
  await fillCouponForm(page, tc, code);
  const responsePromise = page
    .waitForResponse((r) => r.url().includes("/api/admin/coupons") && r.request().method() === "POST", {
      timeout: 1500
    })
    .catch(() => null);

  await page.locator("form").last().locator("button").click();
  return responsePromise;
}

if (tc.expected === "rejected") {
  const response = await attemptCreateCoupon(page, tc, code);
  if (response === null) {
    const invalidInputs = await page.locator("form").last().locator("input").evaluateAll((inputs) =>
      inputs.filter((input) => !input.checkValidity()).length
    );
    expect(invalidInputs).toBeGreaterThan(0);
  } else {
    expect(response.status()).toBeGreaterThanOrEqual(400);
  }
  await expect(page.locator("td").filter({ hasText: code })).toHaveCount(0);
  return;
}

Updated FR-17/test-cases.md:

- Replaced the old BVA rows with:
  - FR17-BVA-001: discount_value = 0 must be rejected.
  - FR17-BVA-002: min_order_amount = -1 must be rejected.
  - FR17-BVA-003: max_uses_per_user = 0 must be rejected.
- Added boundary pair coverage:
  - discount_value: 0 -> reject, >0 -> success.
  - min_order_amount: -1 -> reject, 0 -> success.
  - max_uses_per_user: 0 -> reject, 1 -> success.

Ran data-driven validator:

Command:
python .agents\skills\automation-testing\scripts\validate_test_data.py .\reports\HW4\FR-17

Raw result:

Validation passed: 1 spec file(s), 1 external data file(s).

Ran FR-17 Chromium check:

Command:
$env:HW4_SKIP_WEBSERVER='1';
$env:ADMIN_BASE_URL='http://127.0.0.1:5177';
npx playwright test FR-17/tests/fr-17-coupons.spec.js --project=chromium --timeout=30000

Raw result:

Running 12 tests using 1 worker

  2 failed
  10 passed

Failed Chromium cases:

- FR17-BVA-001: expected HTTP >= 400 for discount_value = 0, received HTTP 200.
- FR17-BVA-002: expected HTTP >= 400 for min_order_amount = -1, received HTTP 200.
- FR17-BVA-003 passed because max_uses_per_user = 0 was blocked by native UI validation before
  any create request was submitted.

Ran FR-17 multi-browser suite:

Command:
$env:HW4_SKIP_WEBSERVER='1';
$env:ADMIN_BASE_URL='http://127.0.0.1:5177';
npx playwright test FR-17/tests/fr-17-coupons.spec.js --timeout=30000

Raw result:

Running 36 tests using 1 worker

  6 failed
  30 passed

Failed cases on Chromium, Firefox, and WebKit:

- FR17-BVA-001: discount_value = 0 is accepted with HTTP 200.
- FR17-BVA-002: min_order_amount = -1 is accepted with HTTP 200.

Passing boundary control:

- FR17-BVA-003: max_uses_per_user = 0 is rejected by native UI validation.

Recorded FR-17 bugs:

- BUG-HW04-FR17-001 - Coupon creation accepts discount_value = 0.
- BUG-HW04-FR17-002 - Coupon creation accepts min_order_amount = -1.

Updated affected reports:

- FR-17/test-cases.md
- FR-17/data/coupon-cases.json
- FR-17/tests/fr-17-coupons.spec.js
- FR-17/bug-report.md
- FR-17/ai-gap-analysis.md
- automation-report.md
- README.md
- main-report.md
```
