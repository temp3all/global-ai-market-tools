# Postgres Durable Workflow Agent Offer

Signal: Hacker News top story discussion around "Just Use Postgres for Durable Workflows" indicates current demand for simpler, cheaper workflow durability without adding Kafka/Temporal/Celery complexity. This is positioned for small AI/SaaS teams that already run Postgres and need reliable background jobs, agent task state, retries, and auditability.

## $50 entry offer

**I will audit one existing background-job or AI-agent workflow and return a concrete Postgres-first durability plan.**

Deliverable within 24 hours:

- Current-state failure map: where jobs can duplicate, disappear, hang, or lose context.
- Minimal schema: `workflow_runs`, `workflow_steps`, `outbox_events`, and `idempotency_keys` tables tailored to the app.
- Retry and timeout policy: exact columns, indexes, and worker query patterns.
- Migration path: how to adopt without rewriting the product.
- One ready-to-paste SQL starter pack.

Price: **$50 equivalent in BTC**.

Payment address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## Who this helps

- AI agent products with multi-step tasks that must resume after crashes.
- SaaS apps using ad-hoc cron scripts and queues.
- Teams avoiding another infra component but needing observable job state.
- Developers who want a pragmatic alternative to heavyweight workflow engines.

## Intake questions

1. What currently triggers the workflow? HTTP request, cron, webhook, queue, or agent loop?
2. What database and ORM are used?
3. What is the worst failure today: duplicate side effects, missed jobs, slow retries, no visibility, or manual cleanup?
4. Which external APIs can be charged or mutate customer data?
5. How many jobs per hour and how long does each normally run?

## Starter SQL skeleton

```sql
create table workflow_runs (
  id bigserial primary key,
  workflow_name text not null,
  external_key text,
  status text not null default 'queued',
  attempt_count int not null default 0,
  max_attempts int not null default 5,
  run_after timestamptz not null default now(),
  locked_at timestamptz,
  locked_by text,
  input jsonb not null default '{}'::jsonb,
  output jsonb,
  last_error text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (workflow_name, external_key)
);

create index workflow_runs_ready_idx
  on workflow_runs (run_after, id)
  where status in ('queued', 'retry');

create table workflow_steps (
  id bigserial primary key,
  run_id bigint not null references workflow_runs(id),
  step_name text not null,
  status text not null default 'pending',
  idempotency_key text not null,
  input jsonb not null default '{}'::jsonb,
  output jsonb,
  last_error text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (run_id, step_name),
  unique (idempotency_key)
);

create table outbox_events (
  id bigserial primary key,
  topic text not null,
  payload jsonb not null,
  status text not null default 'pending',
  attempts int not null default 0,
  run_after timestamptz not null default now(),
  created_at timestamptz not null default now()
);
```

## Worker claim pattern

```sql
with next as (
  select id
  from workflow_runs
  where status in ('queued', 'retry')
    and run_after <= now()
  order by run_after, id
  for update skip locked
  limit 1
)
update workflow_runs w
set status = 'running', locked_at = now(), locked_by = $1, updated_at = now()
from next
where w.id = next.id
returning w.*;
```

## Upsell path

If the audit reveals a clear implementation need, offer a fixed-scope build:

- $150: integrate the schema and one worker loop.
- $300: add dashboard queries, dead-letter handling, and idempotent outbox delivery.
- $500+: migrate an existing queue/cron workflow safely with tests.
