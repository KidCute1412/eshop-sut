import { mkdirSync, readFileSync } from "node:fs";
import { spawnSync } from "node:child_process";

mkdirSync("evidence", { recursive: true });

const jestBin = process.platform === "win32"
  ? "node_modules\\.bin\\jest.cmd"
  : "node_modules/.bin/jest";
const result = spawnSync(
  jestBin,
  [
    "--runInBand",
    "--json",
    "--outputFile=evidence/test-results.json",
  ],
  { encoding: "utf8", shell: process.platform === "win32" },
);

process.stdout.write(result.stdout ?? "");
process.stderr.write(result.stderr ?? "");

let report;
try {
  report = JSON.parse(readFileSync("evidence/test-results.json", "utf8"));
} catch (error) {
  console.error(`LAB ERROR: Jest did not produce readable JSON: ${error.message}`);
  process.exit(2);
}

const expectedDefects = new Set(["FN-01", "SP-01", "API-STATE-01", "SQLI-01"]);
const failed = [];
for (const suite of report.testResults ?? []) {
  for (const assertion of suite.assertionResults ?? []) {
    if (assertion.status === "failed") {
      const id = assertion.title.split(" ", 1)[0];
      failed.push({ id, title: assertion.fullName });
    }
  }
}

const actualIds = new Set(failed.map(({ id }) => id));
const missing = [...expectedDefects].filter((id) => !actualIds.has(id));
const unexpected = failed.filter(({ id }) => !expectedDefects.has(id));

console.log("\n=== MINI LAB CLASSIFICATION ===");
console.log(`Tests: ${report.numTotalTests}`);
console.log(`Assertions passed: ${report.numPassedTests}`);
console.log(`Expected defects detected: ${failed.length - unexpected.length}`);
for (const item of failed) {
  const kind = expectedDefects.has(item.id) ? "EXPECTED DEFECT" : "UNEXPECTED";
  console.log(`- [${kind}] ${item.title}`);
}

if (missing.length || unexpected.length || report.numRuntimeErrorTestSuites > 0) {
  if (missing.length) console.error(`Missing expected defects: ${missing.join(", ")}`);
  if (unexpected.length) {
    console.error(`Unexpected failures: ${unexpected.map((x) => x.id).join(", ")}`);
  }
  process.exit(1);
}

console.log("LAB RESULT: PASS - all expected defects were detected, with no unexpected failures.");
