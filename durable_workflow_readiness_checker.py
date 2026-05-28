#!/usr/bin/env python3
"""
Durable Workflow Readiness Checker

A tiny, dependency-free checklist/scorer for teams running AI agents or background
jobs that need to survive crashes, retries, deploys, rate limits, and human review.

Why it exists: public builder discussion keeps circling back to "just use Postgres"
for durable execution, but many agent/background-job systems still launch tasks
without idempotency keys, retry boundaries, resumable state, or audit trails.

Usage:
  python durable_workflow_readiness_checker.py --example > workflow_readiness_example.json
  python durable_workflow_readiness_checker.py workflow_readiness_example.json

Input: JSON object with boolean fields. Missing fields count as false.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class Check:
    key: str
    label: str
    weight: int
    remediation: str


CHECKS: List[Check] = [
    Check("persistent_state", "Task state is persisted outside process memory", 15, "Store run/job state in Postgres/SQLite/queue storage before executing side effects."),
    Check("idempotency_key", "Every external side effect has an idempotency key", 15, "Attach a deterministic idempotency key to payments, emails, API writes, and tool calls."),
    Check("retry_policy", "Retries are bounded and classified by error type", 10, "Use explicit max attempts, backoff, and non-retryable error classes."),
    Check("resume_pointer", "Long tasks have a checkpoint/resume pointer", 10, "Persist the last completed step/cursor so restarts continue instead of duplicate work."),
    Check("human_approval_gate", "Risky or paid actions require human approval", 10, "Gate spends, deletions, outbound messages, account changes, and public posts."),
    Check("audit_log", "All tool calls and decisions are audit logged", 10, "Write append-only logs with timestamp, actor, input summary, output summary, and status."),
    Check("timeout_and_lease", "Workers use timeouts/leases for claimed jobs", 10, "Add job leases that expire so crashed workers do not strand work forever."),
    Check("dead_letter_queue", "Failed jobs land in a reviewable dead-letter queue", 8, "Move exhausted jobs to a DLQ with error context and manual replay instructions."),
    Check("rate_limit_budget", "External API limits/cost budgets are enforced", 7, "Track per-run usage and stop before quota, spend, or token limits are exceeded."),
    Check("deployment_drain", "Deploys can drain or safely interrupt workers", 5, "Handle SIGTERM, stop claiming new jobs, and persist in-flight checkpoints."),
]


EXAMPLE: Dict[str, bool] = {
    "persistent_state": True,
    "idempotency_key": False,
    "retry_policy": True,
    "resume_pointer": False,
    "human_approval_gate": True,
    "audit_log": True,
    "timeout_and_lease": False,
    "dead_letter_queue": False,
    "rate_limit_budget": True,
    "deployment_drain": False,
}


def score(config: Dict[str, object]) -> Tuple[int, int, List[str], List[str]]:
    total = sum(c.weight for c in CHECKS)
    earned = 0
    passed: List[str] = []
    remediations: List[str] = []
    for check in CHECKS:
        if bool(config.get(check.key, False)):
            earned += check.weight
            passed.append(f"PASS {check.key}: {check.label} (+{check.weight})")
        else:
            remediations.append(f"FIX {check.key}: {check.remediation} ({check.weight} pts)")
    return earned, total, passed, remediations


def grade(percent: float) -> str:
    if percent >= 85:
        return "READY"
    if percent >= 65:
        return "NEEDS_MINOR_HARDENING"
    if percent >= 40:
        return "RISKY_FOR_PRODUCTION"
    return "FRAGILE"


def main() -> int:
    parser = argparse.ArgumentParser(description="Score durable workflow readiness for AI agents/background jobs.")
    parser.add_argument("input", nargs="?", help="JSON file containing boolean readiness fields")
    parser.add_argument("--example", action="store_true", help="Print example JSON input and exit")
    args = parser.parse_args()

    if args.example:
        print(json.dumps(EXAMPLE, indent=2, sort_keys=True))
        return 0

    if not args.input:
        parser.error("provide an input JSON file, or use --example")

    with open(args.input, "r", encoding="utf-8") as f:
        config = json.load(f)
    if not isinstance(config, dict):
        raise SystemExit("input must be a JSON object")

    earned, total, passed, remediations = score(config)
    pct = 100.0 * earned / total
    result = {
        "score": earned,
        "max_score": total,
        "percent": round(pct, 1),
        "grade": grade(pct),
        "passed": passed,
        "priority_fixes": remediations[:5],
        "all_fixes": remediations,
    }
    print(json.dumps(result, indent=2))
    return 0 if pct >= 65 else 2


if __name__ == "__main__":
    raise SystemExit(main())
