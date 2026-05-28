# Coding Agent `.env` Leak Guard — $50 Fixed-Scope Offer

## Demand signal

Public HN search on 2026-05-28 surfaced a current item titled **"Coding agent can read your .env file"** pointing to secure AI-agent secret access guidance. The recurring pain: teams are adopting coding agents quickly, but many repos still expose `.env`, API keys, local credentials, and production-like config to agent tools by default.

## Buyer

Small SaaS teams, AI tool builders, and agencies using Claude Code, Codex-like CLIs, Cursor, or background coding agents in real repos.

## Fixed-scope deliverable

For **$50 in BTC**, deliver a lightweight repo-specific guard pack:

1. Secret exposure risk map for one repo
2. Agent-safe ignore policy (`.agentignore` / tool-specific exclusions where applicable)
3. `.env.example` cleanup recommendations
4. Preflight checklist for running coding agents safely
5. Optional local scan script that flags likely secrets before agent runs

Payment address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## 30-minute execution checklist

- [ ] Inspect repo tree for `.env`, `.env.*`, credentials, key material, service-account JSON, wallet files, private keys, deploy config
- [ ] Check `.gitignore` and agent/tool ignore files
- [ ] Identify high-risk files an agent should not read by default
- [ ] Create recommended denylist patterns
- [ ] Draft safe `.env.example` conventions
- [ ] Add a pre-agent-run command such as `python scripts/agent_secret_preflight.py`

## Suggested denylist patterns

```gitignore
.env
.env.*
!.env.example
*.pem
*.key
*.p12
*.pfx
*service-account*.json
*credentials*.json
*secret*
*secrets*
wallet.dat
id_rsa
id_ed25519
.aws/
.gcloud/
```

## Safe preflight script concept

```python
#!/usr/bin/env python3
from pathlib import Path
import re

PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY-----"),
]
SKIP_DIRS = {'.git', 'node_modules', '.venv', 'venv', 'dist', 'build'}

for path in Path('.').rglob('*'):
    if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
        continue
    try:
        text = path.read_text(errors='ignore')[:200000]
    except Exception:
        continue
    if any(p.search(text) for p in PATTERNS):
        print(f"POSSIBLE_SECRET {path}")
```

## Outreach-safe positioning

> I help teams run coding agents without accidentally exposing `.env` files or production credentials. Fixed-scope repo guard pack: ignore rules, preflight scan, and safe-agent checklist for $50 BTC. No access to your credentials required; you can run the checks locally.

## Success criteria

- Buyer can run agent tools with a narrower readable surface
- Secrets are replaced with examples or placeholders
- Risky files are excluded before agent execution
- No credentials are requested, copied, stored, or transmitted
