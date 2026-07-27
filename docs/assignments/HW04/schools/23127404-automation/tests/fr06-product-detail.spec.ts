import { expect, test } from "@playwright/test";
import { readFileSync } from "node:fs";

type ProductDetailData = {
  testCaseId: string;
  description: string;
  traceability: string[];
  productPath: string;
  expected: {
    name: string;
    price: string;
    description: string;
    category: string;
  };
};

const testData = JSON.parse(
  readFileSync(
    new URL("../test-data/fr06-product-detail.json", import.meta.url),
    "utf8",
  ),
) as ProductDetailData;

test(`${testData.testCaseId}: ${testData.description}`, async ({ page }) => {
  await page.goto(testData.productPath);

  await expect(page).toHaveURL(new RegExp(`${testData.productPath}/?$`));

  const productHeading = page.getByRole("heading", {
    level: 1,
    name: testData.expected.name,
    exact: true,
  });
  await expect(productHeading).toHaveCount(1);
  await expect(productHeading).toBeVisible();

  const productImage = page.getByRole("img", {
    name: testData.expected.name,
    exact: true,
  });
  await expect(productImage).toBeVisible();
  await expect(productImage).toHaveAttribute("src", /.+/);

  await expect(
    page.getByText(testData.expected.price, { exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText(testData.expected.description, { exact: true }),
  ).toBeVisible();

  // FR-06 requires the category to be displayed. This assertion intentionally
  // remains strict so a missing category is reported as an SUT defect.
  await expect(
    page.getByText(testData.expected.category, { exact: true }),
  ).toBeVisible();
});

