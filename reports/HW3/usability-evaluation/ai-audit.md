# AI Audit — Task 2 Usability Evaluation (Prompt + Raw AI Output Only)

AI Tool: Claude (Sonnet 5)
Date: 2026-07-29

## Prompt

```text
You have access to the "gui-usability" Agent Skill I designed for this course (see
.agents/skills/gui-usability/SKILL.md, and its references/usability-evaluation-method.md). Use it
to design Task 2 (Usability Evaluation) of HW03 for the EShop SUT, scoped to one end-to-end flow:
Register -> Login -> Update Profile (README.md FR-01/FR-02/FR-04).

Follow these constraints exactly:

1. Write 4-5 Objectives that state what this evaluation should learn, referencing the concrete
   Task 1 findings already on record for this flow (the broken password-strength hint, the
   mislabeled Login elements) as things to check for real-user impact.
2. Write one Task Scenario, in Vietnamese with an English translation, that is goal-oriented (a
   realistic reason to register and update contact info) rather than a step-by-step instruction —
   it must not name the screens or the order to visit them.
3. Choose a usability scale (SUS or UEQ-S) and justify the choice in 2-3 sentences given this
   flow's characteristics.
4. Write Probe Questions covering at minimum Clarity, Error recovery, Speed, and Trust, plus one
   optional additional probe.
5. Draft Recruitment Criteria (target profile, non-IT/non-tester preference) and Session Logistics
   (recording tool, consent process).
6. Use scripts/create_usability_workspace.py to scaffold the files and
   assets/usability-plan-template.md as the schema. Do not invent participant names, contact
   details, or session data — those must come from the student and from real sessions only.
```

## AI Output (raw, pre-review)

```text
## Objectives

- Can a first-time user complete account registration without external help, and does the
  password-strength feedback actually guide them to a valid password (Task 1 already found this
  client-side check to be broken -- does that surface as real friction for a real user)?
- After registering, can the user log in on their first attempt without confusion (Task 1 found
  the Login screen mislabels/copy-paste-errors several elements -- does a first-time user notice or
  get confused by these)?
- Once logged in, can the user find the profile/account settings and successfully update their
  name, phone number, and shipping address without guidance?
- Do users trust that their updated information was actually saved correctly, and do they
  understand why a phone number might be rejected (format rule: must start with 0, 10-11 digits)?
- Where exactly (registration, login, or profile update) do users hesitate, make errors, or
  express frustration the most?

## Task Scenario

> "Ban vua chuyen den cho o moi va doi sang mot so dien thoai moi. Hay tao mot tai khoan moi tren
> EShop, sau do cap nhat ho so cua ban voi dia chi giao hang va so dien thoai moi, de cac don hang
> sau nay duoc giao dung noi."
>
> ("You just moved to a new place and switched to a new phone number. Create a new account on
> EShop, then update your profile with your new shipping address and phone number, so future
> orders are delivered to the right place.")

This is intentionally goal-oriented (a real-life reason to register + update contact info), not a
step-by-step instruction -- it does not tell the participant to click Register, then Login, then
Profile in that order; reaching that path is exactly what is being observed.

## Instrument

- Selected scale: SUS (System Usability Scale, 10 items, 5-point Likert)
- Justification: SUS was chosen over UEQ-S because this flow is a short, functional (not
  experience/hedonic-heavy) task, and SUS has a well-known benchmark (~68 = average) that makes the
  write-up easy to interpret without extra normalization work.

## Probe Questions

- Clarity: "Was there any point where it wasn't clear what to do next, or what a field expected
  from you (for example, the password rules, or the phone number format)?"
- Error recovery: "If something didn't work the first time (an error message, a rejected value),
  how did you figure out what to do differently?"
- Speed: "Did any step feel slower or more tedious than you expected for something this simple?"
- Trust: "After updating your profile, how confident were you that your new address and phone
  number were actually saved correctly?"
- (Optional additional probe): "Was there any moment you felt unsure whether you were on the
  right page, or unsure the app was doing what you expected?"

## Recruitment Criteria

- Target user profile: general adult smartphone/computer users comfortable shopping online; no
  QA/testing or software-development background required
- Non-IT/non-tester preferred: Yes -- preferred per the assignment, to get authentic (not
  QA-trained) reactions to the friction points

## Session Logistics

- Recording tool: screen recording via OBS Studio (or the phone/laptop's built-in screen recorder
  if the session runs on mobile); audio recorded only with explicit participant consent
- Consent process: before starting, verbally state that (a) the product is being tested, not the
  participant, (b) the session may be screen-recorded (and audio-recorded only if they agree), and
  (c) they can stop at any time; get a clear verbal "yes" before recording starts
```
