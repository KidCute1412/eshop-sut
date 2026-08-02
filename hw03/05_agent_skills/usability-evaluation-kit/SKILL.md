---
name: usability-evaluation-kit
description: Scaffold a small-sample moderated usability evaluation (objectives, task scenario, SUS/UEQ-S instrument, participant recruitment sheet, per-session template, SUS scoring + findings synthesis) for a chosen end-to-end user flow. Use when asked to "plan/design a usability test", "prepare a usability study", or "build session templates" for a specific product flow.
---

# Usability Evaluation Kit

Scaffolds ISTQB-style moderated usability testing (Plan → Conduct → Analyse) for one end-to-end flow, producing every artifact needed to actually run the study — but never fabricates the human data itself.

## When to use this skill

When the user needs to *plan and prepare* a usability evaluation for a specific flow in a specific product. This skill produces templates and a rigorous process; it does not (and must not) invent participants, quotes, or scores — those must come from real sessions the user runs.

## Process

### Phase 1 — Plan & prepare
1. **Pick one end-to-end flow** with the user (e.g. "sign up → add to cart → checkout with coupon"). Ground it in something concrete found in the actual codebase (a known tricky field, a validation quirk, a multi-step form) so the study targets real risk, not a generic walkthrough.
2. **Write objectives**: 4-6 specific research questions, each traceable to a concrete hypothesis about the flow (e.g. "will users notice field X is editable when it shouldn't be").
3. **Write the task scenario**: a goal-oriented paragraph (not step-by-step instructions) the participant reads verbatim, plus a moderator-only notes section (what not to reveal, timing/nudge rules, end condition).
4. **Choose the instrument**: SUS (10-item, general ease-of-use/learnability) vs. UEQ-S (8-item, hedonic+pragmatic quality) — justify the choice against what the objectives are actually trying to measure. Include the 4 minimum probe-question categories: clarity, error recovery, speed, trust.
5. **Build the participant sheet**: an empty table (name, masked contact, eligibility notes) — never pre-fill with invented names. State the eligibility rule (outside the class/team) and the contact-masking format explicitly.
6. **Plan a pilot**: a single test run to catch scenario/timing problems before the real 7 sessions.

### Phase 2 — Conduct (template only — do not simulate this)
Produce one reusable per-session template capturing: timing, a structured live-observation table (time, step, observation, severity), a field for verbatim think-aloud quotes, the instrument's items, and the probe-question answers. Never fill this in with placeholder "example" responses that could be mistaken for real data — leave it genuinely blank for the user to complete.

### Phase 3 — Analyse & report (template only)
1. Scoring template for the chosen instrument (formula + per-participant table + benchmark comparison).
2. A findings-synthesis template pre-seeded with hypothesis clusters drawn from Phase 1's objectives, ready to confirm/refute with real data, plus room for unhypothesized findings.
3. A severity-ranked findings table (Blocker/Major/Minor) and a reminder to file genuine bugs discovered during sessions the same way as any other bug report (issue + screenshot).

## Output format

Produce a `phase1_plan/` (objectives, scenario, instrument, participants), `phase2_sessions/SESSION_TEMPLATE.md`, and `phase3_analysis/` (scoring + synthesis templates), plus a short report file stating clearly that Phase 2/3 data collection is pending real human sessions and listing exactly what the user still needs to do.

## Hard constraints (never violate)

- Never invent participant names, contact info, quotes, or scores.
- Never claim a session happened if it didn't.
- Always state plainly, in the output, which parts are ready-to-use process/instruments and which parts require the user to go run real sessions.
