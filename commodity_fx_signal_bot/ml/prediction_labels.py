from typing import List

_PREDICTION_CANDIDATE_LABELS = [
    "prediction_candidate_ready",
    "prediction_candidate_warning",
    "prediction_candidate_rejected",
    "prediction_candidate_low_confidence",
    "prediction_candidate_high_uncertainty",
    "prediction_candidate_model_quality_failed",
    "prediction_candidate_dataset_quality_failed",
    "prediction_candidate_leakage_risk",
    "prediction_candidate_unknown",
]

_PREDICTION_DIRECTION_LABELS = [
    "predicted_up",
    "predicted_down",
    "predicted_flat",
    "predicted_unknown",
]

_PREDICTION_TASK_LABELS = [
    "classification_prediction",
    "regression_prediction",
    "ensemble_prediction",
    "unknown_prediction_task",
]

_PREDICTION_CONTEXT_LABELS = [
    "ml_context_supportive",
    "ml_context_conflicting",
    "ml_context_neutral",
    "ml_context_uncertain",
    "ml_context_unavailable",
]

def list_prediction_candidate_labels() -> List[str]:
    return _PREDICTION_CANDIDATE_LABELS.copy()

def list_prediction_direction_labels() -> List[str]:
    return _PREDICTION_DIRECTION_LABELS.copy()

def list_prediction_task_labels() -> List[str]:
    return _PREDICTION_TASK_LABELS.copy()

def list_prediction_context_labels() -> List[str]:
    return _PREDICTION_CONTEXT_LABELS.copy()

def validate_prediction_candidate_label(label: str) -> None:
    if label not in _PREDICTION_CANDIDATE_LABELS:
        raise ValueError(f"Invalid prediction candidate label: {label}")

def validate_prediction_direction_label(label: str) -> None:
    if label not in _PREDICTION_DIRECTION_LABELS:
        raise ValueError(f"Invalid prediction direction label: {label}")

def validate_prediction_task_label(label: str) -> None:
    if label not in _PREDICTION_TASK_LABELS:
        raise ValueError(f"Invalid prediction task label: {label}")

def validate_prediction_context_label(label: str) -> None:
    if label not in _PREDICTION_CONTEXT_LABELS:
        raise ValueError(f"Invalid prediction context label: {label}")

def is_blocking_prediction_label(label: str) -> bool:
    """Check if the candidate label implies a rejection or block."""
    return label in [
        "prediction_candidate_rejected",
        "prediction_candidate_model_quality_failed",
        "prediction_candidate_dataset_quality_failed",
        "prediction_candidate_leakage_risk",
    ]
