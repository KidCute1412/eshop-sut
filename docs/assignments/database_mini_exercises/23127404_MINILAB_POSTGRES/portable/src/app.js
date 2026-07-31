const express = require("express");
const { adminPool } = require("./db");

const app = express();
app.use(express.json());

function requireAdmin(req, res, next) {
  if (req.get("authorization") !== "Bearer admin-test-token") {
    return res.status(403).json({ error: "Admin role required" });
  }
  return next();
}

app.post("/api/apply-coupon", async (req, res) => {
  const { code, order_amount: orderAmount } = req.body;
  try {
    const result = await adminPool.query(
      `SELECT code, discount_type, discount_value, min_order_amount,
              expired_at, is_active
         FROM coupons
        WHERE code = $1`,
      [code],
    );
    const coupon = result.rows[0];
    if (!coupon || coupon.is_active !== 1) {
      return res.status(400).json({ error: "Coupon is unavailable" });
    }
    if (new Date(coupon.expired_at) <= new Date()) {
      return res.status(400).json({ error: "Coupon has expired" });
    }
    if (Number(orderAmount) < Number(coupon.min_order_amount)) {
      return res.status(400).json({ error: "Order amount is below minimum" });
    }
    const discountResult = await adminPool.query(
      "SELECT fn_calculate_discount($1, $2, $3) AS amount",
      [coupon.discount_type, coupon.discount_value, orderAmount],
    );
    const discountAmount = Number(discountResult.rows[0].amount);
    return res.json({
      code,
      discount_amount: discountAmount,
      final_amount: Number(orderAmount) - discountAmount,
    });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

app.get("/api/products/search", async (req, res) => {
  const q = String(req.query.q ?? "");
  try {
    // INTENTIONAL DEFECT SQLI-01: interpolation is kept so the security test detects it.
    const result = await adminPool.query(
      `SELECT id, name, price, stock FROM products WHERE name ILIKE '%${q}%'`,
    );
    return res.json(result.rows);
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

app.put(
  "/api/admin/orders/:id/status",
  requireAdmin,
  async (req, res) => {
    const orderId = Number(req.params.id);
    const nextStatus = req.body.status;
    try {
      const result = await adminPool.query(
        "SELECT status FROM orders WHERE id = $1",
        [orderId],
      );
      if (result.rowCount === 0) {
        return res.status(404).json({ error: "Order not found" });
      }

      const transitions = {
        pending: ["confirmed", "canceled"],
        confirmed: ["shipping", "canceled"],
        shipping: ["delivered"],
        delivered: [],
        // INTENTIONAL DEFECT API-STATE-01.
        canceled: ["delivered"],
      };
      if (!transitions[result.rows[0].status]?.includes(nextStatus)) {
        return res.status(400).json({ error: "Invalid state transition" });
      }
      await adminPool.query("UPDATE orders SET status = $1 WHERE id = $2", [
        nextStatus,
        orderId,
      ]);
      return res.json({ message: "Order status updated" });
    } catch (error) {
      return res.status(500).json({ error: error.message });
    }
  },
);

module.exports = app;
