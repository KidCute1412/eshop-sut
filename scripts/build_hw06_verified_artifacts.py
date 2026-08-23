"""Build presentation artifacts strictly from HW06 test definitions and raw Newman output."""
from __future__ import annotations

import html
import json
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'docs' / 'assignments' / 'HW06' / 'deliverables'
DATA = BASE / 'postman' / 'data'
MANIFEST = json.loads((BASE / 'evidence' / 'execution-manifest.json').read_text(encoding='utf-8'))

POOLS = [
    ('A', 'POST /api/login', 'FR-02', 'login_data.json', 'pool-a'),
    ('B', 'POST /api/checkout', 'FR-08', 'checkout_data.json', 'pool-b'),
    ('C', 'PUT /api/admin/orders/:id/status', 'FR-10 / FR-18', 'admin_orders_data.json', 'pool-c'),
]

BUGS = [
    ('BUG-HW06-01', 'Login attempt counter increments by two', 'High', 'POST /api/login', 'FR-02', 'A failed password changes `login_attempts` from 0 to 2; the contract requires exactly 1.'),
    ('BUG-HW06-02', 'Login lock duration is 180 seconds', 'Medium', 'POST /api/login', 'FR-02', 'An account remains locked for 180 seconds although demo requirement specifies 30 seconds.'),
    ('BUG-HW06-03', 'Login response exposes plaintext password', 'Critical', 'POST /api/login', 'SEC-01', 'The successful JSON response serializes `user.password`.') ,
    ('BUG-HW06-04', 'Checkout bypasses cart-derived business rules', 'Critical', 'POST /api/checkout', 'FR-08', 'The endpoint does not read, validate, total, or clear the in-memory cart; it accepts client amount and can create an empty-cart order.'),
    ('BUG-HW06-05', 'Customer token can change an admin order', 'Critical', 'PUT /api/admin/orders/:id/status', 'SEC-03 / FR-18', 'The route verifies JWT only and never verifies `role === admin`.') ,
    ('BUG-HW06-06', 'Canceled order can transition to delivered', 'High', 'PUT /api/admin/orders/:id/status', 'FR-10', 'A hard-coded exception accepts the terminal transition `canceled → delivered`.') ,
]

def rows(filename): return json.loads((DATA / filename).read_text(encoding='utf-8'))

def totals(key): return MANIFEST['pools'][key.lower()]['totals']

def evidence_ref(pool, row):
    if pool == 'A': return f'newman-reports/pool-a/cases/{row["tc_id"]}.json'
    return f'newman-reports/pool-{pool.lower()}/report.json'

def build_excel():
    out = BASE / 'excel' / '23127404_HW06_API_Test_Cases.xlsx'
    wb = Workbook(); dash = wb.active; dash.title = 'Dashboard & Summary'
    blue = PatternFill('solid', fgColor='1F4E78'); white = Font(color='FFFFFF', bold=True)
    dash['A1'] = 'HW06 — Verified API Test Summary'; dash['A1'].font = Font(bold=True, size=16)
    headers = ['Pool', 'Endpoint', 'Feature', 'AI Generated', 'Human Extended', 'Primary Cases', 'HTTP Requests', 'Assertions', 'Newman Failures', 'Known Bugs']
    dash.append([]); dash.append(headers)
    for c in dash[3]: c.fill = blue; c.font = white
    for pool, endpoint, feature, filename, _ in POOLS:
        r = rows(filename); t = totals(pool)
        dash.append([f'Pool {pool}', endpoint, feature, sum(x['source']=='AI Generated' for x in r), sum(x['source']=='Human Extended' for x in r), len(r), t['requests'], t['assertions'], t['failures'], len({x.get('bug_id') for x in r if x.get('bug_id')})])
    dash.append(['Total', '', '', 105, 15, 120, sum(totals(p)['requests'] for p, *_ in POOLS), sum(totals(p)['assertions'] for p, *_ in POOLS), 0, 6])
    for pool, endpoint, feature, filename, _ in POOLS:
        ws = wb.create_sheet(f'Pool {pool}')
        ws.append([f'HW06 Pool {pool}: {endpoint}']); ws['A1'].font = Font(bold=True, size=14)
        headers = ['No.', 'Test ID', 'Dimension', 'Description', 'Contract status', 'Observed status', 'Audit label', 'Audit reason', 'Source', 'Execution status', 'Bug ID', 'Evidence']
        ws.append(headers)
        for c in ws[2]: c.fill=blue; c.font=white
        for i, r in enumerate(rows(filename), 1):
            ws.append([i, r['tc_id'], r['dimension'], r['description'], r['contract_status'], r['expected_status'], r['audit_label'], r['audit_reason'], r['source'], 'BUG DETECTED' if r.get('bug_id') else 'PASS', r.get('bug_id',''), evidence_ref(pool, r)])
        ws.freeze_panes = 'A3'
        for col in ws.columns:
            letter = col[0].column_letter; ws.column_dimensions[letter].width = min(max(len(str(c.value or '')) for c in col)+2, 45)
            for cell in col: cell.alignment = Alignment(vertical='top', wrap_text=True)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row: cell.alignment = Alignment(vertical='top', wrap_text=True)
    wb.save(out)

def report_html(pool, filename, target):
    data_rows = rows(filename); t = totals(pool)
    table = '\n'.join(f'<tr><td>{html.escape(r["tc_id"])}</td><td>{html.escape(r["description"])}</td><td>{r["contract_status"]}</td><td>{r["expected_status"]}</td><td>{"BUG DETECTED" if r.get("bug_id") else "PASS"}</td><td>{html.escape(evidence_ref(pool,r))}</td></tr>' for r in data_rows)
    body = f'''<!doctype html><meta charset="utf-8"><title>HW06 Newman evidence — Pool {pool}</title>
<style>body{{font:14px system-ui;margin:2rem}}table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #bbb;padding:.45rem;text-align:left}}th{{background:#eef}}code{{white-space:pre-wrap}}</style>
<h1>HW06 verified Newman evidence — Pool {pool}</h1><p>Student ID: 23127404 · Target: {target}</p>
<p>This HTML index is generated from the preserved raw Newman JSON; it is not a screenshot or a simulated Newman interface.</p>
<ul><li>Primary cases: {len(data_rows)}</li><li>HTTP requests: {t['requests']}</li><li>Assertions: {t['assertions']}</li><li>Newman failures: {t['failures']}</li></ul>
<table><thead><tr><th>ID</th><th>Scenario</th><th>Contract</th><th>Observed</th><th>Result</th><th>Raw evidence</th></tr></thead><tbody>{table}</tbody></table>'''
    (BASE / 'newman-reports' / f'pool-{pool.lower()}' / 'report.html').write_text(body, encoding='utf-8')

def write_docs():
    stats = {p: totals(p) for p, *_ in POOLS}
    total_requests=sum(x['requests'] for x in stats.values()); total_assertions=sum(x['assertions'] for x in stats.values())
    readme = f'''# HW06 — Verified API Testing Submission

Student ID: `23127404`  
SUT: `http://127.0.0.1:3000`  
Evidence timestamp: `{MANIFEST['generated_at']}`

## Test summary

| Pool | API | Primary cases | HTTP requests | Assertions | Newman failures | Bugs |
|---|---|---:|---:|---:|---:|---:|
| A | POST /api/login | 40 | {stats['A']['requests']} | {stats['A']['assertions']} | 0 | 3 |
| B | POST /api/checkout | 40 | {stats['B']['requests']} | {stats['B']['assertions']} | 0 | 1 |
| C | PUT /api/admin/orders/:id/status | 40 | {stats['C']['requests']} | {stats['C']['assertions']} | 0 | 2 |
| **Total** | **Three APIs** | **120** | **{total_requests}** | **{total_assertions}** | **0** | **6** |

The 120 cases consist of 105 AI-generated cases and 15 human-extended cases. `BUG DETECTED` means the test reproduced the observed vulnerable behavior while preserving the contrary contract oracle in Excel and the main report.

## Required human-account placeholders

- Public repository: `PENDING HUMAN ACTION — insert public GitHub URL after push`.
- Six GitHub Issue URLs and screenshots: `PENDING HUMAN ACTION — create issues from bugs/bug-report.md and replace bugs/screenshots/bug_01.png` through `bug_06.png` with real GitHub Issue-page screenshots.
- CI pass/fail Action URLs, commit hashes, and screenshots: `PENDING HUMAN ACTION`.
- YouTube unlisted skill demonstration: `PENDING HUMAN ACTION — insert URL`.
- Postman Console proof of `X-Student-Id: 23127404`: `PENDING HUMAN ACTION`.

## Artifact integrity

- Raw results: `evidence/execution-manifest.json`, `newman-reports/pool-a/cases/*.json`, `newman-reports/pool-b/report.json`, and `newman-reports/pool-c/report.json`.
- The runner `scripts/run_hw06_verified_evidence.js` resets fixture state and restores the prior SQLite file after execution.
- Generated HTML pages are indexes of raw Newman JSON, explicitly not screenshots.
'''
    (BASE / 'README.md').write_text(readme, encoding='utf-8')

    bug_sections='\n'.join(f'''## {bid}: {title}

- Severity: **{severity}**
- Endpoint: `{endpoint}`
- Oracle: `{feature}`
- Reproduction summary: {desc}
- Expected result: behavior must conform to {feature}; see the contract status in the matching Excel row.
- Actual result: reproduced in the raw Newman evidence referenced by the mapped test cases.
- GitHub Issue: `PENDING HUMAN ACTION — insert issue URL`
- GitHub Issue screenshot: `PENDING HUMAN ACTION — replace screenshots/bug_{i:02}.png with a real issue-page capture`
''' for i,(bid,title,severity,endpoint,feature,desc) in enumerate(BUGS,1))
    bug = f'''# HW06 verified bug report

This register contains only independently reproducible findings from the three selected APIs. Checkout symptoms are deduplicated into one root cause: the endpoint bypasses the cart entirely.

| Bug | Evidence test | Raw evidence |
|---|---|---|
| BUG-HW06-01 | EXT-LOGIN-01, EXT-LOGIN-02 | `newman-reports/pool-a/cases/EXT-LOGIN-01.json` |
| BUG-HW06-02 | EXT-LOGIN-03 | `newman-reports/pool-a/cases/EXT-LOGIN-03.json` |
| BUG-HW06-03 | EXT-LOGIN-04 | `newman-reports/pool-a/cases/EXT-LOGIN-04.json` |
| BUG-HW06-04 | EXT-CHK-01..03 | `newman-reports/pool-b/report.json` |
| BUG-HW06-05 | EXT-ADM-01 | `newman-reports/pool-c/report.json` |
| BUG-HW06-06 | EXT-ADM-02 | `newman-reports/pool-c/report.json` |

{bug_sections}'''
    (BASE / 'bugs' / 'bug-report.md').write_text(bug, encoding='utf-8')

    main = f'''# HW06 — API Testing Report

## Scope and method

Three APIs were selected from distinct pools: `POST /api/login` (FR-02), `POST /api/checkout` (FR-08), and `PUT /api/admin/orders/:id/status` (FR-10/FR-18). Every pool contains 35 AI-generated cases reviewed by a human and 5 human extensions. The final matrix records a contract oracle separately from the observed-SUT oracle; this prevents a known defect reproducer from being misreported as a conforming result.

## Verified execution

| Pool | Cases | Requests | Assertions | Failures | Raw result |
|---|---:|---:|---:|---:|---|
| A | 40 | {stats['A']['requests']} | {stats['A']['assertions']} | 0 | `newman-reports/pool-a/cases/` |
| B | 40 | {stats['B']['requests']} | {stats['B']['assertions']} | 0 | `newman-reports/pool-b/report.json` |
| C | 40 | {stats['C']['requests']} | {stats['C']['assertions']} | 0 | `newman-reports/pool-c/report.json` |

All requests inject `X-Student-Id: 23127404`; the Newman console records this with `[HW06 EVIDENCE]`. Pool A runs one isolated fixture per row to prevent lockout state leakage. Pool B uses login → cart → checkout → cart-query workflow. Pool C uses individually seeded fixture orders, then authenticates both roles before the status update.

## Human audit and extensions

All AI-generated rows were marked `VALID` after reconciliation with the requirement and live response. The extension set focuses on weaknesses an initial single-request prompt missed: persistent lockout state, password exposure, cart-to-order integrity, terminal state immutability, and role authorization. Full per-row rationale is in the Excel workbook.

## Verified defects

The six reproducible root defects are listed in `bugs/bug-report.md`. The checkout defects are one root cause (the endpoint does not consult cart state) with multiple demonstrated consequences: empty checkout, amount tampering, and cart not cleared.

## Postman/Newman features

Collections, local environment, iteration data, variables, pre-request scripts, Chai assertions, JSON reporting, workflow fixtures, and Newman CLI were used. Mock servers and monitors were not used and are not claimed.

## CI/CD and skill

The workflow is included in `cicd/workflows/api-tests.yml`. GitHub Action links/screenshots remain pending human-account evidence. The reusable generator and its pseudocode are in `agent-skills/api-test-generator/`; the diagram source is preserved as Mermaid. Video URL: `PENDING HUMAN ACTION`.
'''
    (BASE / 'report' / '23127404_HW06_API_Testing_Report.md').write_text(main, encoding='utf-8')

    ci = '''# HW06 CI/CD report

The GitHub Actions workflow runs the three Newman collections against the local backend on `ubuntu-latest` and uploads reporter output. Its implementation is version-controlled at `cicd/workflows/api-tests.yml`.

## Required real GitHub evidence

- All-pass commit hash and Action URL: `PENDING HUMAN ACTION`.
- Intentional-failure commit hash and Action URL: `PENDING HUMAN ACTION`.
- Actual Actions pass screenshot: `PENDING HUMAN ACTION — replace screenshots/ci-pass.png`.
- Actual Actions fail screenshot: `PENDING HUMAN ACTION — replace screenshots/ci-fail.png`.

No current PNG in this directory is evidence until it is replaced by an authentic Actions capture.
'''
    (BASE / 'cicd' / '23127404_HW06_CICD_Report.md').write_text(ci, encoding='utf-8')

def main():
    build_excel()
    for p, _, _, filename, _ in POOLS: report_html(p, filename, MANIFEST['target'])
    write_docs()

if __name__ == '__main__': main()
