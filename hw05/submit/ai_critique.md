# AI Critique (200–300 words)

[Write your 200–300 word critique addressing the following questions:]

- Where did the AI get something wrong, biased, or incomplete?
- Why did it fail to catch the issue?
- What principle have you learned about collaborating with AI during this assignment?

---

**Example structure (replace with your own analysis):**

During this performance testing assignment, I used [AI tool] to assist with test plan design and results analysis. While the AI proved helpful as a starting point, I identified several critical issues:

**Incorrect Parameter Suggestion**: The AI recommended a ramp-up time of 10 seconds for 50 virtual users in the stress test. This is unrealistically aggressive for a local SQLite backend — it would cause immediate connection exhaustion rather than gradual degradation. The correct ramp-up should be 120 seconds to observe meaningful performance curves. The AI likely defaulted to a "cloud-native" assumption, not accounting for single-machine constraints.

**Missing Authentication Headers**: The AI-generated test plans omitted the `Authorization: Bearer` header for cart and checkout endpoints. This is a common oversight where the AI focused on request body structure but neglected HTTP header requirements for JWT-protected routes.

**Misinterpreted Metrics**: When analyzing results, the AI incorrectly calculated throughput by dividing total requests by wall-clock time instead of excluding think time. This inflated the reported RPS by approximately 40%.

**Key Principle Learned**: AI is a powerful assistant but not a domain expert. I learned that every AI output must be validated against the specific system under test. The AI's generic knowledge of "performance testing best practices" does not account for the unique characteristics of our SUT — SQLite's single-writer constraint, the in-memory cart implementation, or the account lockout mechanism. Human review is not optional; it is essential for correctness.

[Continue with your own analysis — ensure total word count is 200–300 words]
