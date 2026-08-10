import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC09.json', import.meta.url)));

test('TC09', async ({ page }) => {
  await page.goto(data.inputs.url);
  await page.getByRole('link', { name: new RegExp(data.inputs.loginLink, 'i') }).click();
  await page.getByRole('textbox', { name: new RegExp(data.inputs.emailField, 'i') }).fill(data.inputs.email);
  await page.getByRole('textbox', { name: new RegExp(data.inputs.passwordField, 'i') }).fill(data.inputs.password);
  await page.getByRole('button', { name: new RegExp(data.inputs.loginButtonName, 'i') }).click();
  await page.getByRole('link', { name: new RegExp(data.inputs.orderHistoryLink, 'i') }).click();

  const userOrders = page.getByRole('row').filter({ hasText: data.expected.userIdentifier });
  const otherOrders = page.getByRole('row').filter({ hasText: data.expected.otherUserIdentifier });

  expect(await userOrders.count()).toBeGreaterThan(0);
  expect(await otherOrders.count()).toBe(0);
});
