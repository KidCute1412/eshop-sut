const request = require("supertest");
const app = require("./portable/src/app");
const { adminPool, appUserPool } = require("./portable/src/db");

const ADMIN_TOKEN = "Bearer admin-test-token";

afterEach(async () => {
  await adminPool.query(`
    DELETE FROM order_items WHERE order_id > 200;
    DELETE FROM orders WHERE id > 200;
    UPDATE products
       SET stock = CASE id WHEN 1 THEN 10 WHEN 5 THEN 0 ELSE stock END
     WHERE id IN (1, 5);
    UPDATE orders SET status = 'canceled' WHERE id = 1;
    DELETE FROM users WHERE email = 'duplicate-test@minilab.test';
    SELECT setval('orders_id_seq', GREATEST((SELECT MAX(id) FROM orders), 200));
  `);
});

afterAll(async () => {
  await Promise.all([adminPool.end(), appUserPool.end()]);
});

describe("Schema and constraints", () => {
  test("SCHEMA-01 [EP-INV-01] rejects duplicate UNIQUE email", async () => {
    await adminPool.query(
      "INSERT INTO users(email) VALUES ($1)",
      ["duplicate-test@minilab.test"],
    );

    await expect(
      adminPool.query("INSERT INTO users(email) VALUES ($1)", [
        "duplicate-test@minilab.test",
      ]),
    ).rejects.toMatchObject({ code: "23505" });
  });
});

describe("Function domain and boundary testing", () => {
  test("FN-00 [BVA-BND-01] accepts the on-point 100 percent", async () => {
    const result = await adminPool.query(
      "SELECT fn_calculate_discount('percent', 100, 200) AS amount",
    );
    expect(Number(result.rows[0].amount)).toBe(200);
  });

  test("FN-01 [EP-INV-02/BVA-BND-01] caps 101 and 150 percent at the order amount", async () => {
    const result = await adminPool.query(`
      SELECT value,
             fn_calculate_discount('percent', value, 200) AS amount
        FROM unnest(ARRAY[101, 150]) AS value
       ORDER BY value
    `);
    for (const row of result.rows) {
      expect(Number(row.amount)).toBeLessThanOrEqual(200);
    }
  });
});

describe("Trigger testing", () => {
  test("TRIGGER-00 [BVA-BND-02] permits stock exactly zero", async () => {
    const result = await adminPool.query(
      "UPDATE products SET stock = 0 WHERE id = 1 RETURNING stock",
    );
    expect(result.rows[0].stock).toBe(0);
  });

  test("TRIGGER-01 [EP-INV-03/BVA-BND-02] rejects stock -1 with the trigger error", async () => {
    const trigger = await adminPool.query(`
      SELECT tgname
        FROM pg_trigger
       WHERE tgrelid = 'products'::regclass
         AND tgname = 'trg_prevent_negative_stock'
         AND NOT tgisinternal
    `);
    expect(trigger.rowCount).toBe(1);

    await expect(
      adminPool.query("UPDATE products SET stock = -1 WHERE id = 1"),
    ).rejects.toMatchObject({
      code: "P0001",
      message: expect.stringContaining("trg_prevent_negative_stock"),
    });
  });
});

describe("Stored procedure atomicity", () => {
  test("SP-00 [EP-VAL-04] completes checkout when every item has stock", async () => {
    const before = await adminPool.query(
      "SELECT stock FROM products WHERE id = 1",
    );

    await adminPool.query(
      "CALL sp_process_checkout($1, $2::jsonb)",
      [2, JSON.stringify([{ product_id: 1, quantity: 1 }])],
    );

    const after = await adminPool.query(
      "SELECT stock FROM products WHERE id = 1",
    );
    expect(after.rows[0].stock).toBe(before.rows[0].stock - 1);
  });

  test("SP-01 [EP-INV-04] rolls back every stock and order change when one item is out of stock", async () => {
    const stockBefore = await adminPool.query(
      "SELECT stock FROM products WHERE id = 1",
    );
    const ordersBefore = await adminPool.query(
      "SELECT COUNT(*)::int AS count FROM orders",
    );

    let checkoutError;
    try {
      await adminPool.query(
        "CALL sp_process_checkout($1, $2::jsonb)",
        [
          2,
          JSON.stringify([
            { product_id: 1, quantity: 1 },
            { product_id: 5, quantity: 1 },
          ]),
        ],
      );
    } catch (error) {
      checkoutError = error;
    }

    const stockAfter = await adminPool.query(
      "SELECT stock FROM products WHERE id = 1",
    );
    const ordersAfter = await adminPool.query(
      "SELECT COUNT(*)::int AS count FROM orders",
    );

    expect(checkoutError).toBeDefined();
    expect(stockAfter.rows[0].stock).toBe(stockBefore.rows[0].stock);
    expect(ordersAfter.rows[0].count).toBe(ordersBefore.rows[0].count);
  });
});

describe("Functional API testing", () => {
  test("API-COUPON-01 [EP-INV-05] rejects an expired coupon", async () => {
    const response = await request(app)
      .post("/api/apply-coupon")
      .send({ code: "CP_EXPIRED", order_amount: 300 });
    expect(response.status).toBe(400);
  });

  test("API-COUPON-02 [BVA-BND-03] accepts an order exactly at the coupon minimum", async () => {
    const response = await request(app)
      .post("/api/apply-coupon")
      .send({ code: "CP_OK", order_amount: 200 });
    expect(response.status).toBe(200);
    expect(response.body.final_amount).toBe(180);
  });

  test("API-STATE-01 [EP-INV-06] blocks canceled to delivered transition", async () => {
    const response = await request(app)
      .put("/api/admin/orders/1/status")
      .set("Authorization", ADMIN_TOKEN)
      .send({ status: "delivered" });
    expect(response.status).toBe(400);
  });
});

describe("Security testing", () => {
  test("SQLI-01 [EP-INV-07] treats an injection payload as literal search text", async () => {
    const before = await adminPool.query(
      "SELECT COUNT(*)::int AS count FROM products",
    );
    const response = await request(app)
      .get("/api/products/search")
      .query({ q: "' OR '1'='1" });
    const after = await adminPool.query(
      "SELECT COUNT(*)::int AS count FROM products",
    );

    expect(response.status).not.toBe(500);
    expect(response.body).toEqual([]);
    expect(after.rows[0].count).toBe(before.rows[0].count);
  });

  test("RBAC-01 [EP-INV-08] denies DROP TABLE to app_user", async () => {
    const readable = await appUserPool.query(
      "SELECT COUNT(*)::int AS count FROM products",
    );
    expect(readable.rows[0].count).toBe(5);

    await expect(
      appUserPool.query("DROP TABLE products"),
    ).rejects.toMatchObject({ code: "42501" });
  });
});
