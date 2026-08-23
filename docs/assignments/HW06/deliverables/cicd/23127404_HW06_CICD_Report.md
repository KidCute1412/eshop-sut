# HW06 CI/CD report

The GitHub Actions workflow runs the three Newman collections against the local backend on `ubuntu-latest` and uploads reporter output. Its implementation is version-controlled at `cicd/workflows/api-tests.yml`.

## Verified GitHub Actions evidence

- All-pass evidence: commit [`d07a9b1`](https://github.com/KidCute1412/eshop-sut/commit/d07a9b1), [GitHub Actions run](https://github.com/KidCute1412/eshop-sut/actions/runs/32665200965/job/97257113623), and authentic capture [ci-pass.png](screenshots/ci-pass.png). The `Execute isolated evidence Newman suite` step completed successfully.
- Intentional-failure evidence: commit [`aa32d91`](https://github.com/KidCute1412/eshop-sut/commit/aa32d91), [GitHub Actions run](https://github.com/KidCute1412/eshop-sut/actions/runs/32665781240/job/97258816558), and authentic capture [ci-fail.png](screenshots/ci-fail.png). It deliberately set `TC-LOGIN-01` to expect HTTP `999`; the API returned `200`, so the assertion failed as intended.
- The test data is restored to its correct `200` expectation in the local restoration commit. Push that commit, wait for its green workflow, and replace `ci-pass.png` with the resulting final-green capture before submission. The existing `d07a9b1` capture proves the workflow itself can pass, but predates this red run.
