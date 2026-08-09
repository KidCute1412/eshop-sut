import type { TestInfo } from "@playwright/test";
import type { TraceableCase } from "./types.js";

export async function attachCaseContract(
  testInfo: TestInfo,
  row: TraceableCase,
): Promise<void> {
  await testInfo.attach(`${row.id}-case-contract.json`, {
    body: Buffer.from(`${JSON.stringify(row, null, 2)}\n`, "utf8"),
    contentType: "application/json",
  });
}
