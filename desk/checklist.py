from __future__ import annotations

from .models import Action, ChecklistResult, Signal

HARD_QUESTIONS = [
    "Thesis — one sentence: what do you believe and why now?",
    "Invalidation — when are you wrong (price / time / catalyst)?",
    "Live quote (options) — usable bid/ask? Mid? Spread %? Premium $? BE?",
    "Journal — will you log SIGNAL / ENTRY / COMPLETE with edge_note?",
]

SOFT_QUESTIONS = [
    "Premium roughly in the ~$150–400 soft band?",
    "Short-dated premium over ~$1500? (usually high risk / skip)",
    "Same-name or index stack on an open winner? (second bite)",
    "Afternoon 0DTE crush / re-churn of the same print?",
    "Book conflict (e.g. long call open, chasing puts)?",
    "Does expiry cover the catalyst?",
]

REJECT_TAGS = (
    "0dte_crush",
    "book_conflict",
    "rechurn",
    "second_bite",
    "soft_band_blowout",
    "no_live_quote",
)


def run_checklist(
    signal: Signal,
    *,
    has_live_quote: bool = False,
    reject_tags: list[str] | None = None,
    force_skip: bool = False,
) -> ChecklistResult:
    """Judgment framework — returns recommended action. Does not place trades."""
    reject_tags = list(reject_tags or [])
    soft_notes: list[str] = []
    questions = HARD_QUESTIONS + SOFT_QUESTIONS

    hard_ok = True
    if signal.kind == "options" and not has_live_quote:
        hard_ok = False
        if "no_live_quote" not in reject_tags:
            reject_tags.append("no_live_quote")
        soft_notes.append("No live bid/ask — story_only only.")

    if not (signal.thesis or "").strip():
        soft_notes.append("Thesis empty — fill before sizing.")

    # no_live_quote => story_only (not a hard skip). Other reject tags => skip.
    soft_rejects = {"no_live_quote"}
    hard_skips = [r for r in reject_tags if r not in soft_rejects]

    if force_skip or hard_skips:
        action: Action = "skip"
    elif not hard_ok:
        action = "story_only"
    else:
        action = "story_only"  # free cut never auto-recommends place
        soft_notes.append(
            "Free cut is alert-only. After checklist + live quote, YOU decide size."
        )

    return ChecklistResult(
        hard_ok=hard_ok,
        soft_notes=soft_notes,
        reject_reasons=reject_tags,
        action=action,
        questions=questions,
    )


def print_checklist(result: ChecklistResult) -> None:
    print("=== Desk checklist ===")
    print(f"action: {result.action}")
    print(f"hard_ok: {result.hard_ok}")
    if result.reject_reasons:
        print("reject:", ", ".join(result.reject_reasons))
    for n in result.soft_notes:
        print("-", n)
    print("\nAnswer before you size:")
    for i, q in enumerate(result.questions, 1):
        print(f"  {i}. {q}")
