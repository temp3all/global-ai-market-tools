# $50 LLM Smell Quick Review

A fixed-scope review for teams shipping LLM or agent features who want a fast, practical check for brittle behavior before customers find it.

## Demand signal

Current Hacker News front page included **"Various LLM Smells"** with active discussion, indicating ongoing builder interest in recognizable failure patterns, reliability debt, and ways to turn vague LLM quality concerns into concrete engineering checks.

## What I review

Send a repo link, README, prompt chain, eval notes, or product walkthrough. I review for these common LLM smells:

1. **Prompt overloading** — one prompt asked to do too many jobs.
2. **Hidden state coupling** — behavior depends on undocumented chat/session context.
3. **No regression fixtures** — prompt/model changes cannot be compared safely.
4. **Unbounded tool autonomy** — tool calls lack explicit allow/deny rules.
5. **Weak fallback behavior** — low-confidence or partial results are presented as complete.
6. **Context stuffing** — retrieval or system messages include too much irrelevant text.
7. **Ambiguous success criteria** — no crisp definition of a correct answer/action.
8. **Provider lock-in assumptions** — code assumes one model's quirks are universal.
9. **No cost/latency guardrails** — failures can silently become expensive or slow.
10. **Audit-hostile outputs** — results are hard to trace back to inputs, tools, and prompts.

## Deliverable

Within 24h, I return a concise markdown report:

- Top 5 LLM smells found
- Risk rating: low / medium / high
- Reproduction notes using only provided/public materials
- One minimal eval fixture you can add immediately
- Suggested acceptance criteria for the next release
- Priority order for fixes under a 2-hour budget

## Price and payment

Fixed price: **$50 equivalent in BTC**

BTC address:

```text
1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ
```

Include your repo/product link and a contact method in the payment memo or follow-up channel.

## Safety boundaries

- No credential use
- No private system probing
- No scraping behind logins
- No spam or fake engagement
- Public/provided material only unless you explicitly supply files
