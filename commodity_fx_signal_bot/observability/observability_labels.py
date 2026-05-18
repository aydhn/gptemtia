"""
Controlled label sets for observability, including health status, components, and error categories.
"""

from typing import List


# --- Health Status Labels ---
_HEALTH_STATUS_LABELS = {
    "healthy",
    "degraded",
    "unhealthy",
    "critical",
    "unknown",
}


# --- Component Labels ---
_COMPONENT_LABELS = {
    "config",
    "paths",
    "data_lake",
    "feature_store",
    "data_pipeline",
    "feature_pipeline",
    "signal_pipeline",
    "decision_pipeline",
    "strategy_pipeline",
    "risk_pipeline",
    "sizing_pipeline",
    "level_pipeline",
    "backtest_pipeline",
    "performance_pipeline",
    "validation_pipeline",
    "ml_dataset_pipeline",
    "ml_training_pipeline",
    "ml_prediction_pipeline",
    "ml_integration_pipeline",
    "paper_pipeline",
    "notification_pipeline",
    "orchestration_pipeline",
    "unknown_component",
}


# --- Error Severity Labels ---
_ERROR_SEVERITY_LABELS = {
    "info",
    "warning",
    "error",
    "critical",
    "fatal",
    "unknown",
}


# --- Error Category Labels ---
_ERROR_CATEGORY_LABELS = {
    "config_error",
    "data_error",
    "dependency_error",
    "validation_error",
    "quality_error",
    "runtime_error",
    "io_error",
    "network_error",
    "artifact_error",
    "schema_error",
    "leakage_error",
    "notification_error",
    "orchestration_error",
    "unknown_error",
}


def list_health_status_labels() -> List[str]:
    """List all valid health status labels."""
    return sorted(list(_HEALTH_STATUS_LABELS))


def list_component_labels() -> List[str]:
    """List all valid component labels."""
    return sorted(list(_COMPONENT_LABELS))


def list_error_severity_labels() -> List[str]:
    """List all valid error severity labels."""
    return sorted(list(_ERROR_SEVERITY_LABELS))


def list_error_category_labels() -> List[str]:
    """List all valid error category labels."""
    return sorted(list(_ERROR_CATEGORY_LABELS))


def validate_health_status(label: str) -> None:
    """Validate a health status label."""
    if label not in _HEALTH_STATUS_LABELS:
        raise ValueError(f"Invalid health status label: {label}. Must be one of: {list_health_status_labels()}")


def validate_component_label(label: str) -> None:
    """Validate a component label."""
    if label not in _COMPONENT_LABELS:
        raise ValueError(f"Invalid component label: {label}. Must be one of: {list_component_labels()}")


def validate_error_severity(label: str) -> None:
    """Validate an error severity label."""
    if label not in _ERROR_SEVERITY_LABELS:
        raise ValueError(f"Invalid error severity label: {label}. Must be one of: {list_error_severity_labels()}")


def validate_error_category(label: str) -> None:
    """Validate an error category label."""
    if label not in _ERROR_CATEGORY_LABELS:
        raise ValueError(f"Invalid error category label: {label}. Must be one of: {list_error_category_labels()}")


def infer_health_status_from_score(score: float) -> str:
    """Infer health status label from a normalized score (0.0 to 1.0)."""
    if score < 0.0 or score > 1.0:
        raise ValueError(f"Score must be between 0.0 and 1.0, got: {score}")

    if score >= 0.95:
        return "healthy"
    elif score >= 0.70:
        return "degraded"
    elif score >= 0.40:
        return "unhealthy"
    else:
        return "critical"


def is_critical_health_status(label: str) -> bool:
    """Check if a health status label is critical or fatal."""
    validate_health_status(label)
    return label in {"critical", "fatal"}
