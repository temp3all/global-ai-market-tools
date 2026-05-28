# AI Agent Launch Risk Checklist (Global, 2026)

Derived from recurring public incidents discussed on Hacker News: agent misfires, unsafe automation, and production-impacting actions.

## Why this matters
Teams are shipping autonomous coding/ops agents quickly. Public demand is growing for practical, lightweight risk controls before launch.

## 10-point pre-launch checklist

1. **Hard environment separation**
   - Dev/staging/prod credentials must be isolated.
   - Agent cannot access production secrets by default.

2. **Scoped permissions**
   - Use least privilege tokens.
   - Time-bound elevated access.

3. **Human approval gates**
   - Require explicit approval for destructive actions (delete, migration, force push).
   - Require dual approval for production-impacting steps.

4. **Action allowlist**
   - Define permitted command classes.
   - Block shell/network/file operations outside policy.

5. **Prompt + policy versioning**
   - Track prompt changes like code.
   - Rollback path for bad behaviors.

6. **Replayable audit logs**
   - Store prompts, tool calls, outputs, and approvals.
   - Enable incident reconstruction.

7. **Kill switch + circuit breaker**
   - One-click stop for active runs.
   - Auto-stop on anomaly thresholds.

8. **Synthetic failure drills**
   - Test adversarial prompts, tool misuse, and malformed input.
   - Validate fail-safe defaults.

9. **Cost and rate limits**
   - Per-task and daily budget caps.
   - Alerting on spikes in API/tool usage.

10. **Post-incident template ready**
   - Root-cause format, corrective action owner, deadline.
   - Share sanitized learnings publicly when possible.

## Productized $50 deliverable angle
Offer a "48-hour Agent Risk Sweep" using this checklist:
- Risk scorecard (0-100)
- Top 5 high-risk gaps
- Priority remediation plan
- Minimal policy YAML starter

Payment BTC: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`
