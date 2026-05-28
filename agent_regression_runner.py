#!/usr/bin/env python3
"""Minimal AI-agent regression runner.

Safe scope: run only against your own local agent/stub or an explicitly authorized
endpoint. This runner defaults to an offline stub so teams can wire their own
call_agent() without exposing credentials.
"""
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("Install PyYAML: pip install pyyaml", file=sys.stderr)
    raise


def call_agent(user_input: str) -> dict:
    """Replace this stub with an authorized call to your app/agent."""
    return {"text": "stub response; wire call_agent() to your authorized endpoint", "tool_calls": []}


def text_has_any(text: str, needles) -> bool:
    low = (text or "").lower()
    return any(str(n).lower() in low for n in (needles or []))


def extract_json(text: str):
    try:
        return json.loads(text)
    except Exception:
        return None


def evaluate_case(case: dict, out: dict):
    failures = []
    text = out.get("text", "") if isinstance(out, dict) else str(out)
    tool_calls = out.get("tool_calls", []) if isinstance(out, dict) else []
    tool_names = [x.get("name", x) if isinstance(x, dict) else x for x in tool_calls]

    if case.get("must_include_any") and not text_has_any(text, case["must_include_any"]):
        failures.append("missing one of must_include_any")
    if text_has_any(text, case.get("must_not_include_any")):
        failures.append("included forbidden text")
    forbidden_tools = set(case.get("forbidden_tool_calls") or [])
    if forbidden_tools.intersection(map(str, tool_names)):
        failures.append("called forbidden tool")

    if case.get("expected_json_keys"):
        obj = extract_json(text)
        if not isinstance(obj, dict):
            failures.append("response is not valid JSON object")
        else:
            missing = [k for k in case["expected_json_keys"] if k not in obj]
            forbidden = [k for k in case.get("forbidden_json_keys", []) if k in obj]
            if missing:
                failures.append(f"missing JSON keys: {missing}")
            if forbidden:
                failures.append(f"forbidden JSON keys present: {forbidden}")
    return failures


def main(path: str) -> int:
    suite = yaml.safe_load(Path(path).read_text())
    results = []
    for case in suite.get("cases", []):
        out = call_agent(case.get("user_input", ""))
        failures = evaluate_case(case, out)
        results.append({
            "id": case.get("id"),
            "category": case.get("category"),
            "severity": case.get("severity", "medium"),
            "passed": not failures,
            "failures": failures,
        })
    report = {"suite": suite.get("suite"), "passed": all(r["passed"] for r in results), "results": results}
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: agent_regression_runner.py agent_regression_fixture_template.yaml", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
