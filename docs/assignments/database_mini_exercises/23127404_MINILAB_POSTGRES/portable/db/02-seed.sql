\set ON_ERROR_STOP on

INSERT INTO users(email, role) VALUES
  ('admin@minilab.test', 'admin'),
  ('alice@minilab.test', 'customer'),
  ('bob@minilab.test', 'customer'),
  ('carol@minilab.test', 'customer'),
  ('dave@minilab.test', 'customer');

INSERT INTO products(name, price, stock) VALUES
  ('Keyboard', 200.00, 10),
  ('Mouse', 100.00, 7),
  ('Monitor', 500.00, 4),
  ('USB Cable', 25.00, 30),
  ('Out of Stock Item', 150.00, 0);

INSERT INTO coupons(
  code, discount_type, discount_value, min_order_amount, expired_at, is_active
) VALUES
  ('CP_OK', 'percent', 10, 200, '2099-12-31 23:59:59', 1),
  ('CP_EXPIRED', 'percent', 20, 100, '2000-01-01 00:00:00', 1),
  ('CP_INACTIVE', 'fixed', 50, 100, '2099-12-31 23:59:59', 0),
  ('CP_PERCENT150', 'percent', 150, 0, '2099-12-31 23:59:59', 1);

INSERT INTO orders(user_id, total_amount, final_amount, status, created_at)
SELECT
  ((n - 1) % 5) + 1,
  100 + n,
  100 + n,
  CASE
    WHEN n = 1 THEN 'canceled'
    WHEN n % 5 = 0 THEN 'delivered'
    WHEN n % 3 = 0 THEN 'confirmed'
    ELSE 'pending'
  END,
  TIMESTAMP '2026-01-01 00:00:00' + (n || ' hours')::INTERVAL
FROM generate_series(1, 200) AS n;

SELECT setval('users_id_seq', (SELECT MAX(id) FROM users));
SELECT setval('products_id_seq', (SELECT MAX(id) FROM products));
SELECT setval('coupons_id_seq', (SELECT MAX(id) FROM coupons));
SELECT setval('orders_id_seq', (SELECT MAX(id) FROM orders));
