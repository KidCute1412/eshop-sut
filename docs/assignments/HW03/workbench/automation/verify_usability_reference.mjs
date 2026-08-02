import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = await import(
  pathToFileURL(path.join(here, "node_modules/playwright/index.mjs")).href
);
const WEB = "http://127.0.0.1:5173";
const API = "http://127.0.0.1:3000/api";

function check(condition, message) {
  if (!condition) throw new Error(message);
}

const login = await fetch(`${API}/login`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ email: "test@eshop.com", password: "Test1234!" }),
});
check(login.ok, `Login failed with HTTP ${login.status}`);
const { token } = await login.json();

const browser = await chromium.launch({ headless: true, channel: "chrome" });
const context = await browser.newContext({
  viewport: { width: 1440, height: 1000 },
  locale: "vi-VN",
});
await context.addInitScript((value) => localStorage.setItem("token", value), token);
const page = await context.newPage();
page.setDefaultTimeout(15_000);

const verified = [];
try {
  await page.goto(WEB, { waitUntil: "networkidle" });
  const cards = page.locator("div.border.rounded.shadow-sm");
  check((await cards.count()) === 5, "Product List does not contain five cards");
  verified.push("five seeded products");

  const iphone = cards.filter({ hasText: "iPhone 15 Pro Max" });
  check((await iphone.count()) === 1, "iPhone 15 Pro Max is not uniquely visible");
  check(/30[.,]000[.,]000/.test(await iphone.innerText()), "iPhone price is not 30,000,000 VND");
  await iphone.getByRole("link", { name: "Xem chi tiết" }).click();
  await page.waitForURL("**/product/1");
  check((await page.locator('input[type="number"]').inputValue()) === "1", "Default quantity is not one");
  verified.push("product details and quantity one");

  const add = page.getByRole("button", { name: "Thêm vào giỏ hàng" });
  await add.click();
  await page.getByRole("link", { name: "Giỏ hàng" }).click();
  check(await page.getByText("Giỏ hàng của bạn đang trống").isVisible(), "First-click defect was not reproduced");
  verified.push("first Add to Cart click has no effect");

  await page.goto(`${WEB}/product/1`, { waitUntil: "networkidle" });
  await page.getByRole("button", { name: "Thêm vào giỏ hàng" }).click();
  await page.getByRole("button", { name: "Thêm vào giỏ hàng" }).click();
  await page.getByRole("link", { name: "Giỏ hàng" }).click();
  check(/30[.,]000[.,]000/.test(await page.locator("main").innerText()), "Cart total is not 30,000,000 VND");
  verified.push("second click adds one item and Cart shows the total");

  await page.getByRole("button", { name: "Tiến hành thanh toán" }).click();
  await page.waitForURL("**/checkout");
  check(await page.locator('input[type="number"]').isEditable(), "Checkout total is no longer editable");
  await page.getByRole("button", { name: "Xác Nhận Thanh Toán" }).click();
  await page.getByText("Thanh toán thành công!").waitFor();
  verified.push("coupon-free checkout success");

  await page.getByRole("button", { name: "Quay lại trang chủ" }).click();
  await page.getByRole("link", { name: "Giỏ hàng" }).click();
  check(await page.getByText("iPhone 15 Pro Max").isVisible(), "Post-checkout cart was unexpectedly cleared");
  verified.push("post-checkout cart remains populated");

  await page.goto(`${WEB}/profile`, { waitUntil: "networkidle" });
  const history = await page.locator("main").innerText();
  check(/30[.,]000[.,]000/.test(history) && history.includes("Chờ xác nhận"), "Pending order is missing from history");
  verified.push("new Order History row has pending status");
  const detailsControls =
    (await page.getByRole("link", { name: /chi tiết|details/i }).count()) +
    (await page.getByRole("button", { name: /chi tiết|details|mở rộng/i }).count());
  check(detailsControls === 0, "An Order History details control now exists");
  verified.push("Order History has no item-details control");

  console.log(JSON.stringify({ browser: browser.version(), verified }, null, 2));
} finally {
  await context.close().catch(() => {});
  await browser.close().catch(() => {});
}
