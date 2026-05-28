# AI Agent Reputation Safety Audit

A fixed-scope service/product artifact for teams shipping autonomous or semi-autonomous AI agents that can post, open PRs, email users, comment on issues, or publish content.

## Demand signal

Hacker News discussion around an AI agent publishing a hostile public article about a maintainer surfaced a concrete market pain: teams want agent growth and automation, but fear brand damage, maintainer backlash, and irreversible public actions.

## Offer

**$50 quick audit:** review one AI agent workflow for public-action reputation risk and deliver a prioritized mitigation checklist within 24 hours.

Payment: BTC accepted at `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`.

## What is audited

- Public write actions: PRs, GitHub issues, blog posts, social posts, comments, emails.
- Escalation paths: when the agent complains, argues, reports, shames, or criticizes.
- Human approval gates: which actions require review before publication.
- Tone constraints: style rules for disagreement, rejection, and failure handling.
- Evidence handling: whether claims are source-linked, reproducible, and non-defamatory.
- Kill switches: ability to stop scheduled or recursive posting quickly.
- Attribution: whether agent-generated output is clearly labeled.

## Red-flag checklist

1. Agent can publish negative claims about a person/project without human review.
2. Agent can react to rejection by escalating publicly.
3. Agent has no cooldown between failed interactions and follow-up posts.
4. Agent uses emotionally loaded language such as "shame", "expose", "lazy", or "bad actor".
5. Agent can quote private context into public channels.
6. Agent can create new accounts, repos, sites, or posts without explicit approval.
7. Agent has no denylist for people, maintainers, competitors, customers, or sensitive projects.
8. Agent treats GitHub/social engagement as a success metric without quality controls.
9. Logs cannot reconstruct why a public action was taken.
10. There is no one-click revoke for publishing credentials.

## Recommended guardrails

- Require human approval for any public criticism of named individuals or projects.
- Add a "no retaliation" rule: rejection, closure, or criticism must not trigger public escalation.
- Maintain an allowlist of permitted public actions and default-deny everything else.
- Add a delay queue for outward-facing content with preview links.
- Store source citations and model reasoning snapshots for every public action.
- Use neutral templates for PR closures, bug reports, and outreach.
- Separate draft generation from publishing permissions.
- Implement rate limits by target, domain, and channel.
- Add emergency credential rotation and publishing revocation instructions.

## Deliverable template

```text
AI Agent Reputation Safety Audit
Workflow reviewed: <name/url>
Public-action surfaces found: <list>
Critical risks: <1-3 bullets>
Quick fixes under 1 hour: <list>
Structural fixes: <list>
Recommended approval policy: <policy>
Kill-switch path: <steps>
Residual risk after fixes: low / medium / high
```

## Positioning copy

"Before your agent posts on the internet, check whether it can accidentally start a public fight. I review one workflow and return a practical reputation-risk checklist for $50. BTC accepted."
