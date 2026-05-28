# AI Agent Regression CI Checklist — $50 Fixed-Scope Offer

Demand signal: recent Hacker News item asking how teams catch AI-agent regressions after prompt/model changes. The recurring pain is not model choice; it is repeatable acceptance testing for agent behavior.

## Who this is for

- Small AI-agent startups shipping prompt/tool changes weekly
- Internal automation teams with brittle agent workflows
- SaaS founders adding tool-using LLM features without a QA harness

## $50 deliverable

For one public repo, demo spec, or provided workflow description, I deliver a markdown CI checklist with:

1. **Golden task set** — 10 representative tasks with expected outcome types.
2. **Regression dimensions** — correctness, tool-call safety, latency, cost, refusal behavior, data exposure, and fallback quality.
3. **Minimal eval schema** — JSONL fields for prompt, tools allowed, expected assertions, max spend, and pass/fail notes.
4. **CI gate policy** — when to block merge vs warn only.
5. **Failure triage template** — model drift, prompt drift, retrieval drift, tool/API drift, or user-input edge case.

Payment: BTC `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## Starter CI checklist

- [ ] Pin model/provider/version where possible; log exact runtime metadata.
- [ ] Keep 10-30 tiny golden tasks under version control.
- [ ] Require deterministic fixture data for retrieval and tool responses.
- [ ] Track max tool calls and max token/spend budget per task.
- [ ] Assert final answer properties instead of exact strings where possible.
- [ ] Include at least one malicious/irrelevant input per workflow to verify boundaries.
- [ ] Run evals before prompt changes, dependency upgrades, and provider switches.
- [ ] Store failed traces with redacted secrets and enough context to reproduce.
- [ ] Review flaky tests weekly; delete or rewrite tests that cannot be made actionable.
- [ ] Publish a simple pass-rate trend so regressions are visible before customers report them.

## Safe scope

No unauthorized testing, no credential access, no production traffic generation. Work is limited to user-provided/public artifacts and written recommendations.
