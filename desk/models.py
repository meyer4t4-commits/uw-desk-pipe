from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal


Action = Literal["place_options", "story_only", "skip"]


@dataclass
class Signal:
    """Normalized wake from Unusual Whales (or compatible feed)."""

    id: str
    ticker: str
    grade: str = ""
    kind: str = "options"
    expiry: str = ""
    strike: float | None = None
    right: str = ""  # C | P
    side: str = ""
    premium_or_notional: float | None = None
    thesis: str = ""
    invalidation: str = ""
    action_recommended: Action = "story_only"
    setup_id: str = ""
    source: str = "uw"
    raw: dict[str, Any] = field(default_factory=dict)

    def contract_key(self) -> str:
        return f"{self.ticker}|{self.expiry}|{self.strike}|{self.right}".upper()

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ChecklistResult:
    hard_ok: bool
    soft_notes: list[str]
    reject_reasons: list[str]
    action: Action
    questions: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
