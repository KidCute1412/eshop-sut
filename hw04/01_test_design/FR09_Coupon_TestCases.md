# Test Case Design — FR-09 Discount Coupons

Spec reference: `README.md` FR-09 (5 conditions C1–C5, percent/fixed formula), route `POST /api/apply-coupon`.
Seed data (`backend/database.js`): `SAVE10` (percent 10, min 300000), `BIGBUY` (fixed 50000, min 500000), `VIP100` (fixed 100000, min 300000, max 2 uses), `EXPIRED` (percent 20, expired 2020-01-01).

Data file: `tests/data/fr09-coupon.json`

| TC ID | Type | Coupon | total_amount | user_id | Expected (per spec) | Notes |
|---|---|---|---|---|---|---|
| FR09-TC01 | Positive | SAVE10 | 500000 | logged-in user | discount = 50,000 (10%), final = 450,000 | **known bug**: backend computes `total*(1-10)` → large negative discount |
| FR09-TC02 | Boundary (BVA) | SAVE10 | 300000 (== min_order_amount) | logged-in user | Should be accepted (spec says `>=`) | **known bug**: backend uses strict `>`, rejects exact-threshold orders |
| FR09-TC03 | Boundary (BVA) | SAVE10 | 299999 (min - 1) | logged-in user | Rejected — below minimum | |
| FR09-TC04 | Positive | BIGBUY | 500000 | logged-in user | discount = 50,000 fixed, final = 450,000 | |
| FR09-TC05 | Boundary (BVA) | BIGBUY | 500001 (min + 1) | logged-in user | Accepted | |
| FR09-TC06 | Negative | EXPIRED | 200000 | logged-in user | Rejected — "Mã giảm giá đã hết hạn" | |
| FR09-TC07 | Negative | NOTEXIST | 500000 | logged-in user | 404 — coupon not found / inactive | |
| FR09-TC08 | Negative (C4) | SAVE10 | 500000 | **no user_id / not logged in** | Should be rejected per spec (C4: must be logged in) | **known bug**: backend applies the coupon anyway when `user_id` is omitted |
| FR09-TC09 | Negative (C5) | VIP100 | 500000 | user who already used it 2 times | Should be rejected — "đã đạt giới hạn" | |
| FR09-TC10 | Edge (C5) | VIP100 | 500000 | user who used it exactly 1 time (max 2) | Accepted (usage 1 < max 2) | |
| FR09-TC11 | Edge | SAVE10 | 0 | logged-in user | Rejected — order total must be > 0 (documents actual behavior) | |
| FR09-TC12 | Edge | SAVE10 | -1000 | logged-in user | Should be rejected (negative order total is invalid) | documents actual behavior |
| FR09-TC13 | E2E | SAVE10 | 500000 | logged-in user, full checkout flow | Coupon applied at checkout, cart cleared afterwards, `coupon_usage` recorded | |
| FR09-TC14 | Negative | (empty code) | 500000 | logged-in user | 400 — "Vui lòng nhập mã giảm giá" | |

Total: **14 test cases** (≥ 12 required), covering all 5 spec conditions (C1–C5) plus the percent/fixed formula and BVA around `min_order_amount` and `max_uses_per_user`.
