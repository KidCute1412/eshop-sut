import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC02.json', import.meta.url)));

test('TC02', async ({ page }) => {
  await page.goto(data.inputs.url);

  // Attribute assertion: first product image has a non-empty alt text
  const firstImg = page.locator('img').first();
  await expect(firstImg).toHaveAttribute('alt', /\S+/);

  // Content assertion: first heading is visible and not empty
  const firstHeading = page.getByRole('heading').first();
  await expect(firstHeading).toBeVisible();
  await expect(firstHeading).not.toHaveText('');

  // Price format check
  const priceLocator = page.locator("text=₫").first();
  const priceText = await priceLocator.textContent();
  expect(priceText).toMatch(/\d{1,3}(?:[.,]\d{3})*\s*₫/);
});
