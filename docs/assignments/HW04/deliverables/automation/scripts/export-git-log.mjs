import { spawnSync } from "node:child_process";
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";

const rootResult = spawnSync("git", ["rev-parse", "--show-toplevel"], { encoding: "utf8" });
if (rootResult.status !== 0) throw new Error(rootResult.stderr || "Not inside a Git repository");

const repositoryRoot = rootResult.stdout.trim();
const automationPath = path.relative(repositoryRoot, process.cwd()).replaceAll("\\", "/");
const legacyAutomationPath = "docs/assignments/HW04/schools/23127404-automation";
const logResult = spawnSync(
  "git",
  [
    "log",
    "--date=iso-strict",
    "--pretty=format:commit %H%nAuthor: %an <%ae>%nDate: %ad%nSubject: %s",
    "--name-only",
    "--",
    `${automationPath}/tests/*.spec.ts`,
    `${legacyAutomationPath}/tests/*.spec.ts`,
  ],
  { cwd: repositoryRoot, encoding: "utf8" },
);
if (logResult.status !== 0) throw new Error(logResult.stderr || "git log failed");
if (!logResult.stdout.trim()) throw new Error("No committed automation spec history exists yet; nothing was exported.");

const outputDir = path.resolve("..", "git");
mkdirSync(outputDir, { recursive: true });
const output = path.join(outputDir, "23127404_HW04_git_commit_log.txt");
writeFileSync(output, `${logResult.stdout.trim()}\n`, "utf8");
console.log(`Exported qualifying spec history to ${path.relative(process.cwd(), output)}`);
