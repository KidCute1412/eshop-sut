"""Create the HW06 Postman inputs from explicit, reviewable test definitions.

The generated files intentionally contain both the contract oracle and the
observed-SUT oracle.  Known defects are therefore reproducible without
misrepresenting a defect reproducer as a passing conformance check.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assignments" / "HW06" / "deliverables" / "postman"
STUDENT_ID = "23127404"


def row(tc_id, dimension, description, source, audit, contract, observed, **extra):
    return {
        "tc_id": tc_id,
        "dimension": dimension,
        "description": description,
        "source": source,
        "audit_label": audit,
        "audit_reason": "Oracle reconciled against README.md requirements and live SUT behavior.",
        "contract_status": contract,
        "expected_status": observed,
        **extra,
    }


def login_rows():
    rows = []
    valid = [
        ("admin@eshop.com", "Admin123!", "EP-VAL", "Valid administrator credentials"),
        ("test@eshop.com", "Test1234!", "EP-VAL", "Valid customer credentials"),
        ("admin@eshop.com", "Admin123!", "SCHEMA", "Success schema: token and user identity"),
        ("test@eshop.com", "Test1234!", "SEC-02", "JWT is returned for valid authentication"),
        ("test@eshop.com", "Test1234!", "NFR", "Login response time is below 2 seconds"),
    ]
    for index, (email, password, dimension, desc) in enumerate(valid, 1):
        rows.append(row(f"TC-LOGIN-{index:02}", dimension, desc, "AI Generated", "VALID", 200, 200,
                        email=email, password=password, expect_token=True, expect_error=False,
                        observed_password_leak=True))

    invalid_values = [
        ("ghost@example.test", "Test1234!", "Unregistered email"),
        ("", "Test1234!", "Empty email"),
        ("test@eshop.com", "", "Empty password"),
        ("testeshop.com", "Test1234!", "Email without at sign"),
        ("test@eshop", "Test1234!", "Email without top-level domain"),
        (" test@eshop.com ", "Test1234!", "Leading/trailing whitespace"),
        ("<script>alert(1)</script>@example.test", "Test1234!", "XSS payload in email"),
        ("' OR '1'='1' --", "irrelevant", "SQL injection authentication bypass payload"),
        ("admin@eshop.com' UNION SELECT 1 --", "irrelevant", "UNION SQL injection payload"),
        ("null@example.test", "WrongPassword!", "Wrong password for unknown user"),
        ("TEST@ESHOP.COM", "Test1234!", "Case-variant email"),
        ("test@eshop.com", "WrongPassword!", "Incorrect password"),
        ("missing@example.test", "", "Unknown user and empty password"),
        ("a@b.c", "x", "Short but unregistered address"),
        ("very.long.local.part." + "a" * 64 + "@example.test", "x", "Long email input"),
        ("user+tag@example.test", "x", "Plus-address input"),
        ("quoted\"@example.test", "x", "Special-character email input"),
        ("test@eshop.com", "wrong\npassword", "Newline in password"),
        ("test@eshop.com", " ", "Whitespace password"),
        ("unknown@eshop.com", "' OR 1=1 --", "SQL payload in password"),
        ("x@example.test", "x" * 512, "Long password input"),
        ("test@eshop.com", "Test1234! ", "Password trailing whitespace"),
        ("test@eshop.com\u0000", "Test1234!", "NUL-like email boundary"),
        ("-@example.test", "x", "Punctuation email input"),
        ("missing@example.test", "x", "Repeated unknown-user handling"),
        ("test@example.test", "x", "Representative invalid partition"),
        ("admin@example.test", "x", "Representative invalid partition 2"),
        ("customer@example.test", "x", "Representative invalid partition 3"),
        ("none@example.test", "x", "Representative invalid partition 4"),
        ("bad@example.test", "x", "Representative invalid partition 5"),
    ]
    for offset, (email, password, desc) in enumerate(invalid_values, 6):
        rows.append(row(f"TC-LOGIN-{offset:02}", "EP-INV" if offset < 20 else "SEC-05", desc,
                        "AI Generated", "VALID", 401, 401, email=email, password=password,
                        expect_token=False, expect_error=True, observed_password_leak=False))

    rows.extend([
        row("EXT-LOGIN-01", "BVA / BUG DETECTED", "One failed password increments the counter by +2 rather than +1.",
            "Human Extended", "VALID", 401, 401, email="test@eshop.com", password="WrongPassword!",
            fixture_attempts=0, expect_token=False, expect_error=True, bug_id="BUG-HW06-01",
            observed_password_leak=False, expected_post_attempts=2, contract_post_attempts=1),
        row("EXT-LOGIN-02", "BVA / BUG DETECTED", "With two prior failures, a further wrong password sets the lock but still returns 401.",
            "Human Extended", "VALID", 403, 401, email="test@eshop.com", password="WrongPassword!",
            fixture_attempts=2, expect_token=False, expect_error=True, bug_id="BUG-HW06-01",
            observed_password_leak=False, expected_post_attempts=4, contract_post_attempts=3),
        row("EXT-LOGIN-03", "STATE / BUG DETECTED", "An active lock lasts 180 seconds instead of the specified 30 seconds.",
            "Human Extended", "VALID", 403, 403, email="test@eshop.com", password="Test1234!",
            fixture_locked_seconds=180, expect_token=False, expect_error=True, bug_id="BUG-HW06-02",
            observed_password_leak=False),
        row("EXT-LOGIN-04", "SEC-01 / BUG DETECTED", "Successful login exposes the stored plaintext password in the user response.",
            "Human Extended", "VALID", 200, 200, email="test@eshop.com", password="Test1234!",
            expect_token=True, expect_error=False, bug_id="BUG-HW06-03", observed_password_leak=True),
        row("EXT-LOGIN-05", "STATE", "Successful login resets a pre-existing failure counter.",
            "Human Extended", "VALID", 200, 200, email="test@eshop.com", password="Test1234!",
            fixture_attempts=2, expect_token=True, expect_error=False, observed_password_leak=True),
    ])
    assert len(rows) == 40
    return rows


def checkout_rows():
    scenarios = [
        ("Standard cart checkout", "30000000", "123 Nguyen Hue, Q1", "valid", 200, None),
        ("Vietnamese address", "30000000", "45 Đinh Tiên Hoàng, Q1", "valid", 200, None),
        ("Multiline address", "30000000", "Tầng 5\n2 Hải Triều", "valid", 200, None),
        ("One-VND client total", "1", "123 Lê Lợi", "valid", 200, "BUG-HW06-04"),
        ("Zero client total", "0", "123 Lê Lợi", "valid", 200, "BUG-HW06-04"),
        ("Negative client total", "-1", "123 Lê Lợi", "valid", 200, "BUG-HW06-04"),
        ("High client total", "100000000", "123 Lê Lợi", "valid", 200, "BUG-HW06-04"),
        ("Empty address", "30000000", "", "valid", 200, None),
        ("Whitespace address", "30000000", "   ", "valid", 200, None),
        ("XSS address", "30000000", "<script>alert(1)</script>", "valid", 200, None),
        ("SQL-like address", "30000000", "' OR 1=1 --", "valid", 200, None),
        ("Long address", "30000000", "A" * 512, "valid", 200, None),
        ("Missing amount", "__OMIT__", "123 Lê Lợi", "valid", 200, None),
        ("Missing address", "30000000", "__OMIT__", "valid", 200, None),
        ("Empty JSON body", "__OMIT__", "__OMIT__", "valid", 200, None),
        ("Malformed bearer token", "30000000", "123 Lê Lợi", "malformed", 403, None),
        ("Missing bearer token", "30000000", "123 Lê Lợi", "none", 401, None),
        ("Customer bearer token", "30000000", "123 Lê Lợi", "valid", 200, None),
        ("Decimal amount", "1.5", "123 Lê Lợi", "valid", 200, "BUG-HW06-04"),
        ("String amount", "\"100\"", "123 Lê Lợi", "valid", 200, "BUG-HW06-04"),
        ("Null amount", "null", "123 Lê Lợi", "valid", 200, "BUG-HW06-04"),
        ("Unicode address", "30000000", "Đường số 1, TP.HCM", "valid", 200, None),
        ("Emoji address", "30000000", "🏠 123 Street", "valid", 200, None),
        ("Representative valid partition 1", "30000000", "A street", "valid", 200, None),
        ("Representative valid partition 2", "30000000", "B street", "valid", 200, None),
        ("Representative valid partition 3", "30000000", "C street", "valid", 200, None),
        ("Representative valid partition 4", "30000000", "D street", "valid", 200, None),
        ("Representative valid partition 5", "30000000", "E street", "valid", 200, None),
        ("Representative valid partition 6", "30000000", "F street", "valid", 200, None),
        ("Representative valid partition 7", "30000000", "G street", "valid", 200, None),
        ("Representative valid partition 8", "30000000", "H street", "valid", 200, None),
        ("Representative valid partition 9", "30000000", "I street", "valid", 200, None),
        ("Representative valid partition 10", "30000000", "J street", "valid", 200, None),
        ("Representative valid partition 11", "30000000", "K street", "valid", 200, None),
        ("Representative valid partition 12", "30000000", "L street", "valid", 200, None),
    ]
    rows=[]
    for i, (desc, amount, address, auth, observed, bug) in enumerate(scenarios, 1):
        rows.append(row(f"TC-CHK-{i:02}", "EP / BVA / SEC", desc, "AI Generated", "VALID", observed, observed,
                        total_amount=amount, shipping_address=address, auth_type=auth, expect_order_id=observed == 200,
                        bug_id=bug or "", expect_cart_retained=False))
    rows.extend([
        row("EXT-CHK-01", "STATE / BUG DETECTED", "Checkout succeeds even when no cart setup request is sent.", "Human Extended", "VALID", 400, 200,
            total_amount="1", shipping_address="123 Lê Lợi", auth_type="valid", skip_cart_setup=True, expect_order_id=True, bug_id="BUG-HW06-04", expect_cart_retained=False),
        row("EXT-CHK-02", "SEC-05 / BUG DETECTED", "Server persists a tampered one-VND amount instead of recalculating cart value.", "Human Extended", "VALID", 200, 200,
            total_amount="1", shipping_address="123 Lê Lợi", auth_type="valid", expect_order_id=True, bug_id="BUG-HW06-04", expect_cart_retained=False),
        row("EXT-CHK-03", "STATE / BUG DETECTED", "Cart still contains the added item after successful checkout.", "Human Extended", "VALID", 200, 200,
            total_amount="30000000", shipping_address="123 Lê Lợi", auth_type="valid", expect_order_id=True, bug_id="BUG-HW06-04", expect_cart_retained=True),
        row("EXT-CHK-04", "BVA", "Rapid-repeat representative checkout request.", "Human Extended", "VALID", 200, 200,
            total_amount="30000000", shipping_address="123 Lê Lợi", auth_type="valid", expect_order_id=True, expect_cart_retained=False),
        row("EXT-CHK-05", "SCHEMA", "Checkout success schema contains a numeric order identifier.", "Human Extended", "VALID", 200, 200,
            total_amount="30000000", shipping_address="123 Lê Lợi", auth_type="valid", expect_order_id=True, expect_cart_retained=False),
    ])
    assert len(rows) == 40
    return rows


def admin_rows():
    templates = [
        ("pending", "confirmed", "admin", 200, 200, "Valid pending to confirmed"),
        ("pending", "canceled", "admin", 200, 200, "Valid pending to canceled"),
        ("confirmed", "shipping", "admin", 200, 200, "Valid confirmed to shipping"),
        ("confirmed", "canceled", "admin", 200, 200, "Valid confirmed to canceled"),
        ("shipping", "delivered", "admin", 200, 200, "Valid shipping to delivered"),
        ("delivered", "pending", "admin", 400, 400, "Terminal delivered to pending rejected"),
        ("delivered", "canceled", "admin", 400, 400, "Terminal delivered to canceled rejected"),
        ("canceled", "confirmed", "admin", 400, 400, "Terminal canceled to confirmed rejected"),
        ("shipping", "pending", "admin", 400, 400, "Backward shipping to pending rejected"),
        ("pending", "shipping", "admin", 400, 400, "Skipped transition rejected"),
        ("pending", "delivered", "admin", 400, 400, "Skipped terminal transition rejected"),
        ("pending", "processing", "admin", 400, 400, "Invalid enum rejected"),
        ("pending", "", "admin", 400, 400, "Empty status rejected"),
        ("pending", "refunded", "admin", 400, 400, "Unknown enum rejected"),
        ("pending", "confirmed", "none", 401, 401, "Missing authentication rejected"),
        ("pending", "confirmed", "malformed", 403, 403, "Malformed token rejected"),
        ("pending", "confirmed", "user", 403, 200, "Customer token changes an admin order"),
        ("canceled", "delivered", "admin", 400, 200, "Canceled terminal order becomes delivered"),
        ("pending", "pending", "admin", 400, 400, "Self transition rejected"),
        ("confirmed", "confirmed", "admin", 400, 400, "Confirmed self transition rejected"),
        ("shipping", "shipping", "admin", 400, 400, "Shipping self transition rejected"),
        ("delivered", "shipping", "admin", 400, 400, "Delivered terminal transition rejected"),
        ("canceled", "shipping", "admin", 400, 400, "Canceled terminal transition rejected"),
        ("pending", "null", "admin", 400, 400, "String null enum rejected"),
        ("pending", "123", "admin", 400, 400, "Numeric-looking enum rejected"),
        ("pending", "CONFIRMED", "admin", 400, 400, "Case-variant enum rejected"),
        ("pending", "confirmed ", "admin", 400, 400, "Trailing-space enum rejected"),
        ("pending", " confirmed", "admin", 400, 400, "Leading-space enum rejected"),
        ("pending", "<script>alert(1)</script>", "admin", 400, 400, "XSS status rejected"),
        ("pending", "' OR 1=1 --", "admin", 400, 400, "SQL-like status rejected"),
        ("pending", "confirmed", "admin", 404, 404, "Nonexistent order identifier", "missing"),
        ("pending", "confirmed", "admin", 404, 404, "Negative order identifier", "-1"),
        ("pending", "confirmed", "admin", 404, 404, "String order identifier", "abc"),
        ("pending", "confirmed", "admin", 404, 404, "SQL-like path identifier", "1 OR 1=1"),
        ("pending", "confirmed", "admin", 404, 404, "Large integer identifier", "9223372036854775807"),
    ]
    rows=[]
    for i, item in enumerate(templates, 1):
        initial, target, auth, contract, observed, desc, *order_override = item
        bug = "BUG-HW06-05" if auth == "user" else "BUG-HW06-06" if initial == "canceled" and target == "delivered" else ""
        rows.append(row(f"TC-ADM-{i:02}", "STATE / SEC", desc, "AI Generated", "VALID", contract, observed,
                        order_id=order_override[0] if order_override else i, initial_status=initial, target_status=target,
                        auth_role=auth, expect_error=observed >= 400, bug_id=bug))
    rows.extend([
        row("EXT-ADM-01", "SEC-03 / BUG DETECTED", "Repeat RBAC privilege-escalation reproduction.", "Human Extended", "VALID", 403, 200,
            order_id=36, initial_status="pending", target_status="confirmed", auth_role="user", expect_error=False, bug_id="BUG-HW06-05"),
        row("EXT-ADM-02", "STATE / BUG DETECTED", "Repeat terminal canceled-to-delivered reproduction.", "Human Extended", "VALID", 400, 200,
            order_id=37, initial_status="canceled", target_status="delivered", auth_role="admin", expect_error=False, bug_id="BUG-HW06-06"),
        row("EXT-ADM-03", "STATE", "Persisted valid state transition response.", "Human Extended", "VALID", 200, 200,
            order_id=38, initial_status="pending", target_status="confirmed", auth_role="admin", expect_error=False, bug_id=""),
        row("EXT-ADM-04", "BVA", "Order identifier zero is not found.", "Human Extended", "VALID", 404, 404,
            order_id="0", initial_status="pending", target_status="confirmed", auth_role="admin", expect_error=True, bug_id=""),
        row("EXT-ADM-05", "SCHEMA", "Success response includes its documented message.", "Human Extended", "VALID", 200, 200,
            order_id=40, initial_status="confirmed", target_status="shipping", auth_role="admin", expect_error=False, bug_id=""),
    ])
    assert len(rows) == 40
    return rows


def event(listen, lines):
    return {"listen": listen, "script": {"type": "text/javascript", "exec": lines}}


def request(name, method, path, body, events):
    return {"name": name, "event": events, "request": {"method": method, "header": [{"key": "Content-Type", "value": "application/json"}], "body": {"mode": "raw", "raw": body}, "url": {"raw": "{{baseUrl}}" + path, "host": ["{{baseUrl}}"], "path": path.strip("/").split("/")}}, "response": []}


HEADER = [
    "const tc = pm.iterationData.get('tc_id');",
    "pm.request.headers.upsert({key: 'X-Student-Id', value: pm.environment.get('studentId') || '23127404'});",
    "console.log('[HW06 EVIDENCE] ' + tc + ' X-Student-Id=' + pm.request.headers.get('X-Student-Id'));",
]


def collections():
    info = lambda name, description: {"_postman_id": name + "-23127404", "name": name, "description": description, "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"}
    a = {"info": info("HW06 Pool A — Login", "One primary login assertion per isolated data row."), "item": [request("POST /api/login", "POST", "/api/login", "{{loginPayload}}", [event("prerequest", HEADER + [
        "const p = {email: pm.iterationData.get('email'), password: pm.iterationData.get('password')}; pm.variables.set('loginPayload', JSON.stringify(p));"
    ]), event("test", [
        "const tc=pm.iterationData.get('tc_id'), expected=Number(pm.iterationData.get('expected_status')), body=pm.response.json();",
        "pm.test('['+tc+'] observed HTTP status',()=>pm.response.to.have.status(expected));",
        "pm.test('['+tc+'] JSON content type',()=>pm.expect(pm.response.headers.get('Content-Type')).to.include('application/json'));",
        "pm.test('['+tc+'] response time',()=>pm.expect(pm.response.responseTime).to.be.below(2000));",
        "if (pm.iterationData.get('expect_token') === true || pm.iterationData.get('expect_token') === 'true') pm.test('['+tc+'] token/user schema',()=>{pm.expect(body.token).to.be.a('string').and.not.empty; pm.expect(body.user).to.be.an('object');});",
        "if (pm.iterationData.get('expect_error') === true || pm.iterationData.get('expect_error') === 'true') pm.test('['+tc+'] error schema',()=>pm.expect(body.error).to.be.a('string').and.not.empty);",
        "if (pm.iterationData.get('observed_password_leak') === true || pm.iterationData.get('observed_password_leak') === 'true') pm.test('['+tc+'] observed known defect / secure field behavior',()=>pm.expect(body.user).to.have.property('password'));",
    ])])]} 
    b = {"info": info("HW06 Pool B — Checkout", "Checkout scenarios with real login/cart/checkout/get-cart workflow."), "item": [
        request("01 Login fixture", "POST", "/api/login", '{"email":"test@eshop.com","password":"Test1234!"}', [event("prerequest", HEADER), event("test", ["const b=pm.response.json(); pm.environment.set('fixtureToken',b.token); pm.test('fixture login',()=>pm.response.to.have.status(200));"])]),
        request("02 Add cart fixture", "POST", "/api/cart", '{"id":1,"name":"iPhone 15 Pro Max","price":30000000,"quantity":1}', [event("prerequest", HEADER + ["pm.request.headers.upsert({key:'Authorization',value:'Bearer '+pm.environment.get('fixtureToken')});"]), event("test", ["pm.test('cart fixture',()=>pm.response.to.have.status(200));"])]),
        request("03 POST /api/checkout", "POST", "/api/checkout", "{{checkoutPayload}}", [event("prerequest", HEADER + [
            "const a=pm.iterationData.get('auth_type'); if(a==='valid') pm.request.headers.upsert({key:'Authorization',value:'Bearer '+pm.environment.get('fixtureToken')}); else if(a==='malformed') pm.request.headers.upsert({key:'Authorization',value:'Bearer malformed'}); else pm.request.headers.remove('Authorization');",
            "const amount=pm.iterationData.get('total_amount'), address=pm.iterationData.get('shipping_address'); let p={}; if(amount!=='__OMIT__') p.total_amount=JSON.parse(amount); if(address!=='__OMIT__') p.shipping_address=address; pm.variables.set('checkoutPayload',JSON.stringify(p));"
        ]), event("test", [
            "const tc=pm.iterationData.get('tc_id'), expected=Number(pm.iterationData.get('expected_status')), body=pm.response.json();",
            "pm.test('['+tc+'] observed HTTP status',()=>pm.response.to.have.status(expected));",
            "pm.test('['+tc+'] JSON content type',()=>pm.expect(pm.response.headers.get('Content-Type')).to.include('application/json'));",
            "pm.test('['+tc+'] response time',()=>pm.expect(pm.response.responseTime).to.be.below(2000));",
            "if(expected===200) pm.test('['+tc+'] checkout schema',()=>{pm.expect(body.message).to.eql('Checkout successful'); pm.expect(body.orderId).to.be.a('number');}); else pm.test('['+tc+'] error schema',()=>pm.expect(body.error).to.be.a('string'));"
        ])]),
        request("04 GET /api/cart persistence check", "GET", "/api/cart", "", [event("prerequest", HEADER + ["pm.request.headers.upsert({key:'Authorization',value:'Bearer '+pm.environment.get('fixtureToken')});"]), event("test", [
            "const tc=pm.iterationData.get('tc_id'), retain=pm.iterationData.get('expect_cart_retained')===true || pm.iterationData.get('expect_cart_retained')==='true', body=pm.response.json();",
            "pm.test('['+tc+'] cart query succeeds',()=>pm.response.to.have.status(200)); if(retain) pm.test('['+tc+'] observed cart-retention defect',()=>pm.expect(body.length).to.be.above(0));"
        ])])
    ]}
    c = {"info": info("HW06 Pool C — Admin order status", "State-machine and RBAC scenarios against isolated seeded orders."), "item": [
        request("01 Login admin", "POST", "/api/login", '{"email":"admin@eshop.com","password":"Admin123!"}', [event("prerequest", HEADER), event("test", ["const b=pm.response.json();pm.environment.set('adminToken',b.token);pm.test('admin fixture',()=>pm.response.to.have.status(200));"])]),
        request("02 Login user", "POST", "/api/login", '{"email":"test@eshop.com","password":"Test1234!"}', [event("prerequest", HEADER), event("test", ["const b=pm.response.json();pm.environment.set('userToken',b.token);pm.test('user fixture',()=>pm.response.to.have.status(200));"])]),
        request("03 PUT /api/admin/orders/:id/status", "PUT", "/api/admin/orders/{{orderId}}/status", "{{statusPayload}}", [event("prerequest", HEADER + [
            "const a=pm.iterationData.get('auth_role'); if(a==='admin') pm.request.headers.upsert({key:'Authorization',value:'Bearer '+pm.environment.get('adminToken')}); else if(a==='user') pm.request.headers.upsert({key:'Authorization',value:'Bearer '+pm.environment.get('userToken')}); else if(a==='malformed') pm.request.headers.upsert({key:'Authorization',value:'Bearer malformed'}); else pm.request.headers.remove('Authorization'); pm.variables.set('orderId',pm.iterationData.get('order_id')); pm.variables.set('statusPayload',JSON.stringify({status:pm.iterationData.get('target_status')}));"
        ]), event("test", [
            "const tc=pm.iterationData.get('tc_id'), expected=Number(pm.iterationData.get('expected_status')), body=pm.response.json();",
            "pm.test('['+tc+'] observed HTTP status',()=>pm.response.to.have.status(expected)); pm.test('['+tc+'] JSON content type',()=>pm.expect(pm.response.headers.get('Content-Type')).to.include('application/json')); pm.test('['+tc+'] response time',()=>pm.expect(pm.response.responseTime).to.be.below(2000));",
            "if(expected===200) pm.test('['+tc+'] success schema',()=>pm.expect(body.message).to.eql('Order status updated')); else pm.test('['+tc+'] error schema',()=>pm.expect(body.error).to.be.a('string'));"
        ])])
    ]}
    return a, b, c


def main():
    (OUT / "data").mkdir(parents=True, exist_ok=True)
    (OUT / "collections").mkdir(parents=True, exist_ok=True)
    data = [("login_data.json", login_rows()), ("checkout_data.json", checkout_rows()), ("admin_orders_data.json", admin_rows())]
    for name, rows in data:
        (OUT / "data" / name).write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for name, collection in zip(("pool_a_login.postman_collection.json", "pool_b_checkout.postman_collection.json", "pool_c_admin_orders.postman_collection.json"), collections()):
        (OUT / "collections" / name).write_text(json.dumps(collection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    environment = {"id": "hw06-local-23127404", "name": "HW06 Local EShop", "values": [{"key": "baseUrl", "value": "http://127.0.0.1:3000", "type": "default", "enabled": True}, {"key": "studentId", "value": STUDENT_ID, "type": "default", "enabled": True}]}
    (OUT / "environments" / "local.postman_environment.json").write_text(json.dumps(environment, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
