from __future__ import annotations

"""Known agent targets. Plug-and-play = paste webhook/URL + pick a prompt pack."""

from pathlib import Path

PROMPTS = Path(__file__).resolve().parent / "prompts"

ADAPTERS = {
    "webhook": {
        "label": "Generic webhook (any bot)",
        "env": ["NOTIFY_URL"],
        "prompt": None,
        "notes": "POST JSON SIGNAL + checklist result to any HTTPS endpoint.",
    },
    "grokbot": {
        "label": "Grok Bot",
        "env": ["NOTIFY_URL"],
        "prompt": "grokbot.md",
        "notes": "Paste your Grok Bot / Resend-style wake URL into NOTIFY_URL. Give the bot the prompt pack.",
    },
    "hermes": {
        "label": "Hermes / local gateway",
        "env": ["NOTIFY_URL"],
        "prompt": "hermes.md",
        "notes": "Point NOTIFY_URL at your Hermes/OpenAI-compatible webhook or bridge.",
    },
    "openclaw": {
        "label": "OpenClaw",
        "env": ["NOTIFY_URL"],
        "prompt": "openclaw.md",
        "notes": "Use OpenClaw inbound webhook; load openclaw.md as the skill/prompt.",
    },
    "claw": {
        "label": "Claw / OpenClaw-family",
        "env": ["NOTIFY_URL"],
        "prompt": "claw.md",
        "notes": "Same pattern: webhook in, checklist survivors out.",
    },
    "discord": {
        "label": "Discord incoming webhook",
        "env": ["NOTIFY_URL"],
        "prompt": None,
        "notes": "Discord expects {content: ...} — use --format discord on notify.",
    },
    "slack": {
        "label": "Slack incoming webhook",
        "env": ["NOTIFY_URL"],
        "prompt": None,
        "notes": "Slack expects {text: ...} — use --format slack on notify.",
    },
    "cursor": {
        "label": "Cursor agent / cloud agent",
        "env": ["NOTIFY_URL"],
        "prompt": "cursor.md",
        "notes": "Cursor agent wake or webhook bridge. Paste prompt as agent instructions.",
    },
    "claude": {
        "label": "Claude / Claude Code / Cowork",
        "env": ["NOTIFY_URL"],
        "prompt": "claude.md",
        "notes": "Webhook or relay into Claude; paste prompt as project instructions.",
    },
    "chatgpt": {
        "label": "ChatGPT / custom GPT actions",
        "env": ["NOTIFY_URL"],
        "prompt": "chatgpt.md",
        "notes": "Point a GPT action or Zapier→GPT at NOTIFY_URL; paste prompt into GPT instructions.",
    },
    "lindy": {
        "label": "Lindy",
        "env": ["NOTIFY_URL"],
        "prompt": "lindy.md",
        "notes": "Lindy webhook trigger; paste prompt into the agent.",
    },
    "n8n": {
        "label": "n8n",
        "env": ["NOTIFY_URL"],
        "prompt": None,
        "notes": "n8n Webhook node URL → your agent branch.",
    },
    "make": {
        "label": "Make.com",
        "env": ["NOTIFY_URL"],
        "prompt": None,
        "notes": "Make custom webhook → router to your bot.",
    },
    "zapier": {
        "label": "Zapier",
        "env": ["NOTIFY_URL"],
        "prompt": None,
        "notes": "Zapier Catch Hook URL as NOTIFY_URL.",
    },
    "telegram": {
        "label": "Telegram bot",
        "env": ["NOTIFY_URL"],
        "prompt": "telegram.md",
        "notes": "Use a bridge that accepts JSON POST, or Discord-style formatter later.",
    },
    "windsurf": {
        "label": "Windsurf Cascade",
        "env": ["NOTIFY_URL"],
        "prompt": "windsurf.md",
        "notes": "Webhook/bridge into Cascade; paste prompt as rules.",
    },
    "perplexity": {
        "label": "Perplexity agent / computer",
        "env": ["NOTIFY_URL"],
        "prompt": "perplexity.md",
        "notes": "If you have an inbound webhook, same pattern.",
    },
}


def prompt_text(name: str) -> str | None:
    meta = ADAPTERS.get(name)
    if not meta or not meta.get("prompt"):
        return None
    path = PROMPTS / meta["prompt"]
    return path.read_text() if path.exists() else None
