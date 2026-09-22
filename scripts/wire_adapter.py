#!/usr/bin/env python3
"""Plug-and-play: pick an agent adapter and write NOTIFY_URL + show the prompt pack."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from adapters.registry import ADAPTERS, prompt_text  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="Wire uw-desk-pipe to your agent")
    ap.add_argument("adapter", choices=sorted(ADAPTERS.keys()), help="Target agent/webhook type")
    ap.add_argument("--url", required=True, help="Inbound webhook / wake URL")
    ap.add_argument("--env-file", default=".env", help="Env file to update (default .env)")
    ap.add_argument("--print-prompt", action="store_true", help="Print prompt pack to stdout")
    args = ap.parse_args()

    meta = ADAPTERS[args.adapter]
    env_path = Path(args.env_file)
    if not env_path.exists() and Path(".env.example").exists():
        env_path.write_text(Path(".env.example").read_text())

    lines = env_path.read_text().splitlines() if env_path.exists() else []
    out: list[str] = []
    seen_notify = False
    seen_adapter = False
    for line in lines:
        if line.startswith("NOTIFY_URL="):
            out.append(f"NOTIFY_URL={args.url}")
            seen_notify = True
        elif line.startswith("NOTIFY_ADAPTER="):
            out.append(f"NOTIFY_ADAPTER={args.adapter}")
            seen_adapter = True
        else:
            out.append(line)
    if not seen_notify:
        out.append(f"NOTIFY_URL={args.url}")
    if not seen_adapter:
        out.append(f"NOTIFY_ADAPTER={args.adapter}")
    env_path.write_text("\n".join(out) + "\n")

    print(f"Wired adapter: {meta['label']}")
    print(f"Wrote NOTIFY_URL → {env_path}")
    print(f"Notes: {meta['notes']}")
    prompt = prompt_text(args.adapter)
    if prompt:
        prompt_out = Path("adapters/ACTIVE_PROMPT.md")
        prompt_out.write_text(prompt)
        print(f"Prompt pack → {prompt_out} (paste into your bot)")
        if args.print_prompt:
            print("\n----- PROMPT -----\n")
            print(prompt)
    else:
        print("No prompt pack for this adapter (generic webhook / Discord / Slack).")
    print("\nTest: python3 scripts/notify_signal.py samples/signal.example.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
