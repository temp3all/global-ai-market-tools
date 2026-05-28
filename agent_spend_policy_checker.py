#!/usr/bin/env python3
"""Minimal AI-agent spend policy checker.

Safe fixed-scope artifact for teams giving agents paid API, cloud, SaaS, or
wallet permissions. It does not handle credentials or execute payments; it only
classifies a proposed action as ALLOW, REVIEW, or DENY and appends an audit log.

Usage:
  python agent_spend_policy_checker.py --policy agent_spend_policy.example.yaml \
    --vendor openai.com --amount 1.25 --action api_call --purpose "summarize docs"

The policy file is intentionally simple YAML. If PyYAML is unavailable, JSON is
also accepted because JSON is valid YAML-like data for this schema.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    yaml = None


@dataclass
class Verdict:
    status: str
    reasons: List[str]
    normalized_vendor: str
    amount: float
    action: str


def load_policy(path: str) -> Dict[str, Any]:
    text = Path(path).read_text(encoding="utf-8")
    if yaml is not None:
        data = yaml.safe_load(text)
    else:
        data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("policy must be a mapping/object")
    return data


def as_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(x).strip().lower() for x in value if str(x).strip()]
    return [str(value).strip().lower()] if str(value).strip() else []


def vendor_matches(vendor: str, patterns: List[str]) -> bool:
    v = vendor.lower().strip()
    return any(v == p or v.endswith("." + p) or p in v for p in patterns)


def decide(policy: Dict[str, Any], *, vendor: str, amount: float, action: str, purpose: str) -> Verdict:
    reasons: List[str] = []
    status = "ALLOW"
    vendor_n = vendor.strip().lower() or "unknown"
    action_n = action.strip().lower() or "unspecified"

    limits = policy.get("limits") or {}
    per_action = float(limits.get("per_action", 0) or 0)
    review_above = float(limits.get("review_above", 0) or 0)

    allowed = as_list(policy.get("allowed_vendors"))
    blocked = as_list(policy.get("blocked_vendors"))
    always_review = as_list(policy.get("always_review"))

    if amount < 0:
        status = "DENY"
        reasons.append("negative amount is invalid")
    if not purpose.strip():
        status = max_status(status, "REVIEW")
        reasons.append("missing stated purpose")
    if per_action and amount > per_action:
        status = "DENY"
        reasons.append(f"amount {amount:.2f} exceeds per_action limit {per_action:.2f}")
    if blocked and vendor_matches(vendor_n, blocked):
        status = "DENY"
        reasons.append("vendor matches blocked list")
    if allowed and not vendor_matches(vendor_n, allowed):
        status = max_status(status, "REVIEW")
        reasons.append("vendor is not on allowlist")
    if review_above and amount > review_above and status != "DENY":
        status = "REVIEW"
        reasons.append(f"amount {amount:.2f} exceeds review_above threshold {review_above:.2f}")
    if action_n in always_review and status != "DENY":
        status = "REVIEW"
        reasons.append("action is configured as always_review")
    if not reasons:
        reasons.append("within configured policy")
    return Verdict(status=status, reasons=reasons, normalized_vendor=vendor_n, amount=amount, action=action_n)


def max_status(current: str, candidate: str) -> str:
    order = {"ALLOW": 0, "REVIEW": 1, "DENY": 2}
    return candidate if order[candidate] > order[current] else current


def append_audit(log_path: str, verdict: Verdict, purpose: str) -> None:
    event = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "status": verdict.status,
        "reasons": verdict.reasons,
        "vendor": verdict.normalized_vendor,
        "amount": verdict.amount,
        "action": verdict.action,
        "purpose": purpose,
    }
    with Path(log_path).open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(description="Classify proposed AI-agent spend/provision actions")
    ap.add_argument("--policy", required=True, help="YAML/JSON policy file")
    ap.add_argument("--vendor", required=True, help="vendor/domain/chain/counterparty")
    ap.add_argument("--amount", required=True, type=float, help="proposed amount in policy currency")
    ap.add_argument("--action", required=True, help="api_call, cloud_instance_creation, wallet_transfer, etc.")
    ap.add_argument("--purpose", default="", help="human-readable reason for the spend")
    ap.add_argument("--audit-log", default="agent_spend_audit.jsonl", help="JSONL audit log path")
    args = ap.parse_args()

    policy = load_policy(args.policy)
    verdict = decide(policy, vendor=args.vendor, amount=args.amount, action=args.action, purpose=args.purpose)
    append_audit(args.audit_log, verdict, args.purpose)
    print(json.dumps(verdict.__dict__, indent=2, sort_keys=True))
    return 0 if verdict.status == "ALLOW" else (2 if verdict.status == "REVIEW" else 3)


if __name__ == "__main__":
    sys.exit(main())
