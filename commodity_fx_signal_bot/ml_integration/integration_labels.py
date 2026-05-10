"""
ML Integration Label Definitions
"""

from typing import List


# ML context labels
ML_CONTEXT_SUPPORTIVE = "ml_context_supportive"
ML_CONTEXT_CONFLICTING = "ml_context_conflicting"
ML_CONTEXT_NEUTRAL = "ml_context_neutral"
ML_CONTEXT_UNCERTAIN = "ml_context_uncertain"
ML_CONTEXT_UNAVAILABLE = "ml_context_unavailable"
ML_CONTEXT_QUALITY_FAILED = "ml_context_quality_failed"
ML_CONTEXT_LEAKAGE_RISK = "ml_context_leakage_risk"
UNKNOWN_ML_CONTEXT = "unknown_ml_context"


_ML_CONTEXT_LABELS = [
    ML_CONTEXT_SUPPORTIVE,
    ML_CONTEXT_CONFLICTING,
    ML_CONTEXT_NEUTRAL,
    ML_CONTEXT_UNCERTAIN,
    ML_CONTEXT_UNAVAILABLE,
    ML_CONTEXT_QUALITY_FAILED,
    ML_CONTEXT_LEAKAGE_RISK,
    UNKNOWN_ML_CONTEXT,
]


# Alignment labels
MODEL_ALIGNED_WITH_CANDIDATE = "model_aligned_with_candidate"
MODEL_CONFLICTS_WITH_CANDIDATE = "model_conflicts_with_candidate"
MODEL_NEUTRAL_TO_CANDIDATE = "model_neutral_to_candidate"
MODEL_UNCERTAIN_FOR_CANDIDATE = "model_uncertain_for_candidate"
MODEL_UNAVAILABLE_FOR_CANDIDATE = "model_unavailable_for_candidate"

_MODEL_ALIGNMENT_LABELS = [
    MODEL_ALIGNED_WITH_CANDIDATE,
    MODEL_CONFLICTS_WITH_CANDIDATE,
    MODEL_NEUTRAL_TO_CANDIDATE,
    MODEL_UNCERTAIN_FOR_CANDIDATE,
    MODEL_UNAVAILABLE_FOR_CANDIDATE,
]


# Integration status labels
ML_INTEGRATION_READY = "ml_integration_ready"
ML_INTEGRATION_WARNING = "ml_integration_warning"
ML_INTEGRATION_REJECTED = "ml_integration_rejected"
ML_INTEGRATION_RESEARCH_ONLY = "ml_integration_research_only"
ML_INTEGRATION_UNAVAILABLE = "ml_integration_unavailable"
UNKNOWN_INTEGRATION_STATUS = "unknown_integration_status"

_ML_INTEGRATION_STATUS_LABELS = [
    ML_INTEGRATION_READY,
    ML_INTEGRATION_WARNING,
    ML_INTEGRATION_REJECTED,
    ML_INTEGRATION_RESEARCH_ONLY,
    ML_INTEGRATION_UNAVAILABLE,
    UNKNOWN_INTEGRATION_STATUS,
]


def list_ml_context_labels() -> List[str]:
    return list(_ML_CONTEXT_LABELS)


def list_model_alignment_labels() -> List[str]:
    return list(_MODEL_ALIGNMENT_LABELS)


def list_ml_integration_status_labels() -> List[str]:
    return list(_ML_INTEGRATION_STATUS_LABELS)


def validate_ml_context_label(label: str) -> None:
    if label not in _ML_CONTEXT_LABELS:
        raise ValueError(f"Invalid ML context label: {label}")


def validate_model_alignment_label(label: str) -> None:
    if label not in _MODEL_ALIGNMENT_LABELS:
        raise ValueError(f"Invalid model alignment label: {label}")


def validate_ml_integration_status_label(label: str) -> None:
    if label not in _ML_INTEGRATION_STATUS_LABELS:
        raise ValueError(f"Invalid ML integration status label: {label}")


def is_conflicting_alignment(label: str) -> bool:
    """Check if the label indicates a conflict. Note: conflicting alignment is not a real trade ban."""
    return label == MODEL_CONFLICTS_WITH_CANDIDATE


def is_supportive_alignment(label: str) -> bool:
    """Check if the label indicates support. Note: supportive alignment is not a live trade approval."""
    return label == MODEL_ALIGNED_WITH_CANDIDATE


def is_blocking_ml_context_label(label: str) -> bool:
    """Check if the label blocks integration due to quality/leakage risks."""
    return label in [ML_CONTEXT_QUALITY_FAILED, ML_CONTEXT_LEAKAGE_RISK]
