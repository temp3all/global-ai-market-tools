# $50 AI Agent Tool-Call Policy Quick Audit

A fixed-scope, non-invasive review for teams shipping Python AI agents with tool calls, MCP-style tools, shell/browser actions, or workflow orchestration.

Demand signal: current GitHub repository activity around AI agent control/governance, runnable specs, and production tool-call interception suggests builders need practical policy checks before agents can safely operate with real tools.

## What you get for $50

- Review of one public repo, docs folder, or pasted tool-call configuration.
- A concise risk table covering:
  - tool permission boundaries,
  - argument validation,
  - dry-run / confirmation gates,
  - logging and replayability,
  - secret/path/network allowlists,
  - failure-mode handling.
- A copy-paste `tool_policy.yaml` starter file tailored to the reviewed project.
- Three concrete pull-request-sized fixes ranked by impact.

## Safe scope

I do **not** request credentials, exploit systems, bypass access controls, or run destructive actions. Review is based on public code/docs or user-provided snippets only.

## Buyer instructions

Send:

1. repo/docs URL or pasted tool-call config,
2. agent runtime/framework if known,
3. the tools the agent can invoke,
4. preferred output format: Markdown, YAML, or GitHub issue text.

Payment metadata: BTC `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`.

## Starter `tool_policy.yaml`

```yaml
version: 1
agent_tool_policy:
  default: deny
  tools:
    read_file:
      allow: true
      constraints:
        paths_allow:
          - ./docs/**
          - ./src/**
        max_bytes: 200000
    write_file:
      allow: true
      constraints:
        paths_allow:
          - ./drafts/**
        require_diff_preview: true
        require_human_confirm: true
    shell:
      allow: conditional
      constraints:
        commands_allow:
          - pytest
          - npm test
          - python -m pytest
        network: false
        destructive_patterns_deny:
          - rm -rf
          - curl *|sh
          - sudo
    browser:
      allow: conditional
      constraints:
        domains_allow: []
        no_login: true
        no_forms_without_confirm: true
  logging:
    record_tool_name: true
    record_arguments: redacted
    record_result_hash: true
    retain_days: 14
  secrets:
    env_access: deny_by_default
    redact_patterns:
      - "(?i)api[_-]?key"
      - "(?i)secret"
      - "(?i)token"
```

## Quick self-check

- Can every tool call be explained to a user in one sentence?
- Can a bad prompt make the agent access files outside the project?
- Are network destinations explicit and minimal?
- Are shell commands constrained to known-safe commands?
- Is there a replay log for debugging regressions?
- Are secrets redacted before LLM context injection?
