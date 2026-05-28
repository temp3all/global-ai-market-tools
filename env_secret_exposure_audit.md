# Coding Agent .env / Secret Exposure Audit — $50 Fixed-Scope Offer

## Demand signal
Recent public Hacker News discussion surfaced a practical fear: coding agents can read `.env` files and other local secrets. Teams using AI coding tools need a fast, non-invasive check that their repo and agent instructions reduce accidental secret exposure.

## Fixed-scope deliverable
For **$50 in BTC**, deliver a concise repo safety review covering:

1. Secret-bearing files likely visible to coding agents
2. `.gitignore` / `.dockerignore` / package ignore gaps
3. Agent instruction files that should explicitly forbid secret access or disclosure
4. CI, examples, and tests that may contain real-looking credentials
5. A prioritized remediation checklist with copy-paste patches where obvious

Payment address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## Safe operating rules
- No credential use.
- No attempts to authenticate to third-party services.
- No exfiltration of secret values.
- Report only file paths, variable names, and redacted examples.
- Work only on public repos or explicitly provided archives.

## Intake checklist
Ask for one of:

- Public GitHub/GitLab repo URL, or
- Zip/tar archive with permission to inspect, or
- Specific files pasted into a private workspace

Also ask:

- Which agent tools are in use? (Cursor, Claude Code, Codex, Copilot Workspace, etc.)
- Are agent instruction files present? (`AGENTS.md`, `.cursorrules`, `CLAUDE.md`, etc.)
- Are sample env files expected to contain placeholders only?

## Audit commands
Run locally on an authorized copy only:

```bash
# Secret-bearing file names
find . -type f \
  \( -name '.env*' -o -name '*secret*' -o -name '*credential*' -o -name '*token*' -o -name '*key*' \) \
  -not -path './.git/*'

# Ignore coverage
find . -maxdepth 3 -type f \
  \( -name '.gitignore' -o -name '.dockerignore' -o -name '.npmignore' -o -name '.cursorignore' \)

# Agent instruction files
find . -maxdepth 4 -type f \
  \( -name 'AGENTS.md' -o -name 'CLAUDE.md' -o -name '.cursorrules' -o -name 'GEMINI.md' \)

# High-signal tokens, values redacted in reporting
python3 - <<'PY'
import os,re
patterns=[
  r'(?i)(api[_-]?key|secret|token|password|private[_-]?key)\s*[:=]',
  r'AKIA[0-9A-Z]{16}',
  r'-----BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY-----',
]
for root,dirs,files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in {'.git','node_modules','.venv','venv'}]
    for f in files:
        p=os.path.join(root,f)
        try: s=open(p,'r',errors='ignore').read()
        except Exception: continue
        for pat in patterns:
            if re.search(pat,s):
                print(p)
                break
PY
```

## Recommended agent policy snippet
Add to `AGENTS.md`, `CLAUDE.md`, or equivalent:

```md
## Secrets and credentials
- Do not read `.env`, private keys, credential stores, or files matching `*secret*`, `*token*`, `*credential*` unless the user explicitly asks for a security audit.
- Never print, summarize, transmit, commit, or reuse secret values.
- If a task appears to require a secret, stop and ask for a non-secret placeholder or documented configuration path.
- Prefer reporting variable names and file paths only, with values redacted.
```

## Report template

```md
# Secret Exposure Audit

Repo: <url/name>
Date: <yyyy-mm-dd>
Scope: passive local review; no credential use

## Executive summary
- Risk level: Low / Medium / High
- Main issue: <one sentence>

## Findings
1. <Severity> — <Path> — <Issue>
   - Evidence: variable/file name only, value redacted
   - Fix: <specific action>

## Quick patches
```diff
<optional patch>
```

## Agent policy
- Existing policy file: yes/no
- Recommended snippet added: yes/no

## Non-actions
- No secrets were copied, used, authenticated with, or transmitted.
```

## Distribution copy
"Worried your coding agent can read `.env` or leak local secrets? I’ll do a fixed-scope passive audit of one public/authorized repo for $50 BTC: ignore gaps, agent instruction hardening, real-secret risk patterns, and a remediation checklist. No credential use, no secret exfiltration."
