# HW03 Report — GUI and Usability Testing

| Field | Value |
|---|---|
| Student | Lê Tuấn Lộc (23127404) |
| Email | 23127404@hcmus.edu.vn |
| System under test | EShop |
| Selected scope | FR-07, FR-10, FR-11, FR-18, and mobile product detail (FR-23) |

## Executive summary

This report presents the design and execution framework for GUI checklist testing, moderated usability evaluation, and cross-platform verification of the EShop application. It also documents defects, AI-assisted activities, human review, and a reusable testing skill. Results that require real participants, live browser/device execution, or externally accessible evidence are reported only after verification; outstanding empirical work is identified transparently.

## 1. GUI checklist and defect reporting

### 1.1 Objective and coverage

The checklist evaluates selected customer, mobile, and administrative flows across all four interface aspects: general UI standards (IA-01), forms (IA-02), navigation (IA-03), and feedback/state (IA-04). The canonical checklist contains 45 non-identical items in `checklist/gui_checklist.xlsx` and `checklist/gui_checklist.csv`.

### 1.2 Design and review method

AI was used to propose an initial checklist and assist with static inspection. Each item was reviewed against the selected interface and application behavior. Human-added or materially revised items document the context that the initial AI analysis overlooked. The checklist records preconditions, expected and actual results, execution status, notes, defect mapping, and evidence references where applicable.

### 1.3 Execution summary

| Measure | Result |
|---|---|
| Items designed | 45 |
| Interface aspects covered | IA-01, IA-02, IA-03, IA-04 |
| Items executed | Refer to the final checklist status column |
| Passed / failed | Refer to the final checklist and README summary |
| Defects | 13 candidate records pending final evidence verification |

Detailed defect records are maintained in `bugs/bug_report.md`. Failed checklist items must reference a defect ID and authentic screenshot; each submitted defect must also reference the corresponding GitHub issue screenshot.

## 2. Moderated usability evaluation

### 2.1 Objective

The evaluation investigates whether target users can independently complete a purchase-oriented flow, understand system feedback, recover from errors, and trust the resulting order status. The participant-facing goal is defined in `usability/task_scenario.md`.

### 2.2 Method

One pilot session is conducted before seven official moderated sessions. Participants are asked to think aloud while the moderator observes without leading them. After completing or abandoning the task, each participant completes the System Usability Scale (SUS) and answers probes concerning clarity, error recovery, speed, and trust.

### 2.3 Evidence status

| Evidence | Status | Location |
|---|---|---|
| Pilot session | Not yet conducted | `usability/observation_notes/pilot_notes.md` |
| Seven eligible participants | Not yet verified | `usability/participant_list.md` |
| Session recordings | Not yet collected | `usability/recordings/README.md` |
| SUS responses | Not yet collected | `usability/raw_responses/` |
| Observation notes | Not yet collected | `usability/observation_notes/` |
| Severity-ranked synthesis | Awaiting session evidence | `usability/severity_ranked_findings.md` |

### 2.4 SUS scoring

For odd-numbered items, the contribution is the response minus one. For even-numbered items, the contribution is five minus the response. The ten contributions are summed and multiplied by 2.5, producing a score from 0 to 100. The score is a usability benchmark, not a percentage grade.

| Participant | SUS score | Status |
|---|---:|---|
| P1–P7 | — | Awaiting authentic responses |
| Mean | — | Calculated after all seven sessions |

## 3. Cross-platform verification

The selected flow will be verified on Chrome Desktop, Firefox Desktop, and a real physical or approved cloud mobile environment. Each screenshot must show enough environment context to establish the browser, operating system or device, the SUT localhost URL, and the required `23127404@hcmus.edu.vn` identity overlay.

| Environment | Execution status | Evidence |
|---|---|---|
| Chrome Desktop | Not executed | `cross_platform/chrome_desktop/` |
| Firefox Desktop | Not executed | `cross_platform/firefox_desktop/` |
| Real/approved cloud mobile environment | Not executed | `cross_platform/mobile_real_device/` |

The detailed execution matrix and observed differences are recorded in `cross_platform/cross_platform_report.md` after the real runs.

## 4. Agent Skill and AI documentation

The reusable testing skill is provided in `agent_skills/gui-usability-tester/SKILL.md`. Its demonstration URL will be recorded in the adjacent `demo_video_link.txt` after the end-to-end video is uploaded and access-tested. The mandatory AI Critique and AI Audit Report are supplied in Markdown and PDF under `ai_reports/`.

## 5. Limitations and completion criteria

At the current stage, no usability-session or cross-platform result is claimed. Final conclusions must be based on authentic evidence, the checklist summary must be recalculated from its final statuses, and every external link must be verified before packaging.

## Conclusion

The submission framework provides traceability from assignment requirements to test design, execution evidence, findings, and AI-assisted work. The final report will be considered complete only after the remaining real-world evidence has been collected, reviewed, and incorporated consistently across all source and derived files.

