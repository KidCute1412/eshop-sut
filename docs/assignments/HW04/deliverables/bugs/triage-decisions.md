# HW04 Agent Triage Decisions

Generated from fresh candidate reruns at revision `6b884900be153b5af78a4865c9cca98cedcd9fc9`. The agent classified each candidate using the requirement oracle, runtime result, and test-design audit. The 17 confirmed rows now map to the public Issue URLs in `bug_report.md` and `issue-register.md`.

| Candidate | Case | Decision | Defect | Rationale | Screenshot |
|---|---|---|---|---|---|
| HW04-CAND-001 | FR06-07 | Confirmed | BUG-001 | FR-06 explicitly requires the product category; the same mismatch recurs across all three browsers. | bugs/evidence/HW04-CAND-001/screenshot.png |
| HW04-CAND-002 | FR06-09 | Confirmed | BUG-002 | FR-06 requires a positive integer quantity with minimum one; the missing native constraint is deterministic. | bugs/evidence/HW04-CAND-002/screenshot.png |
| HW04-CAND-003 | FR06-11 | Rejected | — | The requirement permits visible toast, badge, or equivalent feedback; the original assertion hardcodes button text and does not prove cart state. | bugs/evidence/HW04-CAND-003/screenshot.png |
| HW04-CAND-004 | FR06-12 | Rejected | — | Same oracle gap as HW04-CAND-003; this is not independently promoted to a product defect without a stronger feedback/state oracle. | bugs/evidence/HW04-CAND-004/screenshot.png |
| HW04-CAND-005 | FR06-13 | Confirmed | BUG-003 | The requirement rejects non-positive quantities; native validity is deterministic across browsers. | bugs/evidence/HW04-CAND-005/screenshot.png |
| HW04-CAND-006 | FR06-14 | Confirmed | BUG-004 | The requirement rejects negative quantities; native validity is deterministic across browsers. | bugs/evidence/HW04-CAND-006/screenshot.png |
| HW04-CAND-007 | FR10-06 | Confirmed | BUG-005 | The state-machine requirement forbids cancellation after shipping; the UI exposes an invalid action. | bugs/evidence/HW04-CAND-007/screenshot.png |
| HW04-CAND-008 | FR10-11 | Confirmed | BUG-006 | The terminal/role restriction is explicit and the invalid UI action recurs across browsers. | bugs/evidence/HW04-CAND-008/screenshot.png |
| HW04-CAND-009 | FR10-12 | Confirmed | BUG-007 | Shipping orders must reject user cancellation; a successful response violates the state transition contract. | bugs/evidence/HW04-CAND-009/screenshot.png |
| HW04-CAND-010 | FR10-16 | Confirmed | BUG-008 | Canceled is a terminal state under FR-10; accepting delivery is a direct contract violation. | bugs/evidence/HW04-CAND-010/screenshot.png |
| HW04-CAND-011 | FR12-03 | Confirmed | BUG-009 | Admin-user listing must require an admin role; a regular JWT receives protected data. | bugs/evidence/HW04-CAND-011/screenshot.png |
| HW04-CAND-012 | FR12-06 | Confirmed | BUG-010 | Admin-order listing must require an admin role; a regular JWT receives protected data. | bugs/evidence/HW04-CAND-012/screenshot.png |
| HW04-CAND-013 | FR12-08 | Confirmed | BUG-011 | Unauthenticated data mutation must be rejected; the endpoint creates data without a JWT. | bugs/evidence/HW04-CAND-013/screenshot.png |
| HW04-CAND-014 | FR12-09 | Confirmed | BUG-012 | Product creation must require an admin role; a regular JWT is accepted. | bugs/evidence/HW04-CAND-014/screenshot.png |
| HW04-CAND-015 | FR12-11 | Confirmed | BUG-013 | Unauthenticated product mutation must be rejected; the endpoint accepts the request. | bugs/evidence/HW04-CAND-015/screenshot.png |
| HW04-CAND-016 | FR12-12 | Confirmed | BUG-014 | Product deletion must require an admin role; a regular JWT is accepted. | bugs/evidence/HW04-CAND-016/screenshot.png |
| HW04-CAND-017 | FR12-14 | Confirmed | BUG-015 | Category creation must require an admin role; a regular JWT is accepted. | bugs/evidence/HW04-CAND-017/screenshot.png |
| HW04-CAND-018 | FR12-17 | Confirmed | BUG-016 | Coupon creation must require an admin role; a regular JWT is accepted. | bugs/evidence/HW04-CAND-018/screenshot.png |
| HW04-CAND-019 | FR12-19 | Confirmed | BUG-017 | Authorization must be enforced before import validation; a regular JWT reaches the protected operation. | bugs/evidence/HW04-CAND-019/screenshot.png |
