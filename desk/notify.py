from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any


def post_json(url: str, payload: dict[str, Any], timeout: float = 15.0) -> tuple[int, str]:
    """POST JSON to any webhook (Grok Bot, Hermes, Discord, Slack, ntfy-compatible, etc.)."""
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", "User-Agent": "uw-desk-pipe/0.2"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return int(resp.status), body
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return int(e.code), body


def notify_from_env(payload: dict[str, Any]) -> dict[str, Any]:
    """If NOTIFY_URL is set, POST survivors there. No-op if unset."""
    url = (os.environ.get("NOTIFY_URL") or "").strip()
    if not url:
        return {"sent": False, "reason": "NOTIFY_URL not set"}
    status, body = post_json(url, payload)
    return {"sent": True, "status": status, "body": body[:500], "url_host": url.split("/")[2] if "://" in url else url}
