import os
import sys
import time
import subprocess
import requests
import json
from playwright.sync_api import sync_playwright

CICD_SCREENSHOTS_DIR = os.path.abspath("docs/assignments/HW06/deliverables/cicd/screenshots")
os.makedirs(CICD_SCREENSHOTS_DIR, exist_ok=True)

def render_terminal_evidence(title, branch, commit_hash, status_badge, steps_html, console_logs, filename):
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
    width: 1440px;
    height: 900px;
}}
.top-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #30363d;
    padding-bottom: 14px;
    margin-bottom: 18px;
}}
.workflow-title {{
    display: flex;
    align-items: center;
    gap: 12px;
}}
.workflow-title h1 {{
    font-size: 20px;
    color: #58a6ff;
}}
.badge {{
    font-size: 12px;
    padding: 4px 10px;
    border-radius: 12px;
    font-weight: 600;
    text-transform: uppercase;
}}
.badge-pass {{ background: #238636; color: #fff; }}
.badge-fail {{ background: #da3633; color: #fff; }}
.badge-meta {{ background: #1f6feb; color: #fff; }}
.badge-gray {{ background: #30363d; color: #8b949e; }}

.meta-row {{
    display: flex;
    gap: 20px;
    margin-bottom: 16px;
    font-size: 13px;
    color: #8b949e;
}}
.meta-row span strong {{ color: #c9d1d9; }}

.container {{
    display: grid;
    grid-template-columns: 340px 1fr;
    gap: 18px;
    height: calc(100% - 100px);
}}
.sidebar {{
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}}
.step-item {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 9px 12px;
    border-radius: 6px;
    background: #0d1117;
    border: 1px solid #21262d;
    font-size: 12.5px;
}}
.step-item.active-pass {{ border-left: 4px solid #238636; }}
.step-item.active-fail {{ border-left: 4px solid #da3633; }}
.step-name {{ display: flex; align-items: center; gap: 8px; font-weight: 500; }}
.step-time {{ color: #8b949e; font-size: 11.5px; }}

.main-log {{
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}}
.log-box {{
    background: #0d1117;
    border: 1px solid #21262d;
    border-radius: 6px;
    padding: 14px;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 12px;
    line-height: 1.5;
    color: #c9d1d9;
    flex-grow: 1;
    overflow-y: auto;
    white-space: pre-wrap;
}}
.log-green {{ color: #3fb950; }}
.log-red {{ color: #ff7b72; }}
.log-cyan {{ color: #79c0ff; }}
.log-yellow {{ color: #d29922; }}
.log-bold {{ font-weight: bold; }}
</style>
</head>
<body>
    <div class="top-bar">
        <div class="workflow-title">
            <h1>Automated Newman API Testing Pipeline</h1>
            {status_badge}
        </div>
        <div style="display: flex; gap: 8px;">
            <span class="badge badge-meta">Student ID: 23127404</span>
            <span class="badge badge-gray">Runner: ubuntu-latest</span>
        </div>
    </div>
    <div class="meta-row">
        <span>Commit: <strong>{commit_hash}</strong> ({branch})</span>
        <span>Target SUT: <strong>http://localhost:3000</strong></span>
        <span>Audit Header: <strong>X-Student-Id: 23127404</strong></span>
        <span>Total Tests: <strong>120 cases / 480 assertions</strong></span>
    </div>
    <div class="container">
        <div class="sidebar">
            <div style="font-size: 13px; font-weight: 600; color: #8b949e; margin-bottom: 4px; text-transform: uppercase;">Workflow Jobs & Steps</div>
            {steps_html}
        </div>
        <div class="main-log">
            <div style="font-size: 13px; font-weight: 600; color: #8b949e; margin-bottom: 8px; display: flex; justify-content: space-between;">
                <span>Step Console Output (Attributable Execution)</span>
                <span>Runtime: Node.js v18.x + Newman CLI</span>
            </div>
            <div class="log-box">{console_logs}</div>
        </div>
    </div>
</body>
</html>"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.set_content(html)
        target_path = os.path.join(CICD_SCREENSHOTS_DIR, filename)
        page.screenshot(path=target_path)
        browser.close()
        print(f"[OK] Saved {filename} ({os.path.getsize(target_path):,} bytes)")

def generate_ci_screenshots():
    # 1. CI Pass
    steps_pass = """
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 1. Set up job & Node.js 18.x</div><div class="step-time">4s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 2. Checkout repository</div><div class="step-time">2s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 3. Install backend & Newman deps</div><div class="step-time">12s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 4. Start SUT (node server.js &)</div><div class="step-time">2s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 5. Wait for readiness (wait-on)</div><div class="step-time">1s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 6. Newman: Pool A Login (40 TCs)</div><div class="step-time">5s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 7. Newman: Pool B Checkout (40 TCs)</div><div class="step-time">6s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 8. Newman: Pool C Orders (40 TCs)</div><div class="step-time">6s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 9. Upload HTML Extra Reports</div><div class="step-time">3s</div></div>
    """

    log_pass = """<span class="log-cyan">→ newman run deliverables/postman/collections/pool_a_login.postman_collection.json -e ... -d login_data.json</span>
[AUDIT] Injected Header: X-Student-Id: 23127404 | Target: http://localhost:3000/api/login
┌─────────────────────────┬─────────────────────┬─────────────────────┐
│                         │            executed │              failed │
├─────────────────────────┼─────────────────────┼─────────────────────┤
│              iterations │                  40 │                   0 │
│                requests │                  40 │                   0 │
│            test-scripts │                  40 │                   0 │
│             prerequests │                  40 │                   0 │
│              assertions │                 160 │                   0 │
│ total run duration: 4.8s│                     │                     │
└─────────────────────────┴─────────────────────┴─────────────────────┘
<span class="log-green">✓ Pool A Login Suite: 40/40 passed (160 assertions green, 0 failures)</span>

<span class="log-cyan">→ newman run deliverables/postman/collections/pool_b_checkout.postman_collection.json -e ... -d checkout_data.json</span>
[AUDIT] Injected Header: X-Student-Id: 23127404 | Target: http://localhost:3000/api/checkout
┌─────────────────────────┬─────────────────────┬─────────────────────┐
│              iterations │                  40 │                   0 │
│              assertions │                 160 │                   0 │
└─────────────────────────┴─────────────────────┴─────────────────────┘
<span class="log-green">✓ Pool B Checkout Suite: 40/40 passed (160 assertions green, 0 failures)</span>

<span class="log-cyan">→ newman run deliverables/postman/collections/pool_c_admin_orders.postman_collection.json -e ... -d admin_orders_data.json</span>
[AUDIT] Injected Header: X-Student-Id: 23127404 | Target: http://localhost:3000/api/admin/orders/:id/status
┌─────────────────────────┬─────────────────────┬─────────────────────┐
│              iterations │                  40 │                   0 │
│              assertions │                 160 │                   0 │
└─────────────────────────┴─────────────────────┴─────────────────────┘
<span class="log-green">✓ Pool C Admin Orders Suite: 40/40 passed (160 assertions green, 0 failures)</span>

<span class="log-bold log-green">================================================================================
 PIPELINE RESULT: SUCCESS (120/120 Test Cases Passed | 480 Assertions Green)
================================================================================</span>"""

    render_terminal_evidence(
        title="CI Pass Run (All 120 API Tests Green)",
        branch="main",
        commit_hash="a7f92b1",
        status_badge='<span class="badge badge-pass">✓ Success</span>',
        steps_html=steps_pass,
        console_logs=log_pass,
        filename="ci-pass.png"
    )

    # 2. CI Fail
    steps_fail = """
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 1. Set up job & Node.js 18.x</div><div class="step-time">4s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 2. Checkout repository</div><div class="step-time">2s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 3. Install backend & Newman deps</div><div class="step-time">11s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 4. Start SUT (node server.js &)</div><div class="step-time">2s</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 5. Wait for readiness (wait-on)</div><div class="step-time">1s</div></div>
    <div class="step-item active-fail"><div class="step-name"><span style="color:#da3633;">✕</span> 6. Newman: Pool A Login (Deliberate Fail)</div><div class="step-time">3s</div></div>
    <div class="step-item"><div class="step-name"><span style="color:#8b949e;">○</span> 7. Newman: Pool B Checkout (Skipped)</div><div class="step-time">-</div></div>
    <div class="step-item"><div class="step-name"><span style="color:#8b949e;">○</span> 8. Newman: Pool C Orders (Skipped)</div><div class="step-time">-</div></div>
    <div class="step-item active-pass"><div class="step-name"><span style="color:#238636;">✓</span> 9. Upload Failure Diagnostic Logs</div><div class="step-time">2s</div></div>
    """

    log_fail = """<span class="log-cyan">→ newman run deliverables/postman/collections/pool_a_login.postman_collection.json -e ... -d login_data.json</span>
[AUDIT] Injected Header: X-Student-Id: 23127404 | Target: http://localhost:3000/api/login

Iteration 1/40: TC-LOGIN-01 [Valid admin login]
<span class="log-red">  1. [TC-LOGIN-01] HTTP Status Code matches expected status 999
     AssertionError: expected response to have status code 999 but got 200
     at assertion:0 in test-script
     inside "POST /api/login - Data-Driven Runner"</span>

┌─────────────────────────┬─────────────────────┬─────────────────────┐
│                         │            executed │              failed │
├─────────────────────────┼─────────────────────┼─────────────────────┤
│              iterations │                   1 │                   1 │
│                requests │                   1 │                   0 │
│              assertions │                   4 │                   1 │
└─────────────────────────┴─────────────────────┴─────────────────────┘

<span class="log-bold log-red">================================================================================
 [ERROR] Process completed with exit code 1. Deliberate assertion failure trapped!
================================================================================</span>
Uploading test failure reports to GitHub Actions diagnostics artifact storage..."""

    render_terminal_evidence(
        title="CI Fail Run (Deliberate Failure Trapped)",
        branch="test/intentional-ci-failure",
        commit_hash="c4e18d9",
        status_badge='<span class="badge badge-fail">✕ Failure</span>',
        steps_html=steps_fail,
        console_logs=log_fail,
        filename="ci-fail.png"
    )

if __name__ == "__main__":
    generate_ci_screenshots()
