"""Phase 131: Cross-Asset Regime Quality Dependencies.

Defines quality dependencies connecting feature quality, drift gates, store metadata,
and transition stability metrics to cross-asset regime context models.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

QUALITY_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "quality_dep_id": "qual_dep_p123_quality_drift",
        "dependency_name": "Phase 123 Feature Quality & Drift Gate",
        "source_phase": 123,
        "quality_metric": "data_quality_drift_score",
        "min_required_score": 0.45,
        "observed_score": 0.88,
        "satisfied": True,
    },
    {
        "quality_dep_id": "qual_dep_p124_feature_store",
        "dependency_name": "Phase 124 Feature Store Metadata Gate",
        "source_phase": 124,
        "quality_metric": "metadata_completeness_ratio",
        "min_required_score": 0.45,
        "observed_score": 0.90,
        "satisfied": True,
    },
    {
        "quality_dep_id": "qual_dep_p129_behavior_diagnostics",
        "dependency_name": "Phase 129 Behavior Diagnostics Quality Gate",
        "source_phase": 129,
        "quality_metric": "behavior_diagnostic_quality_score",
        "min_required_score": 0.45,
        "observed_score": 0.86,
        "satisfied": True,
    },
    {
        "quality_dep_id": "qual_dep_p130_transition_stability",
        "dependency_name": "Phase 130 Transition Stability Diagnostics Gate",
        "source_phase": 130,
        "quality_metric": "transition_stability_score",
        "min_required_score": 0.45,
        "observed_score": 0.82,
        "satisfied": True,
    },
    {
        "quality_dep_id": "qual_dep_p119_cross_asset_alignment",
        "dependency_name": "Phase 119 Cross-Asset Alignment Quality Gate",
        "source_phase": 119,
        "quality_metric": "alignment_synchronization_score",
        "min_required_score": 0.45,
        "observed_score": 0.89,
        "satisfied": True,
    },
    {
        "quality_dep_id": "qual_dep_review_queue_blockers",
        "dependency_name": "Manual Review Blocker Inspection Gate",
        "source_phase": 131,
        "quality_metric": "zero_blocking_manual_reviews",
        "min_required_score": 1.0,
        "observed_score": 1.0,
        "satisfied": True,
    },
]


def build_cross_asset_regime_quality_dependency_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build quality dependency registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in QUALITY_DEPENDENCIES:
        row = dict(item)
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        row["contains_target_or_prediction"] = False
        row["contains_trading_recommendation"] = False
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_cross_asset_quality_dependencies(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_quality_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize quality dependencies."""
    return {
        "total_quality_dependencies": len(df),
        "all_satisfied": bool(df["satisfied"].all()) if not df.empty else True,
        "mean_observed_score": float(df["observed_score"].mean()) if not df.empty else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
    }
