# Live place (optional) — Robinhood Agentic

Default mode is **alert-only** (ingest → dedupe → checklist → journal).  
You can turn on **live place** once the questionnaire/rules are yours and Robinhood Agentic is wired.

## Flow

1. UW wake → normalize `SIGNAL`
2. Dedupe contract key
3. Run **checklist / questionnaire** (thesis, invalidation, soft band, reject tags)
4. **Live option quote** (usable bid/ask) — no quote → `story_only`, do not place
5. If rules pass and live place is **enabled** → place on **your** Robinhood Agentic account only
6. Journal `ENTRY` on fill; `COMPLETE` + `edge_note` on close

## Rules you set (examples)

- Soft premium band (e.g. ~$150–400)
- Max open tickets / concentration
- No 0DTE stack on an open winner
- No book-conflict puts vs long calls (or the reverse)
- RTH-only options
- Live quote required

## Safety

- Mini / local watcher = **ears only** — do not put broker write keys on the always-on box
- Cloud bot / place path holds the connector and only fires after checklist
- Never commit tokens, account numbers, or cookies to git
- Past results do not predict future results — you can lose money

## Enable

Set in `.env` (names illustrative — wire to your connector):

```
LIVE_PLACE=false
ROBINHOOD_AGENTIC_ACCOUNT=your_agentic_account
```

Flip `LIVE_PLACE=true` only after you trust your questionnaire.
