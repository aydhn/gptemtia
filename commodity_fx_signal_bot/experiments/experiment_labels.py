EXPERIMENT_TYPE_LABELS = [
    "baseline_experiment",
    "candidate_experiment",
    "ablation_experiment",
    "comparison_experiment",
    "rerun_experiment",
    "diagnostic_experiment",
    "unknown_experiment",
]

EXPERIMENT_STATUS_LABELS = [
    "experiment_planned",
    "experiment_running",
    "experiment_completed",
    "experiment_failed",
    "experiment_skipped",
    "experiment_dry_run",
    "experiment_rejected",
    "experiment_unknown",
]

HYPOTHESIS_STATUS_LABELS = [
    "hypothesis_proposed",
    "hypothesis_under_test",
    "hypothesis_supported",
    "hypothesis_not_supported",
    "hypothesis_inconclusive",
    "hypothesis_rejected",
    "hypothesis_unknown",
]

COMPARISON_RESULT_LABELS = [
    "candidate_better",
    "baseline_better",
    "mixed_result",
    "no_material_difference",
    "insufficient_comparison_data",
    "comparison_unknown",
]

def list_experiment_type_labels() -> list[str]:
    return list(EXPERIMENT_TYPE_LABELS)

def list_experiment_status_labels() -> list[str]:
    return list(EXPERIMENT_STATUS_LABELS)

def list_hypothesis_status_labels() -> list[str]:
    return list(HYPOTHESIS_STATUS_LABELS)

def list_comparison_result_labels() -> list[str]:
    return list(COMPARISON_RESULT_LABELS)

def validate_experiment_type(label: str) -> None:
    if label not in EXPERIMENT_TYPE_LABELS:
        raise ValueError(f"Invalid experiment type label: {label}")

def validate_experiment_status(label: str) -> None:
    if label not in EXPERIMENT_STATUS_LABELS:
        raise ValueError(f"Invalid experiment status label: {label}")

def validate_hypothesis_status(label: str) -> None:
    if label not in HYPOTHESIS_STATUS_LABELS:
        raise ValueError(f"Invalid hypothesis status label: {label}")

def validate_comparison_result_label(label: str) -> None:
    if label not in COMPARISON_RESULT_LABELS:
        raise ValueError(f"Invalid comparison result label: {label}")
