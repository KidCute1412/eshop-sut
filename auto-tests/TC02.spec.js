import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC02.json', import.meta.url)));

test(data.id, async ({ page }) => {
  await page.goto(data.inputs.url);

  // Ensure one H1
  await expect(page.locator('h1')).toHaveCount(1);

  // Attribute assertion: first product image has correct alt text
  const firstImg = page.locator('img').first();
  await expect(firstImg).toHaveAttribute('alt', data.expected.firstImageAlt ? data.expected.firstImageAlt : /\S+/);

  // Content assertion: first product name contains expected substring
  await expect(page.getByRole('heading').first()).toContainText(data.expected.firstProductNamePart);

  // Price format check
  const priceLocator = page.locator("text=₫").first();
  const priceText = await priceLocator.textContent();
  expect(priceText).toMatch(/\d{1,3}(?:[.,]\d{3})*\s*₫/);
});
