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

async function addSameProductTwice(page) {
  await page.goto("/");
  await expect(page.locator(".grid button").first()).toBeVisible();
  await page.locator(".grid button").first().click();
  await page.locator(".grid button").first().click();
  await page.locator("a[href='/cart']").click();
}

async function confirmDelete(page, deleteButton) {
  const dialogPromise = page.waitForEvent("dialog", { timeout: 1500 }).catch(() => null);
  await deleteButton.click();
  const dialog = await dialogPromise;

  expect(dialog, "Deleting a cart item must show a confirmation dialog before removal").not.toBeNull();
  expect(dialog.type()).toBe("confirm");
  await dialog.accept();
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

      if (tc.scenario === "add_two_distinct") {
        await addProducts(page, 2);
        await expect(page.locator("tbody tr")).toHaveCount(tc.expectedRows);
      }

      if (tc.scenario === "add_duplicate") {
        await addSameProductTwice(page);
        await expect(page.locator("tbody tr")).toHaveCount(tc.expectedRows);
        await expect(page.locator("tbody tr").first().locator("td").nth(2)).toHaveText(tc.expectedQuantity);
      }

      if (tc.scenario === "remove_only") {
        await addProducts(page, 1);
        await confirmDelete(page, page.locator("tbody button").first());
        await expect(page.locator("tbody tr")).toHaveCount(tc.expectedRows);
        await expect(page.locator("h2")).toBeVisible();
      }

      if (tc.scenario === "remove_first_of_two") {
        await addProducts(page, 2);
        await confirmDelete(page, page.locator("tbody button").first());
        await expect(page.locator("tbody tr")).toHaveCount(tc.expectedRows);
      }

      if (tc.scenario === "guest_checkout_redirect") {
        page.on("dialog", (dialog) => dialog.accept());
        await addProducts(page, 1);
        await page.locator("button").filter({ hasText: /thanh/i }).click();
        await expect(page).toHaveURL(/\/login$/);
      }

      if (tc.scenario === "continue_from_empty") {
        await page.goto("/cart");
        await page.locator("main a[href='/']").last().click();
        await expect(page).toHaveURL(/\/$/);
      }

      if (tc.scenario === "continue_from_nonempty") {
        await addProducts(page, 1);
        await page.locator("a[href='/']").last().click();
        await expect(page).toHaveURL(/\/$/);
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

      if (tc.scenario === "quantity_display_one") {
        await addProducts(page, 1);
        await expect(page.locator("tbody tr").first().locator("td").nth(2)).toHaveText(tc.expectedQuantity);
      }

      if (tc.scenario === "quantity_plus_control") {
        await addProducts(page, 1);
        const row = page.locator("tbody tr").first();
        const plusButton = row.getByRole("button", { name: /^\+$/ });
        await expect(plusButton, "Cart item must provide a + quantity control").toBeVisible();
        await plusButton.click();
        await expect(row.locator("td").nth(2)).toHaveText(tc.expectedQuantity);
      }

      if (tc.scenario === "quantity_minus_control") {
        await addSameProductTwice(page);
        const row = page.locator("tbody tr").first();
        const minusButton = row.getByRole("button", { name: /^-$/ });
        await expect(minusButton, "Cart item must provide a - quantity control").toBeVisible();
        await minusButton.click();
        await expect(row.locator("td").nth(2)).toHaveText(tc.expectedQuantity);
      }
    });
  }
});
