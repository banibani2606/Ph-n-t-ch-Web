# Adapter gateway contract (PROPOSED, NOT the existing CIT Farm API)

Screenshots show HTTP calls but not concrete endpoint definitions. The generator **proposes** a gateway exposing these routes; implement adapters to actual Gemini, Sheets, Farm and Apify. n8n templates will not run as shipped.

**POST `/v1/drafts/generate`**
Request: `{ "source":"schedule|manual|webhook", "run_at":"ISO", "batch_size":5, "posts_per_account_per_day":3, "accounts_count":8 }`.
Adapter responsibilities: select eligible accounts/personas, call Gemini with approved brand rules, check duplicates, write each draft to Sheet, record status `CHO_DUYET`, return `{ "run_id":"uuid", "drafts_created":4, "pending_review":4, "review_sheet_url":"https://..." }`.

**POST `/v1/posts/publish-approved`**
Request: `{ "source":"schedule|webhook", "run_at":"ISO", "batch_size":5, "enforce_approval":true, "request_id":"..." }`.
Adapter responsibilities: authenticate caller; atomically reserve eligible `DA_DUYET` with content hash unchanged; match device, run Farm jobs, reconcile uncertain outcomes by idempotency, update Sheet on actual success. Return `{ "run_id":"uuid", "published":2, "skipped":1, "failed":0, "pending":0, "published_urls":["https://www.threads.net/..."], "sheet_url":"https://..." }`.

**POST `/v1/metrics/collect`**
Request: `{ "source":"schedule|webhook", "run_at":"ISO", "only_published":true }`.
Adapter responsibilities: query published posts with URLs, call configured Apify actor or official analytics, upsert daily snapshot; return `{ "run_id":"uuid", "checked":12, "successful":11, "failed":1, "sheet_url":"https://..." }`.

## Controls

- Gateways require actual authentication (e.g. n8n predefined credential header or reverse proxy), TLS, replay protection; **do not expose unauthenticated POST endpoints**.
- Incoming webhook triggers also require authentication at reverse proxy or n8n configuration; the sample workflows do not assert this control is already in place.
- Idempotency key: `(account_id, slot_at_utc, post_id)`; on retry, query job state and never publish blindly.
- All responses include request ID, error code, timing, status and summary fields. On failure, return explicit `4xx/5xx` and log safe details.
- Separate endpoints by concern; gateway implements integrations. Do not confuse this proposal with Farm repo's actual API.
