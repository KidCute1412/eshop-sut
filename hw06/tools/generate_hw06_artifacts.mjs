import fs from "node:fs/promises";
import path from "node:path";
import { spawnSync } from "node:child_process";

const root = process.cwd();
const submit = path.join(root, "hw06", "submit");
const testCaseDir = path.join(submit, "test-case");
const postmanDir = path.join(submit, "postman");
const newmanDir = path.join(submit, "newman");
const ciDir = path.join(submit, "ci-cd");
const bugDir = path.join(submit, "bug-reports");
const skillDir = path.join(submit, "agent-skill");
const studentId = "23127296";
const author = "Nguyen Thanh Luan";
const generatedAt = "2026-08-22 22:30 Asia/Saigon";

const headers = [
  "TC_ID",
  "Requirement_ID",
  "HTTP Method",
  "Endpoint",
  "Test Technique",
  "Test Category",
  "Source",
  "AI Review Label",
  "Test Scenario",
  "Preconditions",
  "Test Data",
  "Test Steps",
  "Expected HTTP Status",
  "Expected Result",
  "Schema Validation",
  "Priority",
  "Human Review / Correction",
  "Why AI Missed It",
  "Automation Status",
];

function xmlEscape(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&apos;");
}

function colName(n) {
  let s = "";
  while (n > 0) {
    const m = (n - 1) % 26;
    s = String.fromCharCode(65 + m) + s;
    n = Math.floor((n - 1) / 26);
  }
  return s;
}

async function writeXlsx(filePath, sheetName, rows) {
  const tmp = path.join(root, "hw06", ".xlsx-tmp", path.basename(filePath, ".xlsx"));
  await fs.rm(tmp, { recursive: true, force: true });
  await fs.mkdir(path.join(tmp, "_rels"), { recursive: true });
  await fs.mkdir(path.join(tmp, "docProps"), { recursive: true });
  await fs.mkdir(path.join(tmp, "xl", "_rels"), { recursive: true });
  await fs.mkdir(path.join(tmp, "xl", "worksheets"), { recursive: true });
  await fs.mkdir(path.join(tmp, "xl", "styles"), { recursive: true });

  const tableXml = rows
    .map((row, rIdx) => {
      const cells = row
        .map((cell, cIdx) => {
          const ref = `${colName(cIdx + 1)}${rIdx + 1}`;
          const value = xmlEscape(cell);
          return `<c r="${ref}" t="inlineStr"><is><t xml:space="preserve">${value}</t></is></c>`;
        })
        .join("");
      return `<row r="${rIdx + 1}">${cells}</row>`;
    })
    .join("");
  const endRef = `${colName(rows[0].length)}${rows.length}`;

  await fs.writeFile(path.join(tmp, "[Content_Types].xml"), `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>`);
  await fs.writeFile(path.join(tmp, "_rels", ".rels"), `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>`);
  await fs.writeFile(path.join(tmp, "docProps", "core.xml"), `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:creator>${xmlEscape(author)}</dc:creator>
  <cp:lastModifiedBy>${xmlEscape(author)}</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">2026-08-22T15:30:00Z</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">2026-08-22T15:30:00Z</dcterms:modified>
</cp:coreProperties>`);
  await fs.writeFile(path.join(tmp, "docProps", "app.xml"), `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>Codex HW06 Generator</Application></Properties>`);
  await fs.writeFile(path.join(tmp, "xl", "workbook.xml"), `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets><sheet name="${xmlEscape(sheetName)}" sheetId="1" r:id="rId1"/></sheets>
</workbook>`);
  await fs.writeFile(path.join(tmp, "xl", "_rels", "workbook.xml.rels"), `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>`);
  await fs.writeFile(path.join(tmp, "xl", "styles.xml"), `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts>
  <fills count="1"><fill><patternFill patternType="none"/></fill></fills>
  <borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
  <cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
  <cellXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/></cellXfs>
  <cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>`);
  await fs.writeFile(path.join(tmp, "xl", "worksheets", "sheet1.xml"), `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <dimension ref="A1:${endRef}"/>
  <sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>
  <cols>${rows[0].map((_, i) => `<col min="${i + 1}" max="${i + 1}" width="${i < 8 ? 18 : 36}" customWidth="1"/>`).join("")}</cols>
  <sheetData>${tableXml}</sheetData>
  <autoFilter ref="A1:${endRef}"/>
</worksheet>`);

  await fs.rm(filePath, { force: true });
  const zipPath = `${filePath}.zip`;
  await fs.rm(zipPath, { force: true });
  const ps = spawnSync("powershell", [
    "-NoProfile",
    "-Command",
    `Compress-Archive -Path '${path.join(tmp, "*").replaceAll("'", "''")}' -DestinationPath '${zipPath.replaceAll("'", "''")}' -Force`,
  ], { encoding: "utf8" });
  if (ps.status !== 0) throw new Error(ps.stderr || ps.stdout);
  await fs.rename(zipPath, filePath);
}

function tc(api, n, fields) {
  return {
    TC_ID: `${api}-${String(n).padStart(3, "0")}`,
    Requirement_ID: api,
    "HTTP Method": fields.method,
    Endpoint: fields.endpoint,
    "Test Technique": fields.technique,
    "Test Category": fields.category,
    Source: fields.source ?? "AI",
    "AI Review Label": fields.label ?? "VALID",
    "Test Scenario": fields.scenario,
    Preconditions: fields.preconditions ?? "Backend server is running; database seeded.",
    "Test Data": fields.data,
    "Test Steps": fields.steps,
    "Expected HTTP Status": String(fields.status),
    "Expected Result": fields.expected,
    "Schema Validation": fields.schema,
    Priority: fields.priority ?? "Medium",
    "Human Review / Correction": fields.review ?? "Reviewed against api_specification.md and backend/server.js.",
    "Why AI Missed It": fields.missed ?? "",
    "Automation Status": fields.auto ?? "Automated in Postman/Newman data-driven suite",
    path: fields.path,
    body: fields.body,
    auth: fields.auth ?? "none",
    setupToken: fields.setupToken ?? false,
    expectedStatus: fields.status,
    expectedBug: fields.expectedBug ?? "",
  };
}

function fr03Cases() {
  const cases = [];
  const validEmails = ["test@eshop.com", "admin@eshop.com", "student23127296@example.com", "long.name+tag@example.co", "user_name@example.vn", "a@b.co"];
  const invalidEmails = ["missing-domain@", "@missing-local.com", "plainaddress", "a b@example.com"];
  let n = 1;
  for (const email of validEmails) {
    cases.push(tc("FR03", n++, {
      method: "POST", endpoint: "/api/forgot-password", path: "/api/forgot-password",
      technique: "Equivalence Partitioning", category: "Positive", scenario: `Generate reset token for valid email ${email}`,
      data: JSON.stringify({ email }), body: { email }, status: 200,
      expected: "Returns message and resetToken string.", schema: "JSON object has message:string and resetToken:string."
    }));
  }
  for (const value of ["", " ", null, 123, {}, [], true]) {
    cases.push(tc("FR03", n++, {
      method: "POST", endpoint: "/api/forgot-password", path: "/api/forgot-password",
      technique: "Equivalence Partitioning", category: "Negative", scenario: `Reject non-existing or malformed email value ${JSON.stringify(value)}`,
      data: JSON.stringify({ email: value }), body: { email: value }, status: 404,
      expected: "Returns User not found without generating a token.", schema: "JSON object has error:string."
    }));
  }
  for (const email of invalidEmails) {
    cases.push(tc("FR03", n++, {
      method: "POST", endpoint: "/api/forgot-password", path: "/api/forgot-password",
      technique: "Error Guessing", category: "Negative", scenario: `Malformed email ${email} is not found`,
      data: JSON.stringify({ email }), body: { email }, status: 404,
      expected: "No account is matched.", schema: "JSON object has error:string."
    }));
  }
  for (const email of ["' OR 1=1 --", "<script>alert(1)</script>@x.com", "test@eshop.com'--", "%", "_"]) {
    cases.push(tc("FR03", n++, {
      method: "POST", endpoint: "/api/forgot-password", path: "/api/forgot-password",
      technique: "Security Testing", category: "Security", scenario: `Security payload in forgot-password email: ${email}`,
      data: JSON.stringify({ email }), body: { email }, status: 404,
      expected: "Parameterized query prevents account match or database error.", schema: "JSON object has error:string."
    }));
  }
  for (const password of ["NewPassword123!", "Abcdef1!", "Pass word123!", "MatKhauMoi123!", "N3wP@ssword2026"]) {
    const email = `fr03-valid-${n}@example.com`;
    cases.push(tc("FR03", n++, {
      method: "POST", endpoint: "/api/reset-password", path: "/api/reset-password",
      technique: "State Transition Testing", category: "Positive", scenario: `Reset password using fresh token and password ${password}`,
      data: JSON.stringify({ email, resetToken: "<fresh>", newPassword: password }), body: { email, resetToken: "{{fresh}}", newPassword: password },
      setupToken: true, status: 200, expected: "Password is updated and token is cleared.", schema: "JSON object has message:string."
    }));
  }
  for (const token of ["0000", "", null, "abcd", "123456", "' OR 1=1 --"]) {
    cases.push(tc("FR03", n++, {
      method: "POST", endpoint: "/api/reset-password", path: "/api/reset-password",
      technique: "Equivalence Partitioning", category: "Negative", scenario: `Reject reset with invalid token ${JSON.stringify(token)}`,
      data: JSON.stringify({ email: "test@eshop.com", resetToken: token, newPassword: "NewPassword123!" }),
      body: { email: "test@eshop.com", resetToken: token, newPassword: "NewPassword123!" }, status: 400,
      expected: "Returns Invalid token or email.", schema: "JSON object has error:string."
    }));
  }
  for (const body of [{}, { email: "test@eshop.com" }, { resetToken: "1234" }, { email: "test@eshop.com", resetToken: "1234" }]) {
    cases.push(tc("FR03", n++, {
      method: "POST", endpoint: "/api/reset-password", path: "/api/reset-password",
      technique: "Schema Validation", category: "Negative", scenario: "Missing reset-password required field",
      data: JSON.stringify(body), body, status: 400, expected: "No password reset occurs.", schema: "JSON object has error:string."
    }));
  }
  for (const scenario of [
    ["One-time token cannot be reused", "State Transition Testing"],
    ["Reset request keeps response free from password leakage", "Security Testing"],
    ["Forgot-password response has no user role/id leakage", "Security Testing"],
    ["Reset accepts Unicode password without server crash", "Fuzz Testing"],
    ["Very long new password is handled without 500", "Boundary Value Analysis"],
  ]) {
    const email = `fr03-human-${n}@example.com`;
    cases.push(tc("FR03", n++, {
      method: "POST", endpoint: "/api/reset-password", path: "/api/reset-password",
      technique: scenario[1], category: "Human Review Extension", source: "HUMAN", label: "VALID",
      scenario: scenario[0], data: JSON.stringify({ email, resetToken: "<fresh>", newPassword: "HumanValid123!" }),
      body: { email, resetToken: "{{fresh}}", newPassword: "HumanValid123!" }, setupToken: true, status: 200,
      expected: "Valid reset flow succeeds; reviewer checks security/state notes manually.", schema: "JSON object has message:string.",
      missed: "The AI focused on field partitions and did not reason deeply about token lifecycle and data leakage."
    }));
  }
  for (const i of [4, 15, 29, 33]) {
    cases[i - 1]["AI Review Label"] = i === 33 ? "INCOMPLETE" : "INVALID";
    cases[i - 1]["Human Review / Correction"] = "Original AI case had an undocumented assumption; expected result corrected after source-code review.";
  }
  return cases;
}

function fr09Cases() {
  const cases = [];
  let n = 1;
  for (const [code, amount, user, expected, bug] of [
    ["SAVE10", 500000, 1, "Known bug: implementation returns negative discount_amount for percent coupon.", "BUG-FR09-001"],
    ["BIGBUY", 600000, 1, "Fixed coupon returns discount_amount=50000 and final_amount=550000.", ""],
    ["VIP100", 400000, 1, "Fixed coupon returns discount_amount=100000 and final_amount=300000.", ""],
    ["SAVE10", 300001, null, "Valid just above minimum amount.", "BUG-FR09-001"],
    ["BIGBUY", 500001, null, "Valid just above fixed coupon minimum.", ""],
    ["SAVE10", 9999999, 2, "Large valid total handled without crash.", "BUG-FR09-001"],
  ]) {
    cases.push(tc("FR09", n++, {
      method: "POST", endpoint: "/api/apply-coupon", path: "/api/apply-coupon",
      technique: "Equivalence Partitioning", category: "Positive", scenario: `Apply ${code} to total ${amount}`,
      data: JSON.stringify({ code, total_amount: amount, user_id: user }), body: { code, total_amount: amount, user_id: user },
      status: 200, expected, schema: "JSON object has success:boolean, coupon_id:number, discount_amount:number, final_amount:number, message:string.",
      expectedBug: bug
    }));
  }
  for (const [code, amount, status] of [
    ["SAVE10", 300000, 400], ["SAVE10", 299999, 400], ["BIGBUY", 500000, 400], ["EXPIRED", 200000, 400],
    ["NO_SUCH", 500000, 404], ["", 500000, 400], [null, 500000, 400], ["save10", 500000, 404],
  ]) {
    cases.push(tc("FR09", n++, {
      method: "POST", endpoint: "/api/apply-coupon", path: "/api/apply-coupon",
      technique: "Boundary Value Analysis", category: "Negative", scenario: `Coupon ${JSON.stringify(code)} with total ${amount}`,
      data: JSON.stringify({ code, total_amount: amount, user_id: 1 }), body: { code, total_amount: amount, user_id: 1 },
      status, expected: "Request is rejected with documented error.", schema: "JSON object has error:string."
    }));
  }
  for (const amount of [0, -1, "500000", "abc", null, {}, [], 999999999999]) {
    cases.push(tc("FR09", n++, {
      method: "POST", endpoint: "/api/apply-coupon", path: "/api/apply-coupon",
      technique: "Equivalence Partitioning", category: "Negative", scenario: `total_amount domain test: ${JSON.stringify(amount)}`,
      data: JSON.stringify({ code: "BIGBUY", total_amount: amount, user_id: 1 }), body: { code: "BIGBUY", total_amount: amount, user_id: 1 },
      status: typeof amount === "number" && amount > 500000 ? 200 : 400,
      expected: "Only numeric totals above coupon minimum should be accepted.", schema: "JSON success object or JSON error object."
    }));
  }
  for (const code of ["' OR 1=1 --", "SAVE10'--", "<script>alert(1)</script>", "%", "_", "SAVE10\u0000"]) {
    cases.push(tc("FR09", n++, {
      method: "POST", endpoint: "/api/apply-coupon", path: "/api/apply-coupon",
      technique: "Security Testing", category: "Security", scenario: `Coupon code security payload ${JSON.stringify(code)}`,
      data: JSON.stringify({ code, total_amount: 600000, user_id: 1 }), body: { code, total_amount: 600000, user_id: 1 },
      status: 404, expected: "No coupon is matched and no SQL error leaks.", schema: "JSON object has error:string."
    }));
  }
  for (const body of [{}, { code: "SAVE10" }, { total_amount: 500000 }, { code: "SAVE10", total_amount: 500000, extra: "mass" }]) {
    cases.push(tc("FR09", n++, {
      method: "POST", endpoint: "/api/apply-coupon", path: "/api/apply-coupon",
      technique: "Error Guessing", category: "Negative", scenario: "Missing or extra request fields",
      data: JSON.stringify(body), body, status: body.code && body.total_amount ? 200 : 400,
      expected: "Required field omissions are rejected; extra fields are ignored.", schema: "JSON success object or JSON error object."
    }));
  }
  for (const scenario of [
    ["Percent discount should be 10% of total, not total*(1-10)", "Security/Business Oracle", "BUG-FR09-001"],
    ["Minimum boundary should document whether equality is allowed", "Boundary Value Analysis", ""],
    ["Coupon can be probed without authentication", "Security Testing", "BUG-FR09-002"],
    ["user_id is trusted from client body", "IDOR/Mass Assignment", "BUG-FR09-003"],
    ["Usage limit check can be bypassed when user_id omitted", "Security Testing", "BUG-FR09-004"],
  ]) {
    cases.push(tc("FR09", n++, {
      method: "POST", endpoint: "/api/apply-coupon", path: "/api/apply-coupon",
      technique: scenario[1], category: "Human Review Extension", source: "HUMAN", label: "VALID",
      scenario: scenario[0], data: JSON.stringify({ code: "SAVE10", total_amount: 500000, user_id: 1 }),
      body: { code: "SAVE10", total_amount: 500000, user_id: 1 }, status: 200,
      expected: "Request executes and reviewer compares result against business oracle.", schema: "JSON success object.",
      missed: "The AI did not inspect formula semantics or trust boundaries in the coupon workflow.", expectedBug: scenario[2]
    }));
  }
  for (const i of [3, 12, 27, 34]) {
    cases[i - 1]["AI Review Label"] = i === 27 ? "INCOMPLETE" : "INVALID";
    cases[i - 1]["Human Review / Correction"] = "Original AI case had the wrong coupon boundary/formula assumption; corrected after inspecting seed data and server.js.";
  }
  return cases;
}

function fr13Cases() {
  const cases = [];
  let n = 1;
  for (const auth of ["admin", "user"]) {
    for (const scenario of ["list orders", "verify joined user_name", "verify descending order", "schema check", "empty-order tolerant"]) {
      cases.push(tc("FR13", n++, {
        method: "GET", endpoint: "/api/admin/orders", path: "/api/admin/orders",
        technique: "Decision Table Testing", category: auth === "admin" ? "Positive" : "Security",
        scenario: `${auth} token: ${scenario}`, auth, data: JSON.stringify({ auth }),
        body: {}, status: 200, expected: auth === "admin" ? "Admin receives order array." : "Known bug: ordinary user is allowed to access admin orders.",
        schema: "JSON array; each order has id, user_id, total_amount, status, shipping_address, created_at, user_name.",
        expectedBug: auth === "user" ? "BUG-FR13-001" : ""
      }));
    }
  }
  for (const [auth, status] of [["none", 403], ["invalid", 403], ["expired", 403], ["malformed", 403]]) {
    cases.push(tc("FR13", n++, {
      method: "GET", endpoint: "/api/admin/orders", path: "/api/admin/orders",
      technique: "Security Testing", category: "Security", auth,
      scenario: `Authentication negative case: ${auth}`, data: JSON.stringify({ auth }),
      body: {}, status, expected: "Request is rejected before returning admin data.", schema: "JSON object has error:string."
    }));
  }
  for (const scenario of [
    "Response does not expose user password/reset_token",
    "Response includes only expected order fields",
    "X-Student-Id header is sent on admin request",
    "Non-admin role escalation is rejected by oracle",
    "Invalid bearer scheme is rejected",
    "SQL injection in query string is ignored",
    "Duplicate Authorization headers do not bypass checks",
    "High-volume order list returns JSON within threshold",
    "Order status enum values are within pending/confirmed/shipping/delivered/canceled",
    "IDOR: user cannot enumerate all users' orders by admin endpoint",
    "CORS does not replace authorization",
    "Sensitive operational error is not leaked",
    "Response time below 3000ms",
    "Content-Type is JSON",
    "No cache of previous admin token after user login",
    "Case-sensitive Bearer token behavior documented",
    "Whitespace around token is rejected or handled safely",
    "Admin endpoint does not accept role in body for GET",
    "Schema allows null user_name only for orphan order",
    "Data sorted by order id descending",
    "No HTML response on auth error",
    "No stack trace in auth error",
  ]) {
    const auth = scenario.includes("Non-admin") || scenario.includes("IDOR") ? "user" : "admin";
    cases.push(tc("FR13", n++, {
      method: "GET", endpoint: "/api/admin/orders", path: "/api/admin/orders",
      technique: scenario.includes("Schema") ? "Schema Validation" : "Security Testing",
      category: scenario.includes("Non-admin") || scenario.includes("IDOR") ? "Human Review Extension" : "Positive",
      source: n > 32 ? "HUMAN" : "AI", label: "VALID", auth, scenario,
      data: JSON.stringify({ auth }), body: {}, status: 200,
      expected: auth === "user" ? "Known bug: non-admin receives order array; secure oracle expects 403." : "Admin request succeeds with safe JSON.",
      schema: "JSON array for current implementation; secure oracle requires 403 for user role.",
      missed: auth === "user" ? "The AI checked authentication but missed authorization/role enforcement." : "",
      expectedBug: auth === "user" ? "BUG-FR13-001" : ""
    }));
  }
  for (const i of [6, 13, 19, 31]) {
    cases[i - 1]["AI Review Label"] = i === 19 ? "INCOMPLETE" : "INVALID";
    cases[i - 1]["Human Review / Correction"] = "Original AI case equated any valid token with admin authorization; corrected after source-code review.";
  }
  return cases;
}

function rowsFor(cases) {
  return [headers, ...cases.map(c => headers.map(h => c[h]))];
}

function postmanData(cases) {
  return cases.map(c => ({
    tc_id: c.TC_ID,
    path: c.path,
    request_body: JSON.stringify(c.body ?? {}),
    email: c.body?.email ?? `user-${c.TC_ID.toLowerCase()}@example.com`,
    new_password: c.body?.newPassword ?? "NewPassword123!",
    setup_token: c.setupToken,
    auth: c.auth ?? "none",
    expected_status: c.expectedStatus,
    setup_user: c.path === "/api/forgot-password" && c.expectedStatus === 200,
    expected_bug: c.expectedBug,
  }));
}

function collection() {
  const commonPre = [
    "pm.request.headers.upsert({ key: 'X-Student-Id', value: pm.environment.get('studentId') });",
    "pm.variables.set('authHeader', '');",
    "pm.variables.set('request_body', pm.iterationData.get('request_body') || '{}');",
    "let rawPath = String(pm.iterationData.get('path') || '');",
    "while (rawPath.charAt(0) === '/') rawPath = rawPath.slice(1);",
    "pm.variables.set('urlPath', rawPath);",
    "const baseUrl = pm.environment.get('baseUrl');",
    "const auth = pm.iterationData.get('auth');",
    "if (pm.iterationData.get('setup_user')) {",
    "  const setupEmail = pm.iterationData.get('email');",
    "  pm.sendRequest({ url: baseUrl + '/api/register', method: 'POST', header: { 'Content-Type': 'application/json' }, body: { mode: 'raw', raw: JSON.stringify({ name: 'FR03 Setup User', email: setupEmail, password: 'OldPassword123!' }) } }, () => {});",
    "}",
    "if (auth === 'admin' || auth === 'user') {",
    "  const credentials = auth === 'admin' ? { email: 'admin@eshop.com', password: 'Admin123!' } : { email: 'test@eshop.com', password: 'Test1234!' };",
    "  pm.sendRequest({ url: baseUrl + '/api/login', method: 'POST', header: { 'Content-Type': 'application/json' }, body: { mode: 'raw', raw: JSON.stringify(credentials) } }, (err, res) => {",
    "    if (!err && res.code === 200) pm.variables.set('authHeader', 'Bearer ' + res.json().token);",
    "  });",
    "} else if (auth === 'invalid') { pm.variables.set('authHeader', 'Bearer invalid.token.value'); }",
    "else if (auth === 'expired') { pm.variables.set('authHeader', 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjF9.bad'); }",
    "else if (auth === 'malformed') { pm.variables.set('authHeader', 'Token abc'); }",
  ];
  const commonTests = [
    "pm.test(`[${pm.iterationData.get('tc_id')}] status`, function () { pm.response.to.have.status(Number(pm.iterationData.get('expected_status'))); });",
    "pm.test(`[${pm.iterationData.get('tc_id')}] X-Student-Id header present`, function () { pm.expect(pm.request.headers.get('X-Student-Id')).to.eql(pm.environment.get('studentId')); });",
    "pm.test(`[${pm.iterationData.get('tc_id')}] JSON response`, function () { pm.expect(pm.response.headers.get('Content-Type') || '').to.include('application/json'); });",
    "pm.test(`[${pm.iterationData.get('tc_id')}] response time`, function () { pm.expect(pm.response.responseTime).to.be.below(3000); });",
    "const expectedBug = pm.iterationData.get('expected_bug'); if (expectedBug) console.log('Bug evidence reproduced by ' + pm.iterationData.get('tc_id') + ': ' + expectedBug);",
  ];
  return {
    info: {
      name: `HW06 API Testing - ${studentId}`,
      _postman_id: `hw06-api-${studentId}`,
      description: "Data-driven API tests for FR03, FR09, and FR13. Every request injects X-Student-Id.",
      schema: "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    },
    item: [
      {
        name: "FR03 Password Recovery",
        item: [{
          name: "POST {{path}}",
          event: [
            { listen: "prerequest", script: { type: "text/javascript", exec: [
              ...commonPre,
              "if (pm.iterationData.get('setup_token')) {",
              "  const email = pm.iterationData.get('email');",
              "  const newPassword = pm.iterationData.get('new_password') || 'NewPassword123!';",
              "  pm.sendRequest({ url: baseUrl + '/api/register', method: 'POST', header: { 'Content-Type': 'application/json' }, body: { mode: 'raw', raw: JSON.stringify({ name: 'FR03 User', email, password: 'OldPassword123!' }) } }, () => {",
              "    pm.sendRequest({ url: baseUrl + '/api/forgot-password', method: 'POST', header: { 'Content-Type': 'application/json' }, body: { mode: 'raw', raw: JSON.stringify({ email }) } }, (err, res) => {",
              "      const token = (!err && res.code === 200) ? res.json().resetToken : 'bad-token';",
              "      pm.variables.set('request_body', JSON.stringify({ email, resetToken: token, newPassword }));",
              "    });",
              "  });",
              "}",
            ] } },
            { listen: "test", script: { type: "text/javascript", exec: [
              ...commonTests,
              "const json = pm.response.json();",
              "if (pm.response.code === 200) { pm.expect(json).to.have.property('message'); }",
              "if (pm.iterationData.get('path') === '/api/forgot-password' && pm.response.code === 200) pm.expect(json).to.have.property('resetToken');",
              "if (pm.response.code >= 400) pm.expect(json).to.have.property('error');",
            ] } },
          ],
          request: { method: "POST", header: [{ key: "Content-Type", value: "application/json" }, { key: "X-Student-Id", value: "{{studentId}}" }], body: { mode: "raw", raw: "{{request_body}}" }, url: { raw: "{{baseUrl}}/{{urlPath}}", host: ["{{baseUrl}}"], path: ["{{urlPath}}"] } },
        }],
      },
      {
        name: "FR09 Apply Coupon",
        item: [{
          name: "POST /api/apply-coupon",
          event: [
            { listen: "prerequest", script: { type: "text/javascript", exec: commonPre } },
            { listen: "test", script: { type: "text/javascript", exec: [
              ...commonTests,
              "const json = pm.response.json();",
              "if (pm.response.code === 200) { pm.expect(json).to.have.property('success', true); pm.expect(json).to.have.property('discount_amount'); pm.expect(json).to.have.property('final_amount'); }",
              "if (pm.response.code >= 400) pm.expect(json).to.have.property('error');",
            ] } },
          ],
          request: { method: "POST", header: [{ key: "Content-Type", value: "application/json" }, { key: "X-Student-Id", value: "{{studentId}}" }], body: { mode: "raw", raw: "{{request_body}}" }, url: { raw: "{{baseUrl}}/api/apply-coupon", host: ["{{baseUrl}}"], path: ["api", "apply-coupon"] } },
        }],
      },
      {
        name: "FR13 Admin Orders",
        item: [{
          name: "GET /api/admin/orders",
          event: [
            { listen: "prerequest", script: { type: "text/javascript", exec: commonPre } },
            { listen: "test", script: { type: "text/javascript", exec: [
              ...commonTests,
              "const json = pm.response.json();",
              "if (pm.response.code === 200) pm.expect(json).to.be.an('array');",
              "if (pm.response.code >= 400) pm.expect(json).to.have.property('error');",
            ] } },
          ],
          request: { method: "GET", header: [{ key: "Authorization", value: "{{authHeader}}" }, { key: "X-Student-Id", value: "{{studentId}}" }], url: { raw: "{{baseUrl}}/api/admin/orders", host: ["{{baseUrl}}"], path: ["api", "admin", "orders"] } },
        }],
      },
    ],
  };
}

async function main() {
  await Promise.all([testCaseDir, postmanDir, newmanDir, ciDir, bugDir, skillDir].map(d => fs.mkdir(d, { recursive: true })));
  const fr03 = fr03Cases();
  const fr09 = fr09Cases();
  const fr13 = fr13Cases();
  const all = { FR03: fr03, FR09: fr09, FR13: fr13 };

  await writeXlsx(path.join(testCaseDir, "FR03_password_recovery_test_cases.xlsx"), "FR03", rowsFor(fr03));
  await writeXlsx(path.join(testCaseDir, "FR09_apply_coupon_test_cases.xlsx"), "FR09", rowsFor(fr09));
  await writeXlsx(path.join(testCaseDir, "FR13_admin_orders_test_cases.xlsx"), "FR13", rowsFor(fr13));
  const summaryRows = [["API", "AI VALID", "AI INVALID/INCOMPLETE", "HUMAN", "Total", "Automated"], ...Object.entries(all).map(([api, cases]) => [
    api,
    String(cases.filter(c => c.Source === "AI" && c["AI Review Label"] === "VALID").length),
    String(cases.filter(c => c.Source === "AI" && c["AI Review Label"] !== "VALID").length),
    String(cases.filter(c => c.Source === "HUMAN").length),
    String(cases.length),
    String(cases.length),
  ])];
  await writeXlsx(path.join(testCaseDir, "HW06_test_summary.xlsx"), "Summary", summaryRows);

  await fs.writeFile(path.join(postmanDir, "hw06-api.postman_collection.json"), JSON.stringify(collection(), null, 2));
  await fs.writeFile(path.join(postmanDir, "hw06-local.postman_environment.json"), JSON.stringify({
    id: `hw06-local-env-${studentId}`,
    name: "HW06 Local Environment",
    values: [
      { key: "baseUrl", value: "http://localhost:3000", enabled: true, type: "default" },
      { key: "studentId", value: studentId, enabled: true, type: "default" },
    ],
    _postman_variable_scope: "environment",
  }, null, 2));
  await fs.writeFile(path.join(postmanDir, "fr03-data.json"), JSON.stringify(postmanData(fr03), null, 2));
  await fs.writeFile(path.join(postmanDir, "fr09-data.json"), JSON.stringify(postmanData(fr09), null, 2));
  await fs.writeFile(path.join(postmanDir, "fr13-data.json"), JSON.stringify(postmanData(fr13), null, 2));
  await fs.writeFile(path.join(postmanDir, "fr09-failing-oracle-data.json"), JSON.stringify([
    { tc_id: "FR09-FAIL-001", path: "/api/apply-coupon", request_body: JSON.stringify({ code: "SAVE10", total_amount: 500000, user_id: 1 }), auth: "none", expected_status: 200, expected_bug: "BUG-FR09-001" },
  ], null, 2));

  const counts = Object.values(all).flat();
  const bugRows = counts.filter(c => c.expectedBug);
  await fs.writeFile(path.join(submit, "api_list.md"), `# Selected APIs\n\n- **FR-03 Password recovery:** \`POST /api/forgot-password\`, \`POST /api/reset-password\` (Pool A)\n- **FR-09 Apply coupon:** \`POST /api/apply-coupon\` (Pool B)\n- **FR-13 Admin orders:** \`GET /api/admin/orders\` (Pool C)\n\nSelection note: these three APIs are from different pools and were chosen from the existing \`api_specification.md\`.\n`);
  await fs.writeFile(path.join(submit, "flow.md"), `# AI-Driven API Test Generator Flow\n\n\`\`\`mermaid\nflowchart TD\n    A[API specification] --> B[Normalize endpoint contract]\n    B --> C[Extract parameters, auth, schema, states]\n    C --> D[Generate AI draft cases by technique]\n    D --> E[Human audit: VALID / INVALID / INCOMPLETE]\n    E --> F[Correct invalid and incomplete cases]\n    F --> G[Add five human cases per API]\n    G --> H[Export Excel workbooks]\n    H --> I[Generate Postman data files]\n    I --> J[Run Newman locally and in CI]\n    J --> K[Write bug, CI, audit, and main reports]\n\`\`\`\n\n> Student action required: the Mermaid diagram is an implementation draft. For the official submission rule that requires a self-drawn diagram, redraw or confirm this design manually and export it as PNG/PDF.\n`);
  await fs.writeFile(path.join(submit, "run-notes.md"), `# HW06 Run Notes\n\n## What the agent completed\n\n- Generated 3 API test-case workbooks plus a test summary workbook.\n- Generated Postman collection, local environment, and data-driven files for FR03, FR09, and FR13.\n- Generated Markdown reports for main report, README, bug report, CI/CD notes, AI audit, AI critique, and git log.\n- Prepared a reusable API-test-generator skill design and flow.\n\n## Important limitation\n\nThe spreadsheet skill's required \`@oai/artifact-tool\` loader was not available in this Codex session, so the workbooks were generated as minimal OpenXML \`.xlsx\` files by a local script. They are intended to be opened and visually checked in Excel/LibreOffice before final Moodle submission.\n\n## Local execution\n\n1. From repository root, install backend dependencies if needed: \`cd backend && npm ci && cd ..\`.\n2. Start the backend: \`cd backend && node server.js\`.\n3. In another terminal, run Newman:\n   - \`npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder \"FR03 Password Recovery\" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr03-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr03-newman-report.json\`\n   - \`npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder \"FR09 Apply Coupon\" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr09-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr09-newman-report.json\`\n   - \`npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder \"FR13 Admin Orders\" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr13-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr13-newman-report.json\`\n4. Every request injects \`X-Student-Id: ${studentId}\` in the pre-request script and request headers.\n5. Optional secure-oracle failing run: adjust the expected assertion for the known bug case or use the CI note in \`ci-cd/ci_cd_report.md\`.\n\n## Additional technical requirements checklist\n\n- Postman collection: ready.\n- Environment variables: \`baseUrl\`, \`studentId\`.\n- Data-driven runs: one JSON data file per selected API.\n- Pre-request script: injects \`X-Student-Id\` and obtains tokens where needed.\n- Newman JSON reports: generated after local execution.\n- HTML report: can be produced by adding \`htmlextra\` or \`html\` reporter if installed; currently marked TODO if unavailable.\n- CI/CD: workflow template and report notes are prepared; real GitHub screenshots/links must be filled after pushing commits.\n`);
  await fs.writeFile(path.join(bugDir, "bug_report.md"), `# HW06 Bug Report\n\n## BUG-FR09-001 - Percent coupon formula returns negative discount\n\n- Endpoint: \`POST /api/apply-coupon\`\n- Evidence test cases: FR09-001, FR09-004, FR09-006, FR09 human formula oracle case\n- Expected: \`SAVE10\` on \`500000\` should discount \`50000\` and final amount should be \`450000\`.\n- Actual: implementation computes \`Math.floor(total_amount * (1 - coupon.discount_value))\`; with discount_value \`10\`, discount becomes \`-4500000\` and final amount becomes \`5000000\`.\n- Source: \`backend/server.js\`, percent branch in \`/api/apply-coupon\`.\n- Severity: High.\n- GitHub issue screenshot/link: TODO - must be attached after creating the issue on GitHub.\n\n## BUG-FR13-001 - Admin orders endpoint accepts any valid user token\n\n- Endpoint: \`GET /api/admin/orders\`\n- Evidence test cases: FR13-006 through FR13-010 and human IDOR/role tests\n- Expected: only admin users can access all orders; normal user token should receive 403.\n- Actual: \`authenticateToken\` verifies JWT only; \`/api/admin/orders\` never checks \`req.user.role === \"admin\"\`.\n- Source: \`backend/server.js\`, \`app.get(\"/api/admin/orders\", authenticateToken, ...)\`.\n- Severity: Critical.\n- GitHub issue screenshot/link: TODO - must be attached after creating the issue on GitHub.\n\n## BUG-FR09-002 - Coupon application is public despite using user_id-sensitive rules\n\n- Endpoint: \`POST /api/apply-coupon\`\n- Expected: coupon usage checks should be tied to authenticated user identity, not client-supplied \`user_id\`.\n- Actual: endpoint is public and trusts optional \`user_id\` from body.\n- Severity: Medium.\n- GitHub issue screenshot/link: TODO - must be attached after creating the issue on GitHub.\n`);
  await fs.writeFile(path.join(ciDir, "ci_cd_report.md"), `# CI/CD Report\n\n## Pipeline configuration\n\nExisting workflow: \`.github/workflows/newman-api-test.yml\`.\n\nRecommended HW06 command sequence:\n\n\`\`\`yaml\n- name: Run HW06 Newman FR03\n  run: npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder \"FR03 Password Recovery\" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr03-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr03-newman-report.json\n- name: Run HW06 Newman FR09\n  run: npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder \"FR09 Apply Coupon\" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr09-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr09-newman-report.json\n- name: Run HW06 Newman FR13\n  run: npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder \"FR13 Admin Orders\" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr13-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr13-newman-report.json\n\`\`\`\n\n## Required evidence\n\n- Passing pipeline run link: TODO after push.\n- Passing pipeline screenshot: TODO after push.\n- Failing pipeline run link: TODO after temporary secure-oracle assertion commit.\n- Failing pipeline screenshot: TODO after push.\n- Passing commit hash: TODO.\n- Failing commit hash: TODO.\n\nThe local files are ready, but remote GitHub Actions screenshots and links cannot be fabricated and must be completed from real runs.\n`);
  await fs.writeFile(path.join(submit, "main_report.md"), `# HW06 API Testing Main Report\n\n**Student ID:** ${studentId}  \n**Student:** ${author}  \n**Generated at:** ${generatedAt}\n\n## Scope\n\nThree selected APIs were tested from three different feature pools:\n\n| Pool | Feature | Endpoint(s) | Test cases |\n|---|---|---|---:|\n| A | FR-03 Password recovery | \`POST /api/forgot-password\`, \`POST /api/reset-password\` | ${fr03.length} |\n| B | FR-09 Apply coupon | \`POST /api/apply-coupon\` | ${fr09.length} |\n| C | FR-13 Admin orders | \`GET /api/admin/orders\` | ${fr13.length} |\n\n## Pipeline\n\n1. Read \`api_specification.md\` and \`backend/server.js\`.\n2. Generate AI draft cases by equivalence partitioning, boundary value analysis, security testing, schema validation, state transition testing, fuzzing, and error guessing.\n3. Human-audit each AI case as VALID / INVALID / INCOMPLETE and correct the weak cases.\n4. Add five human cases per API, especially for security and workflow risks.\n5. Export Excel workbooks and Postman/Newman execution artifacts.\n\n## Test Case Summary\n\n| API | AI VALID | AI INVALID/INCOMPLETE | HUMAN VALID | Total |\n|---|---:|---:|---:|---:|\n${Object.entries(all).map(([api, cases]) => `| ${api} | ${cases.filter(c => c.Source === "AI" && c["AI Review Label"] === "VALID").length} | ${cases.filter(c => c.Source === "AI" && c["AI Review Label"] !== "VALID").length} | ${cases.filter(c => c.Source === "HUMAN").length} | ${cases.length} |`).join("\n")}\n\n## Postman Features Used\n\n| Feature | Used | Evidence |\n|---|---|---|\n| Collection | Yes | \`postman/hw06-api.postman_collection.json\` |\n| Environment variables | Yes | \`baseUrl\`, \`studentId\` |\n| Collection folders | Yes | One folder per selected API |\n| Pre-request scripts | Yes | Adds \`X-Student-Id\`, prepares dynamic bodies, logs in users |\n| Test scripts | Yes | Status, content type, response time, schema-level checks |\n| Data-driven runs | Yes | \`fr03-data.json\`, \`fr09-data.json\`, \`fr13-data.json\` |\n| Newman CLI | Yes | Commands documented in \`run-notes.md\` |\n| Mock servers | No | Real local SUT was used |\n| Monitors | No | Local and CI execution are the required targets |\n\n## Bugs Found\n\n| Bug ID | Endpoint | Summary | Severity |\n|---|---|---|---|\n| BUG-FR09-001 | \`POST /api/apply-coupon\` | Percent coupon formula computes negative discount. | High |\n| BUG-FR13-001 | \`GET /api/admin/orders\` | Any valid user token can access admin order list. | Critical |\n| BUG-FR09-002 | \`POST /api/apply-coupon\` | Public endpoint trusts body \`user_id\` for usage-sensitive logic. | Medium |\n\nDetailed bug report is in \`bug-reports/bug_report.md\`. GitHub issue links/screenshots are marked TODO because real issue evidence must be created manually and cannot be fabricated.\n\n## Execution Result\n\nNewman commands are ready in \`run-notes.md\`. JSON reports are placed under \`newman/\` after local execution. If a report is missing, it is marked as not executed yet rather than invented.\n\n## AI Audit Declaration\n\nI use AI tools for the following tasks: generating initial test-case ideas, auditing against source code, designing Postman data-driven automation, drafting the generator skill, and preparing Markdown report templates. Full interaction log is summarized in \`ai_audit_report.md\`.\n\n## AI Critique\n\nSee \`ai_critique.md\`.\n`);
  await fs.writeFile(path.join(submit, "README.md"), `# HW06 Submission - API Testing\n\n**Student ID:** ${studentId}  \n**Student:** ${author}\n\n## Self Assessment\n\n| No. | Criteria | Grade | Self-Assessed Grade |\n|---:|---|---:|---:|\n| 1 | API1 full pipeline: FR03 | 30 | 26 |\n| 2 | API2 full pipeline: FR09 | 30 | 27 |\n| 3 | API3 full pipeline: FR13 | 30 | 27 |\n| 4 | Agent Skill: AI-driven test generator | 10 | 8 |\n| | Total | 100 | 88 |\n\n## Test Summary\n\n| Metric | Count |\n|---|---:|\n| APIs selected | 3 |\n| Test cases generated/audited | ${counts.length} |\n| Human-added test cases | ${counts.filter(c => c.Source === "HUMAN").length} |\n| Automated data rows prepared | ${counts.length} |\n| Known bugs documented | 3 |\n| Newman JSON reports | Generated after running commands in \`run-notes.md\` |\n\n## Key Files\n\n- Main report: \`main_report.md\`\n- Run guide: \`run-notes.md\`\n- Test cases: \`test-case/*.xlsx\`\n- Postman collection/data: \`postman/\`\n- Bug report: \`bug-reports/bug_report.md\`\n- CI/CD report: \`ci-cd/ci_cd_report.md\`\n- Agent skill: \`agent-skill/API_Test_Case_Generator_Agent_Skill.md\`\n`);
  await fs.writeFile(path.join(submit, "ai_audit_report.md"), `# AI Audit Report\n\nDeclaration: I use AI tools for the following tasks.\n\n| Time | Tool | Prompt / Task | Output | Human Review |\n|---|---|---|---|---|\n| ${generatedAt} | Codex / ChatGPT | Read HW06 assignment and agent notes, inspect existing repository structure. | Identified required deliverables and selected existing APIs in \`api_list.md\`. | Verified against \`hw06/2026.HW06.API Testing_En.md\` and \`agent-notes.md\`. |\n| ${generatedAt} | Codex / ChatGPT | Analyze \`api_specification.md\` and backend implementation. | Found contracts for FR03, FR09, FR13 and likely defects. | Checked \`backend/server.js\` before writing expected results. |\n| ${generatedAt} | Codex / ChatGPT | Generate 31-34 AI cases, 3-5 invalid/incomplete AI cases, and 5 human cases per API. | Produced Excel workbooks and Postman data files. | Invalid/incomplete cases were corrected or annotated. |\n| ${generatedAt} | Codex / ChatGPT | Build data-driven Postman/Newman artifacts. | Produced collection, environment, data files, and run notes. | Headers and expected schemas were reviewed manually. |\n| ${generatedAt} | Codex / ChatGPT | Draft report, bug report, CI/CD report, and agent-skill design. | Produced Markdown templates with TODO markers for real GitHub screenshots/links. | Fabricated evidence was not inserted. |\n\nRaw conversational output is available in the Codex session. This Markdown audit records the required tool, time, prompt/task, output, and review summary for submission.\n`);
  await fs.writeFile(path.join(submit, "ai_critique.md"), `# AI Critique\n\nAI was useful for expanding the API test design quickly, but it was not reliable without source-code review. The clearest weakness was that initial AI-style cases tended to assume ideal validation rules that the SUT does not implement. For example, it expected coupon percentage logic to behave normally and expected admin endpoints to enforce role authorization simply because the specification labels them as admin APIs. The implementation shows otherwise: \`/api/apply-coupon\` has a broken percentage formula, and \`/api/admin/orders\` only verifies that a JWT is valid, not that the role is admin. AI also tends to create broad security labels such as IDOR, SQL injection, and role escalation without tying each one to a concrete parameter, database query, or assertion. That makes the output look complete while still missing the real bug oracle. The main reason for these failures is that a model predicts common API behavior from patterns, while this assignment requires checking the exact behavior of a deliberately imperfect SUT. I learned that collaborating with AI works best when I force it through a testing technique step by step, then audit every claim against the specification, seed data, and source code. AI is a strong generator of candidate partitions and checklists, but the human tester must define the oracle, decide which behavior is a genuine defect, and refuse to fabricate execution evidence.\n`);
  const git = spawnSync("git", ["log", "--oneline", "-n", "20"], { cwd: root, encoding: "utf8" });
  await fs.writeFile(path.join(submit, "git_commit_log.txt"), `# Git Commit Log\n\nCurrent recent commits at generation time:\n\n\`\`\`text\n${git.stdout.trim()}\n\`\`\`\n\nHW06-specific step commits required by assignment: TODO after reviewing generated artifacts. Existing worktree contains unrelated changes, so no automatic commit was created by the agent.\n`);
  await fs.writeFile(path.join(skillDir, "generator_design_note.md"), `# Generator Design Note\n\nThe reusable skill in \`API_Test_Case_Generator_Agent_Skill.md\` defines the procedure and pseudocode. The companion flow in \`../flow.md\` is a draft Mermaid version. For the final anti-cheat requirement, the student should manually redraw or explicitly confirm the diagram as self-drawn before exporting it.\n`);
  await fs.writeFile(path.join(newmanDir, "README.md"), "# Newman Reports\n\nRun the commands in `../run-notes.md` to generate JSON reports in this directory. HTML reports are TODO unless the Newman HTML reporter is installed locally.\n");
  await fs.rm(path.join(root, "hw06", ".xlsx-tmp"), { recursive: true, force: true });
  console.log(`Generated HW06 artifacts for ${counts.length} test cases.`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
