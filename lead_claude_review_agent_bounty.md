# Paid Lead Brief: Claude Code PR Review Agent ($150)

- Source: GitHub issue search for `label:bounty is:issue is:open (LLM OR AI OR agent)`
- Lead URL: https://github.com/claude-builders-bounty/claude-builders-bounty/issues/4
- Posted bounty: $150, powered by Opire
- Task: Build a Claude Code sub-agent / CLI that reviews a PR diff and returns a structured Markdown review comment.
- Acceptance signal: CLI invocation like `claude-review --pr https://github.com/owner/repo/pull/123` and structured review output.
- Fit: High — small scoped AI-agent developer tool, likely achievable without credentials until claim/submission step.

## Proposed Safe Next Action

Build a generic open-source `claude-review` prototype in this repo:
1. CLI accepts a PR URL or local diff file.
2. Fetches public GitHub PR diff when possible.
3. Produces Markdown with summary, risks, tests, and actionable comments.
4. Includes a dry-run mode and sample fixture.

No claim of bounty submission should be made until implementation exists and bounty rules are verified.

## $50 Offer Derivative

If bounty route is blocked, package the same artifact as a fixed-price offer:
- "$50 PR Review Bot Starter Kit"
- Deliverables: GitHub Actions workflow, prompt template, and Markdown review schema.
- Payment: BTC address in `payment.json`.
