# AI Agent Cost-Claim Audit Pack

A fixed-scope productized service for founders and engineering leads who are publishing claims like “our agents built X for $Y” and need a fast credibility check before launch, investor updates, or customer demos.

## Demand signal

Hacker News / public tech-news discussion is repeatedly surfacing AI-agent cost and capability claims, including skepticism around stories such as agents building complex software cheaply. The monetizable pain point is not debate; it is helping teams avoid exaggerated launch claims, hidden human labor, reproducibility gaps, and embarrassing post-launch scrutiny.

## $50 fixed-scope offer

**Price:** $50 equivalent in BTC  
**Payment address:** `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`  
**Deliverable:** one-page claim audit within 24 hours after payment confirmation and receipt of materials.

### What the buyer sends

- Public draft, landing page, blog post, demo script, or investor-update excerpt.
- Claimed cost/time numbers, if any.
- Brief description of human involvement, tools, model names, and retries.
- Optional: logs, screenshots, commit history, or build notes.

### What they receive

- Claim-risk score: **green / yellow / red**.
- Reproducibility checklist.
- Hidden-labor and hidden-cost table.
- Safer wording alternatives.
- Evidence gaps to fill before publishing.
- 3-line executive summary suitable for internal sharing.

## Audit checklist

### 1. Cost completeness

- Model/API spend included?
- Tooling/subscription spend included?
- Compute and storage included?
- Human review, prompting, debugging, deployment, and QA time included?
- Failed attempts and retries included?
- One-time setup separated from repeatable marginal cost?

### 2. Agent autonomy clarity

- Which steps were fully autonomous?
- Which steps required human intervention?
- Were prompts, constraints, and task definitions written by humans?
- Were outputs selected from multiple attempts?
- Was code manually edited after generation?

### 3. Reproducibility

- Can the result be reproduced from a clean environment?
- Are model versions pinned?
- Are prompts and configuration archived?
- Are random seeds or nondeterministic steps documented?
- Is there an independent verification path?

### 4. Scope realism

- Does “built an operating system/app/platform” actually mean prototype, demo, scaffold, or production-ready system?
- Are security, tests, packaging, deployment, accessibility, docs, and maintenance included?
- Are external libraries or templates fairly credited?

### 5. Safer claim rewrites

Replace broad claims like:

> “AI agents built this for $916.”

With scoped claims like:

> “Using AI coding agents, we produced a working prototype for $916 in direct API/tooling costs, excluding human planning, review, deployment, and post-generation QA.”

Or:

> “Agents automated X% of implementation tasks; humans handled architecture, acceptance criteria, review, and release decisions.”

## One-page report template

```text
AI Agent Claim Audit

Claim reviewed:
Risk rating: Green / Yellow / Red
Main risk:

Cost table:
- Direct model/tool cost:
- Human time excluded/included:
- Infrastructure/subscriptions:
- Failed attempts/retries:
- Repeatable marginal cost estimate:

Autonomy table:
- Agent-only steps:
- Human-guided steps:
- Human-edited steps:

Evidence gaps:
1.
2.
3.

Recommended wording:

Executive summary:
```

## Upsell path

If the buyer needs more than the $50 audit:

- $150: full claim rewrite + evidence appendix.
- $300: reproducibility packet with prompt/log archive structure.
- $500+: ongoing launch-risk review for AI-agent product announcements.

## Positioning copy

**Before you publish a big AI-agent cost claim, get a fast credibility audit.** I check whether the claim is complete, reproducible, and safely worded, then return a one-page report you can act on immediately. Fixed scope: $50 in BTC.
