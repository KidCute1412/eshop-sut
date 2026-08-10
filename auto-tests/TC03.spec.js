import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC03.json', import.meta.url)));

test(data.id, async ({ page }) => {
  await page.goto(data.inputs.url);

  // Ensure one H1
  await expect(page.locator('h1')).toHaveCount(1);

  // Enter search term and submit
  await page.getByRole('textbox', { name: data.inputs.searchBoxName }).fill(data.inputs.search);
  await page.getByRole('button', { name: data.inputs.searchButtonName }).click();

  // Expect the search box to contain the typed query
  await expect(page.getByRole('textbox', { name: data.inputs.searchBoxName })).toHaveValue(data.inputs.search);

  // Content assertion: matching product is visible
  await expect(page.getByText(data.expected.matchingProduct)).toBeVisible();

  // Safe rendering: ensure displayed texts do not include raw HTML
  const contents = await page.locator('main').allTextContents();
  for (const c of contents) expect(c).not.toContain('<');
});
