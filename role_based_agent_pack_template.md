# Role-Based AI Agent Pack Template

Demand signal: Hacker News showed interest in simple markdown-based AI agents mapped to recognizable organizational roles/skills. The buyer pain is not "more agents"; it is making AI assistance legible to managers, reviewers, and non-technical stakeholders.

Use this template to package a paid $50 starter pack for a company, community, or open-source project.

## Offer

**$50 BTC — Role-Based Agent Pack Starter**

I convert a public role framework, team handbook, product docs, or support process into 3–5 copy/paste-ready AI agent markdown files.

Payment address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## Deliverables

- 3–5 role agent markdown files
- Clear scope and refusal rules per role
- Input/output format for each agent
- Handoff checklist between agents
- One smoke-test prompt per role
- 24h turnaround after source docs are provided

## Good target niches

- SaaS support teams needing triage/reply/checklist agents
- Dev teams needing reviewer/tester/release-manager agents
- Compliance-heavy startups needing auditable role boundaries
- Open-source maintainers needing issue triage and docs helper agents
- Agencies standardizing client intake and QA

## Agent file skeleton

```md
# Agent: [Role Name]

## Purpose
[One sentence describing the job this role performs.]

## Source authority
Use only:
- [Doc/link 1]
- [Doc/link 2]
- User-provided context in the current conversation

If information is missing, ask for it or mark it as unknown. Do not invent policy.

## Responsibilities
- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

## Non-responsibilities
- Do not [boundary 1]
- Do not [boundary 2]
- Escalate [case] to [role/person]

## Standard workflow
1. Restate the task and constraints.
2. Inspect relevant source authority.
3. Produce the requested output in the format below.
4. Add risks, unknowns, or escalation notes.

## Output format
- Summary:
- Decision/recommendation:
- Evidence:
- Risks/unknowns:
- Next action:

## Smoke test
Prompt: [Example realistic task]
Expected: [What a good answer should include]
```

## Fast production workflow

1. Collect 1–3 public docs or pasted private docs from buyer.
2. Extract repeated nouns: roles, responsibilities, decisions, handoffs.
3. Create one agent per real-world role, not per vague AI capability.
4. Add refusal/scope boundaries first; then add workflow.
5. Run one smoke test per agent and patch vague instructions.

## Upsell path

- $50 starter: 3–5 markdown agents
- $150 implementation: custom test prompts plus repo-ready folder structure
- $300 team pack: 10+ roles, examples, and onboarding guide

## Non-spam distribution

Publish as a public repo artifact, mention in relevant build logs or owned channels only, and respond only when someone explicitly asks for AI agent role design help.
