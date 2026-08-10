import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC08.json', import.meta.url)));

test('TC08', async ({ page }) => {
  await page.goto(data.inputs.url);
  await page.getByRole('link', { name: new RegExp(data.inputs.loginLink, 'i') }).click();
  await page.getByRole('textbox', { name: new RegExp(data.inputs.emailField, 'i') }).fill(data.inputs.email);
  await page.getByRole('textbox', { name: new RegExp(data.inputs.passwordField, 'i') }).fill(data.inputs.password);
  await page.getByRole('button', { name: new RegExp(data.inputs.loginButtonName, 'i') }).click();
  await page.getByRole('link', { name: new RegExp(data.inputs.orderHistoryLink, 'i') }).click();

  const statusCell = page.getByRole('cell', { name: new RegExp(data.expected.statusTextPattern, 'i') }).first();
  await expect(statusCell).toBeVisible();
  await expect(statusCell).toHaveText(new RegExp(data.expected.statusTextPattern, 'i'));

  const statusStyle = await statusCell.evaluate((element) => {
    const style = window.getComputedStyle(element);
    return style.color || style.backgroundColor || '';
  });

  expect(statusStyle).not.toBe('');
});
