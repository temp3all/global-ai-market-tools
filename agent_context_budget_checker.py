#!/usr/bin/env python3
"""Estimate AI-agent context bloat and suggest low-risk compaction moves.

Reads either a plain text/markdown log or JSON/JSONL events containing common
agent fields such as messages, tool outputs, observations, prompts, or content.
No network calls; safe for local CI use.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

TOKEN_RE = re.compile(r"\w+|[^\w\s]", re.UNICODE)
TOOL_HINTS = ("tool", "observation", "stdout", "stderr", "terminal", "browser", "function")
RISKY_HINTS = ("secret", "token", "password", "api_key", "private key", "credential")


def rough_tokens(text: str) -> int:
    """Cheap deterministic token approximation for budgeting."""
    return max(1, int(len(TOKEN_RE.findall(text)) * 1.15)) if text else 0


def walk_strings(obj: Any, prefix: str = "") -> Iterable[tuple[str, str]]:
    if isinstance(obj, str):
        yield prefix or "text", obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            child = f"{prefix}.{k}" if prefix else str(k)
            yield from walk_strings(v, child)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            child = f"{prefix}[{i}]" if prefix else f"[{i}]"
            yield from walk_strings(v, child)


def load_segments(path: Path) -> list[tuple[str, str]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    segments: list[tuple[str, str]] = []
    try:
        data = json.loads(raw)
        segments.extend(walk_strings(data))
        return segments or [("raw", raw)]
    except json.JSONDecodeError:
        pass

    # JSONL best effort.
    jsonl_ok = False
    for i, line in enumerate(raw.splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            jsonl_ok = True
            segments.extend((f"line{i}:{k}", v) for k, v in walk_strings(data))
        except json.JSONDecodeError:
            if jsonl_ok:
                segments.append((f"line{i}:raw", line))
    if jsonl_ok:
        return segments

    # Markdown/plain text: split into paragraphs to identify biggest blocks.
    parts = [p.strip() for p in re.split(r"\n\s*\n", raw) if p.strip()]
    return [(f"paragraph{i+1}", p) for i, p in enumerate(parts)] or [("raw", raw)]


def classify(name: str, text: str) -> str:
    hay = f"{name}\n{text[:500]}".lower()
    if any(h in hay for h in TOOL_HINTS):
        return "tool_output"
    if any(h in hay for h in RISKY_HINTS):
        return "sensitive_review"
    if len(text) > 4000:
        return "large_context"
    return "message"


def main() -> int:
    ap = argparse.ArgumentParser(description="Score an AI-agent log for context budget waste.")
    ap.add_argument("path", help="Text, markdown, JSON, or JSONL agent trace/log")
    ap.add_argument("--budget", type=int, default=32000, help="target context budget in rough tokens")
    ap.add_argument("--top", type=int, default=8, help="number of largest segments to show")
    args = ap.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    rows = []
    for name, text in load_segments(path):
        toks = rough_tokens(text)
        rows.append({"name": name, "tokens": toks, "chars": len(text), "kind": classify(name, text)})
    total = sum(r["tokens"] for r in rows)
    tool_tokens = sum(r["tokens"] for r in rows if r["kind"] == "tool_output")
    large = [r for r in rows if r["tokens"] > max(1200, args.budget * 0.05)]
    risky = [r for r in rows if r["kind"] == "sensitive_review"]
    over = max(0, total - args.budget)

    print("# Agent Context Budget Report")
    print(f"file: {path}")
    print(f"rough_tokens: {total}")
    print(f"budget: {args.budget}")
    print(f"over_budget: {over}")
    print(f"tool_output_tokens: {tool_tokens} ({(tool_tokens / total * 100) if total else 0:.1f}%)")
    print(f"large_segments: {len(large)}")
    print(f"sensitive_review_segments: {len(risky)}")
    print("\n## Largest segments")
    for r in sorted(rows, key=lambda x: x["tokens"], reverse=True)[: args.top]:
        print(f"- {r['tokens']:>6} tok | {r['kind']:<16} | {r['name']} ({r['chars']} chars)")

    print("\n## Suggested compaction moves")
    if tool_tokens > total * 0.35:
        print("- Summarize or hash large tool outputs before reinserting them into the next prompt.")
    if large:
        print("- Move the largest stable reference blocks to files and pass paths plus short summaries.")
    if risky:
        print("- Review sensitive-looking segments before sharing traces with vendors or public issues.")
    if over:
        print("- Add a rolling summary checkpoint every 8k-12k rough tokens to stay below budget.")
    if not (tool_tokens > total * 0.35 or large or risky or over):
        print("- Trace is within budget; keep current retention policy and monitor growth.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
