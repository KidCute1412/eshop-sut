import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC07.json', import.meta.url)));

test('TC07', async ({ page }) => {
  await page.goto(data.inputs.url);
  await page.getByRole('link', { name: new RegExp(data.inputs.loginLink, 'i') }).click();
  await page.getByRole('textbox', { name: new RegExp(data.inputs.emailField, 'i') }).fill(data.inputs.email);
  await page.getByRole('textbox', { name: new RegExp(data.inputs.passwordField, 'i') }).fill(data.inputs.password);
  await page.getByRole('button', { name: new RegExp(data.inputs.loginButtonName, 'i') }).click();
  await page.getByRole('link', { name: new RegExp(data.inputs.orderHistoryLink, 'i') }).click();

  const firstOrderRow = page.getByRole('row').nth(1);
  const cells = firstOrderRow.getByRole('cell');

  expect(await cells.count()).toBeGreaterThanOrEqual(4);
  await expect(cells.nth(0)).not.toBeEmpty();
  await expect(cells.nth(1)).not.toBeEmpty();
  await expect(cells.nth(2)).toHaveText(new RegExp(data.expected.totalAmountPattern, 'i'));
  await expect(cells.nth(3)).toHaveText(new RegExp(data.expected.statusTextPattern, 'i'));
});
