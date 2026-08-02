# AI Critique

The clearest example of the AI being wrong was checklist item 6.3 (Login Tab order). Without a
live browser available in that working session, the AI predicted the result by reading the source
— reasoning that Login's submit button carrying `tabIndex={1}` would pull keyboard focus ahead of
the Password field, and marked the item Failed on that basis. When the item was later re-tested by
hand in a real browser, focus actually moved in the correct visual order; the predicted defect did
not exist. The AI failed to catch this because a source-level prediction about how an attribute
*should* behave is not the same as observing what a browser actually renders — `tabIndex` values,
CSS, and DOM order interact in ways that are only fully resolved at runtime, and no amount of
careful reading substitutes for that. A second, smaller instance came during SUS analysis: the AI
proposed that participants scoring lower on the SUS scale had additionally hit a "Username" field
confusion issue that the higher-scoring group avoided — a plausible-sounding causal story that
turned out to be contradicted by one participant who hit that same issue while still scoring in the
higher group, once the claim was checked directly against the Observation Logs. In both cases the
AI produced a confident, coherent-sounding claim before the underlying evidence had actually been
checked, and both were only caught by a deliberate cross-check against ground truth (a live-browser
retest; a line-by-line re-read of the raw session data) rather than by the AI itself flagging
uncertainty. The principle: treat any AI-generated claim about *behavior* — whether predicted from
source or inferred from a correlation — as a hypothesis requiring independent verification against
real execution or raw data, never as a finding on its own.
