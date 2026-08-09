import archiver from "archiver";
import { createWriteStream, mkdirSync } from "node:fs";
import path from "node:path";

const outputDir = path.resolve("dist");
mkdirSync(outputDir, { recursive: true });
const outputPath = path.join(outputDir, "23127404_HW04_Automation_Source.zip");
const output = createWriteStream(outputPath);
const archive = archiver("zip", { zlib: { level: 9 } });

const finished = new Promise((resolve, reject) => {
  output.on("close", resolve);
  archive.on("warning", (error) => (error.code === "ENOENT" ? console.warn(error.message) : reject(error)));
  archive.on("error", reject);
});

archive.pipe(output);
archive.glob("**/*", {
  cwd: process.cwd(),
  dot: true,
  ignore: ["node_modules/**", "test-results/**", "reports/**", "dist/**"],
});
await archive.finalize();
await finished;
console.log(`Created ${path.relative(process.cwd(), outputPath)} (${archive.pointer()} bytes)`);
