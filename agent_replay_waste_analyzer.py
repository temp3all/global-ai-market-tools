#!/usr/bin/env python3
"""
Agent Replay Waste Analyzer

Dependency-free JSONL helper for AI-agent teams who are paying to re-run long
multi-step agents after a late failure. It estimates wasted rerun cost and points
to the most valuable checkpoint/replay boundaries.

Why it exists: a current Hacker News Show HN thread for an AI-agent replay
platform describes a concrete pain point: step 9/10 failures can force repeated
full reruns, burning real LLM/tool budget. This CLI gives a small, auditable
starting point for measuring that problem from exported trace logs.

Usage:
  python3 agent_replay_waste_analyzer.py --example > agent_trace_example.jsonl
  python3 agent_replay_waste_analyzer.py agent_trace_example.jsonl

JSONL format, one event per line:
  {"run_id":"r1","case_id":"invoice-7","step_id":"s1","step_index":1,
   "step_name":"fetch_invoice","status":"ok","cost_usd":0.02}

Recommended optional fields:
  total_steps, duration_ms, tool, model, error, replay_of_run_id, replay_from_step

Exit code:
  0 = analyzed successfully
  2 = invalid input
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

EXAMPLE_ROWS: List[Dict[str, Any]] = [
    {"run_id": "r1", "case_id": "invoice-7", "step_id": "s1", "step_index": 1, "total_steps": 10, "step_name": "load_pdf", "status": "ok", "cost_usd": 0.03, "duration_ms": 500},
    {"run_id": "r1", "case_id": "invoice-7", "step_id": "s2", "step_index": 2, "total_steps": 10, "step_name": "ocr", "status": "ok", "cost_usd": 0.12, "duration_ms": 1800},
    {"run_id": "r1", "case_id": "invoice-7", "step_id": "s8", "step_index": 8, "total_steps": 10, "step_name": "classify_tax", "status": "ok", "cost_usd": 0.40, "duration_ms": 2200},
    {"run_id": "r1", "case_id": "invoice-7", "step_id": "s9", "step_index": 9, "total_steps": 10, "step_name": "write_erp", "status": "failed", "cost_usd": 0.35, "duration_ms": 1400, "error": "bad tool args"},
    {"run_id": "r2", "case_id": "invoice-7", "step_id": "s1", "step_index": 1, "total_steps": 10, "step_name": "load_pdf", "status": "ok", "cost_usd": 0.03, "duration_ms": 500, "replay_of_run_id": "r1"},
    {"run_id": "r2", "case_id": "invoice-7", "step_id": "s2", "step_index": 2, "total_steps": 10, "step_name": "ocr", "status": "ok", "cost_usd": 0.12, "duration_ms": 1800, "replay_of_run_id": "r1"},
    {"run_id": "r2", "case_id": "invoice-7", "step_id": "s8", "step_index": 8, "total_steps": 10, "step_name": "classify_tax", "status": "ok", "cost_usd": 0.40, "duration_ms": 2200, "replay_of_run_id": "r1"},
    {"run_id": "r2", "case_id": "invoice-7", "step_id": "s9", "step_index": 9, "total_steps": 10, "step_name": "write_erp", "status": "ok", "cost_usd": 0.35, "duration_ms": 1300, "replay_of_run_id": "r1"},
]

FAIL_STATUSES = {"fail", "failed", "error", "exception", "crashed", "timeout"}


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as e:
                raise SystemExit(f"invalid JSONL {path}:{line_no}: {e}")
            if not isinstance(row, dict):
                raise SystemExit(f"invalid JSONL {path}:{line_no}: row must be an object")
            if not row.get("run_id") or not row.get("step_id"):
                raise SystemExit(f"invalid JSONL {path}:{line_no}: missing run_id or step_id")
            rows.append(row)
    return rows


def fnum(row: Dict[str, Any], key: str, default: float = 0.0) -> float:
    try:
        return float(row.get(key, default) or default)
    except (TypeError, ValueError):
        return default


def inum(row: Dict[str, Any], key: str, default: int = 0) -> int:
    try:
        return int(row.get(key, default) or default)
    except (TypeError, ValueError):
        return default


def group_by(rows: Iterable[Dict[str, Any]], key: str) -> Dict[str, List[Dict[str, Any]]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key, "unknown"))].append(row)
    return grouped


def run_summary(run_id: str, rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    ordered = sorted(rows, key=lambda r: (inum(r, "step_index"), str(r.get("step_id"))))
    cost = round(sum(fnum(r, "cost_usd") for r in ordered), 6)
    duration_ms = int(sum(fnum(r, "duration_ms") for r in ordered))
    failed = [r for r in ordered if str(r.get("status", "")).lower() in FAIL_STATUSES]
    max_step = max((inum(r, "step_index") for r in ordered), default=0)
    total_steps = max((inum(r, "total_steps") for r in ordered), default=max_step)
    fail_step = inum(failed[0], "step_index") if failed else None
    late_failure_ratio = round((fail_step / total_steps), 3) if fail_step and total_steps else None
    return {
        "run_id": run_id,
        "case_id": str(ordered[0].get("case_id", "unknown")) if ordered else "unknown",
        "steps_seen": len(ordered),
        "max_step_index": max_step,
        "total_steps": total_steps,
        "cost_usd": cost,
        "duration_ms": duration_ms,
        "failed": bool(failed),
        "failure_step_index": fail_step,
        "late_failure_ratio": late_failure_ratio,
        "first_error": str(failed[0].get("error", ""))[:160] if failed else "",
        "replay_of_run_id": str(ordered[0].get("replay_of_run_id", "")) if ordered else "",
        "replay_from_step": ordered[0].get("replay_from_step", "") if ordered else "",
    }


def checkpoint_suggestions(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    by_step: Dict[Tuple[int, str], Dict[str, Any]] = {}
    counts: Dict[Tuple[int, str], int] = defaultdict(int)
    costs: Dict[Tuple[int, str], float] = defaultdict(float)
    failures_after: Dict[Tuple[int, str], int] = defaultdict(int)

    for run_rows in group_by(rows, "run_id").values():
        ordered = sorted(run_rows, key=lambda r: (inum(r, "step_index"), str(r.get("step_id"))))
        failed_steps = [inum(r, "step_index") for r in ordered if str(r.get("status", "")).lower() in FAIL_STATUSES]
        first_fail = min(failed_steps) if failed_steps else None
        for row in ordered:
            idx = inum(row, "step_index")
            name = str(row.get("step_name") or row.get("step_id"))
            key = (idx, name)
            by_step.setdefault(key, {"step_index": idx, "step_name": name})
            counts[key] += 1
            costs[key] += fnum(row, "cost_usd")
            if first_fail and idx < first_fail:
                failures_after[key] += 1

    suggestions: List[Dict[str, Any]] = []
    for key, meta in by_step.items():
        replayed_cost = costs[key]
        score = replayed_cost * max(1, failures_after[key])
        if score <= 0:
            continue
        suggestions.append({
            **meta,
            "observed_executions": counts[key],
            "observed_cost_usd": round(replayed_cost, 6),
            "failures_after_step": failures_after[key],
            "checkpoint_value_score": round(score, 6),
        })
    return sorted(suggestions, key=lambda x: (-x["checkpoint_value_score"], x["step_index"]))[:5]


def analyze(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    runs = [run_summary(run_id, run_rows) for run_id, run_rows in sorted(group_by(rows, "run_id").items())]
    failed_late = [r for r in runs if r["failed"] and (r.get("late_failure_ratio") or 0) >= 0.7]
    replay_runs = [r for r in runs if r.get("replay_of_run_id")]

    rerun_cost_by_case: Dict[str, float] = defaultdict(float)
    rerun_count_by_case: Dict[str, int] = defaultdict(int)
    for r in replay_runs:
        rerun_cost_by_case[r["case_id"]] += float(r["cost_usd"])
        rerun_count_by_case[r["case_id"]] += 1

    cases = []
    for case_id in sorted(set(r["case_id"] for r in runs)):
        case_runs = [r for r in runs if r["case_id"] == case_id]
        cases.append({
            "case_id": case_id,
            "runs": len(case_runs),
            "failed_runs": sum(1 for r in case_runs if r["failed"]),
            "replay_runs": rerun_count_by_case.get(case_id, 0),
            "estimated_replay_cost_usd": round(rerun_cost_by_case.get(case_id, 0.0), 6),
        })

    total_cost = round(sum(float(r["cost_usd"]) for r in runs), 6)
    replay_cost = round(sum(rerun_cost_by_case.values()), 6)
    return {
        "runs_analyzed": len(runs),
        "events_analyzed": len(rows),
        "total_cost_usd": total_cost,
        "estimated_replay_cost_usd": replay_cost,
        "replay_cost_percent": round((100.0 * replay_cost / total_cost), 2) if total_cost else 0.0,
        "late_failures": failed_late,
        "cases": cases,
        "top_checkpoint_suggestions": checkpoint_suggestions(rows),
        "next_actions": [
            "Add checkpoints before the highest checkpoint_value_score steps.",
            "Record replay_from_step so future reports separate full reruns from partial replays.",
            "Gate side-effecting steps after replay with a tool-call diff or human review.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Estimate waste from full AI-agent reruns and suggest checkpoints.")
    parser.add_argument("trace", nargs="?", help="agent trace JSONL file")
    parser.add_argument("--example", action="store_true", help="print example JSONL and exit")
    args = parser.parse_args()

    if args.example:
        for row in EXAMPLE_ROWS:
            print(json.dumps(row, sort_keys=True))
        return 0
    if not args.trace:
        parser.error("provide a trace JSONL file, or use --example")

    rows = load_jsonl(Path(args.trace))
    print(json.dumps(analyze(rows), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
