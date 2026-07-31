const app = require("./app");
const { adminPool, appUserPool } = require("./db");

const port = Number(process.env.PORT ?? 3010);
const server = app.listen(port, () => {
  console.log(`Mini lab API listening on http://localhost:${port}`);
});

async function shutdown() {
  server.close();
  await Promise.all([adminPool.end(), appUserPool.end()]);
}

process.on("SIGTERM", shutdown);
process.on("SIGINT", shutdown);
