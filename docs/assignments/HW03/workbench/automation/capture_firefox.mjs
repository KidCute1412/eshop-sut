import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(here, "../../../../..");
const { firefox } = await import(
  pathToFileURL(path.join(here, "node_modules/playwright/index.mjs")).href
);

const WEB = "http://127.0.0.1:5173";
const API = "http://127.0.0.1:3000/api";
const output = path.join(
  repo,
  "docs/assignments/HW03/deliverables/cross_platform/firefox_desktop",
);

await fs.mkdir(output, { recursive: true });

const login = await fetch(`${API}/login`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ email: "test@eshop.com", password: "Test1234!" }),
});
if (!login.ok) throw new Error(`Login failed with HTTP ${login.status}`);
const { token } = await login.json();

const browser = await firefox.launch({ headless: true });
const version = browser.version();
const context = await browser.newContext({
  viewport: { width: 1440, height: 1000 },
  locale: "vi-VN",
});
await context.addInitScript((value) => localStorage.setItem("token", value), token);
const page = await context.newPage();
page.setDefaultTimeout(15_000);

async function capture(filename) {
  await page.evaluate(({ browserVersion }) => {
    document.getElementById("hw03-evidence-caption")?.remove();
    const node = document.createElement("div");
    node.id = "hw03-evidence-caption";
    node.textContent =
      `23127404@hcmus.edu.vn | Firefox ${browserVersion} Desktop | Windows | ${location.href}`;
    Object.assign(node.style, {
      position: "fixed", right: "8px", bottom: "8px", zIndex: "2147483647",
      padding: "6px 9px", color: "#fff", background: "rgba(17,24,39,.88)",
      borderRadius: "4px", font: "12px/1.3 Arial, sans-serif", maxWidth: "70vw",
    });
    document.body.appendChild(node);
  }, { browserVersion: version });
  await page.screenshot({ path: path.join(output, filename), fullPage: true });
}

try {
  await page.goto(WEB, { waitUntil: "networkidle" });
  await capture("01_product_list.png");

  await page.getByRole("link", { name: "Xem chi tiết" }).first().click();
  await page.waitForURL("**/product/**");
  await capture("02_product_detail.png");

  // The verified SUT defect requires two clicks from Product Detail.
  await page.getByRole("button", { name: "Thêm vào giỏ hàng" }).click();
  await page.getByRole("button", { name: "Thêm vào giỏ hàng" }).click();
  await page.getByRole("link", { name: "Giỏ hàng" }).click();
  await page.waitForURL("**/cart");
  await capture("03_cart.png");

  await page.getByRole("button", { name: "Tiến hành thanh toán" }).click();
  await page.waitForURL("**/checkout");
  await capture("04_checkout.png");

  await page.goto(`${WEB}/profile`, { waitUntil: "networkidle" });
  await capture("05_order_history.png");

  console.log(JSON.stringify({ browser: "Firefox", version, screenshots: 5 }));
} finally {
  await context.close().catch(() => {});
  await browser.close().catch(() => {});
}
