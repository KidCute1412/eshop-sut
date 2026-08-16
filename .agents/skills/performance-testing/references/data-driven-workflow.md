# Data-Driven Workflow

Use CSV data. At minimum:

```csv
email,password,search,product_id,product_name,price,quantity,shipping_address
```

Example values from the seeded database:

```csv
test@eshop.com,Test1234!,iPhone,1,iPhone 15 Pro Max,30000000,1,"123 Le Loi, District 1, HCMC"
test@eshop.com,Test1234!,Samsung,2,Samsung Galaxy S24 Ultra,28000000,1,"456 Nguyen Hue, District 1, HCMC"
test@eshop.com,Test1234!,MacBook,3,MacBook Pro M3,45000000,1,"789 Cach Mang Thang 8, District 3, HCMC"
```

Guidelines:

- Keep data outside the `.jmx` or k6 script.
- Use valid credentials for normal performance runs.
- Avoid destructive search strings.
- Use multiple products to avoid every virtual user hammering one detail endpoint only.
- Document whether checkout/cart state was reset before each scenario.

