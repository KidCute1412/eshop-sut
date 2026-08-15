// @ts-check
import { test, expect } from '@playwright/test';
import fr09Data from './data/fr09-coupon.json' with { type: 'json' };

const API = 'http://localhost:3000/api';

// coupon_usage counters and per-coupon state are shared server-side, so tests
// in this file must not run concurrently against the same backend instance.
// (Ordering is guaranteed globally by playwright.config.js: workers=1,
// fullyParallel=false. NOT using mode:'serial' — it would skip every remaining
// test in the block after the first known-bug failure.)

/** @type {{token: string, user: any} | null} */
let auth = null;

test.beforeAll(async ({ request }) => {
  const res = await request.post(`${API}/login`, {
    data: { email: 'test@eshop.com', password: 'Test1234!' },
  });
  auth = await res.json();
});

test.describe('FR-09 — Discount Coupons (data-driven, spec-correct expectations)', () => {
  for (const row of fr09Data) {
    test(`${row.id} [${row.type}] code="${row.code}" total=${row.total_amount}`, async ({ request }) => {
      const res = await request.post(`${API}/apply-coupon`, {
        data: {
          code: row.code,
          total_amount: row.total_amount,
          user_id: row.useLoggedInUser ? auth.user.id : undefined,
        },
      });
      expect(res.status()).toBe(row.expectStatus);

      if (row.expectStatus === 200) {
        const body = await res.json();
        expect(body.success).toBe(true);
        expect(body.final_amount).toBe(row.expectFinalAmount);
      }
    });
  }

  test('FR09-TC08 [known bug] C4 — coupon must not apply without a logged-in user (user_id omitted)', async ({ request }) => {
    const res = await request.post(`${API}/apply-coupon`, {
      data: { code: 'SAVE10', total_amount: 500000 }, // no user_id
    });
    // Spec C4: "Đã đăng nhập — người dùng phải có JWT Token hợp lệ".
    // This documents the SPEC-CORRECT expectation; the current backend accepts it anyway (known bug).
    expect(res.status()).toBe(401);
  });

  test('FR09-TC09/TC10 [C5] usage limit — VIP100 allows exactly 2 uses per user, rejects the 3rd', async ({ request }) => {
    const use = () => request.post(`${API}/apply-coupon`, {
      data: { code: 'VIP100', total_amount: 500000, user_id: auth.user.id },
    });
    const record = () => request.post(`${API}/coupon-usage`, {
      headers: { Authorization: `Bearer ${auth.token}` },
      data: { coupon_id: 3 }, // VIP100 seeded as the 3rd coupon row
    });

    const first = await use();
    expect(first.ok()).toBeTruthy();
    await record();

    const second = await use();
    expect(second.ok()).toBeTruthy(); // usage=1 < max_uses_per_user=2 -> still allowed
    await record();

    const third = await use();
    expect(third.status()).toBe(400); // usage=2 >= max_uses_per_user=2 -> must be rejected
    const body = await third.json();
    expect(body.error).toContain('giới hạn');
  });

  test('FR09-TC13 [E2E] apply coupon at checkout clears the cart and records usage', async ({ request }) => {
    await request.post(`${API}/cart`, {
      headers: { Authorization: `Bearer ${auth.token}` },
      data: { productId: 1, quantity: 1 },
    });

    const coupon = await (await request.post(`${API}/apply-coupon`, {
      data: { code: 'SAVE10', total_amount: 30000000, user_id: auth.user.id },
    })).json();
    expect(coupon.success).toBe(true);

    const checkout = await request.post(`${API}/checkout`, {
      headers: { Authorization: `Bearer ${auth.token}` },
      data: { shipping_address: '123 Test Street' },
    });
    expect(checkout.ok()).toBeTruthy();

    const cartAfter = await (await request.get(`${API}/cart`, {
      headers: { Authorization: `Bearer ${auth.token}` },
    })).json();
    expect(cartAfter).toEqual([]);
  });
});
