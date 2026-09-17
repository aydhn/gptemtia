# -*- coding: utf-8 -*-
"""Phase 143: SHAP Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_shap_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of SHAP placeholders."""
    prof = profile or get_explainability_profile()

    shap_data = [
        ("shap_placeholder_treeshap", "tree_explainer", "lightgbm_xgboost_candidates", "tree_path_shap_values_placeholder"),
        ("shap_placeholder_kernelshap", "kernel_explainer", "baseline_linear_models", "sample_kernel_shap_values_placeholder"),
        ("shap_placeholder_exactshap", "exact_explainer", "small_feature_subsets", "combinatorial_shap_values_placeholder"),
        ("shap_placeholder_interactions", "interaction_explainer", "tree_ensemble_pairs", "pairwise_shap_interaction_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for sid, explainer, target, desc in shap_data:
        rows.append({
            "placeholder_id": sid,
            "explainer_type": explainer,
            "target_model_set": target,
            "description": desc,
            "is_placeholder_only": True,
            "shap_executed": False,
            "calculation_allowed": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_shap_placeholders(df)
    return df, summary


def summarize_shap_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize SHAP placeholders."""
    return {
        "total_shap_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_shap_executed_false": bool((~df["shap_executed"]).all()) if not df.empty else True,
        "all_execution_blocked": bool(df["execution_blocked_by_policy"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
