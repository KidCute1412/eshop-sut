# HW05 Performance Execution Runbook

Use this runbook for the real execution evidence. The current workspace does not have `jmeter` on PATH, so these commands must be run after Apache JMeter is installed or after adding `JMETER_HOME/bin` to PATH.

## 1. Prepare SUT

From the repository root:

```powershell
cd backend
node server.js
```

Keep the backend running on `http://localhost:3000`.

In another terminal, seed the CSV users/products used by the JMeter plans:

```powershell
node hw05\submit\task1\seed_performance_data.js
```

This script also resets `login_attempts` and `locked_until` for `user_load_%@test.com`.

## 2. Run JMeter Plans

From `hw05\submit\task1`:

```powershell
jmeter -n -t 23127296_Load_20260815.jmx -l 23127296_Load_20260815.jtl -e -o 23127296_Load_20260815_html
jmeter -n -t 23127296_Stress_20260815.jmx -l 23127296_Stress_20260815.jtl -e -o 23127296_Stress_20260815_html
jmeter -n -t 23127296_Spike_20260815.jmx -l 23127296_Spike_20260815.jtl -e -o 23127296_Spike_20260815_html
```

Run the seed script again between Stress and Spike if any login failures occur.

## 3. Capture Required Evidence

Capture these screenshots during each scenario:

- JMeter window or CLI run plus Task Manager in the same frame.
- Backend Node.js process resource usage.
- Hardware specs using `dxdiag` or PowerShell:

```powershell
Get-ComputerInfo | Select-Object CsName,OsName,OsVersion,CsProcessor,CsNumberOfLogicalProcessors,CsTotalPhysicalMemory | Format-List
```

Save evidence under `hw05\submit\screenshots`.

## 4. Endurance/Soak Run

Use the Load test plan as the short soak test by running it for 10 minutes. Record:

- Maximum stable RPS from the JMeter dashboard.
- Average, p95, and p99 response times.
- Error rate.
- Peak CPU and memory from Task Manager.

Only fill the threshold tables after reading values from the generated `.jtl` and screenshots.

## 5. Export Git Log

After completing real runs and documentation:

```powershell
git log --oneline --decorate > hw05\submit\git_commit_log.txt
```
