from typing import List

_PERFORMANCE_CHECK_LABELS = [
    "runtime_profile_check",
    "memory_profile_check",
    "cpu_profile_check",
    "gpu_awareness_check",
    "resource_budget_check",
    "cache_check",
    "batch_plan_check",
    "checkpoint_check",
    "stability_check",
    "bottleneck_check",
    "optimization_check",
    "unknown_performance_check"
]

_RESOURCE_STATUS_LABELS = [
    "within_budget",
    "near_budget_limit",
    "over_budget",
    "budget_unknown"
]

_CACHE_STATUS_LABELS = [
    "cache_hit",
    "cache_miss",
    "cache_stale",
    "cache_invalid",
    "cache_disabled",
    "cache_unknown"
]

_OPTIMIZATION_LABELS = [
    "optimization_not_needed",
    "low_risk_optimization_candidate",
    "medium_risk_optimization_candidate",
    "high_risk_manual_review_required",
    "optimization_unknown"
]

_STABILITY_LABELS = [
    "stable_large_run",
    "stable_with_warnings",
    "unstable_large_run",
    "insufficient_stability_data",
    "unknown_stability"
]

def list_performance_check_labels() -> List[str]:
    return _PERFORMANCE_CHECK_LABELS.copy()

def list_resource_status_labels() -> List[str]:
    return _RESOURCE_STATUS_LABELS.copy()

def list_cache_status_labels() -> List[str]:
    return _CACHE_STATUS_LABELS.copy()

def list_optimization_labels() -> List[str]:
    return _OPTIMIZATION_LABELS.copy()

def list_stability_labels() -> List[str]:
    return _STABILITY_LABELS.copy()

def validate_performance_check_label(label: str) -> None:
    if label not in _PERFORMANCE_CHECK_LABELS:
        raise ValueError(f"Invalid performance check label: {label}")

def validate_resource_status_label(label: str) -> None:
    if label not in _RESOURCE_STATUS_LABELS:
        raise ValueError(f"Invalid resource status label: {label}")

def validate_cache_status_label(label: str) -> None:
    if label not in _CACHE_STATUS_LABELS:
        raise ValueError(f"Invalid cache status label: {label}")

def validate_optimization_label(label: str) -> None:
    if label not in _OPTIMIZATION_LABELS:
        raise ValueError(f"Invalid optimization label: {label}")

def validate_stability_label(label: str) -> None:
    if label not in _STABILITY_LABELS:
        raise ValueError(f"Invalid stability label: {label}")
