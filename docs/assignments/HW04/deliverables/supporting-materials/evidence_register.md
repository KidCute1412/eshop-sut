# HW04 Evidence Register

## Evidence-state policy

- `Verified existing`: file and relevant metadata were inspected in this repository.
- `Historical claim`: described by a preserved report but not rerun during this preparation.
- `Not Collected`: required evidence does not yet exist in this deliverables package.
- `PENDING verification`: a student-controlled external artifact must be opened and checked.

## Current register

| Evidence ID | Artifact | Requirement/run linkage | State | Integrity/provenance note |
|---|---|---|---|---|
| `EV-LEG-001` | `../../schools/23127404-automation/tests/fr06-product-detail.spec.ts` | FR-06 / historical `FR06-DT-01` | Verified existing | Source code only; does not prove runtime outcome |
| `EV-LEG-002` | `../../schools/23127404-automation/test-data/fr06-product-detail.json` | FR-06 / historical `FR06-DT-01` | Verified existing | External test data; encoding/content should be revalidated before rerun |
| `EV-LEG-003` | `../../schools/23127404-automation/playwright-report/` | Historical FR-06 / Chromium, Firefox, WebKit | Verified existing directory; historical outcome | Combined report with assets; not a final nine-report set |
| `EV-LEG-004` | `../../schools/23127404.md` | Historical run narrative and AI summary | Verified existing; historical claim | Secondary narrative; exact first prompt/time absent |
| `EV-SRC-001` | `../automation/tests/` and `../automation/test-data/` | FR-06/FR-10/FR-12 source suite | Verified source; Firefox correction committed at `a390bc125713a1759443a4e84929641d432a45dc` | 51 JSON-defined cases; final Firefox reports use the corrected revision |
| `EV-SRC-002` | `../automation/playwright.config.ts` and matrix/report scripts | Nine-run orchestration | Verified source and structurally validated outputs | Identity, timestamp, case-count, completion, report/data-directory presence, and JSON/metadata totals validated; interactive links remain manual |
| `EV-SKILL-SRC` | `../agent-skill/playwright-data-driven-multibrowser/` | Optional Agent Skill source | Verified existing source | Reusable source with separate demo URL recorded in `../video/agent_skill_demo.md` |
| `EV-GIT-001` | `../git/23127404_HW04_git_commit_log.txt` | Git-history assessment | Verified snapshot | Complete HW04 history plus 9 qualifying commits; count met; four-day rule noncompliant |
| `EV-PDF-001` | `../reports/main_report.pdf` | Main report | Generated and text-validated | 8 pages; student ID and extractable text verified after final reconciliation |
| `EV-PDF-002` | `../reports/ai_critique.pdf` | Mandatory AI Critique | Generated and text-validated | 1 page; Markdown source is one 246-word paragraph |
| `EV-PDF-003` | `../reports/ai_audit_report.pdf` | AI Audit Report | Generated and text-validated | 5 pages; known transcript gaps remain disclosed |
| `EV-ZIP-001` | `../23127404_HW04_AI_Automation_100.zip` | Final self-assessed package | Generated and structurally inspected (571 entries) | Archive contains all eight deliverable groups and excludes generated dependencies, logs, and nested ZIPs; final timestamp/link review remains student-controlled |
| `EV-RUN-A-CHR` | `../automation/reports/fr06-chromium-2026-08-09T17-11-54-712Z/` | `RUN-A-CHR` | Attempted; structural validator passed | 16 total / 10 pass / 6 assertion fail; `2026-08-09T17:11:54.712Z` |
| `EV-RUN-A-FF` | `../automation/reports/fr06-firefox-2026-08-09T18-19-41-178Z/` | `RUN-A-FF` | Attempted; structural validator passed | 16 / 10 / 6 assertion fail; Firefox headless corrected run |
| `EV-RUN-A-WK` | `../automation/reports/fr06-webkit-2026-08-09T17-16-10-035Z/` | `RUN-A-WK` | Attempted; structural validator passed | 16 / 10 / 6 assertion fail |
| `EV-RUN-B-CHR` | `../automation/reports/fr10-chromium-2026-08-09T17-17-32-516Z/` | `RUN-B-CHR` | Attempted; structural validator passed | 16 / 12 / 4 assertion fail; post-locator-fix rerun |
| `EV-RUN-B-FF` | `../automation/reports/fr10-firefox-2026-08-09T18-21-10-553Z/` | `RUN-B-FF` | Attempted; structural validator passed | 16 / 12 / 4 assertion fail; Firefox headless corrected run |
| `EV-RUN-B-WK` | `../automation/reports/fr10-webkit-2026-08-09T17-21-22-978Z/` | `RUN-B-WK` | Attempted; structural validator passed | 16 / 12 / 4 assertion fail; `FR10-02` passes after exact-cell fix |
| `EV-RUN-C-CHR` | `../automation/reports/fr12-chromium-2026-08-09T17-22-38-418Z/` | `RUN-C-CHR` | Attempted; structural validator passed | 19 / 10 / 9 assertion fail |
| `EV-RUN-C-FF` | `../automation/reports/fr12-firefox-2026-08-09T18-22-31-674Z/` | `RUN-C-FF` | Attempted; structural validator passed | 19 / 10 / 9 assertion fail; Firefox headless corrected run |
| `EV-RUN-C-WK` | `../automation/reports/fr12-webkit-2026-08-09T17-27-20-694Z/` | `RUN-C-WK` | Attempted; structural validator passed | 19 / 10 / 9 assertion fail |
| `EV-VIDEO-001` | https://youtu.be/Uz9ogf7fKFY | Task 2 | URL supplied; student must verify logged-out access and duration | Unlisted Vietnamese demo URL recorded in `../video/demo_video.md` |
| `EV-SKILL-001` | https://youtu.be/PL3qLI-KcPE | Agent Skills | URL supplied; student must verify logged-out access | Separate Agent Skill demonstration URL recorded in `../video/agent_skill_demo.md`; self-assessed 10/10 |

## Additional evidence entries

| Evidence ID | Relative path or public URL | Case/run/defect IDs | Created at (ISO) | Created by | Environment | Verification state | Verified by/date | Notes |
|---|---|---|---|---|---|---|---|---|
| — | No additional exact evidence entry retained | — | — | — | — | Not applicable | — | Do not add reconstructed or invented evidence |

## Integrity checks

- Screenshots prove only the visible state at capture time.
- HTML reports prove the recorded execution only when their full assets and metadata are preserved.
- Traces/logs support diagnosis but do not replace a user-visible oracle where the requirement is visual.
- Source code supports design and root-cause hypotheses; it does not justify `Pass` or `Fail`.
- Each selected report metadata file records its own exact automation/SUT revision. The final Firefox rerun is pinned to `a390bc125713a1759443a4e84929641d432a45dc`; Chromium/WebKit retain their recorded revision `656991a598bafe43cbed13b54bf1ac3f429c30f2`.
- External links must be tested for access and must not be replaced by invented placeholders in final claims.
- Evidence must not expose passwords, reusable JWTs, secrets, or unnecessary personal data.
