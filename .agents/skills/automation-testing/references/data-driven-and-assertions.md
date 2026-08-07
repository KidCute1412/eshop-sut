# Data-Driven Testing and Assertion Patterns

## Data-Driven: What Counts, What Doesn't

**Does not count** (assignment explicitly rejects this): a `.spec.ts` file with

```ts
const testUsers = [
  { name: "Nguyen Van A", email: "a@test.com", password: "Aa1 aaaa" },
  { name: "Tran Thi B", email: "b@test.com", password: "Bb2 bbbb" },
];
```

defined inline in the script, even though it's technically an array a loop could iterate over — the
assignment's wording is explicit: "hardcoded inline arrays or objects in the script are not
accepted."

**Does count**: the same data moved to `data/register-cases.json`:

```json
[
  { "id": "TC-01", "name": "Nguyen Van A", "email": "a@test.com", "password": "Aa1 aaaa", "expected": "success" },
  { "id": "TC-02", "name": "Tran Thi B", "email": "invalid-email", "password": "Bb2 bbbb", "expected": "error" }
]
```

loaded by the spec via `import testCases from '../data/register-cases.json'` (or a CSV-parsing
helper for `.csv`), then iterated with `for (const tc of testCases) { test(tc.id, async ({ page })
=> { ... }) }`.

See `assets/test-data-template.json` and `assets/test-data-template.csv` for starting schemas — one
row/object per test case, with an `id` field that matches the case's ID in `test-cases.md` so a
failure is traceable back to its design-time source.

## Assertion Pattern Diversity — Concrete Playwright Examples

| Pattern | Example | Good fit for |
| --- | --- | --- |
| Visibility/existence | `await expect(page.getByText('Đăng ký thành công')).toBeVisible();` | Success/error banners |
| Text/value content | `await expect(page.getByRole('heading')).toHaveText('Giỏ hàng của bạn đang trống');` | Exact copy checks |
| URL/navigation | `await expect(page).toHaveURL(/.*\/login/);` | Post-submit redirects |
| Count | `await expect(page.locator('table tbody tr')).toHaveCount(3);` | Cart rows, coupon list rows |
| Element state | `await expect(page.getByRole('button', { name: 'Tạo mã' })).toBeDisabled();` | Pending/disabled submit states |
| API/network response | `const resp = await page.waitForResponse(r => r.url().includes('/api/admin/coupons') && r.request().method() === 'POST'); expect(resp.status()).toBe(201);` | Backend contract, not just UI reflection |

Pick at least 3 of these across the suite (not necessarily 3 per test — 3 across the whole feature's
script file is the assignment's actual bar), and prefer the ones that would genuinely catch a
different class of regression than the others already in use.

## Common Weak-Assertion Smells to Fix in Human Review

- A test that only asserts `page.url()` changed after submit, without checking *what* was actually
  displayed — passes even if the page navigated to an error state that happens to share a URL
  pattern with success.
- A test that asserts an element `toBeVisible()` immediately after a click with no wait strategy,
  relying on Playwright's built-in auto-waiting to paper over what should really be an explicit
  `waitForResponse`/`waitForLoadState` — this often works locally but flakes on a slower CI/browser
  run, which is exactly the "flaky waits" category the assignment asks you to review for.
- An assertion copy-pasted across positive and negative cases that only checks "some text appeared,"
  without checking it's the *correct* text for that specific case.
