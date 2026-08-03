import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:5173/');
  await page.getByRole('link', { name: 'Đăng nhập' }).click();
  await page.locator('div').filter({ hasText: /^Username$/ }).click();
  await page.getByRole('textbox').first().click();
  await page.getByRole('textbox').nth(1).click();
  await page.getByRole('textbox').first().click();
  await page.getByRole('textbox').first().click();
  await page.getByRole('textbox').first().fill('test@eshop.com');
  await page.getByRole('textbox').nth(1).click();
  await page.getByRole('textbox').nth(1).fill('Test1234!');
  await page.getByRole('button', { name: 'Sign In' }).click();
});