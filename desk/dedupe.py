from __future__ import annotations

import json
import time
from pathlib import Path


class DedupeStore:
    """Suppress same contract key for a TTL window (default 2 hours)."""

    def __init__(self, path: str | Path, ttl_seconds: int = 2 * 60 * 60):
        self.path = Path(path)
        self.ttl = ttl_seconds
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("{}")

    def _load(self) -> dict:
        try:
            return json.loads(self.path.read_text() or "{}")
        except json.JSONDecodeError:
            return {}

    def _save(self, data: dict) -> None:
        self.path.write_text(json.dumps(data, indent=2))

    def seen_recently(self, key: str) -> bool:
        data = self._load()
        now = time.time()
        # prune
        data = {k: v for k, v in data.items() if now - float(v) < self.ttl}
        self._save(data)
        return key in data

    def mark(self, key: str) -> None:
        data = self._load()
        data[key] = time.time()
        self._save(data)
