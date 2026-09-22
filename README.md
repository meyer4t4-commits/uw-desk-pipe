# UW → Desk Pipe

**Free tools to turn Unusual Whales options flow into clear trade decisions.**

Built by [Mark Meyer](https://x.com/MarkMeyerBuilds) (@MarkMeyerBuilds).  
Not financial advice. You can lose money trading options.

---

## Why Unusual Whales

Charts alone don’t show when big, unusual options flow hits.  
**Unusual Whales** surfaces graded unusual options activity (the “idea feed”).

This repo does **not** replace UW. It assumes you have UW (or a compatible alert feed).  
Without that feed, there’s nothing for the desk to judge.

**Get UW (partner link — please use this):**  
https://refer.unusualwhales.com/mark-meyer  

New users get **10% off for 3 months**. That’s how this free project stays funded.

---

## What this repo actually does

Most people drown in A/A+ alerts. Volume isn’t the edge.  
**The edge is deciding which prints to ignore vs take seriously.**

This package gives you:

1. **Normalize** a UW-style alert into one standard `SIGNAL` object  
2. **Dedupe** the same contract so re-churn doesn’t spam you  
3. **Run a checklist** — hard questions (thesis, invalidation, live quote, journal) plus soft sizing prefs  
4. **Tag skip reasons** — e.g. 0DTE crush, book conflict, second bite, no live quote  
5. **Journal closes** — one row per closed trade with an `edge_note` so you learn what worked

That’s it. Clear judgment on top of UW. Not a magic signal bot.

---

## What’s in the box (code)

| Piece | Path | Job |
| --- | --- | --- |
| Signal model | `desk/models.py` | Standard shape for an alert |
| Ingest | `desk/ingest.py` | Turn raw JSON into a `SIGNAL` |
| Dedupe | `desk/dedupe.py` | Same contract suppressed for ~2 hours |
| Checklist | `desk/checklist.py` | Questions + skip/story recommendation |
| Journal helper | `desk/journal.py` | Closed-trade row shape + append |
| CLI | `scripts/run_checklist.py` | Run checklist on a sample/alert JSON |
| Journal CLI | `scripts/append_closed_trade.py` | Append a closed trade to JSONL |
| Samples | `samples/` | Example signal + closed-trade rows |

---

## Quick start

```bash
git clone https://github.com/meyer4t4-commits/uw-desk-pipe.git
cd uw-desk-pipe
cp .env.example .env
# put your UW token in .env when you wire a live feed

python3 scripts/run_checklist.py samples/signal.example.json --skip-dedupe
python3 scripts/run_checklist.py samples/signal.example.json --live-quote --skip-dedupe
```

Walk the printed questions before you size anything.

---

## Why this is effective

- **UW gives the raw ideas.** Without them you’re late or blind to unusual flow.  
- **Most graded alerts should die.** The checklist exists to kill bad ones fast (no quote, book conflict, re-churn, lottery sizing).  
- **A close journal compounds.** `edge_note` on every exit beats “I think I remember what worked.”  
- **Same process every time.** Emotion and FOMO get a written gate, not a vibe.

---

## What this is *not* (yet)

These are **not** shipped as ready-made connectors in this repo:

- A full always-on UW watcher binary  
- One-click Robinhood / IBKR auto-trading  
- A hosted bot that places for you  

You (or your agent — Grok Bot, Hermes, Claw, etc.) can **wire** alerts and brokers on top of this checklist. See `PLACE.md` for optional patterns. Don’t expect those adapters to be plug-and-play here today.

---

## Hosted desk (optional, separate)

If you want someone to run a desk like this for you later:

**Join waitlist:**  
https://github.com/meyer4t4-commits/uw-desk-pipe/issues/new?template=hosted-desk-waitlist.yml  

Founding target ~$49/mo. Free repo stays free.

---

## Paste-ready blurb

> Free UW → desk pipe from @MarkMeyerBuilds. Unusual Whales is the idea feed; this repo is the judgment layer (normalize, dedupe, checklist, skip reasons, close journal). Not a signal service. BYO UW key.  
> Repo: https://github.com/meyer4t4-commits/uw-desk-pipe  
> Get UW: https://refer.unusualwhales.com/mark-meyer  
> Hosted waitlist: https://github.com/meyer4t4-commits/uw-desk-pipe/issues/new?template=hosted-desk-waitlist.yml

---

## Legal

Not financial advice. Not a broker, RIA, or CTA. Past results don’t predict future results. You bring your own UW / broker keys and you own every decision and fill.

## License

MIT
