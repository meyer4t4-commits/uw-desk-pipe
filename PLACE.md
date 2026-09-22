# Place & alerts — broker-agnostic

The desk core is broker-blind: **ingest → dedupe → checklist → journal**.  
Where fills happen (or don’t) is your choice.

## Path A — Alerts only (no Agentic / no broker)

Best if you don’t have Robinhood Agentic or don’t want auto-place yet.

1. UW wake → checklist
2. Survivors POST to `NOTIFY_URL` (Grok Bot webhook, Hermes, Claw, Discord, Slack, ntfy, …)
3. Your agent asks the questionnaire / sizes / you click place in whatever broker UI you use

```
NOTIFY_URL=https://your-agent-or-discord-webhook
LIVE_PLACE=false
```

## Path B — Robinhood Agentic live place

1. Checklist + live quote pass
2. `LIVE_PLACE=true`
3. Place on **your** Robinhood Agentic account only

```
LIVE_PLACE=true
BROKER=robinhood_agentic
# ROBINHOOD_AGENTIC_ACCOUNT=
```

## Path C — IBKR (or any broker)

Same as B, different adapter:

```
LIVE_PLACE=true
BROKER=ibkr
# IBKR_HOST=127.0.0.1
# IBKR_PORT=7497
# IBKR_CLIENT_ID=1
```

Wire Client Portal / TWS / Gateway yourself. This repo ships the **checklist contract**, not a full IBKR SDK — bring the client you trust.

## Shared rules

- Questionnaire / reject tags are identical on every path
- Live quote before options place (whichever broker)
- Mini / local watcher = **ears only** — never broker write keys on the always-on box
- Never commit tokens or account numbers

## Enable order

1. Run alerts-only until the questionnaire feels right  
2. Then either keep alerts→agent, or flip `LIVE_PLACE` on the broker you actually use  
