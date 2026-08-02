// Automates the *navigation* through EShop's 5 required screens in a real,
// visible (headed) browser window, pausing at each screen so you can take a
// real OS-level screenshot (with actual browser/OS chrome visible, per the
// assignment's anti-cheat requirement). It does NOT fabricate screenshots —
// it only saves you from manually clicking through register/login/add-to-cart
// on every browser engine.
//
// Usage:
//   npm install -D playwright
//   npx playwright install chromium firefox        # webkit optional, see README note
//   node scripts/capture_screens.mjs chromium
//   node scripts/capture_screens.mjs firefox
//
// At each pause, use your OS screenshot tool (Win+Shift+S on Windows) to
// capture the FULL browser window (address bar + tab visible), then save
// it as screenshots/<engine>_<screen>.png and overlay your username
// (see overlay_username.mjs).

import { chromium, firefox, webkit } from "playwright";

const ENGINES = { chromium, firefox, webkit };
const engineName = process.argv[2] || "chromium";
const BASE_URL = process.env.SUT_URL || "http://localhost:5173";

const TEST_USER = {
  name: "CP Test",
  email: `cptest_${Date.now()}@example.com`,
  password: "Abc12345 ", // note: trailing space — see BUG-12/reset-password regex quirk
};

function pause(label) {
  console.log(`\n=== ${label} — take your OS-level screenshot now ===`);
  console.log("Press Enter in this terminal once you've captured it...");
  return new Promise((resolve) => {
    process.stdin.once("data", () => resolve());
  });
}

async function run() {
  const engine = ENGINES[engineName];
  if (!engine) {
    console.error(`Unknown engine "${engineName}". Use: chromium | firefox | webkit`);
    process.exit(1);
  }

  const browser = await engine.launch({ headless: false });
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });

  await page.goto(BASE_URL);
  await pause(`${engineName}: Home (${BASE_URL})`);

  await page.goto(`${BASE_URL}/register`);
  await pause(`${engineName}: Register`);

  await page.goto(`${BASE_URL}/login`);
  await pause(`${engineName}: Login`);

  // Add first visible product to cart, then go to cart/checkout so those
  // screens aren't empty in the screenshot.
  await page.goto(BASE_URL);
  const firstProductLink = page.locator('a[href^="/product/"]').first();
  if (await firstProductLink.count()) {
    await firstProductLink.click();
    const addToCartBtn = page.getByRole("button", { name: /thêm vào giỏ hàng/i });
    if (await addToCartBtn.count()) {
      await addToCartBtn.click();
      await addToCartBtn.click(); // BUG-25: first click is a no-op, click twice to be safe
    }
  }

  await page.goto(`${BASE_URL}/cart`);
  await pause(`${engineName}: Cart`);

  await page.goto(`${BASE_URL}/checkout`);
  await pause(`${engineName}: Checkout`);

  await browser.close();
  console.log(`Done with ${engineName}.`);
  process.exit(0);
}

run();
