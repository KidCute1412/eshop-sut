import fs from "fs";
import path from "path";

const files = process.argv.slice(2);

if (files.length === 0) {
  console.error("Usage: node analyze_jtl.mjs <file1.jtl> [file2.jtl ...]");
  process.exit(1);
}

function percentile(sorted, p) {
  if (sorted.length === 0) return 0;
  const index = Math.ceil((p / 100) * sorted.length) - 1;
  return sorted[Math.max(0, Math.min(index, sorted.length - 1))];
}

function parseCsvLine(line) {
  const cells = [];
  let cell = "";
  let quoted = false;

  for (const char of line) {
    if (char === '"') {
      quoted = !quoted;
    } else if (char === "," && !quoted) {
      cells.push(cell);
      cell = "";
    } else {
      cell += char;
    }
  }
  cells.push(cell);
  return cells;
}

for (const file of files) {
  const text = fs.readFileSync(file, "utf8").trim();
  const lines = text.split(/\r?\n/);
  const headers = parseCsvLine(lines.shift());
  const elapsedIndex = headers.indexOf("elapsed");
  const successIndex = headers.indexOf("success");
  const timestampIndex = headers.indexOf("timeStamp");
  const labelIndex = headers.indexOf("label");

  if (elapsedIndex < 0 || successIndex < 0 || timestampIndex < 0) {
    console.error(`${file}: unsupported JTL format; expected CSV headers timeStamp, elapsed, success`);
    continue;
  }

  const samples = lines.map((line) => {
    const values = parseCsvLine(line);
    return {
      elapsed: Number(values[elapsedIndex]),
      success: values[successIndex] === "true",
      timestamp: Number(values[timestampIndex]),
      label: labelIndex >= 0 ? values[labelIndex] : "request",
    };
  });

  const elapsed = samples.map((sample) => sample.elapsed).sort((a, b) => a - b);
  const failures = samples.filter((sample) => !sample.success).length;
  const durationMs = Math.max(...samples.map((sample) => sample.timestamp)) - Math.min(...samples.map((sample) => sample.timestamp));
  const rps = durationMs > 0 ? samples.length / (durationMs / 1000) : 0;

  console.log(`\n${path.basename(file)}`);
  console.log(`samples=${samples.length}`);
  console.log(`errors=${failures}`);
  console.log(`errorRate=${((failures / samples.length) * 100).toFixed(2)}%`);
  console.log(`avg=${(elapsed.reduce((sum, value) => sum + value, 0) / elapsed.length).toFixed(2)} ms`);
  console.log(`p95=${percentile(elapsed, 95)} ms`);
  console.log(`p99=${percentile(elapsed, 99)} ms`);
  console.log(`throughput=${rps.toFixed(2)} req/s`);
}
