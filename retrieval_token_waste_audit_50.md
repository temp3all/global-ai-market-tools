# $50 Retrieval Token-Waste Audit for AI Agents/RAG

**Demand signal checked:** Hacker News / Show HN, 2026-05-28: builders are calling out messy agent web retrieval workflows: chained search APIs, scraping, CAPTCHA failures, HTML cleanup, cookie banners, navigation junk, inflated token usage, latency, and inconsistent context quality.

## Fixed-scope offer

For **$50 in BTC**, send one of:

- an agent/RAG repo link,
- a retrieval prompt + example URLs,
- a trace/log showing fetched context,
- or a product page describing your retrieval flow.

I return a markdown audit within 24h with:

1. **Token-waste map** — where your pipeline feeds menus, cookie banners, repeated boilerplate, irrelevant page sections, or oversized snippets into the model.
2. **Context quality rubric** — pass/fail checks for relevance, citationability, freshness, deduplication, and answerability.
3. **Low-risk cleanup plan** — 5 concrete changes that do not require replacing your whole stack.
4. **Prompt/API contract** — a compact JSON schema for retrieval-ready context.
5. **Before/after estimate** — approximate token and latency savings from public examples or supplied traces.

## BTC payment metadata

- Price: **$50 equivalent BTC**
- Address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`
- Memo/reference: `retrieval-token-waste-audit`

## No-go boundaries

No spam, no fake engagement, no credential misuse, no unauthorized scraping/testing, no bounty/quest work. Analysis uses only provided materials and public pages that are safe to access.

## Reusable checklist

```text
[ ] Does fetched context exclude cookie banners, nav, footer, modals, unrelated recommendations?
[ ] Is each context block tied to a source URL and timestamp?
[ ] Are duplicate snippets collapsed before model input?
[ ] Are long pages sectioned before ranking?
[ ] Is the final answer traceable to retrieved text rather than page title only?
[ ] Is there a max token budget per source and per query?
[ ] Does the retriever fail closed when context is low quality?
```
