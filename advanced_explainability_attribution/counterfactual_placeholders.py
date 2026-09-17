# -*- coding: utf-8 -*-
"""Phase 143: Counterfactual Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_counterfactual_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of counterfactual explanation placeholders."""
    prof = profile or get_explainability_profile()

    cf_data = [
        ("cf_placeholder_minimum_perturbation", "min_distance_counterfactual", "candidate_models", "minimum_feature_perturbation_placeholder"),
        ("cf_placeholder_sparsity_constrained", "sparse_counterfactual", "ensemble_predictions", "sparsity_constrained_what_if_placeholder"),
        ("cf_placeholder_actionable_recourse", "actionable_recourse", "regime_dependent_features", "actionable_feature_recourse_placeholder"),
        ("cf_placeholder_plausibility_check", "mahalanobis_plausibility", "historical_distributions", "data_manifold_plausibility_metric_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for cid, ctype, target, desc in cf_data:
        rows.append({
            "placeholder_id": cid,
            "counterfactual_type": ctype,
            "target_model": target,
            "description": desc,
            "is_placeholder_only": True,
            "counterfactual_generated": False,
            "calculation_allowed": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_counterfactual_placeholders(df)
    return df, summary


def summarize_counterfactual_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize counterfactual placeholders."""
    return {
        "total_counterfactual_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_counterfactual_generated_false": bool((~df["counterfactual_generated"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
