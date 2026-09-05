"""Phase 123 Feature Quality and Drift Labels and Enums.

Defines standardized domain, severity, and status labels for quality and drift
diagnostics, enforcing consistent validation and reporting across all Phase 123 layers.
"""

from typing import List

QUALITY_DRIFT_DOMAIN_LABELS: List[str] = [
    "feature_quality_drift_profile_domain",
    "feature_quality_drift_domain",
    "quality_metric_domain",
    "drift_metric_domain",
    "threshold_domain",
    "input_contract_domain",
    "missingness_domain",
    "infinite_value_domain",
    "all_nan_domain",
    "zero_variance_domain",
    "duplicate_value_domain",
    "distribution_summary_domain",
    "distribution_drift_domain",
    "rolling_stability_domain",
    "staleness_domain",
    "namespace_quality_domain",
    "factor_quality_domain",
    "factor_drift_domain",
    "factor_availability_domain",
    "dependency_quality_domain",
    "macro_calendar_news_quality_domain",
    "cross_asset_quality_domain",
    "quality_finding_domain",
    "drift_finding_domain",
    "manual_review_domain",
    "scoring_domain",
    "manifest_domain",
    "health_domain",
    "validation_domain",
    "safety_domain",
    "phase_124_handoff_domain",
    "unknown_quality_drift_domain",
]

QUALITY_DRIFT_SEVERITY_LABELS: List[str] = [
    "quality_critical",
    "quality_high",
    "quality_medium",
    "quality_low",
    "quality_info",
    "drift_critical",
    "drift_high",
    "drift_medium",
    "drift_low",
    "drift_info",
]

QUALITY_DRIFT_STATUS_LABELS: List[str] = [
    "diagnostic_pass",
    "diagnostic_pass_with_warnings",
    "diagnostic_fail",
    "diagnostic_manual_review_required",
    "diagnostic_placeholder_only",
    "diagnostic_blocked_by_safety",
    "diagnostic_unknown",
]


def list_quality_drift_domain_labels() -> List[str]:
    """Return all valid domain labels."""
    return list(QUALITY_DRIFT_DOMAIN_LABELS)


def list_quality_drift_severity_labels() -> List[str]:
    """Return all valid severity labels."""
    return list(QUALITY_DRIFT_SEVERITY_LABELS)


def list_quality_drift_status_labels() -> List[str]:
    """Return all valid status labels."""
    return list(QUALITY_DRIFT_STATUS_LABELS)


def validate_quality_drift_domain_label(label: str) -> bool:
    """Validate whether label is recognized."""
    if label not in QUALITY_DRIFT_DOMAIN_LABELS:
        raise ValueError(f"Unknown domain label: {label}")
    return True


def validate_quality_drift_severity_label(label: str) -> bool:
    """Validate whether severity is recognized."""
    if label not in QUALITY_DRIFT_SEVERITY_LABELS:
        raise ValueError(f"Unknown severity label: {label}")
    return True


def validate_quality_drift_status_label(label: str) -> bool:
    """Validate whether status is recognized."""
    if label not in QUALITY_DRIFT_STATUS_LABELS:
        raise ValueError(f"Unknown status label: {label}")
    return True
