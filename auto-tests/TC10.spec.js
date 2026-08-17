import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC10.json', import.meta.url)));

test('TC10', async ({ page }) => {
  await page.goto(data.inputs.url);
  await page.getByPlaceholder('Email').fill(data.inputs.email);
  await page.getByPlaceholder('Password').fill(data.inputs.password);
  await page.getByRole('button', { name: new RegExp(data.inputs.loginButton, 'i') }).click();

  await page.getByText(new RegExp(data.inputs.productTabLabel, 'i')).click();

  await expect(page.getByRole('heading', { name: new RegExp(data.expected.productFormHeading, 'i') })).toBeVisible();
  for (const header of data.expected.tableHeaders) {
    await expect(page.getByRole('columnheader', { name: new RegExp(header, 'i') })).toBeVisible();
  }

  await expect(page.getByPlaceholder(data.inputs.productNamePlaceholder)).toBeVisible();
});import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC10.json', import.meta.url)));

test('TC10', async ({ page }) => {
  await page.goto(data.inputs.url);
  await page.getByPlaceholder(data.inputs.emailPlaceholder).fill(data.inputs.email);
  await page.getByPlaceholder(data.inputs.passwordPlaceholder).fill(data.inputs.password);
  await page.getByRole('button', { name: new RegExp(data.inputs.loginButton, 'i') }).click();
  await page.getByText(data.inputs.productsTab).click();

  await page.getByPlaceholder(data.inputs.productNamePlaceholder).fill(data.inputs.name);
  await page.getByPlaceholder(data.inputs.pricePlaceholder).fill(String(data.inputs.price));
  await page.locator('select').selectOption({ index: data.inputs.categoryIndex });
  await page.getByPlaceholder(data.inputs.imageUrlPlaceholder).fill(data.inputs.imageUrl);
  await page.getByPlaceholder(data.inputs.descriptionPlaceholder).fill(data.inputs.description);
  await page.getByRole('button', { name: new RegExp(data.inputs.saveButton, 'i') }).click();

  await expect(page.getByText(data.expected.name)).toBeVisible();
  await expect(page.getByText(data.expected.priceText)).toBeVisible();
});
