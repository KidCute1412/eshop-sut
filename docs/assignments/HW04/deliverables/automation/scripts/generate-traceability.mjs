import { readFileSync, readdirSync, writeFileSync } from "node:fs";
import path from "node:path";

const featureConfig = {
  fr06: {
    requirement: "FR-06",
    data: "fr06-product-detail.json",
    spec: "fr06-product-detail.spec.ts",
    precondition: "Seeded product data; frontend and API available",
  },
  fr10: {
    requirement: "FR-10",
    data: "fr10-order-state-machine.json",
    spec: "fr10-order-state-machine.spec.ts",
    precondition: "Seeded users/products; fresh order arranged through API",
  },
  fr12: {
    requirement: "FR-12",
    data: "fr12-access-control.json",
    spec: "fr12-access-control.spec.ts",
    precondition: "Seeded admin/user credentials; API available",
  },
};

const browsers = ["chromium", "firefox", "webkit"];
const reportRoot = path.resolve("reports");
const outputPath = path.resolve("..", "supporting-materials", "test_case_matrix.md");

function allSpecs(suite) {
  return [...(suite.specs ?? []), ...(suite.suites ?? []).flatMap(allSpecs)];
}

function findReport(feature, browser) {
  const matches = readdirSync(reportRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && entry.name.startsWith(`${feature}-${browser}-`))
    .map((entry) => entry.name);
  if (matches.length !== 1) throw new Error(`Expected exactly one selected report for ${feature}/${browser}; found ${matches.length}`);
  return matches[0];
}

function resultMap(reportName) {
  const report = JSON.parse(readFileSync(path.join(reportRoot, reportName, "results.json"), "utf8"));
  const map = new Map();
  for (const spec of report.suites.flatMap(allSpecs)) {
    const id = spec.title.match(/^(FR\d{2}-\d{2})\b/)?.[1];
    if (!id) continue;
    const test = spec.tests?.[0];
    const result = test?.results?.at(-1);
    const errors = JSON.stringify(result?.errors ?? []);
    const state = test?.status === "expected"
      ? "Pass"
      : /browserContext\.newPage|setting up \\"page\\"/i.test(errors)
        ? "Environment failure"
        : "Assertion failure";
    map.set(id, state);
  }
  return map;
}

function escapeCell(value) {
  return String(value).replaceAll("|", "\\|").replaceAll("\n", " ");
}

function summarizeFeature(feature, config) {
  const rows = JSON.parse(readFileSync(path.resolve("test-data", config.data), "utf8"));
  const reports = Object.fromEntries(browsers.map((browser) => [browser, findReport(feature, browser)]));
  const states = browsers.flatMap((browser) => [...resultMap(reports[browser]).values()]);
  return {
    logical: rows.length,
    attempts: states.length,
    reached: states.filter((state) => state !== "Environment failure").length,
    assertionFailures: states.filter((state) => state === "Assertion failure").length,
    environmentFailures: states.filter((state) => state === "Environment failure").length,
  };
}

const summaries = Object.fromEntries(
  Object.entries(featureConfig).map(([feature, config]) => [feature, summarizeFeature(feature, config)]),
);
const totalSummary = Object.values(summaries).reduce(
  (total, current) => Object.fromEntries(Object.keys(total).map((key) => [key, total[key] + current[key]])),
  { logical: 0, attempts: 0, reached: 0, assertionFailures: 0, environmentFailures: 0 },
);

function oracle(feature, row) {
  if (feature === "fr06") {
    const expected = Object.entries(row.expected ?? {}).map(([key, value]) => `${key}=${JSON.stringify(value)}`).join("; ");
    return `${row.assertion}${expected ? `; ${expected}` : ""}`;
  }
  if (feature === "fr10") {
    return `${row.actor} requests ${row.from} → ${row.to}; HTTP ${row.expectedStatus}; final=${row.expectedFinalState}`;
  }
  return `${row.auth} ${row.method} ${row.path}; HTTP ${row.expectedStatus}`;
}

const lines = [
  "# HW04 Final Test-Case and Execution Traceability Matrix",
  "",
  "> Generated from the committed external JSON datasets and the nine selected Playwright JSON reports by `automation/scripts/generate-traceability.mjs`.",
  "> Status semantics: **Pass** and **Assertion failure** reached the test oracle; **Environment failure** timed out while creating the Firefox `page` fixture before the test body/SUT observation.",
  "",
  "## Reconciled coverage",
  "",
  "| Requirement | Logical cases | Browser attempts | Reached assertions | Assertion failures | Environment failures |",
  "|---|---:|---:|---:|---:|---:|",
  `| FR-06 | ${summaries.fr06.logical} | ${summaries.fr06.attempts} | ${summaries.fr06.reached} | ${summaries.fr06.assertionFailures} | ${summaries.fr06.environmentFailures} |`,
  `| FR-10 | ${summaries.fr10.logical} | ${summaries.fr10.attempts} | ${summaries.fr10.reached} | ${summaries.fr10.assertionFailures} | ${summaries.fr10.environmentFailures} |`,
  `| FR-12 | ${summaries.fr12.logical} | ${summaries.fr12.attempts} | ${summaries.fr12.reached} | ${summaries.fr12.assertionFailures} | ${summaries.fr12.environmentFailures} |`,
  `| **Total** | **${totalSummary.logical}** | **${totalSummary.attempts}** | **${totalSummary.reached}** | **${totalSummary.assertionFailures}** | **${totalSummary.environmentFailures}** |`,
  "",
  `Each logical case is automated on all three configured browser projects. The complete external row is the test contract; each selected report records its own automation/SUT revision in run metadata (a single revision is shown here only when SUT_REVISION is explicitly supplied).`,
  "",
];

for (const [feature, config] of Object.entries(featureConfig)) {
  const rows = JSON.parse(readFileSync(path.resolve("test-data", config.data), "utf8"));
  const reports = Object.fromEntries(browsers.map((browser) => [browser, findReport(feature, browser)]));
  const outcomes = Object.fromEntries(browsers.map((browser) => [browser, resultMap(reports[browser])]));
  lines.push(`## ${config.requirement}`, "");
  lines.push(`Data: \`automation/test-data/${config.data}\` · Spec: \`automation/tests/${config.spec}\``, "");
  lines.push("| Case ID | Priority | EP/BVA partitions | Scenario | Preconditions/setup | Expected oracle | Chromium | Firefox | WebKit |", "|---|---|---|---|---|---|---|---|---|");
  for (const row of rows) {
    const partition = [...(row.partition ?? []), ...(row.boundary ?? [])].join(", ");
    const resultCells = browsers.map((browser) => {
      const state = outcomes[browser].get(row.id);
      if (!state) throw new Error(`Missing ${row.id}@${browser}`);
      return `[${state}](../automation/reports/${reports[browser]}/index.html)`;
    });
    lines.push(`| ${row.id} | ${row.priority} | ${escapeCell(partition)} | ${escapeCell(row.title)} | ${escapeCell(config.precondition)} | ${escapeCell(oracle(feature, row))} | ${resultCells.join(" | ")} |`);
  }
  lines.push("");
}

lines.push(
  "## Review and limitations",
  "",
  "- All 51 rows are external JSON objects loaded at runtime; no inline case array is used.",
  `- The selected evidence represents ${totalSummary.attempts} scheduled/attempted browser cases. Exactly ${totalSummary.reached} reached assertions; ${totalSummary.environmentFailures} Firefox attempts failed in page-fixture setup before SUT observation.`,
  "- Assertion failures are defect candidates, not automatically confirmed product defects. Agent triage has now confirmed 17 defects, rejected two oracle-gap candidates, and recorded the corresponding public Issue URLs and local screenshots under `../bugs/`.",
  "- The FR-06 invalid-quantity oracle checks browser constraint validity but does not also prove that cart state remained unchanged after an Add attempt. The FR-12 cleanup helper sends cleanup requests but does not assert deletion success/absence. These are documented current-source limitations and must not be hidden by the historical reports.",
);

writeFileSync(outputPath, `${lines.join("\n")}\n`, "utf8");
console.log(`Generated ${path.relative(process.cwd(), outputPath)}`);
