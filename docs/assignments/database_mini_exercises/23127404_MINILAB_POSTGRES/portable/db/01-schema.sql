\set ON_ERROR_STOP on

REVOKE CREATE ON SCHEMA public FROM PUBLIC;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  role VARCHAR(20) NOT NULL DEFAULT 'customer'
    CHECK (role IN ('customer', 'admin'))
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price NUMERIC(10, 2) NOT NULL CHECK (price > 0),
  stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0)
);

CREATE TABLE coupons (
  id SERIAL PRIMARY KEY,
  code VARCHAR(50) UNIQUE NOT NULL,
  discount_type VARCHAR(20) NOT NULL
    CHECK (discount_type IN ('percent', 'fixed')),
  discount_value NUMERIC(10, 2) NOT NULL CHECK (discount_value >= 0),
  min_order_amount NUMERIC(10, 2) NOT NULL DEFAULT 0
    CHECK (min_order_amount >= 0),
  expired_at TIMESTAMP NOT NULL,
  is_active INT NOT NULL DEFAULT 1 CHECK (is_active IN (0, 1))
);

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  total_amount NUMERIC(10, 2) NOT NULL CHECK (total_amount >= 0),
  final_amount NUMERIC(10, 2) NOT NULL CHECK (final_amount >= 0),
  status VARCHAR(20) NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending', 'confirmed', 'shipping', 'delivered', 'canceled')),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
  id SERIAL PRIMARY KEY,
  order_id INT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
  product_id INT NOT NULL REFERENCES products(id),
  quantity INT NOT NULL CHECK (quantity > 0),
  unit_price NUMERIC(10, 2) NOT NULL CHECK (unit_price > 0)
);

CREATE OR REPLACE FUNCTION fn_calculate_discount(
  p_type VARCHAR,
  p_value NUMERIC,
  p_order_amount NUMERIC
)
RETURNS NUMERIC
LANGUAGE plpgsql
IMMUTABLE
AS $$
BEGIN
  IF p_type = 'percent' THEN
    -- INTENTIONAL DEFECT FN-01: percentage is not capped at the order total.
    RETURN ROUND(p_order_amount * p_value / 100, 2);
  ELSIF p_type = 'fixed' THEN
    -- INTENTIONAL DEFECT FN-01 also affects oversized fixed discounts.
    RETURN p_value;
  END IF;
  RAISE EXCEPTION 'Unsupported discount type: %', p_type;
END;
$$;

CREATE OR REPLACE FUNCTION fn_prevent_negative_stock()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
  IF NEW.stock < 0 THEN
    RAISE EXCEPTION USING
      ERRCODE = 'P0001',
      MESSAGE = 'trg_prevent_negative_stock: stock cannot be negative';
  END IF;
  RETURN NEW;
END;
$$;

CREATE TRIGGER trg_prevent_negative_stock
BEFORE INSERT OR UPDATE OF stock ON products
FOR EACH ROW EXECUTE FUNCTION fn_prevent_negative_stock();

CREATE OR REPLACE PROCEDURE sp_process_checkout(
  p_user_id INT,
  p_items JSONB
)
LANGUAGE plpgsql
AS $$
DECLARE
  v_order_id INT;
  v_item RECORD;
  v_stock INT;
  v_price NUMERIC(10, 2);
  v_total NUMERIC(10, 2) := 0;
BEGIN
  SELECT COALESCE(SUM(p.price * i.quantity), 0)
    INTO v_total
    FROM jsonb_to_recordset(p_items) AS i(product_id INT, quantity INT)
    JOIN products p ON p.id = i.product_id;

  INSERT INTO orders(user_id, total_amount, final_amount, status)
  VALUES (p_user_id, v_total, v_total, 'pending')
  RETURNING id INTO v_order_id;

  FOR v_item IN
    SELECT * FROM jsonb_to_recordset(p_items)
      AS x(product_id INT, quantity INT)
  LOOP
    SELECT stock, price
      INTO v_stock, v_price
      FROM products
      WHERE id = v_item.product_id;

    IF NOT FOUND THEN
      RAISE EXCEPTION 'Product % does not exist', v_item.product_id;
    END IF;
    IF v_stock < v_item.quantity THEN
      RAISE EXCEPTION 'Product % is out of stock', v_item.product_id;
    END IF;

    UPDATE products
       SET stock = stock - v_item.quantity
     WHERE id = v_item.product_id;
    INSERT INTO order_items(order_id, product_id, quantity, unit_price)
    VALUES (v_order_id, v_item.product_id, v_item.quantity, v_price);

    -- INTENTIONAL DEFECT SP-01: committing each line breaks checkout atomicity.
    COMMIT;
  END LOOP;
END;
$$;

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'app_user') THEN
    CREATE ROLE app_user LOGIN PASSWORD 'app_user_lab_only';
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'mcp_reader') THEN
    CREATE ROLE mcp_reader LOGIN PASSWORD 'mcp_reader_lab_only';
  END IF;
END
$$;

GRANT CONNECT ON DATABASE eshop_minilab TO app_user, mcp_reader;
GRANT USAGE ON SCHEMA public TO app_user, mcp_reader;
GRANT SELECT ON products TO app_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO mcp_reader;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO mcp_reader;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT ON TABLES TO mcp_reader;
