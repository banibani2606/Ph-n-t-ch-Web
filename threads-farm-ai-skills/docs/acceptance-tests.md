# End-to-end test scenarios

| ID | Scenario | Expected |
|---|---|---|
| A01 | Generate 8 accounts × 3 desired slots | max 24 valid drafts/day; duplicates/low-quality may be skipped |
| A02 | Draft is `CHO_DUYET` | Cannot publish |
| A03 | Reviewer approves version V, then text is edited | Invalidated approval; cannot publish |
| A04 | Approved post and reserved device | Exactly one Farm job per idempotency key |
| A05 | Two cron executions same time | Only one reservation; no duplicate post |
| A06 | Farm timeout after potential success | Reconcile existing job first; do not blind retry |
| A07 | Farm confirms URL | `DA_DANG` + URL + timestamp + audit |
| A08 | Apify returns missing `views` | Store `null`, do not fabricate 0 |
| A09 | Repeat same metrics snapshot | Upsert; no duplicate snapshots |
| A10 | Telegram API fails | Main state correct, alert retried separately |
| A11 | Bad webhook authentication | Reject at proxy / node auth; no side effects |
| A12 | 403 / platform block | Stop account, notify admin, do not bypass |
| A13 | Workflow JSON import | Import cleanly on user's n8n version, resolve node version/credentials |
| A14 | Payload schema drift | Explicit error; no success report |
