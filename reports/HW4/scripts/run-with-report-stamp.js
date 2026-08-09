const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const studentId = process.env.STUDENT_ID || "23127539";
const stamp = `Run by: ${studentId} - ${new Date().toISOString()}`;
const reportDir = path.join(__dirname, "..", "reports");

const playwrightArgs = ["playwright", "test", ...process.argv.slice(2)];
const command = process.platform === "win32" ? "cmd.exe" : "npx";
const args = process.platform === "win32" ? ["/c", "npx", ...playwrightArgs] : playwrightArgs;
const result = spawnSync(command, args, {
  cwd: path.join(__dirname, ".."),
  env: process.env,
  stdio: "inherit"
});

if (result.error) {
  console.error(result.error.message);
}

function htmlEscape(value) {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function findIndexHtmlFiles(dir) {
  if (!fs.existsSync(dir)) {
    return [];
  }
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...findIndexHtmlFiles(fullPath));
    } else if (entry.isFile() && entry.name.toLowerCase() === "index.html") {
      files.push(fullPath);
    }
  }
  return files;
}

for (const htmlFile of findIndexHtmlFiles(reportDir)) {
  let html = fs.readFileSync(htmlFile, "utf8");
  if (!html.includes("Run by:")) {
    const visibleStamp = `<div data-hw04-run-by="true" style="position:fixed;right:12px;bottom:12px;z-index:99999;background:#111827;color:#fff;font:12px Arial,sans-serif;padding:6px 8px;border-radius:4px">${htmlEscape(stamp)}</div>`;
    html = html.replace("</body>", `${visibleStamp}\n</body>`);
  }
  if (/<title>.*?<\/title>/i.test(html)) {
    html = html.replace(/<title>.*?<\/title>/i, `<title>${htmlEscape(stamp)}</title>`);
  } else {
    html = html.replace("<head>", `<head><title>${htmlEscape(stamp)}</title>`);
  }
  fs.writeFileSync(htmlFile, html, "utf8");
}

process.exit(result.status === null ? 1 : result.status);
