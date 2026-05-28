#!/usr/bin/env python3
"""
Agent Regression Eval Harness

A tiny, dependency-free harness for catching AI agent regressions after prompt,
model, or tool changes. It is intentionally simple so a solo developer or small
team can add it to CI in minutes.

Usage:
  1. Create eval_cases.json (see sample at bottom of this file).
  2. Implement --runner as a command that accepts the user input on stdin and
     prints the agent output to stdout.
  3. Run: python agent_regression_eval_harness.py --cases eval_cases.json --runner './run_agent.sh'

Case schema:
[
  {
    "id": "refund-policy-basic",
    "input": "Can I get a refund after 45 days?",
    "must_include": ["30 days"],
    "must_not_include": ["guaranteed refund"],
    "max_seconds": 20
  }
]

Payment/offer metadata: custom implementation support available for BTC to
1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ
"""
import argparse, json, subprocess, sys, time
from pathlib import Path


def run_case(case, runner):
    started = time.time()
    proc = subprocess.run(
        runner,
        input=case.get("input", ""),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        timeout=case.get("max_seconds", 30),
    )
    elapsed = time.time() - started
    out = proc.stdout.strip()
    failures = []
    if proc.returncode != 0:
        failures.append(f"runner exited {proc.returncode}: {proc.stderr.strip()[:300]}")
    for needle in case.get("must_include", []):
        if needle.lower() not in out.lower():
            failures.append(f"missing required text: {needle!r}")
    for needle in case.get("must_not_include", []):
        if needle.lower() in out.lower():
            failures.append(f"forbidden text present: {needle!r}")
    return {
        "id": case.get("id", "unnamed"),
        "passed": not failures,
        "failures": failures,
        "elapsed_seconds": round(elapsed, 3),
        "output_preview": out[:500],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", required=True, help="Path to eval cases JSON")
    ap.add_argument("--runner", required=True, help="Shell command that runs the agent")
    ap.add_argument("--json-out", default="agent_regression_results.json")
    args = ap.parse_args()

    cases = json.loads(Path(args.cases).read_text())
    results = [run_case(c, args.runner) for c in cases]
    summary = {
        "total": len(results),
        "passed": sum(1 for r in results if r["passed"]),
        "failed": sum(1 for r in results if not r["passed"]),
        "results": results,
    }
    Path(args.json_out).write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
