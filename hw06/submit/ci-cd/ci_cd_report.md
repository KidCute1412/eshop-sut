# CI/CD Report

## Pipeline configuration

Existing workflow: `.github/workflows/newman-api-test.yml`.

Recommended HW06 command sequence:

```yaml
- name: Run HW06 Newman FR03
  run: npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder "FR03 Password Recovery" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr03-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr03-newman-report.json
- name: Run HW06 Newman FR09
  run: npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder "FR09 Apply Coupon" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr09-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr09-newman-report.json
- name: Run HW06 Newman FR13
  run: npx -y newman run hw06/submit/postman/hw06-api.postman_collection.json --folder "FR13 Admin Orders" -e hw06/submit/postman/hw06-local.postman_environment.json -d hw06/submit/postman/fr13-data.json --reporters cli,json --reporter-json-export hw06/submit/newman/fr13-newman-report.json
```

## Required evidence

- Passing pipeline run link: TODO after push.
- Passing pipeline screenshot: TODO after push.
- Failing pipeline run link: TODO after temporary secure-oracle assertion commit.
- Failing pipeline screenshot: TODO after push.
- Passing commit hash: TODO.
- Failing commit hash: TODO.

The local files are ready, but remote GitHub Actions screenshots and links cannot be fabricated and must be completed from real runs.
