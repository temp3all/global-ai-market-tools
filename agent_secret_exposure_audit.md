# Coding Agent Secret Exposure Audit — $50 Fixed-Scope Offer

Demand signal: current Hacker News discussion around coding agents being able to read `.env` files and other local secrets. Teams adopting AI coding agents need a quick, practical audit before giving agents repository or shell access.

## What this delivers

A lightweight review of one repo/workspace for accidental agent access to secrets and high-risk files.

## Checklist

1. **Secret file inventory**
   - `.env`, `.env.*`, `*.pem`, `*.key`, cloud credential folders, package manager tokens, SSH configs.
   - Confirm whether files are ignored, encrypted, or accessible to agent tools.

2. **Agent tool permission map**
   - Which commands can the agent run?
   - Can it read arbitrary files outside the project?
   - Can it access browser/session/cookie/token stores?
   - Can it make network requests or push commits?

3. **Repo-level guardrails**
   - Add or improve `.gitignore` secret patterns.
   - Add a `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` section defining forbidden reads and write boundaries.
   - Add pre-commit secret scanning recommendation.

4. **Workflow hardening**
   - Use scoped test credentials for agent sessions.
   - Prefer secret managers or environment injection over plain files.
   - Run agents in isolated containers where possible.

5. **Deliverable**
   - One-page risk report.
   - Prioritized remediation list.
   - Optional PR with documentation/ignore-rule improvements.

## Fixed-scope price

$50 equivalent, BTC accepted: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## Positioning copy

"Before you let an AI coding agent loose on your repo, I’ll check whether it can see your real secrets, map the highest-risk access paths, and give you a practical hardening checklist in under 24 hours."
