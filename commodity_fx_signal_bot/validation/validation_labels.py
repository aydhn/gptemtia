"""
Controlled label set for validation status, splits, and optimizer candidates.
"""

_VALIDATION_STATUS_LABELS = {
    "validation_passed",
    "validation_failed",
    "validation_warning",
    "insufficient_data",
    "insufficient_trades",
    "overfitting_risk_high",
    "robustness_low",
    "unstable_parameters",
    "unknown_validation_status",
}

_SPLIT_LABELS = {
    "train",
    "test",
    "in_sample",
    "out_of_sample",
    "walk_forward_train",
    "walk_forward_test",
}

_OPTIMIZER_CANDIDATE_LABELS = {
    "optimizer_candidate_passed",
    "optimizer_candidate_rejected",
    "optimizer_candidate_watchlist",
    "optimizer_candidate_overfit_warning",
    "optimizer_candidate_insufficient_data",
    "unknown_optimizer_candidate",
}

_BLOCKING_STATUS_LABELS = {
    "validation_failed",
    "insufficient_data",
    "insufficient_trades",
    "overfitting_risk_high",
    "robustness_low",
    "unstable_parameters",
    "unknown_validation_status",
}


def list_validation_status_labels() -> list[str]:
    """Returns a list of all valid validation status labels."""
    return sorted(list(_VALIDATION_STATUS_LABELS))


def list_split_labels() -> list[str]:
    """Returns a list of all valid split labels."""
    return sorted(list(_SPLIT_LABELS))


def list_optimizer_candidate_labels() -> list[str]:
    """Returns a list of all valid optimizer candidate labels."""
    return sorted(list(_OPTIMIZER_CANDIDATE_LABELS))


def validate_validation_status(label: str) -> None:
    """Validates if a label is a valid validation status."""
    if label not in _VALIDATION_STATUS_LABELS:
        raise ValueError(f"Invalid validation status label: {label}")


def validate_split_label(label: str) -> None:
    """Validates if a label is a valid split label."""
    if label not in _SPLIT_LABELS:
        raise ValueError(f"Invalid split label: {label}")


def validate_optimizer_candidate_label(label: str) -> None:
    """Validates if a label is a valid optimizer candidate label."""
    if label not in _OPTIMIZER_CANDIDATE_LABELS:
        raise ValueError(f"Invalid optimizer candidate label: {label}")


def is_blocking_validation_status(label: str) -> bool:
    """Checks if a validation status label represents a blocking condition."""
    validate_validation_status(label)
    return label in _BLOCKING_STATUS_LABELS
