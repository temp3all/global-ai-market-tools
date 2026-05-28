# AI Agent Observability Quickstart — $50 Fixed Scope

Demand signal: recent Hacker News results include teams asking how to monitor AI agents in production and vendors adding OpenTelemetry observability to agent frameworks. Small teams need a lightweight first pass before buying a platform.

## Offer
For **$50 in BTC**, I prepare a one-page observability quickstart for one AI agent workflow.

Payment address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## What I deliver
- A minimal event taxonomy for your agent: `run_started`, `tool_called`, `retrieval_used`, `model_called`, `guardrail_triggered`, `run_completed`, `run_failed`.
- A JSON log schema you can paste into your app.
- A dashboard checklist: latency, token/cost estimate, tool failure rate, retry count, user-visible failure count, and top failure reasons.
- Five red-flag alerts for production agent risk.
- A 30-minute implementation plan for Python or TypeScript.

## Inputs needed
- Public repo link or pasted agent flow summary.
- Runtime: Python, TypeScript, no-code, or other.
- Model/provider names if public/non-sensitive.
- Existing logs/metrics sample if available.

## Template event schema
```json
{
  "timestamp": "2026-05-28T00:00:00Z",
  "agent_name": "support-agent",
  "run_id": "uuid",
  "event": "tool_called",
  "step": 3,
  "model": "gpt-4.1-mini",
  "tool_name": "search_docs",
  "latency_ms": 842,
  "estimated_input_tokens": 1200,
  "estimated_output_tokens": 220,
  "status": "ok",
  "error_type": null,
  "user_visible": false
}
```

## Quick red-flag alerts
1. Tool error rate over 10% for 10 minutes.
2. Agent run p95 latency over 30 seconds.
3. Estimated cost per successful run doubles versus 7-day median.
4. Retrieval returns zero documents for more than 5% of runs.
5. Guardrail or refusal events spike by 3x versus baseline.

## Ethical boundary
No credential sharing required. No unauthorized access, scraping, spam, fake engagement, or ToS evasion. Work is limited to public code, customer-provided snippets, or local templates.
