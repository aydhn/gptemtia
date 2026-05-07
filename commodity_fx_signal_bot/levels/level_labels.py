_LEVEL_CANDIDATE_LABELS = [
    "level_approved_candidate",
    "level_rejected_candidate",
    "level_watchlist_candidate",
    "level_zero_candidate",
    "insufficient_level_context_candidate",
    "invalid_price_level_candidate",
    "excessive_stop_distance_candidate",
    "insufficient_reward_risk_candidate",
    "unknown_level_candidate",
]

_LEVEL_METHOD_LABELS = [
    "atr_based_theoretical",
    "structure_based_theoretical",
    "volatility_adjusted_theoretical",
    "hybrid_theoretical",
    "zero_level_theoretical",
    "unknown_level_method",
]

_LEVEL_SEVERITY_LABELS = ["low", "moderate", "elevated", "high", "extreme", "unknown"]

_LEVEL_TYPE_LABELS = [
    "stop_candidate",
    "target_candidate",
    "invalidation_candidate",
    "exit_context_candidate",
    "continuation_target_candidate",
    "unknown_level_type",
]


def list_level_candidate_labels() -> list[str]:
    return _LEVEL_CANDIDATE_LABELS.copy()


def list_level_method_labels() -> list[str]:
    return _LEVEL_METHOD_LABELS.copy()


def list_level_severity_labels() -> list[str]:
    return _LEVEL_SEVERITY_LABELS.copy()


def list_level_type_labels() -> list[str]:
    return _LEVEL_TYPE_LABELS.copy()


def validate_level_candidate_label(label: str) -> None:
    if label not in _LEVEL_CANDIDATE_LABELS:
        raise ValueError(f"Geçersiz level candidate label: {label}")


def validate_level_method_label(label: str) -> None:
    if label not in _LEVEL_METHOD_LABELS:
        raise ValueError(f"Geçersiz level method label: {label}")


def validate_level_type_label(label: str) -> None:
    if label not in _LEVEL_TYPE_LABELS:
        raise ValueError(f"Geçersiz level type label: {label}")


def level_severity_from_score(score: float) -> str:
    if score < 0.2:
        return "low"
    elif score < 0.4:
        return "moderate"
    elif score < 0.6:
        return "elevated"
    elif score < 0.8:
        return "high"
    else:
        return "extreme"


def is_blocking_level_label(label: str) -> bool:
    blocking = [
        "level_rejected_candidate",
        "level_zero_candidate",
        "insufficient_level_context_candidate",
        "invalid_price_level_candidate",
        "excessive_stop_distance_candidate",
        "insufficient_reward_risk_candidate",
    ]
    return label in blocking
