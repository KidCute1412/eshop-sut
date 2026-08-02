// Batch-stamps 23127296@hcmus.edu.vn onto every PNG in screenshots/ in one
// pass, instead of opening each image in an editor by hand.
//
// Usage:
//   npm install -D sharp
//   node scripts/overlay_username.mjs
//
// Re-run any time after adding new screenshots — already-stamped files
// (suffix _stamped.png) are skipped so it's safe to re-run.

import sharp from "sharp";
import { readdirSync } from "fs";
import { join, extname, basename } from "path";

const USERNAME = "23127296@hcmus.edu.vn";
const DIR = new URL("../screenshots", import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1");

function overlaySvg(width) {
  return Buffer.from(`
    <svg width="${width}" height="40">
      <rect x="0" y="0" width="${width}" height="40" fill="black" fill-opacity="0.55"/>
      <text x="10" y="27" font-family="Arial, sans-serif" font-size="20" fill="white">${USERNAME}</text>
    </svg>
  `);
}

async function run() {
  const files = readdirSync(DIR).filter(
    (f) => extname(f).toLowerCase() === ".png" && !f.endsWith("_stamped.png"),
  );

  if (files.length === 0) {
    console.log(`No .png files found in ${DIR}`);
    return;
  }

  for (const file of files) {
    const inPath = join(DIR, file);
    const outPath = join(DIR, `${basename(file, ".png")}_stamped.png`);
    const img = sharp(inPath);
    const meta = await img.metadata();

    await img
      .composite([
        {
          input: overlaySvg(meta.width),
          top: meta.height - 40,
          left: 0,
        },
      ])
      .toFile(outPath);

    console.log(`Stamped -> ${outPath}`);
  }
}

run();
