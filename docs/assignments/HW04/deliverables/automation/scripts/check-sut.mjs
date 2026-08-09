const targets = [
  ["Backend API", process.env.API_URL ?? "http://localhost:3000/api/products"],
  ["Frontend Web", process.env.WEB_URL ?? "http://localhost:5173"],
  ["Frontend Admin", process.env.ADMIN_URL ?? "http://localhost:5174"],
];

let failed = false;
for (const [name, url] of targets) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 5_000);
  try {
    const response = await fetch(url, { signal: controller.signal });
    const ok = response.status >= 200 && response.status < 400;
    console.log(`${ok ? "READY" : "FAILED"} ${name}: ${url} (${response.status})`);
    failed ||= !ok;
  } catch (error) {
    failed = true;
    console.error(`FAILED ${name}: ${url} (${error.message})`);
  } finally {
    clearTimeout(timer);
  }
}

if (failed) process.exitCode = 1;
