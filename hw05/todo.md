# HW05 TODO + Execution Runbook

Last reviewed: 2026-08-16.

This file tracks what is already completed and gives the exact commands to finish the real performance-test evidence. Run commands from the repository root unless a step says otherwise.

Repository root:

```powershell
D:\daihoc\HK3-2026\26-KIEM-THU\hw\hw2\group\eshop-sut
```

## 1. Completed In Workspace

- [x] Read and reviewed `hw05/2026.HW05.Performance Testing_En.md`.
- [x] Audited current `hw05/submit` artifacts.
- [x] Renamed JMeter plans from sample ID `25127001` to `23127296`.
- [x] Updated plan date to `20260815`.
- [x] Verified JMX endpoint coverage: auth-heavy, read-heavy, and transactional.
- [x] Verified three different JMeter listener/report views.
- [x] Verified JWT extraction and `Authorization: Bearer ${auth_token}` usage.
- [x] Added `hw05/submit/task1/seed_performance_data.js`.
- [x] Added `hw05/submit/task1/runbook.md`.
- [x] Added `hw05/submit/task2/analyze_jtl.mjs`.
- [x] Rewrote README, Task 1, Task 2, Task 3, AI audit, and AI critique files.
- [x] Added `hw05/submit/git_commit_log.txt`.

## 2. Tool Checks

Check Node.js:

```powershell
node --version
npm --version
```

Check JMeter:

```powershell
jmeter --version
```

If `jmeter` is not recognized, add JMeter `bin` to PATH for this PowerShell session. Adjust the folder if your JMeter path is different:

```powershell
$env:PATH = "C:\apache-jmeter-5.6.3\bin;$env:PATH"
jmeter --version
```

## 3. Start Backend

Open terminal 1:

```powershell
cd D:\daihoc\HK3-2026\26-KIEM-THU\hw\hw2\group\eshop-sut\backend
npm install
node server.js
```

Keep this terminal open. Backend URL:

```text
http://localhost:3000
```

Health check in terminal 2:

```powershell
Invoke-RestMethod http://localhost:3000/api/products
```

## 4. Seed Performance Data

Run from repo root:

```powershell
cd D:\daihoc\HK3-2026\26-KIEM-THU\hw\hw2\group\eshop-sut
node hw05\submit\task1\seed_performance_data.js
```

Expected result:

```text
Seeded 10 performance users and 5 products into ...\backend\database.sqlite
```

Verify login:

```powershell
$body = @{
  email = "user_load_001@test.com"
  password = "Password123!"
} | ConvertTo-Json

Invoke-RestMethod `
  -Uri http://localhost:3000/api/login `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```

## 5. Run JMeter Tests

Move to the JMeter plan folder:

```powershell
cd D:\daihoc\HK3-2026\26-KIEM-THU\hw\hw2\group\eshop-sut\hw05\submit\task1
```

If rerunning, remove old JTL/report outputs:

```powershell
Remove-Item -LiteralPath .\23127296_Load_20260815.jtl -ErrorAction SilentlyContinue
Remove-Item -LiteralPath .\23127296_Stress_20260815.jtl -ErrorAction SilentlyContinue
Remove-Item -LiteralPath .\23127296_Spike_20260815.jtl -ErrorAction SilentlyContinue
Remove-Item -LiteralPath .\23127296_Load_20260815_html -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath .\23127296_Stress_20260815_html -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath .\23127296_Spike_20260815_html -Recurse -Force -ErrorAction SilentlyContinue
```

Run Load test:

```powershell
jmeter -n `
  -t .\23127296_Load_20260815.jmx `
  -l .\23127296_Load_20260815.jtl `
  -e `
  -o .\23127296_Load_20260815_html
```

Run Stress test:

```powershell
node .\seed_performance_data.js

jmeter -n `
  -t .\23127296_Stress_20260815.jmx `
  -l .\23127296_Stress_20260815.jtl `
  -e `
  -o .\23127296_Stress_20260815_html
```

Run Spike test:

```powershell
node .\seed_performance_data.js

jmeter -n `
  -t .\23127296_Spike_20260815.jmx `
  -l .\23127296_Spike_20260815.jtl `
  -e `
  -o .\23127296_Spike_20260815_html
```

Expected files:

- [ ] `hw05/submit/task1/23127296_Load_20260815.jtl`
- [ ] `hw05/submit/task1/23127296_Stress_20260815.jtl`
- [ ] `hw05/submit/task1/23127296_Spike_20260815.jtl`
- [ ] `hw05/submit/task1/23127296_Load_20260815_html/index.html`
- [ ] `hw05/submit/task1/23127296_Stress_20260815_html/index.html`
- [ ] `hw05/submit/task1/23127296_Spike_20260815_html/index.html`

## 6. Capture Screenshots

Create screenshot folder:

```powershell
New-Item -ItemType Directory -Force -Path D:\daihoc\HK3-2026\26-KIEM-THU\hw\hw2\group\eshop-sut\hw05\submit\screenshots
```

Capture manually while each test is running:

- [ ] `screenshots/load_jmeter_task_manager.png`
- [ ] `screenshots/stress_jmeter_task_manager.png`
- [ ] `screenshots/spike_jmeter_task_manager.png`
- [ ] `screenshots/hardware_spec.png`
- [ ] `screenshots/github_issues.png` if issues are filed

Suggested hardware-spec command:

```powershell
Get-ComputerInfo |
  Select-Object CsName,OsName,OsVersion,CsProcessor,CsNumberOfLogicalProcessors,CsTotalPhysicalMemory |
  Format-List
```

Alternative:

```powershell
dxdiag
```

## 7. Analyze JTL Logs

Run after all `.jtl` files exist:

```powershell
cd D:\daihoc\HK3-2026\26-KIEM-THU\hw\hw2\group\eshop-sut

node hw05\submit\task2\analyze_jtl.mjs `
  hw05\submit\task1\23127296_Load_20260815.jtl `
  hw05\submit\task1\23127296_Stress_20260815.jtl `
  hw05\submit\task1\23127296_Spike_20260815.jtl
```

Copy the output numbers into:

- [ ] `hw05/submit/README.md`
- [ ] `hw05/submit/task1/test_plan_review_notes.md`
- [ ] `hw05/submit/task2/ai_analysis_and_review.md`
- [ ] `hw05/submit/task3/continuous_testing_proposal.md`

## 8. Endurance / Soak Threshold

The Load plan already runs for 600 seconds, so it can be used as a short soak run. If a separate soak file is preferred:

```powershell
cd D:\daihoc\HK3-2026\26-KIEM-THU\hw\hw2\group\eshop-sut\hw05\submit\task1
node .\seed_performance_data.js

jmeter -n `
  -t .\23127296_Load_20260815.jmx `
  -l .\23127296_Soak_20260815.jtl `
  -e `
  -o .\23127296_Soak_20260815_html
```

Analyze soak log:

```powershell
cd D:\daihoc\HK3-2026\26-KIEM-THU\hw\hw2\group\eshop-sut
node hw05\submit\task2\analyze_jtl.mjs hw05\submit\task1\23127296_Soak_20260815.jtl
```

Record:

- [ ] Maximum stable RPS
- [ ] Average response time
- [ ] p95 response time
- [ ] p99 response time
- [ ] Error rate
- [ ] Peak CPU usage
- [ ] Peak memory usage

## 9. AI Analysis Step

After `.jtl` files exist, prompt ChatGPT/Codex/Claude/Gemini with the prompt in:

```text
hw05/submit/task2/ai_analysis_and_review.md
```

Then fill:

- [ ] AI output summary
- [ ] At least 3 AI misinterpretations
- [ ] Correct values from raw `.jtl`
- [ ] Feasibility review of optimization recommendations
- [ ] AI-suggested vs validated threshold table

## 10. GitHub Issues

If a real bug or performance issue appears, create an issue at:

```text
https://github.com/KidCute1412/eshop-sut/issues
```

Suggested issue title:

```text
HW05 Performance: High p95 latency on POST /api/checkout during Stress test
```

Attach:

- Screenshot of JMeter result
- Screenshot of Task Manager/resource usage
- Relevant `.jtl` summary values
- Steps to reproduce

## 11. Demo Video

Record at least 6 minutes with Vietnamese narration.

Required content:

- [ ] JMeter Load run and Task Manager in the same frame
- [ ] JMeter Stress run and Task Manager in the same frame
- [ ] JMeter Spike run and Task Manager in the same frame
- [ ] Brief explanation of endpoint workflow
- [ ] Brief explanation of p95/error rate/throughput result
- [ ] Brief explanation of hardware threshold

Upload as unlisted YouTube video. Add the link to:

- [ ] `hw05/submit/README.md`
- [ ] `hw05/submit/task1/test_plan_review_notes.md`

## 12. Update Git Log

After all real evidence and report edits are done:

```powershell
cd D:\daihoc\HK3-2026\26-KIEM-THU\hw\hw2\group\eshop-sut
git status --short
git log --oneline --decorate > hw05\submit\git_commit_log.txt
```

If PowerShell writes an empty file because of environment issues, run:

```powershell
git log --oneline --decorate
```

Then paste the output into:

```text
hw05/submit/git_commit_log.txt
```

## 13. Final Zip

Before zipping, verify:

```powershell
Test-Path hw05\submit\task1\23127296_Load_20260815.jtl
Test-Path hw05\submit\task1\23127296_Stress_20260815.jtl
Test-Path hw05\submit\task1\23127296_Spike_20260815.jtl
Test-Path hw05\submit\task1\23127296_Load_20260815_html\index.html
Test-Path hw05\submit\task1\23127296_Stress_20260815_html\index.html
Test-Path hw05\submit\task1\23127296_Spike_20260815_html\index.html
Test-Path hw05\submit\screenshots\hardware_spec.png
```

Create zip. Replace `090` with the final self-assessed grade:

```powershell
Compress-Archive `
  -Path hw05\submit\* `
  -DestinationPath 23127296_HW05_AI_Performance_090.zip `
  -Force
```

## 14. Information Needed From Student

- [ ] Confirm full name: currently inferred as `Nguyen Thanh Luan`.
- [ ] Provide final self-assessed grade.
- [ ] Provide YouTube demo link and duration.
- [ ] Provide real `.jtl` logs, HTML reports, and screenshots after running JMeter.
- [ ] Confirm whether GitHub Issues were filed and provide links.
