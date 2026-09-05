"""Phase 123 Feature Quality Metric Registry.

Registers standard quality diagnostic metrics evaluated across feature columns.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)

SUPPORTED_QUALITY_METRICS: List[Dict[str, Any]] = [
    {
        "metric_id": "missingness_ratio",
        "metric_name": "Missingness Ratio",
        "domain": "missingness_domain",
        "description": "Proportion of missing (NaN/None) values in feature column.",
        "metric_type": "ratio",
        "severity": "quality_medium",
        "default_warning_threshold": 0.25,
        "default_critical_threshold": 0.50,
    },
    {
        "metric_id": "infinite_value_ratio",
        "metric_name": "Infinite Value Ratio",
        "domain": "infinite_value_domain",
        "description": "Proportion of infinite (+/-inf) values in feature column.",
        "metric_type": "ratio",
        "severity": "quality_critical",
        "default_warning_threshold": 0.0,
        "default_critical_threshold": 0.0,
    },
    {
        "metric_id": "all_nan_flag",
        "metric_name": "All-NaN Flag",
        "domain": "all_nan_domain",
        "description": "Flag indicating column contains exclusively NaN values.",
        "metric_type": "flag",
        "severity": "quality_critical",
        "default_warning_threshold": 0.0,
        "default_critical_threshold": 1.0,
    },
    {
        "metric_id": "zero_variance_flag",
        "metric_name": "Zero Variance Flag",
        "domain": "zero_variance_domain",
        "description": "Flag indicating column standard deviation is zero (constant value).",
        "metric_type": "flag",
        "severity": "quality_high",
        "default_warning_threshold": 1.0,
        "default_critical_threshold": 1.0,
    },
    {
        "metric_id": "duplicate_value_ratio",
        "metric_name": "Duplicate Value Ratio",
        "domain": "duplicate_value_domain",
        "description": "Ratio of modal repeated value frequency to total rows.",
        "metric_type": "ratio",
        "severity": "quality_medium",
        "default_warning_threshold": 0.90,
        "default_critical_threshold": 0.99,
    },
    {
        "metric_id": "numeric_sanity_flag",
        "metric_name": "Numeric Sanity Flag",
        "domain": "quality_metric_domain",
        "description": "Flag indicating numeric types comply with expected dtype ranges.",
        "metric_type": "flag",
        "severity": "quality_high",
        "default_warning_threshold": 0.0,
        "default_critical_threshold": 1.0,
    },
    {
        "metric_id": "namespace_validity_flag",
        "metric_name": "Namespace Validity Flag",
        "domain": "namespace_quality_domain",
        "description": "Flag indicating absence of forward-looking or forbidden name tokens.",
        "metric_type": "flag",
        "severity": "quality_critical",
        "default_warning_threshold": 0.0,
        "default_critical_threshold": 1.0,
    },
    {
        "metric_id": "source_validation_status",
        "metric_name": "Source Validation Status",
        "domain": "quality_metric_domain",
        "description": "Status of upstream Phase 121 validation checks.",
        "metric_type": "status",
        "severity": "quality_high",
        "default_warning_threshold": 0.0,
        "default_critical_threshold": 1.0,
    },
    {
        "metric_id": "manual_review_blocker_count",
        "metric_name": "Manual Review Blocker Count",
        "domain": "manual_review_domain",
        "description": "Number of critical issues requiring manual inspection.",
        "metric_type": "count",
        "severity": "quality_high",
        "default_warning_threshold": 1.0,
        "default_critical_threshold": 5.0,
    },
]


def list_supported_quality_metrics() -> List[str]:
    """Return metric ids of supported quality metrics."""
    return [m["metric_id"] for m in SUPPORTED_QUALITY_METRICS]


def build_feature_quality_metric_registry(
    profile: FeatureQualityDriftProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of registered quality metrics."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    records = []
    for m in SUPPORTED_QUALITY_METRICS:
        records.append({
            "metric_id": m["metric_id"],
            "metric_name": m["metric_name"],
            "domain": m["domain"],
            "description": m["description"],
            "metric_type": m["metric_type"],
            "severity": m["severity"],
            "default_warning_threshold": m["default_warning_threshold"],
            "default_critical_threshold": m["default_critical_threshold"],
            "non_signal": True,
            "destructive_action_allowed": False,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_quality_metrics": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
        "destructive_action_allowed": False,
    }
    return df, summary
