#!/usr/bin/env python3
"""
Minimal AI agent regression eval CLI.

Purpose:
- Catch prompt/model/tooling regressions before users do.
- Designed for small teams that have manually recorded known failures.
- No network calls, no vendor lock-in, safe to run in CI.

Usage:
  python3 agent_regression_minimal_eval_cli.py cases.jsonl outputs.jsonl

cases.jsonl rows:
  {"id":"refund-001","must_include":["refund policy"],"must_not_include":["guaranteed"],"max_chars":1200}

outputs.jsonl rows:
  {"id":"refund-001","output":"...agent response..."}

Exit code is 0 if all cases pass, 1 if any fail.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise SystemExit(f"Invalid JSONL in {path}:{line_no}: {e}")
    return rows


def check_case(case: Dict[str, Any], output: str) -> List[str]:
    failures: List[str] = []
    lower = output.lower()

    for phrase in case.get("must_include", []):
        if str(phrase).lower() not in lower:
            failures.append(f"missing required phrase: {phrase!r}")

    for phrase in case.get("must_not_include", []):
        if str(phrase).lower() in lower:
            failures.append(f"contains forbidden phrase: {phrase!r}")

    max_chars = case.get("max_chars")
    if max_chars is not None and len(output) > int(max_chars):
        failures.append(f"too long: {len(output)} chars > {max_chars}")

    min_chars = case.get("min_chars")
    if min_chars is not None and len(output) < int(min_chars):
        failures.append(f"too short: {len(output)} chars < {min_chars}")

    return failures


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__.strip())
        return 2

    cases = load_jsonl(Path(sys.argv[1]))
    outputs = {str(r.get("id")): str(r.get("output", "")) for r in load_jsonl(Path(sys.argv[2]))}

    failed = 0
    for case in cases:
        cid = str(case.get("id"))
        if cid not in outputs:
            failed += 1
            print(f"FAIL {cid}: missing output")
            continue
        failures = check_case(case, outputs[cid])
        if failures:
            failed += 1
            print(f"FAIL {cid}: " + "; ".join(failures))
        else:
            print(f"PASS {cid}")

    print(json.dumps({"cases": len(cases), "failed": failed, "passed": len(cases) - failed}, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
