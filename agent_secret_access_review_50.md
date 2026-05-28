# $50 Coding Agent Secret Access Review

Demand signal: Hacker News discussions on coding agents reading `.env` files and secrets-manager access show a concrete buyer pain: teams want to adopt coding agents without giving them silent access to production credentials.

## Fixed-scope offer

For **$50 in BTC**, deliver a compact secret-access review for one repository or agent workspace.

BTC payment address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## What is reviewed

- `.env`, `.env.*`, config examples, Docker/Compose files, CI variables references, and local agent instructions.
- Agent tool permissions that can read files, shell out, browse, or call package/build scripts.
- Secret-manager usage patterns where an agent may request, print, copy, or persist credentials.
- Logs, traces, cache folders, generated artifacts, and screenshots that may accidentally retain secrets.

## Deliverable

A one-page markdown report with:

1. **Secret exposure map** — where sensitive values can be reached by the agent.
2. **Unsafe path examples** — up to 5 realistic, non-exfiltrating scenarios showing how a secret could leak into logs or prompts.
3. **Minimal guardrail patch list** — recommended `.gitignore`, agent instruction, CI masking, and tool-permission changes.
4. **Safe verification checklist** — commands/checks the team can run locally without sharing secrets.

## Non-goals

- No credential collection.
- No live exploitation.
- No unauthorized access.
- No production system interaction.

## Intake template

```text
Repo or folder to review:
Agent/tool used:
Allowed files to inspect:
Secret manager used, if any:
CI provider, if relevant:
Known concern:
Payment txid:
```

## Quick self-checklist

- [ ] `.env*` is ignored except `.env.example`.
- [ ] Agent instructions explicitly forbid printing, copying, summarizing, or committing secrets.
- [ ] CI masks known secret patterns in logs.
- [ ] Agent cannot read unrestricted home-directory files by default.
- [ ] Secret-manager calls require explicit human approval or scoped short-lived tokens.
- [ ] Agent traces are retained only after redaction.
