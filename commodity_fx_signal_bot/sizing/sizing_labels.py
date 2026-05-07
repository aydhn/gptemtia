from typing import List

_SIZING_CANDIDATE_LABELS = [
    "sizing_approved_candidate",
    "sizing_rejected_candidate",
    "sizing_watchlist_candidate",
    "sizing_zero_candidate",
    "insufficient_sizing_context_candidate",
    "invalid_risk_candidate",
    "excessive_risk_candidate",
    "insufficient_data_quality_candidate",
    "unknown_sizing_candidate"
]

_SIZING_METHOD_LABELS = [
    "fixed_fractional_theoretical",
    "atr_based_theoretical",
    "volatility_adjusted_theoretical",
    "budget_capped_theoretical",
    "zero_size_theoretical",
    "unknown_sizing_method"
]

_SIZING_SEVERITY_LABELS = [
    "low",
    "moderate",
    "elevated",
    "high",
    "extreme",
    "unknown"
]

def list_sizing_candidate_labels() -> List[str]:
    return _SIZING_CANDIDATE_LABELS.copy()

def list_sizing_method_labels() -> List[str]:
    return _SIZING_METHOD_LABELS.copy()

def list_sizing_severity_labels() -> List[str]:
    return _SIZING_SEVERITY_LABELS.copy()

def validate_sizing_candidate_label(label: str) -> None:
    if label not in _SIZING_CANDIDATE_LABELS:
        raise ValueError(f"Invalid sizing candidate label: {label}")

def validate_sizing_method_label(label: str) -> None:
    if label not in _SIZING_METHOD_LABELS:
        raise ValueError(f"Invalid sizing method label: {label}")

def validate_sizing_severity_label(label: str) -> None:
    if label not in _SIZING_SEVERITY_LABELS:
        raise ValueError(f"Invalid sizing severity label: {label}")

def sizing_severity_from_risk(score: float) -> str:
    """Derives a sizing severity label from a risk score (0-1)."""
    if score < 0.20:
        return "low"
    elif score < 0.40:
        return "moderate"
    elif score < 0.60:
        return "elevated"
    elif score < 0.80:
        return "high"
    else:
        return "extreme"

def is_blocking_sizing_label(label: str) -> bool:
    """Returns True if the label represents a blocked or invalid sizing candidate."""
    return label in [
        "sizing_rejected_candidate",
        "sizing_zero_candidate",
        "insufficient_sizing_context_candidate",
        "invalid_risk_candidate",
        "excessive_risk_candidate",
        "insufficient_data_quality_candidate",
        "unknown_sizing_candidate"
    ]
