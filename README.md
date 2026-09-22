# UW → Desk Pipe (Free)

**Free open-source judgment framework** for Unusual Whales flow → a human desk checklist.  
Not a signal service. Not auto-trading. Not financial advice.

Built by [Mark Meyer](https://x.com/MarkMeyerBuilds) (@MarkMeyerBuilds).  
Promoted via Grok Bot Radar as a free top-of-funnel giveaway.

> **What this is:** a pipe + judgment checklist so you can *differentiate* UW A/A+ noise into skip / story-only / size-and-consider.  
> **What this is not:** Mark’s live Agentic place path, broker credentials, or his private edge tags.

---

## Why this exists

UW will feed **many** graded setups every day. The feed is commodity.  
**Alpha is differentiation:**

- which flows to ignore (afternoon 0DTE crush, re-churn, book conflict, soft-band blowouts, second bites)
- which to story-only
- which to size and consider

This repo gives you the **pipe + the questions**. You bring the judgment (and your own keys).

---

## Requirements

| Need | Notes |
| --- | --- |
| **Unusual Whales account** | Flow / alerts / API access as your plan allows. [Get UW →](#unusual-whales--affiliate) |
| **UW API token** (BYO) | Stored only in your local env / secrets — never committed |
| **Optional: Robinhood paper** | For live-quote practice only. This free cut does **not** include an auto-place path |
| **Python 3.10+** | Local scripts / helpers |
| **Brain** | Soft prefs are guidance, not FAIL religion |

---

## What's included (FREE)

Aligned with desk docs you’ll see named in the private playbook (`AGENTIC-DESK`, `SIGNAL-HANDLING`, `PRE-TRADE-CHECKLIST`, `CLOSED-TRADES`, `EXIT-PATH`):

1. **UW webhook / pipe skeleton** — ingest flow events, normalize a signal object, dedupe by contract key.
2. **Judgment / sizing questions** — concrete prompts (below), soft premium band **~$150–400**.
3. **Live-quote gate (concept)** — for options: no usable bid/ask → **story_only**; do not treat as place-ready.
4. **Reject / skip reasons (starter set)**  
   - afternoon **0DTE crush**  
   - **book conflict** (fights an open book)  
   - **re-churn** / same-contract spam  
   - **second bite** without new info  
   - soft-band blowouts without a real reason
5. **Exit invalidation prompts** — thesis broken → cut; thesis done → take; time-decay lean-cut for short-dated.
6. **Closed-trades journal schema** — win/loss rows with an **empty `edge_note`** for *you* to fill (no preloaded private tags).

## Functions (what each piece does)

| Function | What it does |
| --- | --- |
| **UW ingest / webhook** | Receives Unusual Whales alerts (webhook or poll). Normalizes ticker, expiry, strike, right, grade, notional. |
| **Dedupe** | Same contract key (`ticker\|expiry\|strike\|right`) suppressed for a window (e.g. 2h) so re-churn doesn’t spam you. |
| **SIGNAL object** | Standard JSON for every wake: thesis stubs, grade, setup_id, recommended action (`place_options` / `story_only` / skip). |
| **Pre-trade checklist** | Hard gates (thesis, invalidation, live quote, journal) + soft prefs (~$150–400 premium, concentration, max open tickets). |
| **Live-quote gate** | Options: pull a live bid/ask before treating a ticket as place-ready. No usable quote → `story_only` only. |
| **Reject / skip reasons** | Tagged skips: afternoon 0DTE crush, book conflict, re-churn, second bite, soft-band blowout without a reason. |
| **Risk sanity helper** | Optional `risk_eval` pass/warn on premium vs cash, spread, concentration — input to judgment, not auto-veto theater. |
| **Exit / invalidation prompts** | Thesis broken → cut; thesis done → take; short-dated time-decay lean-cut. |
| **Trade journal** | `SIGNAL` / `ENTRY` / `COMPLETE` event log (noisy path). |
| **Closed-trades W/L journal** | One row per closed ticket + required empty `edge_note` you fill so the desk compounds. |
| **RTH options window** | Options wakes/places intended for weekday regular hours only (when you can actually trade options). |
| **Alert-only mode** | Default free cut: ears + checklist + journal. **No broker auto-place** in the public package. |
| **Hosted / cloud judgment (paid optional)** | Always-on desk that runs the checklist for you and wakes you on fills / material marks — see waitlist below. |

---

## Run modes: Mac Mini (save usage) vs cloud bot

You can run this two ways. Same checklist either path.

### A) Mac Mini / always-on local (cheap ears)

Use a small always-on box (Apple Silicon Mini is ideal) for **repetitive grind** so you don’t burn cloud tokens on every UW print:

| Local job | Why local |
| --- | --- |
| UW watch loop / poll | Continuous, boring, high volume |
| Dedupe + queue file | Disk-cheap |
| Heuristic grade / pre-filter | “Is this even A?” before waking anything expensive |
| Notify / webhook forward | POST only the survivors to your phone or cloud bot |
| Sample journal append | Local JSONL |

**Rule:** Mini is **ears only**. It does **not** place trades and should not hold broker write keys.

Typical local stack: Ollama / small local models (7B-class) for light classify/summarize if you want — optional. The free pipe works with plain Python + UW API even without a local LLM.

### B) Cloud bot (Grok Bot, Claude, ChatGPT agents, etc.)

Point survivors at **whatever cloud agent you already pay for**. That agent does the expensive part:

| Cloud job | Why cloud |
| --- | --- |
| Judgment against the checklist | Sizing questions, reject reasons, “size or pass?” |
| Live broker quotes (if you wire a connector) | Quote gate before any real size talk |
| Material pings | Fills, big mark moves — not every skip |
| Optional assisted place (your keys, your risk) | Only if *you* enable it; **not** in the free OSS cut |

**Rule:** Cloud gets **strategy + connectors**. Local gets **always-on grind**. Don’t put “one general chat does everything” in the middle — that’s where quota burns.

### C) Cloud-only (no Mini)

Fine for starters: run the watch loop on a cheap VPS or only during RTH on your laptop. Cost goes up with alert volume; you’ll feel why Mini ears exist once UW is loud.

### Recommended split (what we use in production)

```
Unusual Whales ──► Mac Mini watcher (dedupe / RTH / ears)
                         │
                         │ only fresh / graded survivors
                         ▼
                   Cloud bot judgment (checklist + live quote)
                         │
                         ├── skip / story_only (quiet journal)
                         └── you decide size (free cut) or hosted desk assists (paid)
```

---

## What's NOT included (KEEP PRIVATE / PAID)

| Kept private | Why |
| --- | --- |
| Mark’s real closed-trades **edge tags** & pattern notes | That’s the compounding journal |
| Day-lock / ping policy (when to wake vs stay quiet) | Ops policy, not OSS |
| Robinhood **auto-place** credentials & live Agentic place path | Liability + secrets |
| Hosted desk runtime (always-on watcher → judgment → optional assisted place) | Product |

Want the hosted desk? → [Hosted desk waitlist](#hosted-desk--waitlist).

---

## Judgment / sizing questions

Use these before you treat any UW wake as “place-ready.” Soft prefs guide sizing; they are **not** rigid FAIL theater.

### Hard (do these)

- [ ] **Thesis** — One sentence: what you believe and why *now*?
- [ ] **Invalidation** — Clear exit if wrong (price / time / catalyst miss).
- [ ] **Live quote (options)** — Usable bid/ask? Mid? Spread %? Premium $? Break-even?
- [ ] **Journal** — Log SIGNAL before risk; ENTRY on fill; COMPLETE on close with `edge_note`.

### Soft prefs (judgment)

- Prefer options premium in the **~$150–400** band (smaller OK; oversized needs a real reason).
- Prefer under ~25% of the risk book in one ticker.
- Prefer max ~2 open risk tickets (options + shares combined).
- Prefer catalyst covered by expiry; skip exhaustion / earnings lottery unless the story is exceptional.
- Day already ugly red? Lean manage / skip new risk — not a mechanical kill switch.

### Differentiation prompts (ask out loud)

1. Is this afternoon **0DTE crush** dressed up as A+?
2. Does this **conflict** with names/direction already on the book?
3. Is this **re-churn** of a contract I already skipped or filled in the last few hours?
4. Is this a **second bite** with no new tape / quote / catalyst?
5. Soft-band blowout — what *exactly* justifies sizing up?
6. If wrong in 30–90 minutes, where do I exit and why?

### Journal schema (starter)

```json
{
  "ts_close_et": "",
  "ticker": "",
  "expiry": "",
  "strike": "",
  "right": "C|P",
  "qty": 0,
  "avg_entry": null,
  "avg_exit": null,
  "realized_pnl": null,
  "result": "win|loss|scratch",
  "entry_source": "uw_a|uw_aplus|discretionary|other",
  "setup_tags": [],
  "why_entered": "",
  "why_exited": "",
  "edge_note": ""
}
```

Fill `edge_note` every close. Empty notes don’t compound.

---

## Quick start (conceptual)

```bash
# 1. Clone (your public repo URL once live)
git clone https://github.com/meyer4t4-commits/uw-desk-pipe.git
cd uw-desk-pipe

# 2. BYO secrets — never commit
cp .env.example .env
# UW_API_TOKEN=...
# WEBHOOK_SECRET=...   # if you expose an ingest URL

# 3. Run the pipe / checklist helpers (names TBD in the public cut)
python3 -m desk.checklist --help
```

Wire UW alerts → your ingest → checklist output.  
**You** decide skip / story / size. This free cut does not place for you.

---

## Monetization / support the desk

### Unusual Whales — affiliate

Need UW for the pipe? Sign up through Mark’s partner link when live:

> **Affiliate link:** `TBD — pending UW partner approval`  
> Apply / program: [https://partners.dub.co/unusual-whales](https://partners.dub.co/unusual-whales)  
> Application: [https://partners.dub.co/unusual-whales/apply](https://partners.dub.co/unusual-whales/apply)

Public program terms (as of research): **~10% per referred sale for 1 year**, referred users get **10% off for 3 months**, **60-day** click tracking, performance tiers. Payouts via Dub partner dashboard.

Until Mark’s personal link is approved, use the official UW site and DM him on X if you want the partner code applied.

### Hosted desk — waitlist ($29–99/mo)

Always-on UW → judgment desk, filtered wakes, optional assisted ops. Soft band + live-quote gate baked in. **No secrets in the free repo.**

> **Waitlist:** [https://x.com/MarkMeyerBuilds](https://x.com/MarkMeyerBuilds) — reply or DM **`HOSTED`**  
> Price band at launch: **$29–99/mo** (tier TBD). Spots limited while the desk stays judgment-first.

### Setup / install offer ($197–497, optional)

One-time install: pipe + checklist wired to *your* UW + paper/live quoting practice, journal schema, reject reasons tuned to your book.

> DM **`SETUP`** on [X @MarkMeyerBuilds](https://x.com/MarkMeyerBuilds) with your stack (UW plan, broker, paper vs live). Quote in the **$197–497** band depending on scope.

---

## Radar-ready promo blurb

> Free open-source UW→desk pipe from @MarkMeyerBuilds — not a signal service. Full function list: ingest, dedupe, checklist, live-quote gate, reject reasons, journals. Run ears on a Mac Mini to save cloud usage, or all-in on Grok Bot / any cloud agent for judgment. BYO UW keys. Hosted desk: DM HOSTED. Not financial advice.

*(2–3 sentences — paste into Grok Bot Radar / Mark’s thread.)*

---

## Legal / NFA

- **Not financial advice.** Education and tooling only.
- **No guarantees.** Markets risk capital. You can lose money.
- **BYO keys / accounts.** You own Unusual Whales, broker, and cloud credentials. Never paste secrets into issues or PRs.
- **No liability.** Authors and promoters are not responsible for trades, misses, outages, or third-party API changes.
- **Not a broker, RIA, or CTA.** No auto-place in this free cut. Hosted / setup offerings (if any) are optional ops help — still your decisions, your risk.
- Past patterns in any example journal **do not** predict future results.

---

## Links

- X: [https://x.com/MarkMeyerBuilds](https://x.com/MarkMeyerBuilds)
- UW affiliate program: [https://partners.dub.co/unusual-whales](https://partners.dub.co/unusual-whales)
- UW partner dashboard: [https://unusualwhales.com/partners](https://unusualwhales.com/partners)
- UW contacts / pod partnerships: [https://unusualwhales.com/contacts](https://unusualwhales.com/contacts)

---

*Desk language mirrors private playbooks (`AGENTIC-DESK`, `SIGNAL-HANDLING`, `PRE-TRADE-CHECKLIST`, `CLOSED-TRADES`, `EXIT-PATH`) without shipping secrets, credentials, day-lock policy, or real edge tags.*
