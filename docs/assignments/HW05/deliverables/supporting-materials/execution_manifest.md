# Execution manifest

| Run | Start (UTC+07) | Result | JTL | HTML report |
| --- | --- | --- | --- | --- |
| Load preflight (invalid CSV header) | 2026-08-17 00:42:57 | 75/200 errors; excluded | `../raw-results/preflight/23127404_Load_20260817_header-data-failure.jtl` | `../html-reports/preflight/load_header-data-failure/` |
| Load | 2026-08-17 00:44:24 | 200/200 successful | `../raw-results/load/23127404_Load_20260817.jtl` | `../html-reports/load/` |
| Stress | 2026-08-17 00:45:38 | 800/800 successful | `../raw-results/stress/23127404_Stress_20260817.jtl` | `../html-reports/stress/` |
| Spike | 2026-08-17 00:46:55 | 500/500 successful | `../raw-results/spike/23127404_Spike_20260817.jtl` | `../html-reports/spike/` |
| Endurance | 2026-08-17 00:49:36 | 4,400/4,400 successful; 10 m 41 s | `../raw-results/endurance/23127404_Endurance_20260817.jtl` | `../html-reports/endurance/` |
| Endurance (validated plan) | 2026-08-17 (local) | 4,400/4,400 successful; 632.403 s | `../raw-results/endurance/23127404_Endurance_VALIDATED_20260817.jtl` | `../html-reports/endurance-validated/` |
| Stepped endurance profile, 20 VU | 2026-08-17 (local) | 3,200/3,200 successful; 24.014 RPS; p95 10 ms | `../raw-results/threshold/020VU/020VU.jtl` | `../html-reports/threshold/020VU/` |
| Lockout verification | 2026-08-17 (local) | first invalid attempt: HTTP 401; second invalid attempt: HTTP 401; valid login after second invalid attempt: HTTP 403 | `../bugs/BUG-HW05-LOCKOUT-001.md` | Not applicable |

## Reproduction configuration

- Repository commit before HW05 artifact commits: `22e11214b254865292084d7a10c65e9bd8a8f1bf`.
- Local SUT command: `node server.js` from `backend/`; base URL: `http://localhost:3000`.
- Each final performance run used a fresh local backend/database state, JMeter 5.6.3, and the headerless `../test-data/workflow.csv`.
- Hardware and monitor evidence is EV-HW-001 and EV-HW-002. Same-frame JMeter/Task Manager evidence is EV-RUN-LOAD, EV-RUN-STRESS, and EV-RUN-SPIKE.

## Screenshot evidence

| Evidence ID | Artifact |
| --- | --- |
| EV-RUN-LOAD | `../evidence/execution/EV-RUN-LOAD-JMETER-TASKMANAGER.png` |
| EV-RUN-STRESS | `../evidence/execution/EV-RUN-STRESS-JMETER-TASKMANAGER.png` |
| EV-RUN-SPIKE | `../evidence/execution/EV-RUN-SPIKE-JMETER-TASKMANAGER.png` |
| EV-HW-001 | `../evidence/hardware/EV-HW-DXDIAG-SYSTEM.png` |
| EV-HW-002 | `../evidence/hardware/EV-HW-TASKMANAGER-PERFORMANCE.png` |
| EV-LOCKOUT-001 | `../evidence/lockout-reset/EV-LOCKOUT-INVALID-LOGIN-SEQUENCE.png` |
| EV-LOCKOUT-002 | `../evidence/lockout-reset/EV-LOCKOUT-RESET-VALID-LOGIN.png` |
