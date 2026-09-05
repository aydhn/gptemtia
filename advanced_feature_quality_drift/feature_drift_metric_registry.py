"""Phase 123 Feature Drift Metric Registry.

Registers standard distribution drift and stability monitoring metrics.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)

SUPPORTED_DRIFT_METRICS: List[Dict[str, Any]] = [
    {
        "metric_id": "distribution_mean_shift",
        "metric_name": "Distribution Mean Shift",
        "domain": "distribution_drift_domain",
        "description": "Absolute delta between baseline and current window sample means.",
        "drift_type": "central_tendency",
        "severity": "drift_medium",
        "default_warning_threshold": 0.50,
        "default_critical_threshold": 1.00,
    },
    {
        "metric_id": "distribution_std_shift",
        "metric_name": "Distribution Std Shift",
        "domain": "distribution_drift_domain",
        "description": "Absolute delta between baseline and current window standard deviations.",
        "drift_type": "dispersion",
        "severity": "drift_medium",
        "default_warning_threshold": 0.50,
        "default_critical_threshold": 1.00,
    },
    {
        "metric_id": "quantile_shift",
        "metric_name": "Quantile Shift",
        "domain": "distribution_drift_domain",
        "description": "Composite absolute shift across 25th, 50th, and 75th percentiles.",
        "drift_type": "shape",
        "severity": "drift_medium",
        "default_warning_threshold": 0.60,
        "default_critical_threshold": 1.20,
    },
    {
        "metric_id": "missingness_shift",
        "metric_name": "Missingness Shift",
        "domain": "missingness_domain",
        "description": "Increase in missingness ratio compared to baseline window.",
        "drift_type": "data_integrity",
        "severity": "drift_high",
        "default_warning_threshold": 0.15,
        "default_critical_threshold": 0.30,
    },
    {
        "metric_id": "zero_variance_new_flag",
        "metric_name": "New Zero Variance Flag",
        "domain": "zero_variance_domain",
        "description": "Flag indicating feature became constant in current window while non-constant in baseline.",
        "drift_type": "collapse",
        "severity": "drift_critical",
        "default_warning_threshold": 1.0,
        "default_critical_threshold": 1.0,
    },
    {
        "metric_id": "stability_score",
        "metric_name": "Rolling Stability Score",
        "domain": "rolling_stability_domain",
        "description": "Normalized stability score over rolling observation windows.",
        "drift_type": "stability",
        "severity": "drift_low",
        "default_warning_threshold": 0.60,
        "default_critical_threshold": 0.40,
    },
    {
        "metric_id": "rolling_mean_stability",
        "metric_name": "Rolling Mean Stability",
        "domain": "rolling_stability_domain",
        "description": "Coefficient of variation of rolling means.",
        "drift_type": "stability",
        "severity": "drift_medium",
        "default_warning_threshold": 0.40,
        "default_critical_threshold": 0.80,
    },
    {
        "metric_id": "rolling_std_stability",
        "metric_name": "Rolling Std Stability",
        "domain": "rolling_stability_domain",
        "description": "Coefficient of variation of rolling standard deviations.",
        "drift_type": "stability",
        "severity": "drift_medium",
        "default_warning_threshold": 0.40,
        "default_critical_threshold": 0.80,
    },
    {
        "metric_id": "population_shift_placeholder",
        "metric_name": "Population Shift Placeholder",
        "domain": "distribution_drift_domain",
        "description": "Placeholder for multivariate covariate shift diagnostics.",
        "drift_type": "multivariate",
        "severity": "drift_info",
        "default_warning_threshold": 0.50,
        "default_critical_threshold": 1.00,
    },
    {
        "metric_id": "factor_family_drift_placeholder",
        "metric_name": "Factor Family Drift Placeholder",
        "domain": "factor_drift_domain",
        "description": "Placeholder for factor family aggregate distribution drift.",
        "drift_type": "factor_level",
        "severity": "drift_info",
        "default_warning_threshold": 0.50,
        "default_critical_threshold": 1.00,
    },
]


def list_supported_drift_metrics() -> List[str]:
    """Return metric ids of supported drift metrics."""
    return [m["metric_id"] for m in SUPPORTED_DRIFT_METRICS]


def build_feature_drift_metric_registry(
    profile: FeatureQualityDriftProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary of registered drift metrics."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    records = []
    for m in SUPPORTED_DRIFT_METRICS:
        records.append({
            "metric_id": m["metric_id"],
            "metric_name": m["metric_name"],
            "domain": m["domain"],
            "description": m["description"],
            "drift_type": m["drift_type"],
            "severity": m["severity"],
            "default_warning_threshold": m["default_warning_threshold"],
            "default_critical_threshold": m["default_critical_threshold"],
            "non_signal": True,
            "destructive_action_allowed": False,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_drift_metrics": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
        "destructive_action_allowed": False,
    }
    return df, summary
