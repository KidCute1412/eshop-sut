# HW6 - CI/CD Report

## Pipeline Configuration

- Workflow file draft: ci/github-actions-api-tests.yml
- Tool: Newman
- Backend startup: npm install in backend, node database.js, mkdir reports/HW6/newman, node server.js in background, wait-on with 60s timeout
- Command: newman run reports/HW6/postman/HW06_FR01_FR07_FR17.postman_collection.json -e reports/HW6/postman/HW06_local.postman_environment.json --env-var studentId=<StudentID> --reporters cli,html --reporter-html-export reports/HW6/newman/report.html
- Artifact: Newman HTML report

## Passing Run

- Commit: TODO real commit hash
- Run link: TODO real GitHub Actions link
- Screenshot: TODO
- Summary: Pending real CI execution.

## Intentionally Failing Run

- Commit: TODO real commit hash
- Run link: TODO real GitHub Actions link
- Screenshot: TODO
- Failing test: TODO, create one temporary assertion mismatch for demonstration
- Why it failed intentionally: Required by HW6 to demonstrate CI failure reporting.

## Notes / Blockers

Real CI links cannot be fabricated. Push this repository to GitHub, enable Actions, then run both passing and intentionally failing commits.
