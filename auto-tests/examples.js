// @ts-check
import { test, expect } from '@playwright/test';

// Example TC:
//TC-XX: Login with full credentials, expected: pass to the default screen
test('TC-XX: Login', async ({ page }) => {
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

// An example run of the frontend for web
test('test', async ({ page }) => {
  await page.goto('http://localhost:5173/');
  await expect(page.getByRole('heading', { name: 'Danh sách sản phẩm' })).toBeVisible();
  await expect(page.getByRole('banner')).toContainText('EShop');
  await expect(page.getByRole('heading', { name: 'Danh sách sản phẩm' })).toBeVisible();
  await expect(page.getByRole('textbox', { name: 'Tìm kiếm...' })).toBeEmpty();
  await expect(page.getByRole('banner')).toMatchAriaSnapshot(`
    - banner:
      - link "EShop":
        - /url: /
      - navigation:
        - link "Giỏ hàng":
          - /url: /cart
        - link "Đăng nhập":
          - /url: /login
        - link "Đăng ký":
          - /url: /register
    `);
  await page.getByText('Giỏ hàngĐăng nhậpĐăng ký').click();
  await page.getByRole('link', { name: 'Đăng nhập' }).click();
  await page.getByRole('link', { name: 'Đăng nhập' }).dblclick();
  await page.getByRole('textbox').first().click();
  await page.getByRole('textbox').first().fill('test@eshop.com');
  await page.getByRole('textbox').nth(1).click();
  await page.getByRole('textbox').nth(1).fill('Test1234!');
  await page.getByRole('button', { name: 'Sign In' }).click();
  await page.getByRole('textbox', { name: 'Tìm kiếm...' }).click();
  await page.getByRole('textbox', { name: 'Tìm kiếm...' }).fill('iphone');
  await page.getByRole('button', { name: 'Tìm' }).click();
  await page.getByRole('button', { name: 'Thêm vào giỏ' }).click();
  await page.getByRole('heading', { name: 'iPhone 15 Pro Max' }).click();
  await expect(page.getByRole('heading', { name: 'iPhone 15 Pro Max' })).toBeVisible();
  await expect(page.getByText('iPhone 15 Pro Max30,000,000')).toBeVisible();
  await expect(page.getByText('VND')).toBeVisible();
  await page.getByRole('button', { name: 'Thêm vào giỏ' }).click();
  await page.getByRole('link', { name: 'Giỏ hàng' }).click();
  await page.getByRole('button', { name: 'Tiến hành thanh toán' }).click();
  await page.getByRole('button', { name: 'Xác Nhận Thanh Toán' }).click();
});
// An example run of the frontend for web 2
test('test', async ({ page }) => {
  await page.goto('http://localhost:5173/');
  await page.getByRole('link', { name: 'Đăng nhập' }).click();
  await page.getByRole('textbox').first().click();
  await page.getByRole('textbox').first().click();
  await page.getByRole('textbox').first().fill('test@eshop.com');
  await page.getByRole('textbox').nth(1).click();
  await page.getByRole('textbox').first().fill('test@eshop.comTest1234!');
  await page.getByRole('textbox').nth(1).press('ControlOrMeta+z');
  await page.getByRole('textbox').first().fill('test@eshop.com');
  await page.getByRole('textbox').nth(1).click();
  await page.getByRole('textbox').nth(1).click();
  await page.getByRole('textbox').nth(1).fill('Test1234!');
  await page.getByRole('button', { name: 'Sign In' }).click();
  await page.getByText('EShopGiỏ hàngChào, Test').click();
  await page.getByRole('link', { name: 'Chào, Test User' }).click();
  await page.getByText('Lịch sử đơn hàngMã ĐHNgày đặ').click();
  await expect(page.getByRole('heading', { name: 'Lịch sử đơn hàng' })).toBeVisible();
  await expect(page.getByRole('cell', { name: '8/10/' }).first()).toBeVisible();
  await expect(page.getByRole('columnheader', { name: 'Mã ĐH' })).toBeVisible();
  await expect(page.getByRole('columnheader', { name: 'Ngày đặt' })).toBeVisible();
  await page.getByRole('columnheader', { name: 'Tổng tiền' }).click();
  await expect(page.getByRole('columnheader', { name: 'Tổng tiền' })).toBeVisible();
  await expect(page.getByRole('columnheader', { name: 'Trạng thái' })).toBeVisible();
  await expect(page.getByRole('columnheader', { name: 'Thao tác' })).toBeVisible();
  page.once('dialog', dialog => {
    console.log(`Dialog message: ${dialog.message()}`);
    dialog.dismiss().catch(() => {});
  });
  await page.getByRole('row', { name: '#1 8/10/2026 28,000,000 ₫ Ch' }).getByRole('button').click();
  await page.getByText('Chờ xác nhận').click();
  await expect(page.getByText('Chờ xác nhận')).toBeVisible();
  await page.getByText('Hồ sơ của bạnEmail (Không đổi').click();
});
// An example run of the frontend for admins
test('test', async ({ page }) => {
  await page.goto('http://localhost:5174/');
  await page.getByRole('textbox', { name: 'Email' }).click();
  await page.getByRole('textbox', { name: 'Email' }).fill('admin@eshop.com');
  await page.getByText('Admin LoginLogin').click();
  await page.getByRole('textbox', { name: 'Password' }).click();
  await page.getByRole('textbox', { name: 'Password' }).click();
  await page.getByRole('textbox', { name: 'Password' }).fill('Admin123!');
  await page.getByRole('button', { name: 'Login' }).click();
  await page.getByText('Sản phẩm').click();
  await expect(page.getByText('📂 Import sản phẩm từ CSVTải file mẫu (template.csv)Import 0 sản phẩm')).toBeVisible();
  await expect(page.getByRole('button', { name: 'Choose File' })).toBeVisible();
  await page.getByRole('button', { name: 'Choose File' }).setInputFiles('import_i.csv');
  await page.getByRole('button', { name: 'Choose File' }).setInputFiles('import_v.csv');
  await page.getByRole('button', { name: 'Import 2 sản phẩm' }).click();
  await page.getByRole('textbox', { name: 'Tên sản phẩm' }).click();
  await page.getByRole('textbox', { name: 'Tên sản phẩm' }).fill('Iphone1 1');
  await page.getByRole('spinbutton', { name: 'Giá tiền' }).click();
  await page.getByRole('spinbutton', { name: 'Giá tiền' }).fill('1000');
  await page.getByRole('textbox', { name: 'URL Ảnh' }).click();
  await page.getByRole('textbox', { name: 'Mô tả' }).click();
  await page.getByRole('textbox', { name: 'Mô tả' }).fill('None');
  await page.getByRole('button', { name: 'Lưu sản phẩm' }).click();
  await page.getByRole('img', { name: 'Sản phẩm Mới 2' }).click();
  await page.getByRole('button', { name: 'Sửa' }).first().click();
  await page.getByRole('spinbutton', { name: 'Giá tiền' }).click();
  await page.getByRole('spinbutton', { name: 'Giá tiền' }).fill('3000000');
  page.once('dialog', dialog => {
    console.log(`Dialog message: ${dialog.message()}`);
    dialog.dismiss().catch(() => {});
  });
  await page.getByRole('button', { name: 'Lưu sản phẩm' }).click();
  await page.locator('tr:nth-child(8) > .p-3.flex > .bg-red-500').click();
  await page.getByRole('combobox').selectOption('2');
  await page.getByRole('heading', { name: 'Thêm sản phẩm mới' }).click();
});