import csv, statistics, sys
rows=list(csv.DictReader(open(sys.argv[1], encoding='utf-8')))
if not rows: raise SystemExit('empty JTL')
times=sorted(int(r['elapsed']) for r in rows); n=len(rows)
start=min(int(r['timeStamp']) for r in rows); end=max(int(r['timeStamp']) for r in rows)
print({'samples':n,'errors':sum(r['success']!='true' for r in rows),'mean_ms':round(statistics.mean(times),2),'p95_ms':times[int(.95*(n-1))],'min_ms':times[0],'max_ms':times[-1],'duration_s':round((end-start)/1000,3),'rps':round(n/((end-start)/1000),3)})
