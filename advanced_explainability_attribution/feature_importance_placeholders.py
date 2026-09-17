# -*- coding: utf-8 -*-
"""Phase 143: Feature Importance Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_feature_importance_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of feature importance placeholders."""
    prof = profile or get_explainability_profile()

    placeholders_data = [
        ("feat_imp_placeholder_trees", "tree_split_gain_placeholder", "candidate_lightgbm_xgboost", "mean_gain_placeholder"),
        ("feat_imp_placeholder_linear", "linear_coefficient_magnitude_placeholder", "candidate_logistic_ridge", "abs_coefficient_placeholder"),
        ("feat_imp_placeholder_permutation", "permutation_drop_placeholder", "baseline_all_models", "degradation_placeholder"),
        ("feat_imp_placeholder_ensemble", "ensemble_weighted_importance_placeholder", "ensemble_voting_blending", "weighted_rank_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for pid, ptype, target, metric in placeholders_data:
        rows.append({
            "placeholder_id": pid,
            "placeholder_type": ptype,
            "target_model": target,
            "metric_type": metric,
            "is_placeholder_only": True,
            "calculation_executed": False,
            "calculation_allowed": False,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_feature_importance_placeholders(df)
    return df, summary


def summarize_feature_importance_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize feature importance placeholders."""
    return {
        "total_feature_importance_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_calculation_executed_false": bool((~df["calculation_executed"]).all()) if not df.empty else True,
        "all_feature_importance_calculated_false": bool((~df["calculation_executed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }

