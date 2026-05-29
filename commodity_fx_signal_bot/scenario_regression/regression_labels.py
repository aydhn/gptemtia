_regression_type_labels = [
    "golden_output_regression",
    "snapshot_regression",
    "deterministic_replay_regression",
    "fixture_reproducibility_regression",
    "output_contract_regression",
    "demo_workflow_regression",
    "end_to_end_acceptance_regression",
    "drift_regression",
    "unknown_regression",
]

_regression_status_labels = [
    "regression_passed",
    "regression_passed_with_warnings",
    "regression_failed",
    "regression_blocked",
    "regression_skipped",
    "regression_unknown",
]

_snapshot_diff_labels = [
    "snapshot_identical",
    "snapshot_numeric_diff_within_tolerance",
    "snapshot_text_diff_within_tolerance",
    "snapshot_minor_diff",
    "snapshot_major_diff",
    "snapshot_missing",
    "snapshot_unknown",
]

_replay_status_labels = [
    "replay_consistent",
    "replay_consistent_with_warnings",
    "replay_inconsistent",
    "replay_blocked",
    "replay_skipped",
    "replay_unknown",
]

_acceptance_labels = [
    "demo_accepted_offline",
    "demo_accepted_with_warnings",
    "demo_not_accepted",
    "demo_blocked_by_safety",
    "demo_insufficient_data",
    "demo_unknown",
]

def list_regression_type_labels() -> list[str]:
    return _regression_type_labels

def list_regression_status_labels() -> list[str]:
    return _regression_status_labels

def list_snapshot_diff_labels() -> list[str]:
    return _snapshot_diff_labels

def list_replay_status_labels() -> list[str]:
    return _replay_status_labels

def list_acceptance_labels() -> list[str]:
    return _acceptance_labels

def validate_regression_type(label: str) -> None:
    if label not in _regression_type_labels:
        raise ValueError(f"Invalid regression type label: {label}")

def validate_regression_status(label: str) -> None:
    if label not in _regression_status_labels:
        raise ValueError(f"Invalid regression status label: {label}")

def validate_snapshot_diff_label(label: str) -> None:
    if label not in _snapshot_diff_labels:
        raise ValueError(f"Invalid snapshot diff label: {label}")

def validate_replay_status(label: str) -> None:
    if label not in _replay_status_labels:
        raise ValueError(f"Invalid replay status label: {label}")

def validate_acceptance_label(label: str) -> None:
    if label not in _acceptance_labels:
        raise ValueError(f"Invalid acceptance label: {label}")
