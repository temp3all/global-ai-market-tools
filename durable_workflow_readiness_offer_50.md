# $50 Durable Workflow Readiness Quick Audit

A fixed-scope review for small teams shipping AI agents, background jobs, or automation that must survive crashes, retries, deploys, duplicate events, and human approval boundaries.

## Demand signal

Hacker News top-story discussion on durable workflows/Postgres-first execution highlights recurring builder pain: many agent and job systems work in demos but lack durable state, idempotency, resumability, audit logs, and safe replay once real customers or paid actions are involved.

## What I deliver for $50 BTC

Within 24 hours, send a repo link, architecture sketch, worker/job code excerpt, or short description. I return a markdown report with:

1. Durable workflow readiness score using `durable_workflow_readiness_checker.py`
2. Top 5 failure modes likely to cause duplicate work, stuck jobs, or lost state
3. Idempotency and retry boundary recommendations
4. Minimal Postgres/SQLite schema sketch for job state and audit logs
5. Human-approval gate suggestions for paid/risky tool calls

## Scope limits

- Public or user-provided materials only
- No unauthorized testing
- No credential handling required
- No bounties, contests, quest farming, spam, or fake engagement

## Payment

Price: **$50 BTC**

BTC address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

After payment, provide transaction ID plus the repo/notes to review.

## Self-check tool

```bash
python durable_workflow_readiness_checker.py --example > workflow_readiness_example.json
python durable_workflow_readiness_checker.py workflow_readiness_example.json
```
