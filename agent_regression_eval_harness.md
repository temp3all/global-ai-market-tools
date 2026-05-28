# AI Agent Regression Eval Harness

Demand signal: a current Hacker News Ask HN thread asked how teams catch AI agent regressions after prompt/model changes. The pain is practical: a fixed failure reappears silently after a prompt, model, or tool update.

This repo now includes `agent_regression_eval_harness.py`, a dependency-free smoke-test runner for agent behavior.

## What it checks

Each eval case can assert:

- required strings in the agent output (`must_include`)
- forbidden strings in the agent output (`must_not_include`)
- maximum execution time (`max_seconds`)
- non-zero runner exits

This is not a full eval platform. It is a fast CI guardrail for teams that currently have nothing.

## Quick start

Create `eval_cases.json`:

```json
[
  {
    "id": "refund-policy-basic",
    "input": "Can I get a refund after 45 days?",
    "must_include": ["30 days"],
    "must_not_include": ["guaranteed refund"],
    "max_seconds": 20
  }
]
```

Create a runner command that reads user input from stdin and prints the agent result to stdout, then run:

```bash
python agent_regression_eval_harness.py \
  --cases eval_cases.json \
  --runner './run_agent.sh' \
  --json-out agent_regression_results.json
```

Exit code is `0` only if all cases pass, so it can be dropped into GitHub Actions or any CI.

## Suggested paid service angle

Offer a fixed-price setup:

- convert the team's top 10 historical agent failures into regression cases
- wire this harness into CI
- add a weekly regression report
- define a minimal policy for prompt/model changes

BTC payment address for implementation support: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`
