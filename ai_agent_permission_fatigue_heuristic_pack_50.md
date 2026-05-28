# AI Agent Permission Fatigue Heuristic Pack — $50 Quick Fix

**Demand signal:** Hacker News top-story discussion around "Continue? Y/N", a game about AI agent permission fatigue, indicates recurring developer/operator pain: agents either ask for approval too often or take risky actions without enough friction.

## $50 outcome
A lightweight review of one agent workflow that produces:

1. A permission-friction map
2. A safe-action allowlist
3. A high-risk action escalation list
4. Better confirmation copy for irreversible actions
5. A 10-case regression checklist to prevent future prompt/tool changes from reintroducing fatigue

Payment: BTC accepted at `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`.

## 20-minute audit workflow

### 1. Inventory tool calls
Create a table:

| Tool/action | Frequency | User-visible risk | Current permission behavior | Recommendation |
|---|---:|---|---|---|
| Read/search local docs | High | Low | Ask every time | Auto-allow within workspace |
| Run tests/builds | Medium | Low/Medium | Ask sometimes | Auto-allow with timeout/logging |
| Edit files | Medium | Medium | Ask broad approval | Batch edits + diff summary |
| Network publish/post | Low | High | May be implicit | Always explicit confirmation |
| Delete/overwrite data | Rare | High | Varies | Require typed confirmation or dry-run |

### 2. Classify actions

**Auto-allow candidates**
- Read-only repo inspection
- Searching public docs
- Running non-destructive tests
- Creating new local artifacts
- Formatting/linting generated files

**Batch-confirm candidates**
- Multi-file edits
- Dependency installs
- Long-running jobs
- Local database migrations on disposable/dev data

**Always-confirm candidates**
- Public posting or messaging
- Payments or financial transactions
- Credential/secret changes
- Production deploys
- Destructive deletes or irreversible overwrites
- Actions that impersonate a user or contact third parties

### 3. Replace vague prompts
Bad confirmation:
> Continue? Y/N

Better confirmation:
> I will edit 3 files in `src/`, run tests, and show a diff. No network publishing or destructive deletion. Continue?

For high-risk actions:
> High-risk action: publish this message publicly from your account. Destination: X. Exact content below. Reply `PUBLISH` to proceed.

### 4. Regression tests
Run these after every agent prompt/tool-policy change:

- Low-risk read does not ask approval repeatedly.
- Repeated test runs are batched or auto-approved after first confirmation.
- File edits show concise diff summary before completion.
- Public post requires explicit confirmation.
- Payment action requires explicit confirmation.
- Delete action offers dry-run/trash path first.
- Secret-bearing file is never pasted into chat/logs.
- Network request destination is visible for medium/high-risk calls.
- Long-running command has timeout and cancellation note.
- Agent explains *why* a confirmation is required when blocking.

## Deliverable format

```md
# Permission Fatigue Audit

## Workflow reviewed
...

## Top friction points
1. ...
2. ...
3. ...

## Actions to auto-allow
- ...

## Actions to batch-confirm
- ...

## Actions to always-confirm
- ...

## Replacement confirmation copy
- ...

## Regression checklist result
- Pass/fail table
```

## Minimal implementation policy snippet

```txt
Default to autonomous execution for reversible, local, low-risk actions.
Ask for confirmation only when an action is public, financial, credential-related,
destructive, production-impacting, or meaningfully outside the user's stated scope.
When asking, describe exact action, destination, reversibility, and required user reply.
Batch low/medium-risk confirmations to avoid repeated Continue? prompts.
```
