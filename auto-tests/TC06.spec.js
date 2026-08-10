import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC06.json', import.meta.url)));

test('TC06', async ({ page }) => {
  await page.goto(data.inputs.url);
  await page.getByRole('link', { name: new RegExp(data.inputs.loginLink, 'i') }).click();
  await page.getByRole('textbox', { name: new RegExp(data.inputs.emailField, 'i') }).fill(data.inputs.email);
  await page.getByRole('textbox', { name: new RegExp(data.inputs.passwordField, 'i') }).fill(data.inputs.password);
  await page.getByRole('button', { name: new RegExp(data.inputs.loginButtonName, 'i') }).click();
  await page.getByRole('link', { name: new RegExp(data.inputs.orderHistoryLink, 'i') }).click();

  await expect(page.getByRole('heading', { name: new RegExp(data.expected.pageHeading, 'i') })).toBeVisible();
  for (const header of data.expected.columnHeaders) {
    await expect(page.getByRole('columnheader', { name: new RegExp(header, 'i') })).toBeVisible();
  }

  const allRows = page.getByRole('row');
  expect(await allRows.count()).toBeGreaterThan(1);
});
