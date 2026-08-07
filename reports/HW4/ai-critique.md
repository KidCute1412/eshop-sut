# AI Critique

The most concrete AI mistake in this automation work was the first FR-01 password oracle. The
automation initially treated `Aa1!aaaa` as an expected client-side password failure because that was
the current behavior of the page. After re-checking the requirement, this was wrong: `README.md`
explicitly allows special characters such as `@` and `!`, so the expected result should be
successful registration. The corrected tests showed that `Aa1!aaaa`, `Aa1@aaaa`, and the
20-character `Aa1!aaaaaaaaaaaaaaaa` are all rejected before any register API request is sent, while a
20-character password using whitespace passes. That means the bug is not a maximum-length problem
but an incorrect regex that requires whitespace instead of the documented special-character set.
A second AI mistake was the first FR-07 cart implementation. It
looked reasonable at a glance: add a product on the home page, then navigate to `/cart` and assert
that a table row exists. In the real SUT, however, the cart is held only in React context. Calling
`page.goto("/cart")` reloads the app and destroys that in-memory state, so the test produced many
false failures. The fix was to navigate through the application's own Cart link, preserving the
single-page-app session. The AI missed this because it treated routing as interchangeable with user
navigation and did not inspect how state survives between screens. A second mistake appeared in
FR-01: the duplicate-email test initially waited for any `/api/register` response and could capture
the wrong 200 response. Filtering the wait to POST made the assertion reliable, and the remaining
failure exposed another real defect: duplicate registration is accepted. The collaboration
principle is that AI-generated automation is only a draft. Selectors, waits, state transitions, and
test oracles all need human review against real execution evidence and the written requirement.
