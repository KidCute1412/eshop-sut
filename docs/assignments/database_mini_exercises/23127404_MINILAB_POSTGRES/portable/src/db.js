const { Pool } = require("pg");

const adminPool = new Pool({
  connectionString:
    process.env.DATABASE_URL ??
    "postgresql://lab_admin:lab_admin_only@localhost:5432/eshop_minilab",
});

const appUserPool = new Pool({
  connectionString:
    process.env.APP_USER_DATABASE_URL ??
    "postgresql://app_user:app_user_lab_only@localhost:5432/eshop_minilab",
});

module.exports = { adminPool, appUserPool };
