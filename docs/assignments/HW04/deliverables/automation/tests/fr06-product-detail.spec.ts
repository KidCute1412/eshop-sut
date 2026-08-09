import { expect, test } from "@playwright/test";
import { loadCases } from "../src/data-loader.js";
import type { ProductDetailCase } from "../src/types.js";

const cases = loadCases<ProductDetailCase>("../test-data/fr06-product-detail.json", 12);

function digits(value: string): string {
  return value.replace(/\D/g, "");
}

test.describe("FR-06 Product Detail", () => {
  for (const row of cases) {
    test(`${row.id} [${row.priority}] ${row.title}`, async ({ page }) => {
      await test.step(`Traceability: ${[...row.partition, ...(row.boundary ?? [])].join(", ")}`, async () => {});
      await page.goto(`/product/${row.productId}`);

      const main = page.locator("main");
      const quantity = main.getByRole("spinbutton");
      const addButton = main.getByRole("button");

      switch (row.assertion) {
        case "full-content": {
          await expect(main.getByRole("heading", { level: 1 })).toHaveText(row.expected!.name!);
          await expect(main.getByRole("img", { name: row.expected!.name! })).toBeVisible();
          await expect(main).toContainText(row.expected!.description!);
          const priceText = await main.locator("p.font-bold").first().innerText();
          expect(digits(priceText)).toBe(row.expected!.price);
          break;
        }
        case "single-heading":
          await expect(main.locator("h1")).toHaveCount(1);
          await expect(main.locator("h1")).toHaveText(row.expected!.name!);
          break;
        case "image": {
          const image = main.getByRole("img", { name: row.expected!.name! });
          await expect(image).toBeVisible();
          await expect(image).toHaveAttribute("alt", row.expected!.name!);
          await expect(image).toHaveClass(/w-full/);
          break;
        }
        case "price": {
          const priceText = await main.locator("p.font-bold").first().innerText();
          expect(priceText).not.toContain("NaN");
          expect(priceText).toContain("₫");
          expect(digits(priceText)).toBe(row.expected!.price);
          expect(priceText).toMatch(/\d[.,]\d{3}[.,]\d{3}/);
          break;
        }
        case "description":
          await expect(main).toContainText(row.expected!.description!);
          break;
        case "category":
          await expect(main.getByText(row.expected!.category!, { exact: true })).toBeVisible();
          break;
        case "quantity-type":
          await expect(quantity).toHaveAttribute("type", "number");
          break;
        case "quantity-min":
          await expect(quantity).toHaveAttribute("min", "1");
          break;
        case "quantity-default":
          await expect(quantity).toHaveValue("1");
          break;
        case "add-feedback-first-click":
        case "add-feedback-valid-quantity":
          await quantity.fill(row.quantity!);
          await expect(quantity).toHaveValue(row.quantity!);
          await addButton.click();
          await expect(addButton).toContainText(/Đã thêm/i);
          break;
        case "reject-zero":
        case "reject-negative":
        case "reject-fraction":
          await quantity.fill(row.quantity!);
          expect(await quantity.evaluate((input: HTMLInputElement) => input.validity.valid)).toBe(false);
          break;
        case "not-found":
          await expect(main).toContainText(/không tồn tại|not found/i);
          await expect(main.locator("h1")).toHaveCount(0);
          break;
      }
    });
  }
});
