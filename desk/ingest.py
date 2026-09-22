from __future__ import annotations

import json
import uuid
from typing import Any

from .models import Signal


def normalize_uw_payload(payload: dict[str, Any]) -> Signal:
    """Best-effort normalize of a UW-like or Mini watcher payload into Signal."""
    # Nested signal from notify_signal style
    if isinstance(payload.get("signal"), dict):
        payload = {**payload, **payload["signal"]}

    contract = payload.get("contract") or {}
    if isinstance(contract, dict):
        expiry = str(contract.get("expiry") or payload.get("expiry") or "")
        strike = contract.get("strike", payload.get("strike"))
        right = str(contract.get("right") or payload.get("right") or "")
    else:
        expiry = str(payload.get("expiry") or "")
        strike = payload.get("strike")
        right = str(payload.get("right") or "")

    ticker = str(payload.get("ticker") or payload.get("symbol") or "").upper()
    sid = str(payload.get("id") or f"sig_{uuid.uuid4().hex[:12]}")
    setup = str(payload.get("setup_id") or "")
    if not setup and ticker:
        setup = f"{ticker}_{expiry}_{strike}{right}"

    action = payload.get("action_recommended") or payload.get("action") or "story_only"
    if action not in ("place_options", "story_only", "skip"):
        action = "story_only"

    return Signal(
        id=sid,
        ticker=ticker,
        grade=str(payload.get("grade") or ""),
        kind=str(payload.get("kind") or "options"),
        expiry=expiry,
        strike=float(strike) if strike not in (None, "") else None,
        right=right,
        side=str(payload.get("side") or ""),
        premium_or_notional=_num(payload.get("premium_or_notional") or payload.get("notional")),
        thesis=str(payload.get("thesis") or ""),
        invalidation=str(payload.get("invalidation") or ""),
        action_recommended=action,  # type: ignore[arg-type]
        setup_id=setup,
        source=str(payload.get("source") or "uw"),
        raw=payload,
    )


def normalize_json_text(text: str) -> Signal:
    return normalize_uw_payload(json.loads(text))


def _num(v: Any) -> float | None:
    try:
        return float(v) if v is not None and v != "" else None
    except (TypeError, ValueError):
        return None
