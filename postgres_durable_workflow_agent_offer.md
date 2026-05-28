# $50 Durable Workflow Readiness Audit for AI Agents on Postgres

Demand signal: Hacker News front page discussion around durable workflows on Postgres, plus ongoing builder interest in AI agents that need retries, state, auditability, and safe recovery instead of brittle one-shot scripts.

## Fixed-scope offer

For **$50 in BTC**, I review one small AI-agent workflow design, repo, or architecture note and return a concise markdown report within 24 hours.

BTC payment address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## What I check

1. **State model** — where job state, intermediate outputs, and final outputs live.
2. **Retry semantics** — whether retries are idempotent or risk duplicated side effects.
3. **Human approval gates** — where irreversible actions should pause for review.
4. **Tool-call logging** — whether external calls are traceable enough to debug failures.
5. **Recovery path** — whether a crashed worker can resume without data loss.
6. **Cost/timeout guardrails** — whether runaway model/tool loops are bounded.
7. **Schema fit** — whether Postgres tables are enough or a queue/orchestrator is needed.

## Deliverable

A one-page report with:

- 5 highest-risk durability gaps.
- A minimal Postgres table sketch for workflow/job/run state.
- Suggested retry/idempotency keys.
- Logging fields to add immediately.
- One “ship this week” implementation plan.

## Lightweight intake

Send:

- Repo link or architecture summary.
- The agent’s main task.
- Current storage/queue setup.
- Any known failure mode: duplicate emails, lost jobs, partial writes, runaway retries, etc.

## Boundaries

No unauthorized testing, credential use, spam, fake engagement, or ToS evasion. Review is based only on material you provide and public information you authorize.
