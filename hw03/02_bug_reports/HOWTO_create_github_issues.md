# How to publish these bugs as real GitHub Issues (action required before submission)

This workspace's `eshop-clone` folder is a local copy only — it is not connected to a GitHub remote, so Claude cannot create real Issues on your behalf (and per the assignment's anti-cheat rules, the actual bug screenshots must come from you running the app, not from a generated placeholder).

Do the following yourself:

1. Fork `https://github.com/ttbhanh/eshop-sut` to your own GitHub account (or use your own repo if your class setup differs).
2. Run the SUT locally (`backend`, `frontend-web`, `frontend-admin`, `frontend-mobile` — see `eshop-clone/setup_guide.md`).
3. For each row in `Bug_Report.md`'s index table:
   - Click "New Issue" on your fork.
   - Title: use the bug's title exactly (e.g. "BUG-11: Login password field is not masked (type=\"text\")").
   - Labels: apply the labels listed in the detailed entry (or just `bug` + severity if your repo doesn't have custom labels).
   - Body: paste the Steps to Reproduce / Expected / Actual from `Bug_Report.md` (or the matching row of `GUI_Checklist.csv`).
   - Reproduce the bug in your running app, take a screenshot, and drag it into the Issue body (GitHub auto-uploads and links it).
4. Copy the resulting Issue URL back into the `GitHub Issue URL` column of the index table in `Bug_Report.md`.
5. Save a copy of each screenshot into `02_bug_reports/screenshots/BUG-XX.png` as well, so the zip submission is self-contained even without internet access to GitHub.

This step cannot be automated for you because it requires an authenticated GitHub session and a real running instance of the SUT with genuine screenshots — both of which are outside this Claude Code session's reach.
