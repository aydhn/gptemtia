_STRATEGY_FAMILIES = {
    "trend_following",
    "mean_reversion",
    "breakout",
    "pullback",
    "volatility_expansion",
    "volatility_squeeze",
    "divergence_reversal",
    "momentum_continuation",
    "range_reversion",
    "macro_context",
    "no_trade",
    "watchlist",
    "unknown",
}

_STRATEGY_STATUS_LABELS = {
    "selected_candidate",
    "watchlist_candidate",
    "blocked_candidate",
    "no_trade_candidate",
    "insufficient_quality",
    "insufficient_context",
    "conflict_blocked",
    "unknown",
}


def list_strategy_families() -> list[str]:
    return sorted(list(_STRATEGY_FAMILIES))


def list_strategy_status_labels() -> list[str]:
    return sorted(list(_STRATEGY_STATUS_LABELS))


def validate_strategy_family(label: str) -> None:
    if label not in _STRATEGY_FAMILIES:
        raise ValueError(f"Invalid strategy family: {label}")


def validate_strategy_status(label: str) -> None:
    if label not in _STRATEGY_STATUS_LABELS:
        raise ValueError(f"Invalid strategy status label: {label}")


def is_directional_strategy_family(label: str) -> bool:
    validate_strategy_family(label)
    return label not in {"no_trade", "watchlist", "unknown", "macro_context"}


def is_no_trade_strategy_family(label: str) -> bool:
    validate_strategy_family(label)
    return label == "no_trade"


def is_watchlist_strategy_family(label: str) -> bool:
    validate_strategy_family(label)
    return label == "watchlist"
