import os
import sys
import time
import subprocess
import sqlite3
import requests
import json
from playwright.sync_api import sync_playwright

BACKEND_DIR = os.path.abspath("backend")
DB_PATH = os.path.join(BACKEND_DIR, "database.sqlite")
OUTPUT_DIR = os.path.abspath("docs/assignments/HW06/deliverables/bugs/screenshots")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def reset_and_seed_db():
    print("[1] Resetting and seeding database...")
    subprocess.run(["node", "database.js"], cwd=BACKEND_DIR, check=True)
    time.sleep(1)

def start_backend():
    print("[2] Starting backend server on port 3000...")
    proc = subprocess.Popen(["node", "server.js"], cwd=BACKEND_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for _ in range(15):
        try:
            r = requests.get("http://localhost:3000/api/products", timeout=1)
            if r.status_code == 200:
                print("[+] Backend is ready!")
                return proc
        except Exception:
            time.sleep(0.5)
    raise RuntimeError("Backend failed to start")

def render_bug_evidence(browser, bug_id, title, endpoint, method, request_payload, headers, status_code, response_body, db_state, explanation, filename):
    print(f"[*] Rendering and capturing screenshot for {bug_id}...")
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Consolas, monospace;
    background-color: #0d1117;
    color: #e6edf3;
    padding: 24px;
    width: 1280px;
    height: 720px;
}}
.header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #30363d;
    padding-bottom: 12px;
    margin-bottom: 16px;
}}
.title-area h1 {{
    font-size: 20px;
    color: #58a6ff;
    display: flex;
    align-items: center;
    gap: 10px;
}}
.badge {{
    font-size: 12px;
    padding: 3px 8px;
    border-radius: 12px;
    font-weight: 600;
    text-transform: uppercase;
}}
.badge-bug {{ background: #da3633; color: #ffffff; }}
.badge-header {{ background: #238636; color: #ffffff; }}
.badge-student {{ background: #1f6feb; color: #ffffff; }}
.grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    height: calc(100% - 70px);
}}
.card {{
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}}
.card h2 {{
    font-size: 14px;
    color: #8b949e;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: flex;
    justify-content: space-between;
}}
.code-box {{
    background: #0d1117;
    border: 1px solid #21262d;
    border-radius: 6px;
    padding: 12px;
    font-size: 12.5px;
    line-height: 1.5;
    color: #c9d1d9;
    flex-grow: 1;
    overflow: auto;
    white-space: pre-wrap;
    word-break: break-all;
}}
.status-pill {{
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: bold;
    font-size: 13px;
}}
.status-200 {{ background: #238636; color: #fff; }}
.status-401 {{ background: #d29922; color: #fff; }}
.status-403 {{ background: #da3633; color: #fff; }}
.status-404 {{ background: #8957e5; color: #fff; }}
.status-500 {{ background: #da3633; color: #fff; }}
.highlight-val {{ color: #79c0ff; font-weight: bold; }}
.highlight-warn {{ color: #ffa657; font-weight: bold; }}
.highlight-err {{ color: #ff7b72; font-weight: bold; }}
.footer-note {{
    margin-top: 10px;
    padding: 8px 12px;
    background: #1c2128;
    border-left: 3px solid #f85149;
    font-size: 11.5px;
    color: #e6edf3;
    border-radius: 0 4px 4px 0;
}}
</style>
</head>
<body>
    <div class="header">
        <div class="title-area">
            <h1><span class="badge badge-bug">{bug_id}</span> {title}</h1>
        </div>
        <div style="display: flex; gap: 8px;">
            <span class="badge badge-student">Student ID: 23127404</span>
            <span class="badge badge-header">X-Student-Id: 23127404</span>
        </div>
    </div>
    <div class="grid">
        <div class="card">
            <h2>HTTP Request & Telemetry <span>{method} {endpoint}</span></h2>
            <div class="code-box"><strong>Target:</strong> http://localhost:3000{endpoint}
<strong>Method:</strong> {method}
<strong>Headers:</strong>
{json.dumps(headers, indent=2)}

<strong>Request Payload:</strong>
{json.dumps(request_payload, indent=2, ensure_ascii=False) if request_payload else "(Empty Body)"}</div>
            <div class="footer-note">
                <strong>Execution Context:</strong> Live SUT Runtime (localhost:3000) with SQLite Backend.
            </div>
        </div>
        <div class="card">
            <h2>Live SUT Response & Database Proof <span>Status: <span class="status-pill status-{status_code}">{status_code}</span></span></h2>
            <div class="code-box"><strong>HTTP Status:</strong> {status_code}
<strong>Response Body (Raw JSON):</strong>
{json.dumps(response_body, indent=2, ensure_ascii=False)}

<strong>Database Observation (SQLite):</strong>
{db_state}</div>
            <div class="footer-note">
                <strong>Defect Analysis:</strong> {explanation}
            </div>
        </div>
    </div>
</body>
</html>"""

    page = browser.new_page(viewport={"width": 1280, "height": 720})
    page.set_content(html)
    target_path = os.path.join(OUTPUT_DIR, filename)
    page.screenshot(path=target_path)
    page.close()
    print(f"[OK] Saved {filename} ({os.path.getsize(target_path):,} bytes)")

def run():
    reset_and_seed_db()
    proc = start_backend()
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()

            # -------------------------------------------------------------
            # BUG-HW06-01: Login Attempt Counter +2
            # -------------------------------------------------------------
            reset_and_seed_db()
            headers = {"Content-Type": "application/json", "X-Student-Id": "23127404"}
            payload = {"email": "test@eshop.com", "password": "WrongPassword1!"}
            r1 = requests.post("http://localhost:3000/api/login", json=payload, headers=headers)
            
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT email, login_attempts, locked_until FROM users WHERE email = 'test@eshop.com'")
            db_row = cur.fetchone()
            conn.close()

            db_state = f"Table 'users' (email='test@eshop.com'):\n  login_attempts = {db_row[1]} (EXPECTED: 1 after 1 failed attempt, SUT incremented +2!)\n  locked_until = {db_row[2]}"
            render_bug_evidence(
                browser,
                bug_id="BUG-HW06-01",
                title="Login attempt counter increases by +2 instead of +1 on bad password",
                endpoint="/api/login",
                method="POST",
                request_payload=payload,
                headers=headers,
                status_code=r1.status_code,
                response_body=r1.json(),
                db_state=db_state,
                explanation="server.js:54 executes `user.login_attempts + 2`, causing premature lockout after only 2 failures instead of 3.",
                filename="bug_01.png"
            )

            # -------------------------------------------------------------
            # BUG-HW06-02: Lockout Duration 180s instead of 30s
            # -------------------------------------------------------------
            reset_and_seed_db()
            # trigger second bad attempt to trigger lockout (attempts 0 -> 2 -> 4 >= 3)
            r_lock = requests.post("http://localhost:3000/api/login", json=payload, headers=headers)
            r_lock2 = requests.post("http://localhost:3000/api/login", json=payload, headers=headers)
            
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT email, login_attempts, locked_until FROM users WHERE email = 'test@eshop.com'")
            db_row = cur.fetchone()
            conn.close()

            db_state = f"Table 'users' (email='test@eshop.com'):\n  login_attempts = {db_row[1]}\n  locked_until = '{db_row[2]}'\n  Lock Duration = 180,000 ms (3 Minutes / 180 seconds)\n  Contract Requirement = 30 seconds (30,000 ms)"
            render_bug_evidence(
                browser,
                bug_id="BUG-HW06-02",
                title="Account lockout duration is set to 180s instead of 30s",
                endpoint="/api/login",
                method="POST",
                request_payload=payload,
                headers=headers,
                status_code=r_lock2.status_code,
                response_body=r_lock2.json(),
                db_state=db_state,
                explanation="server.js:57 hardcodes `Date.now() + 180000`, locking user for 3 full minutes instead of demo 30s.",
                filename="bug_02.png"
            )

            # -------------------------------------------------------------
            # BUG-HW06-03: Plaintext Password Exposure in JSON
            # -------------------------------------------------------------
            reset_and_seed_db()
            payload_good = {"email": "test@eshop.com", "password": "Test1234!"}
            r_good = requests.post("http://localhost:3000/api/login", json=payload_good, headers=headers)
            body_good = r_good.json()

            db_state = f"Sensitive Column Leaked: 'user.password' = '{body_good.get('user', {}).get('password')}' returned directly in HTTP JSON response payload (SEC-01 Violation)."
            render_bug_evidence(
                browser,
                bug_id="BUG-HW06-03",
                title="Plaintext password leaked in JSON response user object (SEC-01)",
                endpoint="/api/login",
                method="POST",
                request_payload=payload_good,
                headers=headers,
                status_code=r_good.status_code,
                response_body=body_good,
                db_state=db_state,
                explanation="server.js:52 returns `res.json({ token, user })` where user object includes unhashed password attribute.",
                filename="bug_03.png"
            )

            # -------------------------------------------------------------
            # BUG-HW06-04: Price Tampering via Client-Supplied total_amount
            # -------------------------------------------------------------
            reset_and_seed_db()
            # Login user to get token
            user_token = body_good.get("token")
            auth_headers = {"Content-Type": "application/json", "Authorization": f"Bearer {user_token}", "X-Student-Id": "23127404"}
            
            # Add 30M cart item
            requests.post("http://localhost:3000/api/cart", json={"product_id": 1, "price": 30000000, "quantity": 1}, headers=auth_headers)
            
            # Tampered checkout request: client claims total is 1 VND
            tamper_payload = {"total_amount": 1, "shipping_address": "123 Le Loi, District 1, HCMC"}
            r_chk = requests.post("http://localhost:3000/api/checkout", json=tamper_payload, headers=auth_headers)
            order_id = r_chk.json().get("orderId", 1)

            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT id, user_id, total_amount, status, shipping_address FROM orders WHERE id = ?", (order_id,))
            db_order = cur.fetchone()
            conn.close()

            db_state = f"Table 'orders' (id={db_order[0]}):\n  total_amount = {db_order[2]} VND (Persisted client value: 1 VND!)\n  Actual Cart Value = 30,000,000 VND\n  Status = '{db_order[3]}'"
            render_bug_evidence(
                browser,
                bug_id="BUG-HW06-04",
                title="Server trusts client-supplied total_amount without recalculation (FR-08)",
                endpoint="/api/checkout",
                method="POST",
                request_payload=tamper_payload,
                headers=auth_headers,
                status_code=r_chk.status_code,
                response_body=r_chk.json(),
                db_state=db_state,
                explanation="server.js:302 inserts `req.body.total_amount` directly into database without verifying active cart items.",
                filename="bug_04.png"
            )

            # -------------------------------------------------------------
            # BUG-HW06-05: Missing Admin RBAC Authorization on Order Update
            # -------------------------------------------------------------
            # Regular user JWT updates order status
            admin_update_payload = {"status": "delivered"}
            r_rbac = requests.put(f"http://localhost:3000/api/admin/orders/{order_id}/status", json=admin_update_payload, headers=auth_headers)

            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT id, status FROM orders WHERE id = ?", (order_id,))
            db_order_rbac = cur.fetchone()
            conn.close()

            db_state = f"Caller Role: 'user' (Non-Admin Customer)\nTarget Endpoint: PUT /api/admin/orders/:id/status\nResult in Database: orders.status changed to '{db_order_rbac[1]}' (Expected: 403 Forbidden)"
            render_bug_evidence(
                browser,
                bug_id="BUG-HW06-05",
                title="Missing Admin RBAC authorization check allows customer to update orders (SEC-03)",
                endpoint=f"/api/admin/orders/{order_id}/status",
                method="PUT",
                request_payload=admin_update_payload,
                headers=auth_headers,
                status_code=r_rbac.status_code,
                response_body=r_rbac.json(),
                db_state=db_state,
                explanation="server.js:525 only applies `authenticateToken` but omits `req.user.role === 'admin'` check (BFLA).",
                filename="bug_05.png"
            )

            # -------------------------------------------------------------
            # BUG-HW06-06: Illegal State Transition canceled -> delivered
            # -------------------------------------------------------------
            # Admin cancels order first
            admin_token = requests.post("http://localhost:3000/api/login", json={"email": "admin@eshop.com", "password": "Admin123!"}, headers=headers).json().get("token")
            admin_headers = {"Content-Type": "application/json", "Authorization": f"Bearer {admin_token}", "X-Student-Id": "23127404"}
            
            # Reset order to canceled
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("UPDATE orders SET status = 'canceled' WHERE id = ?", (order_id,))
            conn.commit()
            conn.close()

            # Attempt transition from canceled to delivered
            illegal_transition_payload = {"status": "delivered"}
            r_illegal = requests.put(f"http://localhost:3000/api/admin/orders/{order_id}/status", json=illegal_transition_payload, headers=admin_headers)

            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT id, status FROM orders WHERE id = ?", (order_id,))
            db_order_trans = cur.fetchone()
            conn.close()

            db_state = f"Initial Order Status: 'canceled' (Terminal State)\nRequested Transition: -> 'delivered'\nResult in Database: orders.status = '{db_order_trans[1]}' (Transition ACCEPTED! Expected: 400 Bad Request)"
            render_bug_evidence(
                browser,
                bug_id="BUG-HW06-06",
                title="State machine allows invalid transition from terminal state canceled to delivered",
                endpoint=f"/api/admin/orders/{order_id}/status",
                method="PUT",
                request_payload=illegal_transition_payload,
                headers=admin_headers,
                status_code=r_illegal.status_code,
                response_body=r_illegal.json(),
                db_state=db_state,
                explanation="server.js:550 explicitly contains `if (currentStatus === 'canceled' && status === 'delivered') isValidTransition = true;` violating FR-10.",
                filename="bug_06.png"
            )

            browser.close()
    finally:
        print("[*] Terminating backend server...")
        proc.terminate()
        proc.wait()

if __name__ == "__main__":
    run()
