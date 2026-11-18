# Implementation guide

## Sequence

1. Clone repo / extract ZIP and fill `examples/project-config.json` with approved planning values **only** (no keys).
2. Deploy/configure n8n and reachable adapter gateway. If n8n runs in Docker on Mac, `host.docker.internal` MAY reach a service on your Mac, but this is not portable to cloud. Configure TLS URL and auth per deployment.
3. Create Google Sheet tabs `Accounts`, `Posts`, `Metrics`, `Audit` using `contracts/data-model.md`. Set human editor permissions.
4. Define all 8 persona specs in secure, approved configuration. Gemini prompt asks for constrained JSON drafts; gate claims/disclosures.
5. Implement adapter routes in `contracts/gateway-api.md` against actual APIs; validate external payload samples first.
6. Import generated JSON into n8n, connect all HTTP credential headers (in n8n UI), configure Telegram bot and authorized chat, and ensure timezone settings match.
7. Protect manual/webhook triggers with proper authentication/rate limiting and enable error workflows in production.
8. First test one draft → human approves → one Farm job → URL saved → one Apify metrics snapshot, then increase batch size (5 in source diagram).
9. Set a retry policy with idempotency and device throttling; monitor failures and daily run counts.
10. Activate each workflow after passing checks, one by one.

## Notes on generated sample

Generator creates **three separate workflows**. Each has Schedule Trigger and Webhook Trigger feeding one HTTP Request node for a gateway adapter, then a Code summary node. Telegram is represented by a **placeholder notification node** in generator to avoid embedding secrets or requiring Telegram credentials; instructions specify how to replace/configure it with the real Telegram node. This is NOT the exact screenshot export. Sample webhook responses are n8n default `onReceived` (they acknowledge trigger, not completion). For synchronous response use Respond to Webhook with explicit timeout and error mapping.

The screenshot showed Telegram `sendMessage` errors; verify bot token/chat ID and permissions rather than assuming ready.

## Anti-covert-marketing check

An automated set of persona accounts can be deceptive if marketing is framed as organic independent user testimony. Keep ownership/affiliation transparent and do not fabricate personal experiences, successes, or reviews. Workflows should not encourage platform rule violations.
