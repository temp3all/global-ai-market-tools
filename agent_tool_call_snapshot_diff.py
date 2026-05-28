#!/usr/bin/env python3
"""
Agent Tool-Call Snapshot Diff

Dependency-free CI helper for AI-agent teams that want to catch tool-call
regressions after a prompt/model/framework change.

Why it exists: current public GitHub demand around agent harness engineering and
agent eval tooling is converging on snapshotting behavior and diffing tool calls,
not just grading final text. This tiny checker focuses on the risky part: tool
names, call counts, side-effect parameters, and newly introduced high-risk tools.

Usage:
  python3 agent_tool_call_snapshot_diff.py baseline.jsonl current.jsonl
  python3 agent_tool_call_snapshot_diff.py --example > tool_call_snapshot_example.jsonl

JSONL format, one event per line:
  {"case_id":"refund-001","tool":"search_docs","args":{"query":"refund policy"}}

Exit code:
  0 = no risky diff detected
  1 = risky diff detected
  2 = invalid usage/input
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

HIGH_RISK_TOOL_WORDS = (
    "send",
    "email",
    "post",
    "tweet",
    "delete",
    "charge",
    "pay",
    "payment",
    "transfer",
    "trade",
    "swap",
    "withdraw",
    "deploy",
    "write",
    "update",
    "admin",
)

SIDE_EFFECT_ARG_WORDS = (
    "amount",
    "address",
    "recipient",
    "to",
    "subject",
    "body",
    "path",
    "url",
    "symbol",
    "quantity",
    "order",
    "message",
)

EXAMPLE_ROWS = [
    {"case_id": "refund-001", "tool": "search_docs", "args": {"query": "refund policy"}},
    {"case_id": "refund-001", "tool": "send_email", "args": {"to": "user@example.com", "subject": "Refund update"}},
]


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
                raise SystemExit(f"invalid JSONL {path}:{line_no}: row must be object")
            for key in ("case_id", "tool"):
                if key not in row:
                    raise SystemExit(f"invalid JSONL {path}:{line_no}: missing {key!r}")
            if "args" in row and not isinstance(row["args"], dict):
                raise SystemExit(f"invalid JSONL {path}:{line_no}: args must be object when present")
            rows.append(row)
    return rows


def by_case(rows: Iterable[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["case_id"])].append(row)
    return grouped


def risky_tool(tool: str) -> bool:
    low = tool.lower()
    return any(word in low for word in HIGH_RISK_TOOL_WORDS)


def arg_fingerprint(row: Dict[str, Any]) -> Tuple[str, Tuple[Tuple[str, str], ...]]:
    args = row.get("args") or {}
    focused = []
    for key, value in sorted(args.items()):
        key_s = str(key)
        if any(word in key_s.lower() for word in SIDE_EFFECT_ARG_WORDS):
            focused.append((key_s, json.dumps(value, sort_keys=True)))
    return str(row["tool"]), tuple(focused)


def summarize(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "tool_counts": Counter(str(r["tool"]) for r in rows),
        "risky_tools": sorted({str(r["tool"]) for r in rows if risky_tool(str(r["tool"]))}),
        "side_effect_fingerprints": Counter(arg_fingerprint(r) for r in rows),
    }


def diff_case(case_id: str, base_rows: List[Dict[str, Any]], cur_rows: List[Dict[str, Any]]) -> List[str]:
    findings: List[str] = []
    base = summarize(base_rows)
    cur = summarize(cur_rows)

    added_tools = sorted(set(cur["tool_counts"]) - set(base["tool_counts"]))
    removed_tools = sorted(set(base["tool_counts"]) - set(cur["tool_counts"]))
    for tool in added_tools:
        severity = "HIGH" if risky_tool(tool) else "MEDIUM"
        findings.append(f"{severity} {case_id}: added tool {tool!r}")
    for tool in removed_tools:
        findings.append(f"LOW {case_id}: removed tool {tool!r}")

    for tool in sorted(set(base["tool_counts"]) | set(cur["tool_counts"])):
        before = base["tool_counts"].get(tool, 0)
        after = cur["tool_counts"].get(tool, 0)
        if before != after:
            severity = "HIGH" if risky_tool(tool) and after > before else "MEDIUM"
            findings.append(f"{severity} {case_id}: call count changed for {tool!r}: {before} -> {after}")

    added_risky = sorted(set(cur["risky_tools"]) - set(base["risky_tools"]))
    for tool in added_risky:
        findings.append(f"HIGH {case_id}: newly introduced high-risk tool {tool!r}")

    base_fp = base["side_effect_fingerprints"]
    cur_fp = cur["side_effect_fingerprints"]
    if base_fp != cur_fp:
        findings.append(f"HIGH {case_id}: side-effect argument fingerprint changed")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Diff AI-agent tool-call snapshots and flag risky regressions.")
    parser.add_argument("baseline", nargs="?", help="baseline JSONL snapshot")
    parser.add_argument("current", nargs="?", help="current JSONL snapshot")
    parser.add_argument("--example", action="store_true", help="print example JSONL and exit")
    args = parser.parse_args()

    if args.example:
        for row in EXAMPLE_ROWS:
            print(json.dumps(row, sort_keys=True))
        return 0

    if not args.baseline or not args.current:
        parser.error("provide baseline and current JSONL files, or use --example")

    baseline = by_case(load_jsonl(Path(args.baseline)))
    current = by_case(load_jsonl(Path(args.current)))

    findings: List[str] = []
    for case_id in sorted(set(baseline) | set(current)):
        findings.extend(diff_case(case_id, baseline.get(case_id, []), current.get(case_id, [])))

    result = {
        "baseline_cases": len(baseline),
        "current_cases": len(current),
        "findings": findings,
        "risky_diff": any(f.startswith("HIGH") or f.startswith("MEDIUM") for f in findings),
    }
    print(json.dumps(result, indent=2))
    return 1 if result["risky_diff"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
