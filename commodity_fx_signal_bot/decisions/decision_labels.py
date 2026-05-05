from typing import List

_DECISION_LABELS = {
    "unknown",
    "long_bias_candidate",
    "short_bias_candidate",
    "neutral_candidate",
    "no_trade_candidate",
    "watchlist_candidate",
    "conflict_candidate",
    "insufficient_quality_candidate",
    "insufficient_context_candidate",
    "risk_warning_candidate",
}

_DECISION_REASON_LABELS = {
    "strong_directional_consensus",
    "weak_directional_consensus",
    "regime_confirmed",
    "regime_conflict",
    "mtf_confirmed",
    "mtf_conflict",
    "macro_supportive",
    "macro_conflicting",
    "asset_profile_supportive",
    "asset_profile_conflicting",
    "low_quality",
    "high_conflict",
    "insufficient_data",
    "neutral_bias",
    "risk_precheck_failed",
    "watchlist_only",
}


def list_decision_labels() -> List[str]:
    return sorted(list(_DECISION_LABELS))


def list_decision_reason_labels() -> List[str]:
    return sorted(list(_DECISION_REASON_LABELS))


def validate_decision_label(label: str) -> None:
    if label not in _DECISION_LABELS:
        raise ValueError(f"Invalid decision label: {label}")


def is_directional_decision(label: str) -> bool:
    return label in {"long_bias_candidate", "short_bias_candidate"}


def is_no_trade_decision(label: str) -> bool:
    return label in {
        "no_trade_candidate",
        "conflict_candidate",
        "insufficient_quality_candidate",
        "insufficient_context_candidate",
    }


def is_warning_decision(label: str) -> bool:
    return label in {
        "risk_warning_candidate",
        "conflict_candidate",
        "insufficient_quality_candidate",
        "insufficient_context_candidate",
    }
