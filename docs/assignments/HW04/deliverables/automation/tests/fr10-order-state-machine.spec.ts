import { expect, test } from "@playwright/test";
import { ApiDriver } from "../src/api-driver.js";
import { loadCases } from "../src/data-loader.js";
import type { OrderTransitionCase } from "../src/types.js";

const cases = loadCases<OrderTransitionCase>("../test-data/fr10-order-state-machine.json", 12);
const statusLabels = {
  pending: "Chờ xác nhận",
  confirmed: "Đã xác nhận",
  shipping: "Đang giao",
  delivered: "Đã giao",
  canceled: "Đã hủy",
} as const;

test.describe("FR-10 Order State Machine", () => {
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
    test(`${row.id} [${row.priority}] ${row.from} -> ${row.to}: ${row.title}`, async ({ page, request }) => {
      await test.step(`Traceability: ${row.partition.join(", ")}`, async () => {});
      const api = new ApiDriver(request);
      const orderId = await api.arrangeOrder(row.setup, userToken, adminToken);
      expect((await api.getOrder(orderId)).status, "arranged source state").toBe(row.from);

      const response =
        row.actor === "admin"
          ? await api.adminTransition(orderId, row.to, adminToken)
          : await api.userCancel(orderId, userToken);

      expect.soft(response.status(), await response.text()).toBe(row.expectedStatus);
      if (row.expectedStatus >= 400) {
        expect.soft(await response.text()).toMatch(/error|invalid|cannot|forbidden/i);
      }
      expect.soft((await api.getOrder(orderId)).status, "persisted state after transition").toBe(
        row.expectedFinalState,
      );

      await page.addInitScript((token) => localStorage.setItem("token", token), userToken);
      await page.goto("/profile");
      const exactOrderCell = page.getByRole("cell", {
        name: `#${orderId}`,
        exact: true,
      });
      const orderRow = page.getByRole("row").filter({ has: exactOrderCell });
      await expect(orderRow).toBeVisible();
      await expect(orderRow.locator("span")).toHaveText(
        statusLabels[row.expectedFinalState],
      );
      const userMayCancel = row.expectedFinalState === "pending" || row.expectedFinalState === "confirmed";
      await expect(orderRow.getByRole("button")).toHaveCount(userMayCancel ? 1 : 0);
    });
  }
});
