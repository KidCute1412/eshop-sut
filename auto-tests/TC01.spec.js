import { test, expect } from '@playwright/test';
import fs from 'fs';

const data = JSON.parse(await fs.promises.readFile(new URL('./TC01.json', import.meta.url)));

test("TC01", async ({ page }) => {
  await page.goto(data.inputs.url);

  // Ensure exactly one H1 on the page
  await expect(page.locator('h1')).toHaveCount(1);

  // Role-based assertion: main heading and banner
  await expect(page.getByRole('heading', { name: data.expected.heading })).toBeVisible();
  await expect(page.getByRole('banner')).toContainText(data.expected.brand);

  // Structural/count assertion: product card count (articles used for product cards)
  const cards = page.getByRole('article');
  await expect(cards).toHaveCount(data.expected.visibleCount);

  // Images should have alt text
  for (let i = 0; i < Math.min(3, await cards.count()); i++) {
    const img = cards.nth(i).locator('img').first();
    await expect(img).toHaveAttribute('alt', /\S+/);
  }

  // Price format check: at least one price contains thousands separator and currency
  const priceLocator = page.locator("text=₫").first();
  const priceText = await priceLocator.textContent();
  expect(priceText).toMatch(/\d{1,3}(?:[.,]\d{3})*\s*₫/);

  // Search box should be empty on default view
  await expect(page.getByRole('textbox', { name: data.inputs.searchBoxName })).toBeEmpty();

  // Check for safe rendering: product card texts should not contain raw HTML tags
  const texts = await cards.allTextContents();
  for (const t of texts) {
    expect(t).not.toContain('<script');
    expect(t).not.toContain('<');
  }

  // Optional: try to detect a loading indicator briefly (non-fatal)
  try {
    const loading = page.getByText(/đang tải|loading/i).first();
    await expect(loading).toBeVisible({ timeout: 1000 });
  } catch (e) {
    // ignore if not present quickly
  }
});
