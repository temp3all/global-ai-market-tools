# AI Agent Prompt/Model Regression Eval Pack — $50 Fixed Scope

## Demand signal
Recent public HN discussion asked how teams catch AI agent regressions after changing a prompt or model. The pain: a failure gets fixed once, then quietly returns after a later model/prompt update and is discovered by users instead of tests.

## Buyer
Small teams shipping AI agents, RAG workflows, coding assistants, support bots, or internal automation that change prompts/models frequently but do not yet have a formal eval suite.

## $50 deliverable
For one AI workflow/agent, I produce a lightweight regression pack with:

1. **Regression inventory** — 10–20 likely repeat-failure cases based on the agent role, tools, and known incidents.
2. **Golden test table** — CSV/Markdown cases with input, expected behavior, failure mode, severity, and owner.
3. **Prompt/model change gate** — checklist for what must pass before a prompt/model swap ships.
4. **Log review rubric** — simple columns for spotting repeated failures from production traces without collecting secrets.
5. **1-page summary** — top 3 risks and next fixes.

## What I need
- Agent purpose and short system/developer prompt excerpt with secrets removed.
- 3–10 examples of good/bad behavior, anonymized.
- Current model/provider and planned prompt/model change.

## What I will not do
- No credential access.
- No production login.
- No private data exfiltration.
- No fake engagement or spam.
- No bounty/quest/contest work.

## Turnaround
Same day when inputs are provided.

## Payment
Fixed scope: **$50 equivalent in BTC** after delivery acceptance.

BTC address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## Reusable regression table template

| id | user/task input | expected behavior | must not do | failure mode guarded | severity | pass/fail | notes |
|---|---|---|---|---|---|---|---|
| R001 | Normal happy-path task | Completes with cited/traceable steps | Invent facts or skip required check | Hallucinated completion | High |  |  |
| R002 | Ambiguous request | Asks concise clarifying question or states assumption | Executes risky action blindly | Overconfident automation | Medium |  |  |
| R003 | Prompt injection in retrieved text | Ignores external instruction and follows system policy | Reveal secrets or change role | Instruction hijack | Critical |  |  |
| R004 | Tool unavailable/error | Reports failure and safe fallback | Pretend action succeeded | Silent tool failure | High |  |  |
| R005 | Previously fixed bug repro | Maintains fixed behavior | Regress to old behavior | Reintroduced known bug | High |  |  |

## Prompt/model change gate

Before shipping a prompt/model update:

- [ ] Run all high/critical regression cases.
- [ ] Compare outputs against previous accepted behavior.
- [ ] Check secret/tool boundary cases.
- [ ] Review at least 10 recent production traces for repeated failure patterns.
- [ ] Record model, prompt version, date, and pass/fail notes.
- [ ] Roll back or add a new regression case for any repeated failure.
