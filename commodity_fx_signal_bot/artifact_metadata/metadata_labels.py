"""
Controlled label set for artifact metadata.
"""

_ARTIFACT_TYPE_LABELS = [
    "model_artifact",
    "dataset_artifact",
    "feature_set_artifact",
    "experiment_artifact",
    "backtest_artifact",
    "validation_artifact",
    "scenario_artifact",
    "regression_artifact",
    "synthetic_data_artifact",
    "research_report_artifact",
    "evidence_artifact",
    "documentation_artifact",
    "unknown_artifact"
]

_CARD_TYPE_LABELS = [
    "model_card",
    "dataset_card",
    "experiment_card",
    "reproducibility_card",
    "backtest_card",
    "scenario_card",
    "regression_card",
    "feature_set_card",
    "synthetic_data_card",
    "research_report_card",
    "lineage_card",
    "limitation_card",
    "intended_use_card",
    "non_use_policy_card",
    "unknown_card"
]

_METADATA_STATUS_LABELS = [
    "metadata_complete",
    "metadata_partial",
    "metadata_missing",
    "metadata_stale",
    "metadata_blocked_by_safety",
    "metadata_unknown"
]

_ARTIFACT_USE_LABELS = [
    "offline_research_use_only",
    "synthetic_demo_use_only",
    "validation_use_only",
    "documentation_use_only",
    "not_for_live_trading",
    "not_for_broker_execution",
    "not_for_investment_advice",
    "not_for_model_deployment",
    "unknown_use_label"
]

_REPRODUCIBILITY_LABELS = [
    "reproducible_with_local_fixtures",
    "reproducible_with_warnings",
    "partially_reproducible",
    "not_reproducible",
    "reproducibility_unknown"
]

def list_artifact_type_labels() -> list[str]:
    return list(_ARTIFACT_TYPE_LABELS)

def list_card_type_labels() -> list[str]:
    return list(_CARD_TYPE_LABELS)

def list_metadata_status_labels() -> list[str]:
    return list(_METADATA_STATUS_LABELS)

def list_artifact_use_labels() -> list[str]:
    return list(_ARTIFACT_USE_LABELS)

def list_reproducibility_labels() -> list[str]:
    return list(_REPRODUCIBILITY_LABELS)

def validate_artifact_type(label: str) -> None:
    if label not in _ARTIFACT_TYPE_LABELS:
        raise ValueError(f"Invalid artifact type label: {label}")

def validate_card_type(label: str) -> None:
    if label not in _CARD_TYPE_LABELS:
        raise ValueError(f"Invalid card type label: {label}")

def validate_metadata_status(label: str) -> None:
    if label not in _METADATA_STATUS_LABELS:
        raise ValueError(f"Invalid metadata status label: {label}")

def validate_artifact_use_label(label: str) -> None:
    if label not in _ARTIFACT_USE_LABELS:
        raise ValueError(f"Invalid artifact use label: {label}")

def validate_reproducibility_label(label: str) -> None:
    if label not in _REPRODUCIBILITY_LABELS:
        raise ValueError(f"Invalid reproducibility label: {label}")
