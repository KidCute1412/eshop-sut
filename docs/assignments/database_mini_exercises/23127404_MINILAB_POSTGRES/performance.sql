\set ON_ERROR_STOP on
\timing on

\echo '=== BEFORE INDEX ==='
DROP INDEX IF EXISTS idx_orders_user_id;
ANALYZE orders;

EXPLAIN (ANALYZE, BUFFERS)
SELECT user_id, SUM(final_amount)
FROM orders
GROUP BY user_id
ORDER BY SUM(final_amount) DESC;

\echo '=== CREATE INDEX ==='
CREATE INDEX idx_orders_user_id ON orders(user_id);
ANALYZE orders;

\echo '=== AFTER INDEX ==='
EXPLAIN (ANALYZE, BUFFERS)
SELECT user_id, SUM(final_amount)
FROM orders
GROUP BY user_id
ORDER BY SUM(final_amount) DESC;
