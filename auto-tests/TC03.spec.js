import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC03.json', import.meta.url)));

test('TC03', async ({ page }) => {
  await page.goto(data.inputs.url);


  // Enter search term and submit
  await page.getByRole('textbox', { name: data.inputs.searchBoxName }).fill(data.inputs.search);
  await page.getByRole('button', { name: data.inputs.searchButtonName }).click();

  // Expect the search box to contain the typed query
  await expect(page.getByRole('textbox', { name: data.inputs.searchBoxName })).toHaveValue(data.inputs.search);

  // Generic assertion: at least one product card is visible after search
  const cards = page.getByRole('article');
  await expect(cards).toHaveCount(1);

  // Safe rendering: ensure displayed texts do not include raw HTML
  const contents = await page.locator('main').allTextContents();
  for (const c of contents) expect(c).not.toContain('<');
});
