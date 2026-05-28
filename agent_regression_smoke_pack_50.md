# AI Agent Regression Smoke Pack — $50 fixed-scope offer

## Demand signal

Public Hacker News discussion/search on 2026-05-28 surfaced a direct founder/operator pain point:

> Teams fix a failure in an agent, change the prompt or model a week later, and the same failure quietly comes back. Nobody catches it until a user does.

This pack turns that recurring pain into a small, safe, fixed-scope deliverable for AI agent teams.

## What the buyer gets for $50

Within 24 hours, for one public repo, demo workflow, or provided prompt/spec:

1. **Regression map** — 5-10 likely failure modes after prompt/model/tool changes.
2. **Smoke test matrix** — copy-paste markdown table of test cases with inputs, expected behavior, and pass/fail criteria.
3. **Minimal eval harness** — language-agnostic pseudocode or Python skeleton for repeatable checks.
4. **Release gate checklist** — what must pass before shipping a prompt/model update.
5. **Cost notes** — suggestions to keep eval runs cheap.

No private credentials required. No unauthorized testing. Buyer provides only public links or redacted examples.

## Intake form

Send:

- Product/repo/demo URL
- One sentence describing the agent's job
- 2-3 examples of recent failures or unwanted behavior
- Current model/provider if public or shareable
- Constraints: latency, cost, safety, compliance, tone, etc.

Payment: **$50 BTC** to `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## Smoke test matrix template

| ID | Risk | Test input | Expected behavior | Fail condition | Priority |
|---|---|---|---|---|---|
| R1 | Old bug returns after prompt edit | Recreate the previously fixed user path | Agent avoids the old failure and explains limits | Same bad answer/action reappears | High |
| R2 | Tool call regression | Ask for a task requiring the main tool | Correct tool selected with valid arguments | Hallucinated result or wrong tool | High |
| R3 | Policy/permission drift | Ask for an action outside allowed scope | Agent refuses or asks for authorization | Performs/claims unauthorized action | High |
| R4 | Context truncation | Provide long but relevant context | Uses key facts and cites uncertainty | Ignores constraints or fabricates | Medium |
| R5 | Model migration drift | Run same cases on old/new model | Equivalent or improved result quality | New model breaks critical case | High |

## Minimal eval harness skeleton

```python
from dataclasses import dataclass

@dataclass
class Case:
    id: str
    prompt: str
    must_include: list[str]
    must_not_include: list[str]

CASES = [
    Case(
        id="R1_old_bug",
        prompt="PASTE REGRESSION PROMPT HERE",
        must_include=["EXPECTED_SAFE_SIGNAL"],
        must_not_include=["KNOWN_BAD_PATTERN"],
    ),
]

def call_agent(prompt: str) -> str:
    # Replace with your local dev/staging agent call.
    raise NotImplementedError

def check(case: Case) -> tuple[bool, str]:
    out = call_agent(case.prompt)
    missing = [s for s in case.must_include if s not in out]
    forbidden = [s for s in case.must_not_include if s in out]
    ok = not missing and not forbidden
    return ok, f"missing={missing} forbidden={forbidden} output={out[:300]!r}"

if __name__ == "__main__":
    failed = []
    for case in CASES:
        ok, detail = check(case)
        print(f"{case.id}: {'PASS' if ok else 'FAIL'} — {detail}")
        if not ok:
            failed.append(case.id)
    raise SystemExit(1 if failed else 0)
```

## Delivery note

This is intentionally a small smoke pack, not a full enterprise eval platform. The goal is to catch obvious regressions before users do.
