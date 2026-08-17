from pathlib import Path
import sys
r=Path(sys.argv[1]); required=['plans/23127404_Load_20260817.jmx','plans/23127404_Stress_20260817.jmx','plans/23127404_Spike_20260817.jmx','raw-results/load/23127404_Load_20260817.jtl','raw-results/stress/23127404_Stress_20260817.jtl','raw-results/spike/23127404_Spike_20260817.jtl']
missing=[p for p in required if not (r/p).exists()]
print('PASS' if not missing else 'MISSING: '+', '.join(missing))
raise SystemExit(bool(missing))
