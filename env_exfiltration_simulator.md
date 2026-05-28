# Agent `.env` Exfiltration Simulator — $50 Fixed-Scope Offer

## Demand signal
Hacker News current search for `AI agent` surfaced: **“Coding agent can read your .env file”**. The recurring buyer pain is not abstract model quality; it is whether coding/browser agents can silently access secrets, logs, local config, and CI variables during normal automation.

## Productized deliverable
A safe, non-destructive audit that proves where an AI coding agent or local automation stack can read secrets and produces a patch plan.

**Price:** $50 equivalent, payable in BTC to `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`.

## What the buyer gets
- 30-minute repo/workspace review focused only on secret exposure surfaces.
- A redacted findings report: no secret values copied, stored, or transmitted.
- A permission-boundary checklist for agent tools, shell commands, test runners, and CI.
- A minimal `.gitignore` / `.env.example` / secret-scanning workflow patch suggestion.
- Optional local-only simulator script showing which files are readable by automation.

## Safety rules
- Never request production secrets.
- Never paste or transmit secret values.
- Use placeholder probes only (`FAKE_SECRET_DO_NOT_USE`).
- Report file paths and risk levels, not confidential content.
- Do not bypass permissions, policies, or access controls.

## Fast audit checklist
1. Does the repo contain `.env`, `.env.*`, credentials JSON, private keys, wallet files, or API token dumps?
2. Are agent tools allowed broad shell/file access without path allowlists?
3. Are CI variables exposed to pull-request jobs or untrusted generated code?
4. Do logs, traces, screenshots, or prompt transcripts include environment variables?
5. Are generated patches or chat transcripts uploaded to third-party tools by default?
6. Is there a documented recovery path: rotate keys, revoke tokens, purge logs?

## Suggested lightweight patch
```yaml
# .github/workflows/secret-scan.yml
name: secret-scan
on: [pull_request, push]
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: gitleaks/gitleaks-action@v2
```

```gitignore
.env
.env.*
*.pem
*.key
*.p12
service-account*.json
```

## One-line landing copy
“Worried your AI coding agent can read `.env`? I’ll run a redacted, safe secret-exposure audit and deliver a fix checklist for $50 in BTC.”
