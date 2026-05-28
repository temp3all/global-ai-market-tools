# $50 AI Agent Tool-Call Snapshot Diff Setup

A fixed-scope, 24-hour quick setup for teams shipping AI agents after prompt/model/framework changes.

## Demand signal

Public GitHub activity around agent harness engineering and eval tools shows practical demand for behavior snapshots, CI regression checks, and tool-call diffs. The immediate pain: final-answer tests miss risky changes in tools, side effects, call counts, and parameters.

## What I deliver for $50 BTC

- A small baseline/current JSONL snapshot format for your agent traces
- A dependency-free tool-call diff script wired for local or CI use
- A one-page report listing newly added tools, changed call counts, risky side-effect parameters, and suggested gates
- A minimal GitHub Actions snippet if your repo uses GitHub CI

## Inputs needed

- 5-20 recorded agent runs or tool-call traces
- A list of high-risk tools/actions in your product
- Optional: current CI command

## Payment

Send $50 equivalent in BTC to:

`1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

Then open an issue or send the repo/trace bundle reference. No credential sharing required. Do not send secrets; redact API keys and private customer data.

## Included artifact

This repo includes `agent_tool_call_snapshot_diff.py` plus baseline/current example JSONL files.
