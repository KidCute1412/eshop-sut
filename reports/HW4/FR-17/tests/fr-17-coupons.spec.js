const { test, expect, loginAdmin, openCouponsTab } = require("../../fixtures/hw4-test");
const cases = require("../data/coupon-cases.json");

function dateWithOffset(days) {
  const date = new Date();
  date.setDate(date.getDate() + days);
  return date.toISOString().slice(0, 10);
}

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

test.describe("FR-17 Coupon management", () => {
  for (const tc of cases) {
    test(`${tc.id} ${tc.type} ${tc.scenario}`, async ({ page }) => {
      const suffix = `${Date.now()}${test.info().workerIndex}`;
      const code = `${tc.codePrefix}${suffix}`.toUpperCase();

      await loginAdmin(page);
      await openCouponsTab(page);

      if (tc.expected === "native_required") {
        await fillCouponForm(page, tc, code);
        await page.locator("form").last().locator("button").click();
        const invalidInputs = await page.locator("form").last().locator("input").evaluateAll((inputs) =>
          inputs.filter((input) => !input.checkValidity()).length
        );
        expect(invalidInputs).toBeGreaterThan(0);
        return;
      }

      if (tc.expected === "server_error") {
        await createCoupon(page, tc, code);
        await expect(page.locator("td").filter({ hasText: code })).toBeVisible();
        page.on("dialog", (dialog) => dialog.accept());
        const secondResponse = await createCoupon(page, tc, code);
        expect(secondResponse.status()).toBeGreaterThanOrEqual(400);
        return;
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

      const response = await createCoupon(page, tc, code);
      expect(response.ok()).toBeTruthy();
      await expect(page.locator("td").filter({ hasText: code })).toBeVisible();

      if (tc.expected === "deleted") {
        const row = page.locator("tr").filter({ hasText: code });
        const deleteResponse = page.waitForResponse((r) =>
          r.url().includes("/api/admin/coupons/") && r.request().method() === "DELETE"
        );
        await row.locator("button").click();
        expect((await deleteResponse).ok()).toBeTruthy();
        await expect(row).toHaveCount(0);
      }

    });
  }
});
