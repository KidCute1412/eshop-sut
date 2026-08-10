import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC05.json', import.meta.url)));

test('TC05', async ({ page }) => {
  await page.goto(data.inputs.url);


  // Enter a non-matching search and submit
  await page.getByRole('textbox', { name: data.inputs.searchBoxName }).fill(data.inputs.search);
  await page.getByRole('button', { name: data.inputs.searchButtonName }).click();

  // Structural assertion: no product cards visible
  await expect(page.getByRole('article')).toHaveCount(0);

});
