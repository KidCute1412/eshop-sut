import { expect, test, type APIRequestContext, type APIResponse } from "@playwright/test";
import { ApiDriver } from "../src/api-driver.js";
import { loadCases } from "../src/data-loader.js";
import type { AccessControlCase, AuthMode, CleanupKind } from "../src/types.js";

const API_URL = process.env.API_URL ?? "http://localhost:3000/api";
const ADMIN_URL = process.env.ADMIN_URL ?? "http://localhost:5174";
const cases = loadCases<AccessControlCase>("../test-data/fr12-access-control.json", 12);

function tokenFor(mode: AuthMode, adminToken: string, userToken: string): string | undefined {
  if (mode === "admin") return adminToken;
  if (mode === "user") return userToken;
  if (mode === "malformed") return "not-a-valid-jwt";
  return undefined;
}

async function removeProbe(
  request: APIRequestContext,
  kind: CleanupKind | undefined,
  id: number | undefined,
  adminToken: string,
): Promise<void> {
  if (!kind || !id) return;
  const paths: Record<CleanupKind, string> = {
    product: `/products/${id}`,
    category: `/categories/${id}`,
    coupon: `/admin/coupons/${id}`,
  };
  await request.delete(`${API_URL}${paths[kind]}`, {
    headers: { Authorization: `Bearer ${adminToken}` },
  });
}

test.describe("FR-12 Access Control", () => {
  let adminToken: string;
  let userToken: string;

  test.beforeAll(async ({ request }) => {
    const api = new ApiDriver(request);
    [adminToken, userToken] = await Promise.all([
      api.login("admin@eshop.com", "Admin123!"),
      api.login("test@eshop.com", "Test1234!"),
    ]);
  });

  for (const row of cases) {
    test(`${row.id} [${row.priority}] ${row.auth} ${row.method} ${row.path}: ${row.title}`, async ({ page, request }) => {
      await test.step(`Traceability: ${row.partition.join(", ")}`, async () => {});
      const token = tokenFor(row.auth, adminToken, userToken);
      let response: APIResponse | undefined;
      let createdId: number | undefined;

      try {
        const data = row.body ? { ...row.body } : undefined;
        if (row.cleanup === "coupon" && data?.code) {
          data.code = `${String(data.code).slice(0, 12)}-${crypto.randomUUID().slice(0, 8)}`;
        }
        response = await request.fetch(`${API_URL}${row.path}`, {
          method: row.method,
          headers: token ? { Authorization: `Bearer ${token}` } : {},
          data,
        });

        const text = await response.text();
        try {
          const body = JSON.parse(text) as { id?: number };
          createdId = body.id;
        } catch {
          // A non-JSON error is still asserted through status and content type below.
        }

        expect.soft(response.status(), `${row.method} ${row.path}: ${text}`).toBe(row.expectedStatus);
        expect.soft(response.headers()["content-type"]).toContain("application/json");
        if (row.expectedStatus >= 400) expect.soft(text).toMatch(/error|unauthorized|forbidden/i);
        if (row.expectedStatus === 200 && row.method === "GET") {
          expect.soft(Array.isArray(JSON.parse(text))).toBe(true);
        }
      } finally {
        await removeProbe(request, row.cleanup, createdId, adminToken);
      }

      if (token) {
        await page.addInitScript(
          ({ storedToken }) => localStorage.setItem("adminToken", storedToken),
          { storedToken: token },
        );
      }
      await page.goto(ADMIN_URL);
      if (row.auth === "admin") {
        await expect.soft(page.getByRole("heading", { name: "EShop Admin" })).toBeVisible({ timeout: 3_000 });
      } else {
        await expect.soft(page.getByRole("heading", { name: "Admin Login" })).toBeVisible({ timeout: 3_000 });
      }
    });
  }
});
