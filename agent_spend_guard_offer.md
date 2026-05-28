# AI Agent Spend Guard — $50 Fixed-Scope Offer

Demand signal: public Hacker News discussion around agent monitoring and payment safety shows a concrete pain point: autonomous agents are being given API keys, wallets, SaaS credentials, and purchasing authority before teams have simple spend controls.

## Buyer

- Solo founder or small team running an AI agent that can call paid APIs, create cloud resources, buy SaaS credits, or move crypto/stablecoin funds.
- Engineering lead who wants a lightweight pre-flight safety layer before giving agents broader permissions.

## $50 deliverable

A compact spend-control pack that can be applied to one agent/workflow:

1. **Spend policy file** (`agent_spend_policy.yaml`)
   - daily and per-action limits
   - allowlisted vendors/domains/chains
   - blocked vendors/domains/chains
   - human-approval thresholds
   - repeat-transaction guardrails
2. **Python pre-flight checker**
   - validates amount, vendor, frequency, and stated purpose
   - returns `ALLOW`, `REVIEW`, or `DENY`
   - logs decisions to JSONL for auditability
3. **Integration notes**
   - where to call the checker before a payment/API action
   - examples for API-credit purchases, cloud provisioning, and wallet transfers
4. **One-page risk review**
   - obvious bypasses
   - missing metadata
   - recommended next controls

## Boundaries

- No custody of funds.
- No credential handling.
- No production deployment access required.
- Customer provides sanitized action examples only.

## Fast intake questions

1. What can the agent currently spend or provision?
2. What is the maximum safe spend per day?
3. Which vendors/chains/domains are explicitly allowed?
4. Which actions should always require human review?
5. Where can a pre-flight function be inserted?

## Delivery message

> I can add a lightweight spend guard to one AI-agent workflow for $50. You get a YAML policy, Python checker, audit log format, and integration notes. No credentials or fund custody needed. BTC accepted: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`.

## Example policy

```yaml
agent_name: research_agent
currency: USD
limits:
  per_action: 10
  daily_total: 50
  review_above: 5
allowed_vendors:
  - openai.com
  - anthropic.com
  - aws.amazon.com
blocked_vendors:
  - unknown
  - gift_cards
repeat_guard:
  same_vendor_same_amount_minutes: 30
always_review:
  - wallet_transfer
  - new_vendor
  - cloud_instance_creation
```

## Example verdicts

- `ALLOW`: $1.20 OpenAI API call within daily budget.
- `REVIEW`: $8.00 new SaaS subscription even if under daily cap.
- `DENY`: repeat $10 charge to same unknown vendor within 5 minutes.
