#!/usr/bin/env python3
"""Run checklist on a signal JSON and POST to NOTIFY_URL if set."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from desk.checklist import run_checklist  # noqa: E402
from desk.ingest import normalize_uw_payload  # noqa: E402
from desk.notify import notify_from_env, post_json  # noqa: E402


def load_env(path: str = ".env") -> None:
    p = Path(path)
    if not p.exists():
        return
    for line in p.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def format_payload(signal, result, fmt: str) -> dict:
    base = {"type": "uw_desk_signal", "signal": signal.to_dict(), "checklist": result.to_dict()}
    if fmt == "raw":
        return base
    # Human one-liner for chat webhooks
    summary = (
        f"UW desk: {signal.ticker} {signal.expiry} {signal.strike}{signal.right} "
        f"grade={signal.grade} → {result.action}"
    )
    if result.reject_reasons:
        summary += f" ({', '.join(result.reject_reasons)})"
    if fmt == "discord":
        return {"content": summary[:1900]}
    if fmt == "slack":
        return {"text": summary}
    # default: raw JSON for agent bots
    return base


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("signal_json")
    ap.add_argument("--live-quote", action="store_true")
    ap.add_argument("--reject", action="append", default=[])
    ap.add_argument("--format", choices=["raw", "discord", "slack"], default="raw")
    ap.add_argument("--dry-run", action="store_true", help="Print payload, do not POST")
    args = ap.parse_args()
    load_env()

    payload_in = json.loads(Path(args.signal_json).read_text())
    signal = normalize_uw_payload(payload_in)
    result = run_checklist(signal, has_live_quote=args.live_quote, reject_tags=args.reject)
    out = format_payload(signal, result, args.format)

    if args.dry_run:
        print(json.dumps(out, indent=2))
        return 0

    if args.format in ("discord", "slack"):
        url = (os.environ.get("NOTIFY_URL") or "").strip()
        if not url:
            print("NOTIFY_URL not set", file=sys.stderr)
            return 1
        status, body = post_json(url, out)
        print(json.dumps({"sent": True, "status": status, "body": body[:300]}))
        return 0 if status < 400 else 1

    info = notify_from_env(out)
    print(json.dumps(info, indent=2))
    print(json.dumps({"action": result.action, "rejects": result.reject_reasons}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
