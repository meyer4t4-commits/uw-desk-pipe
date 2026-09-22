# Plug-and-play agents + optional live place

## Agents (included)

One command wires your bot:

```bash
python3 scripts/wire_adapter.py grokbot --url 'https://YOUR_WAKE_OR_WEBHOOK'
# also: hermes | openclaw | claw | webhook | discord | slack
```

That writes `NOTIFY_URL` into `.env` and drops a prompt pack at `adapters/ACTIVE_PROMPT.md` — paste that into the bot.

Test:

```bash
python3 scripts/notify_signal.py samples/signal.example.json --dry-run
python3 scripts/notify_signal.py samples/signal.example.json
```

Survivors after checklist POST as JSON (`type: uw_desk_signal`). Discord/Slack use `--format discord|slack`.

## Brokers (not plug-and-play yet)

Robinhood Agentic / IBKR live place is still **you wire it**. Keep `LIVE_PLACE=false` until then. Mini/watchers should stay ears-only (no write keys).
