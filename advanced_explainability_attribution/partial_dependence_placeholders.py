# -*- coding: utf-8 -*-
"""Phase 143: Partial Dependence Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_partial_dependence_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of partial dependence (PDP) placeholders."""
    prof = profile or get_explainability_profile()

    pdp_data = [
        ("pdp_placeholder_1d_grid", "1d_partial_dependence", "top_continuous_features", "marginal_prediction_curve_placeholder"),
        ("pdp_placeholder_2d_interaction", "2d_partial_dependence", "top_feature_pairs", "interaction_contour_surface_placeholder"),
        ("pdp_placeholder_percentile_grid", "percentile_sampled_grid", "skewed_distribution_features", "quantile_grid_evaluation_placeholder"),
        ("pdp_placeholder_regime_overlay", "regime_stratified_pdp", "macro_regime_features", "regime_specific_marginal_effect_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for pid, gtype, target, desc in pdp_data:
        rows.append({
            "placeholder_id": pid,
            "grid_type": gtype,
            "target_features": target,
            "description": desc,
            "is_placeholder_only": True,
            "pdp_executed": False,
            "calculation_allowed": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_partial_dependence_placeholders(df)
    return df, summary


def summarize_partial_dependence_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize PDP placeholders."""
    return {
        "total_pdp_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_pdp_executed_false": bool((~df["pdp_executed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
