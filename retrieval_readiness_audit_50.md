# Retrieval-Ready AI Agent Audit — $50 BTC

## Demand signal

Public source checked: Hacker News Algolia search, 2026-05-28 UTC.

Observed pain point: builders shipping AI agents/RAG products are still chaining generic search APIs, scraping, captcha handling, HTML cleanup, content extraction, and prompt formatting. This creates noisy context, inflated token spend, latency, and brittle output.

Representative current signal: "Show HN: Search Router – retrieval-ready web search for AI agents" describes demand for cleaner structured retrieved context and MCP-friendly search integration.

## Fixed-scope deliverable

For **$50 in BTC**, I will review one AI agent/RAG retrieval flow and return a concise markdown report within 24h.

Send one of:

- GitHub repo link
- Docs for your retrieval/search flow
- Prompt/tool schema snippets
- Example raw retrieved pages plus final LLM context
- Product page describing your agent/RAG workflow

## What the audit checks

1. **Context hygiene**
   - Cookie banners/nav/footer noise
   - Duplicate boilerplate
   - Unclear source attribution
   - HTML/text extraction artifacts

2. **Token cost waste**
   - Unnecessary raw HTML passed to model
   - Overlong snippets
   - Repeated source chunks
   - Missing compression/summarization boundary

3. **Reliability risk**
   - Search result drift
   - Fragile selectors/scrapers
   - Missing retry/fallback logic
   - Captcha or anti-bot dependency risk

4. **Agent tool interface**
   - Whether retrieval output is model-readable
   - Whether tool responses include URL/title/date/snippet/source
   - Whether the agent can cite or reject weak sources
   - MCP/tool-call schema clarity if applicable

5. **Quick fixes**
   - 5 highest-impact cleanup recommendations
   - Suggested JSON shape for retrieved context
   - Minimal eval cases to catch retrieval regressions

## Report format

```md
# Retrieval Readiness Audit

## Score
- Context hygiene: /10
- Token efficiency: /10
- Reliability: /10
- Agent usability: /10

## Top 5 fixes
1.
2.
3.
4.
5.

## Suggested retrieved-context JSON
...

## Regression test cases
...
```

## Payment

Price: **$50 BTC**

BTC address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

Note: payment is only counted when verified on-chain. No fake engagement, no unauthorized access, no spam.
