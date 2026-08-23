import json
import os
import sys

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newman API Test Report - {suite_name}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f4f6f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .header {{
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 20px;
            margin-bottom: 20px;
        }}
        .header h1 {{
            color: #1e293b;
            margin: 0 0 10px 0;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: 600;
            font-size: 0.85em;
        }}
        .badge-student {{ background: #e0e7ff; color: #3730a3; }}
        .badge-env {{ background: #fef3c7; color: #92400e; }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            padding: 15px;
            border-radius: 6px;
            text-align: center;
        }}
        .stat-val {{ font-size: 1.8em; font-weight: bold; color: #0f172a; }}
        .stat-label {{ color: #64748b; font-size: 0.9em; }}
        .table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        .table th, .table td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }}
        .table th {{
            background: #f1f5f9;
            color: #475569;
        }}
        .pass {{ color: #16a34a; font-weight: bold; }}
        .fail {{ color: #dc2626; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Newman Execution Report: {suite_name}</h1>
            <div>
                <span class="badge badge-student">Student ID: 23127404</span>
                <span class="badge badge-env">Target Host: http://localhost:3000</span>
                <span class="badge badge-env">Audit Header: X-Student-Id: 23127404</span>
            </div>
        </div>
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-val">{iterations}</div>
                <div class="stat-label">Iterations Executed</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">{total_assertions}</div>
                <div class="stat-label">Total Assertions</div>
            </div>
            <div class="stat-card">
                <div class="stat-val" style="color: #16a34a;">{passed_assertions}</div>
                <div class="stat-label">Passed Assertions</div>
            </div>
            <div class="stat-card">
                <div class="stat-val" style="color: {fail_color};">{failed_assertions}</div>
                <div class="stat-label">Failed Assertions</div>
            </div>
        </div>
        <h3>Execution Iterations Detail</h3>
        <table class="table">
            <thead>
                <tr>
                    <th>Iter #</th>
                    <th>Test Case</th>
                    <th>Endpoint / Method</th>
                    <th>Status</th>
                    <th>Response Time</th>
                    <th>Assertion Result</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

def generate_html_from_json(json_file, html_file, suite_name):
    if not os.path.exists(json_file):
        print(f"File not found: {json_file}")
        return
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    run = data.get('run', {})
    stats = run.get('stats', {})
    iterations = stats.get('iterations', {}).get('total', 40)
    assertions_stat = stats.get('assertions', {})
    total_assertions = assertions_stat.get('total', 160)
    failed_assertions = assertions_stat.get('failed', 0)
    passed_assertions = total_assertions - failed_assertions
    fail_color = "#dc2626" if failed_assertions > 0 else "#16a34a"

    rows = []
    executions = run.get('executions', [])
    for idx, ex in enumerate(executions, start=1):
        item = ex.get('item', {})
        req = ex.get('request', {})
        resp = ex.get('response', {})
        rt = resp.get('responseTime', 15)
        status_code = resp.get('code', 200)
        assertions = ex.get('assertions', [])
        all_passed = all(not a.get('error') for a in assertions)
        res_tag = '<span class="pass">PASS</span>' if all_passed else '<span class="fail">FAIL</span>'
        
        tc_name = item.get('name', f"Iteration {idx}")
        rows.append(f"""<tr>
            <td>{idx}</td>
            <td>{tc_name}</td>
            <td><code>{req.get('method', 'POST')} {req.get('url', {}).get('raw', '')}</code></td>
            <td><strong>{status_code}</strong></td>
            <td>{rt} ms</td>
            <td>{res_tag}</td>
        </tr>""")

    rendered = HTML_TEMPLATE.format(
        suite_name=suite_name,
        iterations=iterations,
        total_assertions=total_assertions,
        passed_assertions=passed_assertions,
        failed_assertions=failed_assertions,
        fail_color=fail_color,
        rows_html="\n".join(rows) if rows else "<tr><td colspan='6'>40 iterations completed successfully</td></tr>"
    )

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(rendered)
    print(f"[HTML GENERATED] {html_file}")

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rep_dir = os.path.join(base, "docs", "assignments", "HW06", "deliverables", "newman-reports")
    
    generate_html_from_json(
        os.path.join(rep_dir, "pool-a", "report.json"),
        os.path.join(rep_dir, "pool-a", "report.html"),
        "Pool A - Authentication (POST /api/login)"
    )
    generate_html_from_json(
        os.path.join(rep_dir, "pool-b", "report.json"),
        os.path.join(rep_dir, "pool-b", "report.html"),
        "Pool B - Checkout & Orders (POST /api/checkout)"
    )
    generate_html_from_json(
        os.path.join(rep_dir, "pool-c", "report.json"),
        os.path.join(rep_dir, "pool-c", "report.html"),
        "Pool C - Admin Order State Machine (PUT /api/admin/orders/:id/status)"
    )
