"""Phase 123 Feature Drift Threshold Registry.

Defines threshold boundaries for distribution shift and stability diagnostics,
strictly prohibiting automatic strategy generation or trade signaling.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)

DEFAULT_DRIFT_THRESHOLDS = {
    "distribution_mean_shift": {
        "warning": 0.50,
        "critical": 1.00,
        "unit": "standardized_delta",
        "description": "Warning if normalized mean shift > 0.50, critical if > 1.00.",
    },
    "distribution_std_shift": {
        "warning": 0.50,
        "critical": 1.00,
        "unit": "ratio_delta",
        "description": "Warning if standard deviation change ratio > 0.50, critical if > 1.00.",
    },
    "quantile_shift": {
        "warning": 0.60,
        "critical": 1.20,
        "unit": "quantile_delta",
        "description": "Warning if quantile composite shift > 0.60, critical if > 1.20.",
    },
    "missingness_shift": {
        "warning": 0.15,
        "critical": 0.30,
        "unit": "ratio_delta",
        "description": "Warning if missingness ratio increases by > 15%, critical if > 30%.",
    },
    "min_sample_size": {
        "warning": 30.0,
        "critical": 15.0,
        "unit": "count",
        "description": "Manual review required if observation count < 30 bars in comparison window.",
    },
}


def get_default_drift_thresholds() -> Dict[str, Dict[str, Any]]:
    """Return default drift threshold definitions."""
    return dict(DEFAULT_DRIFT_THRESHOLDS)


def build_feature_drift_threshold_registry(
    profile: FeatureQualityDriftProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary of drift threshold registry."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    records = []
    for metric_id, t in DEFAULT_DRIFT_THRESHOLDS.items():
        records.append({
            "threshold_id": f"thresh_drift_{metric_id}",
            "metric_id": metric_id,
            "warning_threshold": t["warning"],
            "critical_threshold": t["critical"],
            "unit": t["unit"],
            "description": t["description"],
            "auto_drop_allowed": False,
            "auto_fix_allowed": False,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_thresholds": len(records),
        "current_phase": active_profile.current_phase,
        "auto_drop_allowed": False,
        "auto_fix_allowed": False,
        "non_signal": True,
    }
    return df, summary
