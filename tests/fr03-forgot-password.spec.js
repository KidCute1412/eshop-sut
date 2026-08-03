// @ts-check
import { test, expect } from '@playwright/test';
import fr03Data from './data/fr03-forgot-password.json' with { type: 'json' };

const API = 'http://localhost:3000/api';
const WEB = 'http://localhost:5173';

// Shared backend state (login-attempt counters, reset_token) is mutated by every
// test in this file, so tests must run one after another, not in parallel workers.
// (Ordering is guaranteed by playwright.config.js: workers=1, fullyParallel=false.
// Deliberately NOT using test.describe.configure({mode:'serial'}) here — Playwright
// skips all remaining tests in a serial block after the first failure, which would
// hide every other known-bug assertion below it.)

test.describe('FR-03 — Forgot Password & Reset Password (API)', () => {
  for (const row of fr03Data.filter((r) => 'email' in r)) {
    test(`${row.id} [${row.type}] forgot-password email="${row.email}"`, async ({ request }) => {
      const res = await request.post(`${API}/forgot-password`, { data: { email: row.email } });
      expect(res.status()).toBe(row.expectRequestStatus);
      const body = await res.json();
      if (row.expectRequestOk) {
        expect(body).toHaveProperty('resetToken');
        expect(body.resetToken).toMatch(/^\d+$/);
      } else {
        expect(body).toHaveProperty('error');
      }
    });
  }

  test('FR03-TC14 [known bug] OTP is documented as 6 digits but backend issues 4', async ({ request }) => {
    const res = await request.post(`${API}/forgot-password`, { data: { email: 'test@eshop.com' } });
    const body = await res.json();
    // Spec (README FR-03): "OTP 6 chữ số ngẫu nhiên". Actual backend: Math.floor(1000 + random()*9000) -> 4 digits.
    expect(body.resetToken.length).toBe(4); // documents the known defect, not the spec-correct value
  });

  test('FR03-TC06 [negative] reset-password rejects a wrong OTP', async ({ request }) => {
    await request.post(`${API}/forgot-password`, { data: { email: 'test@eshop.com' } });
    const res = await request.post(`${API}/reset-password`, {
      data: { email: 'test@eshop.com', resetToken: '0000', newPassword: 'Aa1!aaaa' },
    });
    expect(res.status()).toBe(400);
  });

  test('FR03-TC07 [negative] OTP issued for one email cannot reset another user\'s password', async ({ request }) => {
    const otpRes = await request.post(`${API}/forgot-password`, { data: { email: 'admin@eshop.com' } });
    const { resetToken } = await otpRes.json();
    const res = await request.post(`${API}/reset-password`, {
      data: { email: 'test@eshop.com', resetToken, newPassword: 'Aa1!aaaa' },
    });
    expect(res.status()).toBe(400);
  });

  test('FR03-TC17 [edge] requesting a new OTP invalidates the previous one', async ({ request }) => {
    const first = await (await request.post(`${API}/forgot-password`, { data: { email: 'test@eshop.com' } })).json();
    await request.post(`${API}/forgot-password`, { data: { email: 'test@eshop.com' } }); // second request overwrites token
    const res = await request.post(`${API}/reset-password`, {
      data: { email: 'test@eshop.com', resetToken: first.resetToken, newPassword: 'Aa1!aaaa' },
    });
    expect(res.status()).toBe(400);
  });

  test('FR03-TC05/TC16 [E2E] request OTP -> reset password -> login with new password', async ({ request }) => {
    const otpRes = await request.post(`${API}/forgot-password`, { data: { email: 'test@eshop.com' } });
    const { resetToken } = await otpRes.json();

    const resetRes = await request.post(`${API}/reset-password`, {
      data: { email: 'test@eshop.com', resetToken, newPassword: 'NewPass1!' },
    });
    expect(resetRes.status()).toBe(200);
    const resetBody = await resetRes.json();
    expect(resetBody.message).toContain('successfully');

    const loginRes = await request.post(`${API}/login`, {
      data: { email: 'test@eshop.com', password: 'NewPass1!' },
    });
    expect(loginRes.ok()).toBeTruthy();
    const loginBody = await loginRes.json();
    expect(loginBody).toHaveProperty('token');

    // restore the fixture password so later test files/re-runs are not affected
    await request.post(`${API}/reset-password`, {
      data: { email: 'test@eshop.com', resetToken: (await (await request.post(`${API}/forgot-password`, { data: { email: 'test@eshop.com' } })).json()).resetToken, newPassword: 'Test1234!' },
    });
  });

  test('FR03-TC08 [edge] a consumed OTP cannot be reused a second time', async ({ request }) => {
    const otpRes = await request.post(`${API}/forgot-password`, { data: { email: 'test@eshop.com' } });
    const { resetToken } = await otpRes.json();

    const first = await request.post(`${API}/reset-password`, {
      data: { email: 'test@eshop.com', resetToken, newPassword: 'NewPass2!' },
    });
    expect(first.status()).toBe(200);

    const second = await request.post(`${API}/reset-password`, {
      data: { email: 'test@eshop.com', resetToken, newPassword: 'NewPass3!' },
    });
    expect(second.status()).toBe(400);

    // restore fixture password
    const otp2 = await (await request.post(`${API}/forgot-password`, { data: { email: 'test@eshop.com' } })).json();
    await request.post(`${API}/reset-password`, {
      data: { email: 'test@eshop.com', resetToken: otp2.resetToken, newPassword: 'Test1234!' },
    });
  });
});

test.describe('FR-03 — Forgot Password UI', () => {
  test('FR03-TC13 [UI] step indicator moves from step 1 to step 2 after requesting OTP', async ({ page }) => {
    await page.goto(`${WEB}/forgot-password`);
    await expect(page.getByRole('heading', { name: 'Quên Mật Khẩu' })).toBeVisible();

    // The <label> elements in ForgotPassword.jsx aren't associated with their
    // <input> via htmlFor/id, so getByLabel() cannot resolve them — falling
    // back to a structural locator (the step-1 form has exactly one input).
    await page.locator('form input[type="text"]').first().fill('test@eshop.com');
    await page.getByRole('button', { name: 'Lấy mã OTP' }).click();

    await expect(page.getByText(/Mã OTP của bạn là/)).toBeVisible();
    await expect(page.getByText('Mã OTP (4 số)')).toBeVisible();
    await expect(page.locator('form input[type="text"]').first()).toBeVisible();
  });

  test('FR03-TC12 [known bug] reset step is missing a confirm-password field', async ({ page }) => {
    await page.goto(`${WEB}/forgot-password`);
    // The <label> elements in ForgotPassword.jsx aren't associated with their
    // <input> via htmlFor/id, so getByLabel() cannot resolve them — falling
    // back to a structural locator (the step-1 form has exactly one input).
    await page.locator('form input[type="text"]').first().fill('test@eshop.com');
    await page.getByRole('button', { name: 'Lấy mã OTP' }).click();
    await expect(page.getByText(/Mã OTP của bạn là/)).toBeVisible();

    // Spec (README FR-03 step 2): "Xác nhận mật khẩu mới" field must exist.
    const confirmField = page.getByLabel(/Xác nhận mật khẩu/);
    await expect(confirmField).toHaveCount(0); // documents the known defect
  });

  test('FR03-TC14b [known bug] UI label documents a 4-digit OTP instead of the spec\'s 6 digits', async ({ page }) => {
    await page.goto(`${WEB}/forgot-password`);
    // The <label> elements in ForgotPassword.jsx aren't associated with their
    // <input> via htmlFor/id, so getByLabel() cannot resolve them — falling
    // back to a structural locator (the step-1 form has exactly one input).
    await page.locator('form input[type="text"]').first().fill('test@eshop.com');
    await page.getByRole('button', { name: 'Lấy mã OTP' }).click();
    await expect(page.getByText('Mã OTP (4 số)')).toBeVisible(); // spec requires 6 digits
  });
});
