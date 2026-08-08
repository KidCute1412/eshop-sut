# AI Audit - FR-01 Account Registration (Prompt + Raw AI Output Only)

- AI Tool: Codex (GPT-5)
- Date: 2026-08-06 to 2026-08-07
- Feature: FR-01 Account registration
- Final reviewed artifacts: [test-cases.md](test-cases.md), [data/register-cases.json](data/register-cases.json), [tests/fr-01-register.spec.js](tests/fr-01-register.spec.js), [bug-report.md](bug-report.md)

## Interaction 1 - Generate FR-01 Data-Driven Playwright Automation

- AI Tool: Codex (GPT-5)
- Date: 2026-08-06

### Prompt 

```text
Complete HW04 Automation Testing for the EShop SUT.

First, read the repository, the HW04 assignment PDF, the HW02 selected-feature artifacts,
and the existing HW03 report structure. For FR-01 Account Registration, convert the selected
HW02 Domain Testing and Boundary Value Analysis cases into data-driven Playwright automation.

Store all test inputs and expected results in an external JSON data file. Create a Playwright
specification that can run on Chromium, Firefox, and WebKit, and keep the workflow auditable
through test-case documentation, an AI audit, AI gap analysis, bug reporting, and report references.

Do not fabricate execution results. When a real SUT defect is observed, preserve it as a failing
assertion and document the evidence clearly.
```

### AI Output 

```text
Created a Playwright workspace under reports/HW4 with:

- package.json
- playwright.config.js
- fixtures/hw4-test.js
- FR-01/data/register-cases.json
- FR-01/tests/fr-01-register.spec.js
- FR-01/test-cases.md
- FR-01/bug-report.md
- FR-01/ai-gap-analysis.md

Selected FR-01 cases:

- FR01-DT-001 Positive registration
- FR01-DT-002 Positive registration
- FR01-DT-003 Negative weak password
- FR01-DT-004 Negative password without uppercase
- FR01-DT-005 Negative password without digit
- FR01-DT-006 Negative documented special-character password
- FR01-DT-007 Edge minimum accepted current password
- FR01-DT-008 Negative missing name
- FR01-DT-009 Negative missing email
- FR01-DT-010 Negative missing password
- FR01-DT-011 Negative duplicate email
- FR01-DT-012 Edge long multi-word name

Generated external test data in FR-01/data/register-cases.json:

[
  {
    "id": "FR01-DT-001",
    "type": "Positive",
    "name": "Automation User Alpha",
    "emailPrefix": "fr01.alpha",
    "email": "",
    "password": "Aa1 aaaa",
    "expected": "success"
  },
  {
    "id": "FR01-DT-006",
    "type": "Negative",
    "name": "Documented Special Character User",
    "emailPrefix": "fr01.special",
    "email": "",
    "password": "Aa1!aaaa",
    "expected": "password_error"
  },
  {
    "id": "FR01-DT-011",
    "type": "Negative",
    "name": "Duplicate Email User",
    "emailPrefix": "fr01.duplicate",
    "email": "",
    "password": "Aa1 aaaa",
    "expected": "duplicate_error"
  }
]

Generated core Playwright loop in FR-01/tests/fr-01-register.spec.js:

const {
  test,
  expect,
  uniqueEmail,
  fillCustomerRegisterForm
} = require("../../fixtures/hw4-test");
const cases = require("../data/register-cases.json");

test.describe("FR-01 Account registration", () => {
  for (const tc of cases) {
    test(`${tc.id} ${tc.type} registration`, async ({ page, request }) => {
      const data = { ...tc };
      if (data.email === "") {
        data.email = uniqueEmail(data.emailPrefix);
      }

      if (data.expected === "duplicate_error") {
        await request.post("http://localhost:3000/api/register", {
          data: {
            name: "Existing Automation User",
            email: data.email,
            password: data.password
          }
        });
      }

      await page.goto("/register");
      await fillCustomerRegisterForm(page, data);

      const submitResponse =
        data.expected === "success" || data.expected === "duplicate_error"
          ? page
              .waitForResponse(
                (r) =>
                  r.url().includes("/api/register") &&
                  r.request().method() === "POST"
              )
              .catch(() => null)
          : Promise.resolve(null);

      await page.locator("form button[type='submit']").click();
      const response = await submitResponse;

      if (data.expected === "success") {
        expect(response && response.ok()).toBeTruthy();
        await expect(page).toHaveURL(/\/login$/);
      }

      if (data.expected === "password_error") {
        await expect(page.locator("[class*='bg-red']").first()).toBeVisible();
        await expect(page).toHaveURL(/\/register$/);
      }

      if (data.expected === "duplicate_error") {
        expect(response && response.status()).toBe(500);
        await expect(page.locator("[class*='bg-red']").first()).toBeVisible();
      }

      if (data.expected && data.expected.startsWith("native_required")) {
        await expect(page).toHaveURL(/\/register$/);
        const invalidInputs = await page.locator("form input").evaluateAll((inputs) =>
          inputs.filter((input) => !input.checkValidity()).length
        );
        expect(invalidInputs).toBeGreaterThan(0);
      }
    });
  }
});

Initial FR-01 multi-browser result:

- 36 tests executed
- 33 passed
- 3 failed
- Failing case: FR01-DT-011 duplicate email on Chromium, Firefox, and WebKit
- Observed failure: Expected HTTP 500, received HTTP 200
- Recorded bug: duplicate email registration is accepted
```

## Interaction 2 - Re-check Password Special Characters and Long Password

- AI Tool: Codex (GPT-5)
- Date: 2026-08-07

### Prompt 

```text
Re-check FR-01 Account Registration password validation on the registration page.

According to the project requirements, a strong password should be accepted when it has at least
8 characters, including uppercase letters, lowercase letters, digits, and a documented special
character such as @ or !. Verify the UI behavior for passwords such as Aa1!aaaa and Aa1@aaaa,
because the registration page appears to reject them unless a whitespace character is used.

Also check whether a long valid password of approximately 20 characters, for example
Aa1!aaaaaaaaaaaaaaaa, is rejected by the registration page. Compare it against a 20-character
password that uses whitespace as the special character to determine whether the failure is caused
by length or by the special-character validation rule.

Update the data-driven test cases, bug report, and automation summary based only on real
Playwright execution evidence.
```

### AI Output

```text
Checked the FR-01 password oracle against README.md:

README.md says a strong password must have:

- at least 8 characters
- at least one uppercase letter
- at least one lowercase letter
- at least one digit
- at least one special character from @, $, !, %, *, ?, &

Corrected the data-driven oracle:

- FR01-DT-006 changed from expected password_error to expected success
- Added FR01-BVA-009 for password Aa1@aaaa
- Added FR01-BVA-010 for 20-character password Aa1!aaaaaaaaaaaaaaaa
- Added FR01-BVA-011 as control check for 20-character password with whitespace:
  Aa1 aaaaaaaaaaaaaaaa

Updated FR-01/data/register-cases.json:

{
  "id": "FR01-DT-006",
  "type": "Positive",
  "name": "Documented Special Character User",
  "emailPrefix": "fr01.special",
  "email": "",
  "password": "Aa1!aaaa",
  "expected": "success"
}

{
  "id": "FR01-BVA-009",
  "type": "Edge",
  "name": "At Special Character User",
  "emailPrefix": "fr01.at",
  "email": "",
  "password": "Aa1@aaaa",
  "expected": "success"
}

{
  "id": "FR01-BVA-010",
  "type": "Edge",
  "name": "Twenty Character Password User",
  "emailPrefix": "fr01.longpassword",
  "email": "",
  "password": "Aa1!aaaaaaaaaaaaaaaa",
  "expected": "success"
}

{
  "id": "FR01-BVA-011",
  "type": "Edge",
  "name": "Twenty Character Space Password User",
  "emailPrefix": "fr01.longspacepassword",
  "email": "",
  "password": "Aa1 aaaaaaaaaaaaaaaa",
  "expected": "success"
}

Ran focused Chromium check for the three requirement-valid passwords:

Command:
$env:HW4_SKIP_WEBSERVER='1';
$env:WEB_BASE_URL='http://localhost:5176';
npx playwright test FR-01/tests/fr-01-register.spec.js --project=chromium --grep "FR01-DT-006|FR01-BVA-009|FR01-BVA-010" --timeout=30000

Raw result:

Running 3 tests using 1 worker

  x  1 [chromium] › FR-01 Account registration › FR01-DT-006 Positive registration
  x  2 [chromium] › FR-01 Account registration › FR01-BVA-009 Edge registration
  x  3 [chromium] › FR-01 Account registration › FR01-BVA-010 Edge registration

Failure pattern:

Error: expect(received).toBeTruthy()
Received: null

Meaning:

- No POST /api/register response was observed.
- The UI blocked submission client-side.
- The documented special-character passwords using ! and @ were rejected before the API call.

Ran control check for long password with whitespace:

Command:
$env:HW4_SKIP_WEBSERVER='1';
$env:WEB_BASE_URL='http://localhost:5176';
npx playwright test FR-01/tests/fr-01-register.spec.js --project=chromium --grep "FR01-BVA-011" --timeout=30000

Raw result:

Running 1 test using 1 worker

  ok 1 [chromium] › FR-01 Account registration › FR01-BVA-011 Edge registration

Conclusion:

- Password length 20 is not the real reason for the failure.
- A 20-character password with whitespace passes.
- A 20-character password with documented special character ! fails.
- The defect is the registration UI regex requiring whitespace instead of accepting README.md's
  documented special-character set.

Ran updated full suite:

Command:
$env:HW4_SKIP_WEBSERVER='1';
$env:WEB_BASE_URL='http://localhost:5176';
$env:ADMIN_BASE_URL='http://localhost:5177';
node scripts\run-with-report-stamp.js --timeout=30000

Raw result:

Running 117 tests using 1 worker

  12 failed
  105 passed

Failed FR-01 cases on Chromium, Firefox, and WebKit:

- FR01-DT-006: password Aa1!aaaa is rejected
- FR01-DT-011: duplicate email is accepted
- FR01-BVA-009: password Aa1@aaaa is rejected
- FR01-BVA-010: 20-character password Aa1!aaaaaaaaaaaaaaaa is rejected

Recorded new bug:

BUG-HW04-FR01-002 - Registration rejects documented special characters in strong passwords

Updated affected reports:

- FR-01/test-cases.md
- FR-01/bug-report.md
- FR-01/ai-gap-analysis.md
- automation-report.md
- README.md
- main-report.md
- ai-critique.md
```
