#!/usr/bin/env python3
"""Run desk checklist on a JSON signal file (alert-only)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from desk.checklist import print_checklist, run_checklist  # noqa: E402
from desk.dedupe import DedupeStore  # noqa: E402
from desk.ingest import normalize_uw_payload  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="UW → desk checklist (no place)")
    ap.add_argument("signal_json", help="Path to signal JSON")
    ap.add_argument("--live-quote", action="store_true", help="You already have a live bid/ask")
    ap.add_argument("--reject", action="append", default=[], help="Reject tag (repeatable)")
    ap.add_argument("--dedupe-file", default="data/dedupe.json")
    ap.add_argument("--skip-dedupe", action="store_true")
    args = ap.parse_args()

    payload = json.loads(Path(args.signal_json).read_text())
    signal = normalize_uw_payload(payload)
    key = signal.contract_key()

    if not args.skip_dedupe:
        store = DedupeStore(args.dedupe_file)
        if store.seen_recently(key):
            print(f"DEDUPED recent contract: {key}")
            return 0
        store.mark(key)

    result = run_checklist(
        signal,
        has_live_quote=args.live_quote,
        reject_tags=args.reject,
    )
    print(json.dumps(signal.to_dict(), indent=2))
    print()
    print_checklist(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
