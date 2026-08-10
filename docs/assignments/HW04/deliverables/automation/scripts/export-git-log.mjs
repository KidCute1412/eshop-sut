import { spawnSync } from "node:child_process";
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";

const rootResult = spawnSync("git", ["rev-parse", "--show-toplevel"], { encoding: "utf8" });
if (rootResult.status !== 0) throw new Error(rootResult.stderr || "Not inside a Git repository");

const repositoryRoot = rootResult.stdout.trim();
const automationPath = path.relative(repositoryRoot, process.cwd()).replaceAll("\\", "/");
const legacyAutomationPath = "docs/assignments/HW04/schools/23127404-automation";
function gitLog(pathspecs) {
  const result = spawnSync(
    "git",
    [
      "log",
      "--date=iso-strict",
      "--pretty=format:commit %H%nAuthor: %an <%ae>%nDate: %ad%nSubject: %s",
      "--name-only",
      "--",
      ...pathspecs,
    ],
    { cwd: repositoryRoot, encoding: "utf8" },
  );
  if (result.status !== 0) throw new Error(result.stderr || "git log failed");
  return result.stdout.trim();
}

const completeHistory = gitLog(["docs/assignments/HW04"]);
const qualifyingHistory = gitLog([
  `${automationPath}/tests/*.spec.ts`,
  `${legacyAutomationPath}/tests/*.spec.ts`,
]);
if (!completeHistory) throw new Error("No committed HW04 history exists yet; nothing was exported.");

const outputDir = path.resolve("..", "git");
mkdirSync(outputDir, { recursive: true });
const output = path.join(outputDir, "23127404_HW04_git_commit_log.txt");
writeFileSync(
  output,
  [
    "HW04 COMPLETE HISTORY — all commits on the current submission branch that touch docs/assignments/HW04",
    "",
    completeHistory,
    "",
    "QUALIFYING TEST-SCRIPT HISTORY — commits that touch HW04 Playwright .spec.ts files",
    "",
    qualifyingHistory,
    "",
  ].join("\n"),
  "utf8",
);
console.log(`Exported complete HW04 history and qualifying spec history to ${path.relative(process.cwd(), output)}`);
