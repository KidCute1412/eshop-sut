import { existsSync, readFileSync, readdirSync } from "node:fs";
import path from "node:path";

const studentId = "23127404";
const reportRoot = path.resolve("reports");
const allowPartial = process.argv.includes("--allow-partial");
const isoPattern = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{3})?(?:Z|[+-]\d{2}:\d{2})$/;
const expectedPairs = new Set(
  ["fr06", "fr10", "fr12"].flatMap((feature) =>
    ["chromium", "firefox", "webkit"].map((browser) => `${feature}/${browser}`),
  ),
);
const expectedCases = { fr06: 16, fr10: 16, fr12: 19 };

function allSpecs(suite) {
  return [...(suite.specs ?? []), ...(suite.suites ?? []).flatMap(allSpecs)];
}

if (!existsSync(reportRoot)) throw new Error("No reports directory. Execute npm run run:matrix first.");

const directories = readdirSync(reportRoot, { withFileTypes: true }).filter((entry) => entry.isDirectory());
if (directories.length === 0) throw new Error("No generated report directories found.");

const latestByPair = new Map();
for (const entry of directories) {
  const dir = path.join(reportRoot, entry.name);
  const metadataPath = path.join(dir, "run-metadata.json");
  const indexPath = path.join(dir, "index.html");
  const jsonPath = path.join(dir, "results.json");
  if (!existsSync(metadataPath) || !existsSync(indexPath) || !existsSync(jsonPath)) continue;
  const metadata = JSON.parse(readFileSync(metadataPath, "utf8"));
  const key = `${metadata.feature}/${metadata.browser}`;
  if (!expectedPairs.has(key)) continue;
  const previous = latestByPair.get(key);
  if (!previous || metadata.runTimestamp > previous.metadata.runTimestamp) {
    latestByPair.set(key, { dir, metadata, indexPath });
  }
}

const errors = [];
for (const pair of expectedPairs) {
  const found = latestByPair.get(pair);
  if (!found) {
    if (!allowPartial) errors.push(`${pair}: missing HTML, JSON, or metadata report assets`);
    continue;
  }
  const { metadata, indexPath, dir } = found;
  const html = readFileSync(indexPath, "utf8");
  const expectedTotal = expectedCases[metadata.feature];
  if (metadata.runBy !== studentId) errors.push(`${pair}: wrong runBy metadata`);
  if (!isoPattern.test(metadata.runTimestamp)) errors.push(`${pair}: invalid ISO timestamp`);
  if (metadata.status === "running") errors.push(`${pair}: incomplete run metadata`);
  if (!html.includes(`Run by: ${studentId}`)) errors.push(`${pair}: student ID is not embedded in HTML`);
  if (!html.includes(metadata.runTimestamp)) errors.push(`${pair}: timestamp is not embedded in HTML`);
  const jsonReport = JSON.parse(readFileSync(path.join(dir, "results.json"), "utf8"));
  if (!Array.isArray(jsonReport.suites)) errors.push(`${pair}: invalid Playwright JSON report`);
  const specCount = Array.isArray(jsonReport.suites) ? jsonReport.suites.flatMap(allSpecs).length : 0;
  const statsTotal = ["expected", "skipped", "unexpected", "flaky"]
    .reduce((sum, key) => sum + (jsonReport.stats?.[key] ?? 0), 0);
  if (metadata.total !== expectedTotal || specCount !== expectedTotal) {
    errors.push(`${pair}: expected ${expectedTotal} cases, metadata=${metadata.total}, JSON specs=${specCount}`);
  }
  if (statsTotal !== metadata.total) errors.push(`${pair}: JSON stats total ${statsTotal} differs from metadata ${metadata.total}`);
  if (Buffer.byteLength(html) < 100_000) errors.push(`${pair}: HTML report is unexpectedly small`);
  if ((jsonReport.stats?.unexpected ?? 0) > 0 && !existsSync(path.join(dir, "data"))) {
    errors.push(`${pair}: failed run has no retained data directory`);
  }
  console.log(`FOUND ${pair}: ${path.relative(process.cwd(), dir)} (${metadata.status}, ${metadata.total} tests)`);
}

if (errors.length) {
  for (const error of errors) console.error(`INVALID ${error}`);
  process.exitCode = 1;
} else {
  console.log(`Validated ${latestByPair.size} feature/browser report(s).`);
}
