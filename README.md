# UW → Desk Pipe

**Free tools to turn Unusual Whales options flow into clear trade decisions — set up by your AI bot.**

Built by [Mark Meyer](https://x.com/MarkMeyerBuilds) (@MarkMeyerBuilds).  
Not financial advice. You can lose money trading options.

---

## Do this next (in order)

1. **Get Unusual Whales** (required — this is the idea feed)  
   https://refer.unusualwhales.com/mark-meyer  
   New users: **10% off for 3 months**. Please use that link.

2. **Send this repo link to your AI bot** and say **“set this up for me”**  
   Repo: https://github.com/meyer4t4-commits/uw-desk-pipe  
   Your bot should open **[BOT-SETUP.md](BOT-SETUP.md)**, ask a few plain-language questions, wire itself, and confirm when alerts are ready.  
   **Humans should not need webhooks, env files, or API jargon** — that’s the bot’s job.

3. **Optional (humans who want to poke around)**
   ```bash
   git clone https://github.com/meyer4t4-commits/uw-desk-pipe.git
   cd uw-desk-pipe
   cp .env.example .env
   python3 scripts/run_checklist.py samples/signal.example.json --skip-dedupe
   ```

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
| 1 | Turns a UW-style alert into one clean `SIGNAL` |
| 2 | Skips the same contract if it already fired (~2 hours) |
| 3 | Runs a checklist (thesis, invalidation, live quote, sizing questions) |
| 4 | Tags skip reasons (0DTE crush, book conflict, second bite, …) |
| 5 | Journals closes with an `edge_note` |
| 6 | Sends clean alerts to your AI bot |

Not a magic “buy every A print” bot.

---

## Plug-and-play agents

**Your bot picks the right one** when you send it this repo (see [BOT-SETUP.md](BOT-SETUP.md)).

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
| `discord` / `slack` | Team chat |
| `n8n` / `make` / `zapier` | Automation relays |
| `telegram` | Telegram via bridge |
| `webhook` | Anything else your bot can wake |

Bots: follow **BOT-SETUP.md**. Humans: ignore the adapter names — just paste the repo link to your bot.

---

## Why this works

- UW = raw unusual-flow ideas you won’t get from charts alone  
- Checklist kills bad prints fast  
- Close journal compounds learning  
- Your agent gets clean alerts instead of the full firehose  

---

## Not included (yet)

- Always-on UW watcher binary  
- One-click Robinhood / IBKR auto-place clients  
- Hosted trading for you  

Clean alerts to your bot **are** included. Live broker place is something your bot wires only after you say yes — and it stays off until then.

---

## Code map

| Path | Job |
| --- | --- |
| `BOT-SETUP.md` | **Bots start here** — interview + wiring script |
| `desk/` | Signal, ingest, dedupe, checklist, journal, notify |
| `scripts/run_checklist.py` | Try the checklist |
| `scripts/wire_adapter.py` | Connect your bot (bot runs this) |
| `scripts/notify_signal.py` | Checklist → alert your bot |
| `scripts/append_closed_trade.py` | Log a closed trade |
| `adapters/prompts/` | Judgment prompts for agents |
| `samples/` | Example JSON |

---

## Paste-ready blurb

> Free UW → desk pipe from @MarkMeyerBuilds. Unusual Whales is the idea feed; this repo is the judgment layer. Send the repo to your AI bot and say “set this up for me.” Not a signal service.  
> Repo: https://github.com/meyer4t4-commits/uw-desk-pipe  
> Get UW: https://refer.unusualwhales.com/mark-meyer

---

## Legal

Not financial advice. Not a broker, RIA, or CTA. Past results don’t predict future results. You own every decision and fill.

## License

MIT
