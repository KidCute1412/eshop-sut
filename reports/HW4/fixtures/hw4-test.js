const { test: base, expect } = require("@playwright/test");

const STUDENT_ID = process.env.STUDENT_ID || "23127539";
const ADMIN_EMAIL = process.env.ADMIN_EMAIL || "admin@eshop.com";
const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD || "Admin123!";
const RUN_ID = process.env.RUN_ID || `${Date.now()}`;

const test = base.extend({});

test.beforeEach(async ({}, testInfo) => {
  testInfo.annotations.push({
    type: "Run by",
    description: `${STUDENT_ID} - ${new Date().toISOString()}`
  });
});

function uniqueEmail(prefix) {
  return `${prefix}.${RUN_ID}@example.test`;
}

async function fillCustomerRegisterForm(page, data) {
  const form = page.locator("form");
  const inputs = form.locator("input");

  if (data.name !== null) {
    await inputs.nth(0).fill(data.name);
  }
  if (data.email !== null) {
    await inputs.nth(1).fill(data.email || uniqueEmail(data.emailPrefix));
  }
  if (data.password !== null) {
    await inputs.nth(2).fill(data.password);
  }
}

async function loginAdmin(page) {
  await page.goto(process.env.ADMIN_BASE_URL || "http://localhost:5174");
  await page.getByPlaceholder("Email").fill(ADMIN_EMAIL);
  await page.getByPlaceholder("Password").fill(ADMIN_PASSWORD);
  await Promise.all([
    page.waitForResponse((r) => r.url().includes("/api/login")),
    page.locator("form button").click()
  ]);
  await expect(page.getByText("EShop Admin")).toBeVisible();
}

async function openCouponsTab(page) {
  await page.locator("ul li").nth(3).click();
  await expect(page.locator("form").filter({ has: page.locator("button") }).last()).toBeVisible();
}

async function addFirstProductToCart(page) {
  await page.goto("/");
  await expect(page.locator(".grid").locator("button").first()).toBeVisible();
  const productName = (await page.locator(".grid h2").first().innerText()).trim();
  await page.locator(".grid button").first().click();
  await page.goto("/cart");
  await expect(page.locator("tbody tr")).toHaveCount(1);
  return productName;
}

module.exports = {
  test,
  expect,
  uniqueEmail,
  fillCustomerRegisterForm,
  loginAdmin,
  openCouponsTab,
  addFirstProductToCart
};
