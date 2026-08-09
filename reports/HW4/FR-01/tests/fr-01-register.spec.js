const {
  test,
  expect,
  uniqueEmail,
  fillCustomerRegisterForm
} = require("../../fixtures/hw4-test");
const cases = require("../data/register-cases.json");

test.describe("FR-01 Account registration", () => {
  for (const tc of cases) {
    test(`${tc.id} ${tc.type} registration`, async ({ page, request }) => {
      const data = { ...tc };
      if (data.email === "") {
        data.email = uniqueEmail(data.emailPrefix);
      }

      if (data.expected === "duplicate_error") {
        await request.post("http://localhost:3000/api/register", {
          data: {
            name: "Existing Automation User",
            email: data.email,
            password: data.password
          }
        });
      }

      await page.goto("/register");
      await fillCustomerRegisterForm(page, data);

      const submitResponse =
        data.expected === "success" || data.expected === "duplicate_error"
          ? page
              .waitForResponse(
                (r) =>
                  r.url().includes("/api/register") &&
                  r.request().method() === "POST",
                { timeout: 5000 }
              )
              .catch(() => null)
          : Promise.resolve(null);

      await page.locator("form button[type='submit']").click();
      const response = await submitResponse;

      if (data.expected === "success") {
        expect(response && response.ok()).toBeTruthy();
        await expect(page).toHaveURL(/\/login$/);
      }
      
      if (data.expected === "password_error") {
        await expect(page.locator("[class*='bg-red']").first()).toBeVisible();
        await expect(page).toHaveURL(/\/register$/);
      }

      if (data.expected === "duplicate_error") {
        expect(response && response.status()).toBe(500);
        await expect(page.locator("[class*='bg-red']").first()).toBeVisible();
      }

      if (data.expected && data.expected.startsWith("native_required")) {
        await expect(page).toHaveURL(/\/register$/);
        const invalidInputs = await page.locator("form input").evaluateAll((inputs) =>
          inputs.filter((input) => !input.checkValidity()).length
        );
        expect(invalidInputs).toBeGreaterThan(0);
      }
    });
  }
});
