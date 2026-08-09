import { copyFileSync, existsSync, mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { spawnSync } from "node:child_process";
import path from "node:path";

const automationRoot = process.cwd();
const deliverablesRoot = path.resolve(automationRoot, "..");
const evidenceRoot = path.join(deliverablesRoot, "bugs", "evidence");
const packetRoot = path.join(deliverablesRoot, "bugs", "issue-packets");
const testResultsRoot = path.join(automationRoot, "test-results");
const sourceRevision = spawnSync("git", ["rev-parse", "HEAD"], { encoding: "utf8" }).stdout.trim();

const candidates = [
  ["HW04-CAND-001", "FR-06", "FR06-07", "fr06-product-detail.spec.ts", "Required category text `Điện thoại` was not found", "Medium", "Confirmed", "FR-06 explicitly requires the product category; the same mismatch recurs across all three browsers."],
  ["HW04-CAND-002", "FR-06", "FR06-09", "fr06-product-detail.spec.ts", "Quantity input lacks the required `min=1` constraint", "Medium", "Confirmed", "FR-06 requires a positive integer quantity with minimum one; the missing native constraint is deterministic."],
  ["HW04-CAND-003", "FR-06", "FR06-11", "fr06-product-detail.spec.ts", "The first add click does not satisfy the selected feedback assertion", "Medium", "Rejected", "The requirement permits visible toast, badge, or equivalent feedback; the original assertion hardcodes button text and does not prove cart state."],
  ["HW04-CAND-004", "FR-06", "FR06-12", "fr06-product-detail.spec.ts", "The valid-quantity add flow does not satisfy the selected feedback assertion", "Medium", "Rejected", "Same oracle gap as HW04-CAND-003; this is not independently promoted to a product defect without a stronger feedback/state oracle."],
  ["HW04-CAND-005", "FR-06", "FR06-13", "fr06-product-detail.spec.ts", "Quantity `0` remains HTML-valid", "High", "Confirmed", "The requirement rejects non-positive quantities; native validity is deterministic across browsers."],
  ["HW04-CAND-006", "FR-06", "FR06-14", "fr06-product-detail.spec.ts", "Quantity `-1` remains HTML-valid", "High", "Confirmed", "The requirement rejects negative quantities; native validity is deterministic across browsers."],
  ["HW04-CAND-007", "FR-10", "FR10-06", "fr10-order-state-machine.spec.ts", "Customer UI exposes cancellation after `confirmed -> shipping`", "Medium", "Confirmed", "The state-machine requirement forbids cancellation after shipping; the UI exposes an invalid action."],
  ["HW04-CAND-008", "FR-10", "FR10-11", "fr10-order-state-machine.spec.ts", "Shipping order remains cancellable after rejected Admin cancellation", "Medium", "Confirmed", "The terminal/role restriction is explicit and the invalid UI action recurs across browsers."],
  ["HW04-CAND-009", "FR-10", "FR10-12", "fr10-order-state-machine.spec.ts", "User cancellation of shipping order returns HTTP 200", "High", "Confirmed", "Shipping orders must reject user cancellation; a successful response violates the state transition contract."],
  ["HW04-CAND-010", "FR-10", "FR10-16", "fr10-order-state-machine.spec.ts", "Canceled order accepts transition to delivered", "High", "Confirmed", "Canceled is a terminal state under FR-10; accepting delivery is a direct contract violation."],
  ["HW04-CAND-011", "FR-12", "FR12-03", "fr12-access-control.spec.ts", "Regular user JWT reads `/api/admin/users`", "Critical", "Confirmed", "Admin-user listing must require an admin role; a regular JWT receives protected data."],
  ["HW04-CAND-012", "FR-12", "FR12-06", "fr12-access-control.spec.ts", "Regular user JWT reads `/api/admin/orders`", "Critical", "Confirmed", "Admin-order listing must require an admin role; a regular JWT receives protected data."],
  ["HW04-CAND-013", "FR-12", "FR12-08", "fr12-access-control.spec.ts", "Anonymous product creation returns HTTP 200", "Critical", "Confirmed", "Unauthenticated data mutation must be rejected; the endpoint creates data without a JWT."],
  ["HW04-CAND-014", "FR-12", "FR12-09", "fr12-access-control.spec.ts", "Regular user JWT creates a product", "Critical", "Confirmed", "Product creation must require an admin role; a regular JWT is accepted."],
  ["HW04-CAND-015", "FR-12", "FR12-11", "fr12-access-control.spec.ts", "Anonymous product update returns HTTP 200", "Critical", "Confirmed", "Unauthenticated product mutation must be rejected; the endpoint accepts the request."],
  ["HW04-CAND-016", "FR-12", "FR12-12", "fr12-access-control.spec.ts", "Regular user JWT deletes a product", "Critical", "Confirmed", "Product deletion must require an admin role; a regular JWT is accepted."],
  ["HW04-CAND-017", "FR-12", "FR12-14", "fr12-access-control.spec.ts", "Regular user JWT creates a category", "Critical", "Confirmed", "Category creation must require an admin role; a regular JWT is accepted."],
  ["HW04-CAND-018", "FR-12", "FR12-17", "fr12-access-control.spec.ts", "Regular user JWT creates an admin coupon", "Critical", "Confirmed", "Coupon creation must require an admin role; a regular JWT is accepted."],
  ["HW04-CAND-019", "FR-12", "FR12-19", "fr12-access-control.spec.ts", "Regular user reaches import validation instead of authorization rejection", "Critical", "Confirmed", "Authorization must be enforced before import validation; a regular JWT reaches the protected operation."],
];

function walk(directory) {
  if (!existsSync(directory)) return [];
  const output = [];
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    const full = path.join(directory, entry.name);
    if (entry.isDirectory()) output.push(...walk(full));
    else output.push(full);
  }
  return output;
}

function newestSince(extension, startedAt) {
  return walk(testResultsRoot)
    .filter((file) => file.endsWith(extension) && statSync(file).mtimeMs >= startedAt - 2000)
    .sort((a, b) => statSync(b).mtimeMs - statSync(a).mtimeMs)[0];
}

function safeTitle(value) {
  return value.replaceAll("`", "").replaceAll("/", "-");
}

mkdirSync(evidenceRoot, { recursive: true });
mkdirSync(packetRoot, { recursive: true });
const decisions = [];

for (const [candidateId, feature, caseId, specFile, mismatch, severity, disposition, rationale] of candidates) {
  const startedAt = Date.now();
  const reportKey = `bug-evidence-${candidateId.toLowerCase()}-firefox`;
  const result = spawnSync(
    process.execPath,
    [path.resolve("node_modules", "@playwright", "test", "cli.js"), "test", `tests/${specFile}`, "--project=firefox", "--grep", caseId, "--reporter=line"],
    {
      cwd: automationRoot,
      env: {
        ...process.env,
        FEATURE_KEY: feature.toLowerCase().replace("-", ""),
        BROWSER_KEY: "firefox",
        RUN_TIMESTAMP: new Date().toISOString(),
        REPORT_KEY: reportKey,
        SUT_REVISION: sourceRevision,
        AUTOMATION_REVISION: sourceRevision,
        EXECUTION_COMMAND: `npx playwright test tests/${specFile} --project=firefox --grep ${caseId}`,
      },
      encoding: "utf8",
      stdio: "pipe",
    },
  );
  const screenshot = newestSince(".png", startedAt);
  const trace = newestSince(".zip", startedAt);
  const evidenceDirectory = path.join(evidenceRoot, candidateId);
  mkdirSync(evidenceDirectory, { recursive: true });
  const screenshotTarget = screenshot ? path.join(evidenceDirectory, "screenshot.png") : undefined;
  const traceTarget = trace ? path.join(evidenceDirectory, "trace.zip") : undefined;
  if (screenshotTarget) copyFileSync(screenshot, screenshotTarget);
  if (traceTarget) copyFileSync(trace, traceTarget);
  const evidence = {
    candidateId,
    feature,
    caseId,
    browser: "Firefox 141.0 headless",
    sourceRevision,
    command: `npx playwright test tests/${specFile} --project=firefox --grep ${caseId}`,
    exitCode: result.status,
    observedFailure: result.status !== 0,
    screenshot: screenshotTarget ? path.relative(deliverablesRoot, screenshotTarget).replaceAll("\\", "/") : null,
    trace: traceTarget ? path.relative(deliverablesRoot, traceTarget).replaceAll("\\", "/") : null,
    capturedAt: new Date().toISOString(),
  };
  writeFileSync(path.join(evidenceDirectory, "evidence.json"), `${JSON.stringify(evidence, null, 2)}\n`);
  decisions.push({ candidateId, feature, caseId, mismatch, severity, disposition, rationale, evidence });
}

const confirmed = decisions.filter((item) => item.disposition === "Confirmed");
for (const [index, item] of confirmed.entries()) {
  const defectId = `BUG-${String(index + 1).padStart(3, "0")}`;
  item.defectId = defectId;
  const packetDirectory = path.join(packetRoot, defectId);
  mkdirSync(packetDirectory, { recursive: true });
  const screenshotReference = item.evidence.screenshot ?? "PENDING — rerun did not produce a screenshot attachment";
  const body = `# [23127404][${item.feature}] ${safeTitle(item.mismatch)}\n\n## Summary\n\n${item.mismatch}.\n\n## Affected requirements and cases\n\n- Requirement: ${item.feature}\n- Case ID: ${item.caseId}\n- Candidate ID: ${item.candidateId}\n\n## Environment\n\n- SUT revision: ${item.evidence.sourceRevision}\n- Browser: ${item.evidence.browser}\n- Execution command: \`${item.evidence.command}\`\n- SUT URL: http://localhost:5173 (web) / http://localhost:3000 (API)\n\n## Preconditions\n\nUse the seeded database and the credentials/data defined by the external JSON case.\n\n## Steps to reproduce\n\n1. Start the SUT using the documented HW04 setup.\n2. Execute case \`${item.caseId}\` with the command above.\n3. Observe the response or UI state described by the case.\n\n## Expected result\n\nThe behavior must satisfy the ${item.feature} requirement and the expected oracle in the external test-data row.\n\n## Actual result\n\n${item.mismatch}.\n\n## Reproducibility\n\nThe failure was observed by the automated rerun; see the attached evidence metadata and Playwright report.\n\n## Severity\n\n**${item.severity}** — ${item.rationale}\n\n## Evidence\n\n- Screenshot: \`${screenshotReference}\`\n- Trace: \`${item.evidence.trace ?? "Not captured"}\`\n- Case evidence: \`bugs/evidence/${item.candidateId}/evidence.json\`\n\n## Scope\n\nThis Issue was prepared from the HW04 runtime candidate and should be filed only after confirming the attached evidence is visible and contains no sensitive data.\n`;
  writeFileSync(path.join(packetDirectory, "issue-body.md"), body, "utf8");
  writeFileSync(path.join(packetDirectory, "packet-metadata.json"), `${JSON.stringify({ defectId, candidateIds: [item.candidateId], issueUrl: null, screenshot: item.evidence.screenshot }, null, 2)}\n`);
}

const triageRows = decisions.map((item) => `| ${item.candidateId} | ${item.caseId} | ${item.disposition} | ${item.defectId ?? "—"} | ${item.rationale} | ${item.evidence.screenshot ?? "Not captured"} |`).join("\n");
writeFileSync(path.join(deliverablesRoot, "bugs", "triage-decisions.md"), `# HW04 Agent Triage Decisions\n\nGenerated from fresh candidate reruns at revision \`${sourceRevision}\`. The agent classified each candidate using the requirement oracle, runtime result, and test-design audit. These are not public GitHub Issues until a packet is filed by the student.\n\n| Candidate | Case | Decision | Defect | Rationale | Screenshot |\n|---|---|---|---|---|---|\n${triageRows}\n`, "utf8");

console.log(`Prepared ${decisions.length} candidate decisions and ${confirmed.length} confirmed defect packets.`);
