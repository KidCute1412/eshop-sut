# Project: HW03 GUI Testing and Usability Evaluation for EShop SUT

## Architecture
- **Target Application**: EShop SUT (Backend: Node.js/Express + SQLite on port 3000, Frontend Web: React 19 + Vite on port 5173, Frontend Admin: React 19 + Vite on port 5174, Frontend Mobile: React Native + Expo ~54).
- **Deliverables Directory**: `docs/assignments/HW03/deliverables/`
- **Assigned Functional Requirements**:
  - `FR-07`: Shopping Cart (Web & Mobile)
  - `FR-10`: Order State Machine (Backend API & State Transitions)
  - `FR-11`: Order History View (User Web & Mobile)
  - `FR-18`: Order Management (Admin Web)
  - `FR-23`: Product Detail View (Mobile - FR-06 on Mobile)

## Feature Inventory
| # | Feature | Description | Aspect / Scope | Milestone | Source |
|---|---------|-------------|----------------|-----------|--------|
| 1 | FR-07.1 | Cart Quantity & Pricing Calculation | IA-01, IA-02 | M1 | Survey |
| 2 | FR-07.2 | Cart Item Removal & Empty State | IA-03, IA-04 | M1 | Survey |
| 3 | FR-07.3 | Web & Mobile Cart Synchronization / Checkout | IA-02, IA-03 | M1 | Survey |
| 4 | FR-10.1 | Order Status Transitions (pending -> confirmed -> shipping -> delivered / canceled) | IA-04, Logic | M1 | Survey |
| 5 | FR-10.2 | Order Cancellation Rules & State Enforcement | IA-03, IA-04 | M1 | Survey |
| 6 | FR-11.1 | Order History List & Order Detail Display | IA-01, IA-03 | M1 | Survey |
| 7 | FR-11.2 | Order History Empty State & Search/Filter | IA-04 | M1 | Survey |
| 8 | FR-18.1 | Admin Order Management Table & Status Change Actions | IA-01, IA-03 | M1 | Survey |
| 9 | FR-18.2 | Admin Dashboard Revenue & Security Escaping | IA-01, Security | M1 | Survey |
| 10 | FR-23.1 | Mobile Product Detail Display & Image Aspect Ratio | IA-01 | M1 | Survey |
| 11 | FR-23.2 | Mobile Product Add-to-Cart & Options Selector | IA-02, IA-03 | M1 | Survey |
| 12 | R1-Task 1 | GUI Checklist (>40 items across IA-01 to IA-04) + Excel/CSV | Checklist | M1 | Specs |
| 13 | R1-Bugs | Bug Report (`bugs/bug_report.md`), Evidence Images & GitHub Screenshots | Bug Logging | M1 | Specs |
| 14 | R2-Task 2 | Usability Task Scenario (Customer role: FR-23 -> FR-07 -> FR-10/11) | Scenario | M2 | Specs |
| 15 | R2-Participants | Participant List (7 real users, masked phone numbers) | Participants | M2 | Specs |
| 16 | R2-SUS | SUS Survey Sheet (10 standard + 4 probe questions, Excel/CSV) | Evaluation | M2 | Specs |
| 17 | R2-Recordings | Screen Recording Folder Structure & Observation Notes | Recordings | M2 | Specs |
| 18 | R3-Task 3 | Cross-Platform Screenshots (Chrome, Firefox, Real Mobile) with Watermark Overlay | Evidence | M3 | Specs |
| 19 | R4-Skill | Agent Skill (`agent_skills/gui-usability-tester/SKILL.md`) | Agent Skill | M4 | Specs |
| 20 | R4-Reports | AI Critique (`ai_reports/ai_critique.md`, 200-300 words) & Audit Report | Reports | M4 | Specs |
| 21 | R4-GitLog | Git Commit Log (`git_commit_log.txt`, 13 distinct commits) | Progress | M4 | Specs |
| 22 | R4-Package | Final README (100/100 self-eval) & ZIP `23127404_HW03_AI_GUIUsability_100.zip` | Deliverables | M4 | Specs |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Task 1 - GUI Checklist & Bug Reports | Design & execute ≥40 checklist items across IA-01..04 for 5 FRs; log bugs, evidence images, github screenshots | Survey complete | PLANNED |
| M2 | Task 2 - Usability Evaluation Setup & Analysis | Task scenario (Customer role), participant list (7 users), SUS survey (10 + 4 probe questions), recordings structure, observation notes | M1 | PLANNED |
| M3 | Task 3 - Cross-Platform Screenshots | Evidence screenshots on Chrome Desktop, Firefox Desktop, Real Mobile Device with identity watermark overlay | M1, M2 | PLANNED |
| M4 | Task 4 - Agent Skill, Reports & Deliverable ZIP | SKILL.md, ai_critique.md (200-300 words), ai_audit_report.md, git_commit_log.txt (13 commits), README.md (100/100 matrix), ZIP package | M1, M2, M3 | PLANNED |

## Interface Contracts & Constraints
- **Student Identity String**: `Lê Tuấn Lộc - 23127404 - 23127404@hcmus.edu.vn`
- **Deliverables Root**: `D:/HCMUS/Third Year/Software Testing/eshop-sut/docs/assignments/HW03/deliverables/`
- **ZIP File Target**: `docs/assignments/HW03/deliverables/23127404_HW03_AI_GUIUsability_100.zip`
- **Participant Privacy**: Mask 4 middle digits of phone/Zalo (e.g., `0987****321`).
- **AI Critique Constraints**: Strictly 200 to 300 words in `ai_reports/ai_critique.md`.
- **Git Commit Log**: Exactly 13 distinct commit messages in `git_commit_log.txt`.

## Deliverables Tree Layout
```text
docs/assignments/HW03/deliverables/
├── README.md
├── git_commit_log.txt
├── main_report.md
├── main_report.pdf
├── ai_reports/
│   ├── ai_audit_report.md
│   ├── ai_audit_report.pdf
│   ├── ai_critique.md
│   └── ai_critique.pdf
├── checklist/
│   ├── gui_checklist.xlsx
│   └── gui_checklist.csv
├── bugs/
│   ├── bug_report.md
│   ├── github_issues_screenshots/
│   └── evidence_images/
├── usability/
│   ├── task_scenario.md
│   ├── participant_list.md
│   ├── sus_survey_results.xlsx
│   ├── sus_survey_results.csv
│   ├── observation_notes.md
│   ├── raw_responses/
│   └── recordings/
├── cross_platform/
│   ├── chrome_desktop/
│   ├── firefox_desktop/
│   └── mobile_real_device/
└── agent_skills/
    └── gui-usability-tester/
        ├── SKILL.md
        └── demo_video_link.txt
```
