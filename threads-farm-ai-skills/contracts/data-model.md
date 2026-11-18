# Logical model / Suggested Sheets schema

Use immutable UUID for `post_id`; do not key on row number.

**Accounts**: `account_id`, `persona_id`, `account_handle`, `enabled`, `device_id`, `timezone`, `disclosure_policy`, `last_published_at`.

**Posts**: `post_id`, `account_id`, `persona_id`, `campaign_id`, `text`, `text_hash`, `approved_hash`, `status`, `slot_at_utc`, `drafted_at_utc`, `reviewer_id`, `reviewed_at_utc`, `reserved_at_utc`, `publish_job_id`, `published_at_utc`, `published_url`, `external_post_id`, `retry_count`, `last_error`, `request_id`.

**Metrics**: `post_id`, `captured_at_utc`, `source`, `actor_run_id`, `likes`, `replies`, `reposts`, `quotes`, `shares`, `views`, `schema_version`, `confidence`, `error`.

**Audit**: `event_id`, `post_id`, `actor_type`, `actor_id`, `from_state`, `to_state`, `at_utc`, `request_id`, `detail`.

## State transitions
`CHO_DUYET → DA_DUYET / TU_CHOI`; `DA_DUYET → DANG_DAT_CHO → DANG_DANG → DA_DANG`; errors to `THAT_BAI` with explicit retry policy.

Use a durable atomic DB/queue for publish reservation; Sheets alone is not sufficient to prevent double-posting during concurrent executions.
