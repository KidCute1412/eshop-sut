const frontendUrl = process.env.BASE_URL ?? "http://localhost:5173";
const backendUrl = process.env.BACKEND_URL ?? "http://localhost:3000";

async function check(name, url) {
  try {
    const response = await fetch(url, {
      signal: AbortSignal.timeout(5000),
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    console.log(`[ready] ${name}: ${url}`);
  } catch (error) {
    console.error(`[not ready] ${name}: ${url}`);
    console.error(`Reason: ${error.message}`);
    process.exitCode = 1;
  }
}

await check("EShop backend product API", `${backendUrl}/api/products/1`);
await check("EShop frontend", `${frontendUrl}/product/1`);

if (process.exitCode) {
  console.error(
    "Start the EShop backend and frontend, then run the test again. " +
      "Override BASE_URL and BACKEND_URL when the SUT uses different URLs.",
  );
}
