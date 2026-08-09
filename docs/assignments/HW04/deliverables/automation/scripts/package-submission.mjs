import archiver from "archiver";
import { createWriteStream } from "node:fs";
import path from "node:path";

const grade = process.argv[2] ?? "063";
if (!/^\d{3}$/.test(grade) || Number(grade) > 100) {
  throw new Error("Grade must be a three-digit value from 000 to 100.");
}

const deliverablesRoot = path.resolve("..");
const outputPath = path.join(deliverablesRoot, `23127404_HW04_AI_Automation_${grade}.zip`);
const output = createWriteStream(outputPath);
const archive = archiver("zip", { zlib: { level: 9 } });

const finished = new Promise((resolve, reject) => {
  output.on("close", resolve);
  archive.on("warning", (error) => (error.code === "ENOENT" ? console.warn(error.message) : reject(error)));
  archive.on("error", reject);
});

archive.pipe(output);
archive.glob("**/*", {
  cwd: deliverablesRoot,
  dot: true,
  ignore: [
    "automation/node_modules/**",
    "automation/test-results/**",
    "automation/dist/**",
    "*_HW04_AI_Automation_*.zip",
  ],
});
await archive.finalize();
await finished;
console.log(`Created ${outputPath} (${archive.pointer()} bytes)`);
