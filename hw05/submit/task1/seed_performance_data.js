const fs = require("fs");
const path = require("path");
const sqlite3 = require("sqlite3").verbose();

const taskDir = __dirname;
const backendDir = path.resolve(taskDir, "../../../backend");
const dbPath = path.join(backendDir, "database.sqlite");
const usersCsv = path.join(taskDir, "test_data_users.csv");
const productsCsv = path.join(taskDir, "test_data_products.csv");

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

function readCsv(file) {
  const lines = fs.readFileSync(file, "utf8").trim().split(/\r?\n/);
  const headers = parseCsvLine(lines.shift());
  return lines.map((line) => {
    const values = parseCsvLine(line);
    return Object.fromEntries(headers.map((header, index) => [header, values[index] || ""]));
  });
}

const users = readCsv(usersCsv);
const products = readCsv(productsCsv);
const db = new sqlite3.Database(dbPath);

db.serialize(() => {
  db.run("DELETE FROM users WHERE email LIKE 'user_load_%@test.com'");

  const insertUser = db.prepare(`
    INSERT INTO users (name, email, password, role, login_attempts, locked_until, shipping_address, phone)
    VALUES (?, ?, ?, 'user', 0, NULL, ?, ?)
  `);

  users.forEach((user) => {
    insertUser.run(user.name, user.email, user.password, user.shipping_address, user.phone);
  });
  insertUser.finalize();

  const upsertProduct = db.prepare(`
    INSERT INTO products (id, name, price, description, imageUrl, category_id)
    VALUES (?, ?, ?, ?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
      name = excluded.name,
      price = excluded.price,
      description = excluded.description,
      imageUrl = excluded.imageUrl,
      category_id = excluded.category_id
  `);

  products.forEach((product) => {
    upsertProduct.run(
      Number(product.product_id),
      product.product_name,
      Number(product.product_price),
      `Performance data item for keyword ${product.search_keyword}`,
      `https://placehold.co/300x300/png?text=${encodeURIComponent(product.product_name)}`,
      3,
    );
  });
  upsertProduct.finalize();
});

db.close((err) => {
  if (err) {
    console.error(err.message);
    process.exitCode = 1;
    return;
  }
  console.log(`Seeded ${users.length} performance users and ${products.length} products into ${dbPath}`);
});
