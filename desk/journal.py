from __future__ import annotations

import json
from pathlib import Path
from typing import Any


CLOSED_TRADE_FIELDS = [
    "ts_close_et",
    "ticker",
    "expiry",
    "strike",
    "right",
    "qty",
    "avg_entry",
    "avg_exit",
    "realized_pnl",
    "result",
    "entry_source",
    "setup_tags",
    "why_entered",
    "why_exited",
    "edge_note",
]


def append_jsonl(path: str | Path, row: dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a") as f:
        f.write(json.dumps(row) + "\n")


def sample_closed_trade() -> dict[str, Any]:
    return {
        "ts_close_et": "2026-01-01T15:30:00-05:00",
        "ticker": "EXAMPLE",
        "expiry": "2026-01-02",
        "strike": 100,
        "right": "C",
        "qty": 1,
        "avg_entry": 1.0,
        "avg_exit": 1.5,
        "realized_pnl": 50.0,
        "result": "win",
        "entry_source": "uw_a",
        "setup_tags": ["weekly", "sample"],
        "why_entered": "Sample only — replace with your thesis.",
        "why_exited": "Sample only — replace with your exit reason.",
        "edge_note": "",  # YOU fill this every real close
    }
