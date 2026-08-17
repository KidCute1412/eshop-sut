import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC11.json', import.meta.url)));

test('TC11', async ({ page }) => {
  await page.goto(data.inputs.url);
  await page.getByPlaceholder(data.inputs.emailPlaceholder).fill(data.inputs.email);
  await page.getByPlaceholder(data.inputs.passwordPlaceholder).fill(data.inputs.password);
  await page.getByRole('button', { name: new RegExp(data.inputs.loginButton, 'i') }).click();
  await page.getByText(data.inputs.productsTab).click();

  for (const product of data.inputs.initialProducts) {
    await page.getByPlaceholder(data.inputs.productNamePlaceholder).fill(product.name);
    await page.getByPlaceholder(data.inputs.pricePlaceholder).fill(String(product.price));
    await page.locator('select').selectOption({ index: data.inputs.categoryIndex });
    await page.getByPlaceholder(data.inputs.imageUrlPlaceholder).fill(product.imageUrl);
    await page.getByPlaceholder(data.inputs.descriptionPlaceholder).fill(product.description);
    await page.getByRole('button', { name: new RegExp(data.inputs.saveButton, 'i') }).click();
  }

  const row = page.locator('tr', { hasText: data.inputs.originalName });
  await row.getByRole('button', { name: new RegExp(data.inputs.editButton, 'i') }).click();
  await page.getByPlaceholder(data.inputs.productNamePlaceholder).fill(data.inputs.updatedName);
  await page.getByPlaceholder(data.inputs.pricePlaceholder).fill(String(data.inputs.updatedPrice));
  await page.getByRole('button', { name: new RegExp(data.inputs.saveButton, 'i') }).click();

  await expect(page.getByText(data.expected.updatedName)).toBeVisible();
  await expect(page.getByText(data.expected.updatedPriceText)).toBeVisible();
  await expect(page.getByText(data.expected.otherProductName)).toBeVisible();
});
