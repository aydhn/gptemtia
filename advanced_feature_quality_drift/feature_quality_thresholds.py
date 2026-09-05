"""Phase 123 Feature Quality Threshold Registry.

Defines threshold boundaries for feature quality diagnostics, enforcing manual review
instead of automated deletion or destructive manipulation.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)

DEFAULT_QUALITY_THRESHOLDS = {
    "missingness_ratio": {
        "warning": 0.25,
        "critical": 0.50,
        "unit": "ratio",
        "description": "Warning if missingness > 25%, critical if > 50%.",
    },
    "infinite_value_ratio": {
        "warning": 0.0001,
        "critical": 0.0001,
        "unit": "ratio",
        "description": "Critical if any infinite values are present (> 0).",
    },
    "all_nan_flag": {
        "warning": 1.0,
        "critical": 1.0,
        "unit": "flag",
        "description": "Critical if feature column contains all NaN values.",
    },
    "zero_variance_flag": {
        "warning": 1.0,
        "critical": 1.0,
        "unit": "flag",
        "description": "Warning if column variance is zero (constant feature).",
    },
    "duplicate_value_ratio": {
        "warning": 0.90,
        "critical": 0.99,
        "unit": "ratio",
        "description": "Warning if single value constitutes > 90% of rows.",
    },
    "staleness_max_unchanged_bars": {
        "warning": 30.0,
        "critical": 60.0,
        "unit": "count",
        "description": "Warning if feature remains unchanged for > 30 consecutive bars.",
    },
}


def get_default_quality_thresholds() -> Dict[str, Dict[str, Any]]:
    """Return default quality threshold definitions."""
    return dict(DEFAULT_QUALITY_THRESHOLDS)


def build_feature_quality_threshold_registry(
    profile: FeatureQualityDriftProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary of quality threshold registry."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    records = []
    for metric_id, t in DEFAULT_QUALITY_THRESHOLDS.items():
        records.append({
            "threshold_id": f"thresh_quality_{metric_id}",
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
