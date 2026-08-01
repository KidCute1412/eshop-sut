# Usability Evaluation Plan - Register -> Login -> Update Profile

## Objectives

- Can a first-time user complete account registration without external help, and does the
  password-strength feedback actually guide them to a valid password (Task 1 already found this
  client-side check to be broken — does that surface as real friction for a real user)?
- After registering, can the user log in on their first attempt without confusion (Task 1 found
  the Login screen mislabels/copy-paste-errors several elements — does a first-time user notice or
  get confused by these)?
- Once logged in, can the user find the profile/account settings and successfully update their
  name, phone number, and shipping address without guidance?
- Do users trust that their updated information was actually saved correctly, and do they
  understand why a phone number might be rejected (format rule: must start with 0, 10-11 digits)?
- Where exactly (registration, login, or profile update) do users hesitate, make errors, or
  express frustration the most?

## Task Scenario

> You just moved to a new place and switched to a new phone number. Create a new account on
> EShop, then update your profile with your new shipping address and phone number, so future
> orders are delivered to the right place.

This is intentionally goal-oriented (a real-life reason to register + update contact info), not a
step-by-step instruction — it does not tell the participant to click Register, then Login, then
Profile in that order; reaching that path is exactly what is being observed.

## Instrument

- Selected scale: **SUS** (System Usability Scale, 10 items, 5-point Likert)
- Justification (required if Custom): N/A — SUS was chosen over UEQ-S because this flow is a
  short, functional (not experience/hedonic-heavy) task, and SUS has a well-known benchmark
  (~68 = average) that makes the write-up easy to interpret without extra normalization work.
  `scripts/compute_sus_score.py` is used to score it once real responses exist.

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

## Human Review

- Reviewer: Nguyen Thanh Tien 
- Review Date and Time: 2026-07-30
- Review Scope: Usability Evaluation Plan for Register -> Login -> Update Profile, covering
  Objectives, Task Scenario, Instrument, Probe Questions, Recruitment Criteria, and the
  no-pilot-required waiver
- Corrections Made: Pilot Session marked N/A per the lecturer's in-class clarification (see
  `.agents/skills/gui-usability/references/instructor-clarifications.md` item 12) instead of being
  run as originally planned; Recruitment Criteria's "Non-IT/non-tester preferred" and target-profile
  language were kept as originally drafted since all 7 recruited participants matched that profile.
- Approved to Begin Sessions: Yes
