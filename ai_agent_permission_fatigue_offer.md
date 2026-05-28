# AI Agent Permission-Fatigue Hardening Sprint (Fixed Scope)

## Demand signal
Inspired by current Hacker News discussion around repeated AI-agent confirmation prompts and operator fatigue ("Continue? Y/N" pattern), which creates real security and usability risk in production workflows.

## Offer (global, remote)
I will harden your coding/ops agent workflow to reduce blind approvals and improve safe autonomy.

### Scope (48-hour turnaround)
1. **Prompt/approval flow audit**
   - Map high-frequency confirmation points
   - Identify low-signal prompts that train unsafe "yes-clicking"
2. **Policy redesign**
   - Convert repetitive approvals into policy-based allow/deny rules
   - Keep explicit approval only for high-risk actions (secrets, deletes, production writes)
3. **Risk-tier action matrix**
   - Tier 0: auto-allow (read-only, formatting, lint)
   - Tier 1: bounded allow (test runs, branch-local edits)
   - Tier 2: explicit approval (networked writes, prod changes, credential access)
4. **Operator runbook**
   - Escalation rules
   - Daily review checklist
   - Incident rollback steps

## Deliverables
- `permission_flow_map.md`
- `risk_tier_matrix.md`
- `agent_guardrail_policy.md`
- `operator_runbook.md`

## Price
- **$50 fixed scope** (single repo/workflow)
- Payment: **BTC**
- Address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## Positioning copy (for outreach)
"If your team is spamming Y/N confirmations to keep agents safe, you may be increasing risk through approval fatigue. I’ll implement a practical risk-tiered approval policy in 48h for a fixed $50 (BTC)."
