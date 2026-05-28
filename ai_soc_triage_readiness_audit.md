# AI SOC Triage Readiness Audit — $50 Fixed Scope

Demand signal: recent GitHub search for newly created AI security/SOC tools shows interest in AI-assisted alert fusion, purple-team drills, MITRE ATT&CK investigation, and agent-assisted triage. Small teams adopting these tools still need a fast readiness check before trusting an agent in the alert path.

## Offer

For **$50 in BTC**, I review one public or provided AI SOC / security-alert triage workflow and return a concise readiness report.

BTC payment address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## What you get

- Alert-input inventory: logs, tickets, SIEM exports, enrichment APIs, and human notes.
- Agent boundary map: what the agent may read, summarize, call, or modify.
- False-positive / false-negative risk table for common SOC use cases.
- MITRE ATT&CK mapping sanity check for generated investigations.
- Evidence-retention checklist so triage output remains auditable.
- Safe rollout plan: read-only shadow mode → analyst approval → limited automation.
- 5 concrete fixes ranked by impact and implementation effort.

## Scope limits

- No unauthorized access, exploit attempts, credential misuse, or live incident response.
- Public docs, pasted configuration, sample alerts, or owner-authorized repositories only.
- No bounty or contest submissions.
- One workflow/repo/system per $50 report.

## Input needed

Send any of:

1. Public repo/docs URL for the AI SOC or triage workflow.
2. Redacted sample alerts/tickets and the intended agent prompt/tool list.
3. Short description of the current analyst workflow and planned automation.

## Delivery format

A Markdown report with:

- Executive summary
- Risk matrix
- Agent boundary recommendations
- Auditability checklist
- Quick-win fixes
- Next-step implementation notes

## Why this exists

AI SOC tools can speed alert review, but the risk is silent over-trust: hallucinated root cause, missing evidence, unsafe tool permissions, or summaries that cannot be audited later. This fixed-scope audit gives teams a low-friction way to harden adoption before adding automation.
