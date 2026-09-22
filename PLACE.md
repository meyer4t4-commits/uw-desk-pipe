# Optional: alerts and live place (you wire these)

The **included** code stops at: ingest → dedupe → checklist → journal.

If you want more, you add it:

## Alerts to an agent (common)

After checklist, POST survivors to whatever you already use:

- Grok Bot webhook / Hermes / Claw  
- Discord / Slack / ntfy  

No broker required. Your agent (or you) decides whether to trade.

Set `NOTIFY_URL` in `.env` when you build that forwarder.

## Live place on a broker (advanced)

Only after checklist + a **live** options quote:

- Robinhood Agentic, or  
- IBKR, or  
- any API you trust  

Keep `LIVE_PLACE=false` until your rules feel solid.  
Don’t put broker write keys on an always-on Mini doing the watch loop — ears only there.

This repo does **not** ship a finished RH/IBKR place client. Bring your own.
