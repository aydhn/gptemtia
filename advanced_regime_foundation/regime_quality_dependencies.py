"""Phase 126: Regime Quality Dependencies Registry.

Registers quality, drift, and diagnostic prerequisites required from Phase 123 for regime datasets.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

QUALITY_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "quality_id": "qual_dep_01_missingness",
        "quality_metric": "missingness_score",
        "threshold_condition": "missingness_ratio <= 0.05",
        "scope": "All regime input features",
        "description": "Requires maximum allowable missing data ratio under 5% across feature lookback window",
        "source_phase": 123,
        "non_signal": True,
        "blocking": True,
    },
    {
        "quality_id": "qual_dep_02_drift",
        "quality_metric": "drift_score",
        "threshold_condition": "drift_magnitude <= 0.25",
        "scope": "All regime input features and factors",
        "description": "Requires population stability index (PSI) / Kolmogorov-Smirnov drift score below alert threshold",
        "source_phase": 123,
        "non_signal": True,
        "blocking": True,
    },
    {
        "quality_id": "qual_dep_03_staleness",
        "quality_metric": "staleness_diagnostics",
        "threshold_condition": "max_stale_bars <= 3",
        "scope": "High-frequency and quote features",
        "description": "Flags features repeating identical values across multiple consecutive time periods",
        "source_phase": 123,
        "non_signal": True,
        "blocking": True,
    },
    {
        "quality_id": "qual_dep_04_availability",
        "quality_metric": "factor_availability",
        "threshold_condition": "factor_availability_ratio == 1.0",
        "scope": "Registered factor families in Phase 122",
        "description": "All referenced factor columns must be fully calculated and present in the input feature store",
        "source_phase": 122,
        "non_signal": True,
        "blocking": True,
    },
    {
        "quality_id": "qual_dep_05_manual_review",
        "quality_metric": "manual_review_blockers",
        "threshold_condition": "active_blocking_reviews == 0",
        "scope": "Feature Store manual review blocker registry",
        "description": "No unresolved blocking manual review items may exist for input features before regime usage",
        "source_phase": 124,
        "non_signal": True,
        "blocking": True,
    },
    {
        "quality_id": "qual_dep_06_namespace_quality",
        "quality_metric": "namespace_quality",
        "threshold_condition": "conforms_to_canonical_snake_case == True",
        "scope": "Feature and regime naming",
        "description": "Enforces strict canonical naming schema without unapproved abbreviations or forbidden keywords",
        "source_phase": 124,
        "non_signal": True,
        "blocking": True,
    },
    {
        "quality_id": "qual_dep_07_data_availability",
        "quality_metric": "data_availability",
        "threshold_condition": "feed_status == ACTIVE",
        "scope": "Data Lake underlying raw partitions",
        "description": "Ensures raw source partitions are verified and intact without source file corruption",
        "source_phase": 115,
        "non_signal": True,
        "blocking": True,
    },
]


def build_regime_quality_dependency_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime quality dependency registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(QUALITY_DEPENDENCIES)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_metrics": len(df),
        "all_blocking": bool((df["blocking"] == True).all()),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_regime_quality_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime quality dependencies DataFrame."""
    return {
        "total_metrics": len(df),
        "quality_metrics": list(df["quality_metric"].unique()) if "quality_metric" in df.columns else [],
        "all_blocking": True,
        "non_signal": True,
    }
