# UW → Desk Pipe

**Free tools to turn Unusual Whales options flow into clear trade decisions.**

Built by [Mark Meyer](https://x.com/MarkMeyerBuilds) (@MarkMeyerBuilds).  
Not financial advice. You can lose money trading options.

---

## Do this next (in order)

1. **Get Unusual Whales** (required — this is the idea feed)  
   https://refer.unusualwhales.com/mark-meyer  
   New users: **10% off for 3 months**. Please use that link.

2. **Clone and try the checklist**
   ```bash
   git clone https://github.com/meyer4t4-commits/uw-desk-pipe.git
   cd uw-desk-pipe
   cp .env.example .env
   python3 scripts/run_checklist.py samples/signal.example.json --skip-dedupe
   ```

3. **Plug in your agent** (one command)
   ```bash
   python3 scripts/wire_adapter.py grokbot --url 'https://YOUR_INBOUND_WEBHOOK'
   # then paste adapters/ACTIVE_PROMPT.md into that bot
   python3 scripts/notify_signal.py samples/signal.example.json --dry-run
   ```

That’s the whole onboarding path.

---

## Why Unusual Whales

Charts alone don’t show when big, unusual options flow hits.  
UW surfaces that graded flow. **Without UW, this desk has nothing to judge.**

This repo does not replace UW. It sits on top of it.

---

## What it does (included)

Most A/A+ alerts should be ignored. The edge is **which ones to skip vs take seriously**.

| Step | What happens |
| --- | --- |
| 1 | Normalize a UW-style alert into one `SIGNAL` |
| 2 | Dedupe the same contract (~2 hours) |
| 3 | Run a checklist (thesis, invalidation, live quote, sizing questions) |
| 4 | Tag skip reasons (0DTE crush, book conflict, second bite, …) |
| 5 | Journal closes with an `edge_note` |
| 6 | Optionally POST survivors to your agent webhook |

Not a magic “buy every A print” bot.

---

## Plug-and-play agents

```bash
python3 scripts/wire_adapter.py <adapter> --url 'https://YOUR_WEBHOOK'
```

| Adapter | For |
| --- | --- |
| `grokbot` | Grok Bot |
| `hermes` | Hermes / local gateway |
| `openclaw` / `claw` | OpenClaw family |
| `cursor` | Cursor agent |
| `claude` | Claude / Claude Code |
| `chatgpt` | ChatGPT / custom GPT |
| `lindy` | Lindy |
| `windsurf` | Windsurf Cascade |
| `perplexity` | Perplexity agent |
| `discord` / `slack` | Team chat webhooks |
| `n8n` / `make` / `zapier` | Automation relays |
| `telegram` | Telegram via bridge |
| `webhook` | Anything else with an HTTPS POST URL |

Each prompt-pack adapter writes `adapters/ACTIVE_PROMPT.md` — paste that into the bot.  
Details: `PLACE.md`.

---

## Why this works

- UW = raw unusual-flow ideas you won’t get from charts alone  
- Checklist kills bad prints fast  
- Close journal compounds learning  
- Your agent gets clean wakes instead of the full firehose  

---

## Not included (yet)

- Always-on UW watcher binary  
- One-click Robinhood / IBKR auto-place clients  
- Hosted trading for you  

Agent wake **is** included. Broker place is still something you or your agent wire.

---

## Code map

| Path | Job |
| --- | --- |
| `desk/` | Signal, ingest, dedupe, checklist, journal, notify |
| `scripts/run_checklist.py` | Try the checklist |
| `scripts/wire_adapter.py` | Connect your bot |
| `scripts/notify_signal.py` | Checklist → POST to bot |
| `scripts/append_closed_trade.py` | Log a closed trade |
| `adapters/prompts/` | Paste-ready agent instructions |
| `samples/` | Example JSON |

---

## Paste-ready blurb

> Free UW → desk pipe from @MarkMeyerBuilds. Unusual Whales is the idea feed; this repo is the judgment layer + plug-and-play wakes to your agent. Not a signal service.  
> Repo: https://github.com/meyer4t4-commits/uw-desk-pipe  
> Get UW: https://refer.unusualwhales.com/mark-meyer

---

## Legal

Not financial advice. Not a broker, RIA, or CTA. Past results don’t predict future results. You own every decision and fill.

## License

MIT
