# Evidence Register

| ID | Claim | Evidence | Status |
| --- | --- | --- | --- |
| EV-RUN-LOAD | GUI Load execution with backend process visible | `../evidence/execution/EV-RUN-LOAD-JMETER-TASKMANAGER.png` | Captured |
| EV-RUN-STRESS | GUI Stress execution with backend process visible | `../evidence/execution/EV-RUN-STRESS-JMETER-TASKMANAGER.png` | Captured |
| EV-RUN-SPIKE | GUI Spike execution with backend process visible | `../evidence/execution/EV-RUN-SPIKE-JMETER-TASKMANAGER.png` | Captured |
| EV-HW-001 | Machine identity and system specification | `../evidence/hardware/EV-HW-DXDIAG-SYSTEM.png` | Captured |
| EV-HW-002 | CPU and memory performance view | `../evidence/hardware/EV-HW-TASKMANAGER-PERFORMANCE.png` | Captured |
| EV-LOCKOUT-001 | Two invalid attempts returned 401; the third returned 403 | `../evidence/lockout-reset/EV-LOCKOUT-INVALID-LOGIN-SEQUENCE.png` | Captured |
| EV-LOCKOUT-002 | Restart/reset restored valid login with HTTP 200 | `../evidence/lockout-reset/EV-LOCKOUT-RESET-VALID-LOGIN.png` | Captured |
| EV-LOCKOUT-003 | Fresh runtime check: two invalid logins followed by valid login returned 401, 401, 403 | `../bugs/BUG-HW05-LOCKOUT-001.md` | Verified on 17 August 2026 |
| EV-JTL-LOAD | Final Load metrics | `../raw-results/load/23127404_Load_20260817.jtl` | Verified by summarizer |
| EV-JTL-STRESS | Final Stress metrics | `../raw-results/stress/23127404_Stress_20260817.jtl` | Verified by summarizer |
| EV-JTL-SPIKE | Final Spike metrics | `../raw-results/spike/23127404_Spike_20260817.jtl` | Verified by summarizer |
| EV-JTL-ENDURANCE | Endurance metrics and timing window | `../raw-results/endurance/23127404_Endurance_20260817.jtl` | Verified by summarizer |
