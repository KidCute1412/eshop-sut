import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC04.json', import.meta.url)));

test('TC04', async ({ page }) => {
  await page.goto(data.inputs.url);


  // Enter a blank search (single space) and submit
  await page.getByRole('textbox', { name: data.inputs.searchBoxName }).fill(data.inputs.search);
  await page.getByRole('button', { name: data.inputs.searchButtonName }).click();

  // Structural assertion: full product list is shown again
  await expect(page.getByRole('article')).toHaveCount(data.expected.fullCount);

  // Price format check on first visible product
  const price = page.locator("text=₫").first();
  const priceText = await price.textContent();
  expect(priceText).toMatch(/\d{1,3}(?:[.,]\d{3})*\s*₫/);
});
