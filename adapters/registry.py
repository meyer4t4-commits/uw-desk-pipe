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
}


def prompt_text(name: str) -> str | None:
    meta = ADAPTERS.get(name)
    if not meta or not meta.get("prompt"):
        return None
    path = PROMPTS / meta["prompt"]
    return path.read_text() if path.exists() else None
