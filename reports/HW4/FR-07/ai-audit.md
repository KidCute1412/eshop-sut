# AI Audit - FR-07 Shopping Cart (Prompt + Raw AI Output Only)

- AI Tool: Codex (GPT-5)
- Date: 2026-08-06 to 2026-08-08
- Feature: FR-07 Shopping cart
- Final reviewed artifacts: [test-cases.md](test-cases.md), [data/cart-cases.json](data/cart-cases.json), [tests/fr-07-cart.spec.js](tests/fr-07-cart.spec.js), [bug-report.md](bug-report.md)

## Interaction 1 - Generate FR-07 Data-Driven Playwright Automation

- AI Tool: Codex (GPT-5)
- Date: 2026-08-06

### Prompt

```text
Complete HW04 Automation Testing for the EShop SUT.

First, read the repository, the HW04 assignment PDF, the HW02 selected-feature artifacts,
and the existing HW03 report structure. For FR-07 Shopping Cart, convert the selected HW02
Domain Testing and Boundary Value Analysis cases into data-driven Playwright automation.

Store all test inputs and expected results in an external JSON data file. Create a Playwright
specification that can run on Chromium, Firefox, and WebKit. Keep the workflow auditable through
test-case documentation, an AI audit, AI gap analysis, bug reporting, and report references.

Use Playwright assertions that verify observable cart behavior, including empty cart state,
add-to-cart behavior, row counts, remove behavior, checkout navigation, continue-shopping
navigation, table headers, total display, and quantity display. Do not fabricate execution
results. When a real SUT defect is observed, preserve it as a failing assertion and document
the evidence clearly.
```

### AI Output

```text
Created FR-07 automation artifacts under reports/HW4:

- FR-07/data/cart-cases.json
- FR-07/tests/fr-07-cart.spec.js
- FR-07/test-cases.md
- FR-07/bug-report.md
- FR-07/ai-gap-analysis.md

Selected initial FR-07 cases:

- FR07-DT-001 empty cart state
- FR07-DT-002 add one product
- FR07-DT-003 add two distinct products
- FR07-DT-004 add the same product twice
- FR07-DT-005 remove one product
- FR07-DT-006 remove one of two products
- FR07-DT-007 guest checkout redirect
- FR07-DT-008 continue shopping from empty cart
- FR07-DT-009 continue shopping from non-empty cart
- FR07-DT-010 cart table headers
- FR07-DT-011 total display
- FR07-BVA-001 quantity display equals 1

Generated external test data in FR-07/data/cart-cases.json:

[
  { "id": "FR07-DT-001", "type": "Positive", "scenario": "empty_cart", "expectedRows": 0 },
  { "id": "FR07-DT-002", "type": "Positive", "scenario": "add_single", "expectedRows": 1 },
  { "id": "FR07-DT-003", "type": "Positive", "scenario": "add_two_distinct", "expectedRows": 2 },
  { "id": "FR07-DT-004", "type": "Edge", "scenario": "add_duplicate", "expectedRows": 2 },
  { "id": "FR07-DT-005", "type": "Positive", "scenario": "remove_only", "expectedRows": 0 },
  { "id": "FR07-DT-006", "type": "Positive", "scenario": "remove_first_of_two", "expectedRows": 1 },
  { "id": "FR07-DT-007", "type": "Negative", "scenario": "guest_checkout_redirect", "expectedPath": "/login" },
  { "id": "FR07-DT-008", "type": "Positive", "scenario": "continue_from_empty", "expectedPath": "/" },
  { "id": "FR07-DT-009", "type": "Positive", "scenario": "continue_from_nonempty", "expectedPath": "/" },
  { "id": "FR07-DT-010", "type": "Positive", "scenario": "headers_visible", "expectedRows": 1 },
  { "id": "FR07-DT-011", "type": "Positive", "scenario": "total_visible", "expectedRows": 1 },
  { "id": "FR07-BVA-001", "type": "Edge", "scenario": "quantity_display_one", "expectedQuantity": "1" }
]

Generated core Playwright loop in FR-07/tests/fr-07-cart.spec.js:

const { test, expect } = require("../../fixtures/hw4-test");
const cases = require("../data/cart-cases.json");

async function addProducts(page, count) {
  await page.goto("/");
  await expect(page.locator(".grid button").first()).toBeVisible();
  for (let i = 0; i < count; i += 1) {
    await page.locator(".grid button").nth(i).click();
  }
  await page.locator("a[href='/cart']").click();
}

test.describe("FR-07 Shopping cart", () => {
  for (const tc of cases) {
    test(`${tc.id} ${tc.type} ${tc.scenario}`, async ({ page }) => {
      if (tc.scenario === "empty_cart") {
        await page.goto("/cart");
        await expect(page.locator("h2")).toBeVisible();
        await expect(page.locator("main a[href='/']").last()).toBeVisible();
        await expect(page.locator("tbody tr")).toHaveCount(0);
      }

      if (tc.scenario === "add_single") {
        await addProducts(page, 1);
        await expect(page.locator("tbody tr")).toHaveCount(tc.expectedRows);
      }

      if (tc.scenario === "add_duplicate") {
        await page.goto("/");
        await expect(page.locator(".grid button").first()).toBeVisible();
        await page.locator(".grid button").first().click();
        await page.locator(".grid button").first().click();
        await page.locator("a[href='/cart']").click();
        await expect(page.locator("tbody tr")).toHaveCount(tc.expectedRows);
      }
    });
  }
});

Human review of this first pass found these issues:

- Page reload navigation lost React cart context; changed to SPA link navigation.
- `a[href='/']` matched multiple links; scoped Continue Shopping locators under `main`.
- Duplicate-add expected value was based on the current implementation instead of the requirement.
- Delete tests checked only the final row count and skipped the required confirmation dialog.
- Header and total checks were too weak because they verified presence/count instead of exact text.
- Quantity-control coverage was incomplete because only the display value `1` was automated.

Initial FR-07 result before the later oracle correction:

- 36 browser executions
- 36 passed
- 0 failed
- This pass result was later judged too weak because several assertions matched the SUT's current
  behavior instead of the HW02/FR-07 requirement oracle.
```

## Interaction 2 - Strengthen FR-07 Cart Oracle and Assertions

- AI Tool: Codex (GPT-5)
- Date: 2026-08-08

### Prompt

```text
Revise the FR-07 Shopping Cart automation and reports based on the following human review findings.

For FR07-DT-004, adding the same product twice must be tested as one cart row with quantity = 2,
not two separate rows. For FR07-DT-005, deletion must first verify a confirmation dialog; only
after confirming should the cart become empty. For FR07-DT-006, deletion of one item from a
two-item cart must also verify the confirmation dialog before checking that one row remains.

For FR07-DT-010, do not only check that five headers exist. Verify the exact required header names:
Sản phẩm, Đơn giá, Số lượng, Thành tiền, and Thao tác. For FR07-DT-011, do not only check that
the total area is visible. Verify the exact total label Tổng cộng. Keep FR07-BVA-001 for quantity
= 1, but add tests for the + and - quantity controls.

Update the external JSON test data, Playwright spec, FR-07 test-case report, bug report, automation
summary, and AI gap analysis based only on real execution evidence.
```

### AI Output

```text
Updated FR-07/data/cart-cases.json:

- FR07-DT-004 changed from expectedRows = 2 to expectedRows = 1 and expectedQuantity = "2".
- FR07-DT-005 and FR07-DT-006 now mark deletion as requiring confirmation.
- FR07-DT-010 now stores expectedHeaders:
  ["Sản phẩm", "Đơn giá", "Số lượng", "Thành tiền", "Thao tác"]
- FR07-DT-011 now stores expectedTotalLabel = "Tổng cộng".
- FR07-BVA-001 was retained for quantity display "1".
- FR07-BVA-002 was added for the + quantity control.
- FR07-BVA-003 was added for the - quantity control.

Updated FR-07/tests/fr-07-cart.spec.js:

- Added addSameProductTwice(page) helper.
- Added confirmDelete(page, deleteButton) helper using page.waitForEvent("dialog").
- FR07-DT-004 now asserts one row and quantity text "2".
- FR07-DT-005 and FR07-DT-006 now require a confirmation dialog before row-count assertions.
- FR07-DT-010 now compares the full header array against the required names.
- FR07-DT-011 now requires "Tổng cộng" and rejects "Tổng tạm tính".
- FR07-BVA-002 expects a visible + button and then quantity "2".
- FR07-BVA-003 expects a visible - button and then quantity "1".

Generated representative corrected code:

async function confirmDelete(page, deleteButton) {
  const dialogPromise = page.waitForEvent("dialog", { timeout: 1500 }).catch(() => null);
  await deleteButton.click();
  const dialog = await dialogPromise;

  expect(dialog, "Deleting a cart item must show a confirmation dialog before removal").not.toBeNull();
  expect(dialog.type()).toBe("confirm");
  await dialog.accept();
}

if (tc.scenario === "headers_visible") {
  await addProducts(page, 1);
  const headers = (await page.locator("thead th").allInnerTexts()).map((header) => header.trim());
  expect(headers).toEqual(tc.expectedHeaders);
}

if (tc.scenario === "total_visible") {
  await addProducts(page, 1);
  const totalLine = page.locator(".text-xl.font-bold").filter({ has: page.locator(".text-red-600") });
  await expect(totalLine).toContainText(tc.expectedTotalLabel);
  await expect(totalLine).not.toContainText("Tổng tạm tính");
}

Ran FR-07 Chromium focused check:

Command:
$env:HW4_SKIP_WEBSERVER='1';
$env:WEB_BASE_URL='http://127.0.0.1:5176';
npx playwright test FR-07/tests/fr-07-cart.spec.js --project=chromium --timeout=30000

Raw result:

Running 14 tests using 1 worker

  7 failed
  7 passed

Failed Chromium cases:

- FR07-DT-004: Expected one row, received two rows.
- FR07-DT-005: No confirmation dialog appeared before deletion.
- FR07-DT-006: No confirmation dialog appeared before deletion.
- FR07-DT-010: Expected `Đơn giá`, received `Giá`.
- FR07-DT-011: Expected `Tổng cộng`, received `Tổng tạm tính`.
- FR07-BVA-002: + quantity control was not found.
- FR07-BVA-003: - quantity control was not found.

Ran FR-07 multi-browser suite:

Command:
$env:HW4_SKIP_WEBSERVER='1';
$env:WEB_BASE_URL='http://127.0.0.1:5176';
npx playwright test FR-07/tests/fr-07-cart.spec.js --timeout=30000

Raw result:

Running 42 tests using 1 worker

  21 failed
  21 passed

Failed cases on Chromium, Firefox, and WebKit:

- FR07-DT-004: duplicate product creates separate rows instead of one row with quantity 2
- FR07-DT-005: delete only item has no confirmation dialog
- FR07-DT-006: delete one of two items has no confirmation dialog
- FR07-DT-010: table header uses `Giá` instead of required `Đơn giá`
- FR07-DT-011: total label uses `Tổng tạm tính` instead of required `Tổng cộng`
- FR07-BVA-002: missing + quantity control
- FR07-BVA-003: missing - quantity control

Recorded FR-07 bugs:

- BUG-HW04-FR07-001 - Duplicate product creates separate cart rows
- BUG-HW04-FR07-002 - Delete does not show confirmation before removal
- BUG-HW04-FR07-003 - Cart header uses `Giá` instead of `Đơn giá`
- BUG-HW04-FR07-004 - Total label is not `Tổng cộng`
- BUG-HW04-FR07-005 - Cart page has no `+` / `-` quantity controls

Updated affected reports:

- FR-07/test-cases.md
- FR-07/data/cart-cases.json
- FR-07/tests/fr-07-cart.spec.js
- FR-07/bug-report.md
- FR-07/ai-gap-analysis.md
- automation-report.md
- README.md
- main-report.md

Validation:

- Data-driven validation passed for FR-07:
  Validation passed: 1 spec file(s), 1 external data file(s).
- HTML report validation was not finalized after the interrupted wrapper run. The previous direct
  Playwright run produced valid execution results but overwrote the HTML report without the wrapper
  stamp, so the HTML report needs to be regenerated through scripts/run-with-report-stamp.js before
  final submission.
```
