# HW06 — AI Audit Report

Student ID: `23127404`  
AI usage declaration: **“I use AI tools for the following tasks.”**

## Recorded use in this workspace

The AI-assisted work for this package was performed with Codex (GPT-5) on 2026-08-23 (UTC+07). The work was deliberately split into specification review, equivalence/boundary design, state/security review, artifact generation, and live execution review. The resulting machine-readable test definitions preserve the generated cases, audit labels, source (`AI Generated` or `Human Extended`), and rationale in `postman/data/*.json` and the Excel workbook.

| Activity | Input supplied to AI | Human review/output retained |
|---|---|---|
| Pool A design | FR-02, API spec, `server.js` | 35 audited rows and 5 extensions; raw Newman case JSON |
| Pool B design | FR-08, cart/checkout API behavior | 35 audited rows and 5 extensions; workflow raw JSON |
| Pool C design | FR-10/FR-18 state graph and SEC-03 | 35 audited rows and 5 extensions; workflow raw JSON |
| Evidence audit | Newman raw output and SQLite observations | execution manifest and six-root-cause bug register |
| Generator design | API specification and testing techniques | generator source, pseudocode, Mermaid design sources |

## Human-review decisions

1. Contract expectations and observed-SUT expectations are kept separate. A known-defect reproducer is marked `BUG DETECTED`; it is never presented as a conforming contract pass.
2. Each Pool A case runs with an isolated fixture to prevent the lockout counter from contaminating later tests.
3. Pool B uses an actual login → cart → checkout → cart-query workflow; Pool C seeds a unique order precondition per state test.
4. Generated screenshots and invented execution metrics were removed. Only raw Newman output is used for numeric claims.

## Student completion requirement

Before submission, the student must append any AI interaction not represented by the retained workspace artifacts with its exact tool/model, timestamp, unmodified prompt, and unmodified output. This report intentionally does not invent conversations or timestamps that are not recoverable from the workspace.
