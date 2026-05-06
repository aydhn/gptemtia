_RISK_CANDIDATE_LABELS = [
    "risk_approval_candidate",
    "risk_rejection_candidate",
    "risk_watchlist_candidate",
    "risk_warning_candidate",
    "insufficient_risk_context_candidate",
    "invalid_data_risk_candidate",
    "extreme_volatility_risk_candidate",
    "high_conflict_risk_candidate",
    "unknown_risk_candidate",
]
_RISK_COMPONENT_LABELS = [
    "volatility_risk",
    "gap_risk",
    "liquidity_risk",
    "data_quality_risk",
    "regime_risk",
    "mtf_risk",
    "macro_risk",
    "asset_profile_risk",
    "conflict_risk",
    "unknown_risk",
]
_RISK_SEVERITY_LABELS = ["low", "moderate", "elevated", "high", "extreme", "unknown"]


def list_risk_candidate_labels() -> list[str]:
    return list(_RISK_CANDIDATE_LABELS)


def list_risk_component_labels() -> list[str]:
    return list(_RISK_COMPONENT_LABELS)


def list_risk_severity_labels() -> list[str]:
    return list(_RISK_SEVERITY_LABELS)


def validate_risk_candidate_label(label: str) -> None:
    if label not in _RISK_CANDIDATE_LABELS:
        raise ValueError(f"Invalid risk candidate label: {label}")


def validate_risk_component_label(label: str) -> None:
    if label not in _RISK_COMPONENT_LABELS:
        raise ValueError(f"Invalid risk component label: {label}")


def validate_risk_severity_label(label: str) -> None:
    if label not in _RISK_SEVERITY_LABELS:
        raise ValueError(f"Invalid risk severity label: {label}")


def severity_from_score(score: float) -> str:
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


def is_blocking_risk_label(label: str) -> bool:
    return label in [
        "risk_rejection_candidate",
        "invalid_data_risk_candidate",
        "extreme_volatility_risk_candidate",
        "high_conflict_risk_candidate",
    ]
