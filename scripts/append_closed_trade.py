#!/usr/bin/env python3
"""Append one closed-trade JSON object to data/closed-trades.jsonl."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from desk.journal import CLOSED_TRADE_FIELDS, append_jsonl  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("json_row", help="JSON object string or @path")
    ap.add_argument("--out", default="data/closed-trades.jsonl")
    args = ap.parse_args()
    raw = args.json_row
    if raw.startswith("@"):
        raw = Path(raw[1:]).read_text()
    row = json.loads(raw)
    missing = [f for f in ("ticker", "edge_note", "result") if f not in row]
    if missing:
        print("warn missing fields:", ", ".join(missing), file=sys.stderr)
    append_jsonl(args.out, row)
    print("appended", args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
