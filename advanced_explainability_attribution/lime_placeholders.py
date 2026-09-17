# -*- coding: utf-8 -*-
"""Phase 143: LIME Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_lime_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of LIME placeholders."""
    prof = profile or get_explainability_profile()

    lime_data = [
        ("lime_placeholder_tabular", "lime_tabular_explainer", "candidate_models_all", "local_linear_surrogate_coefficients_placeholder"),
        ("lime_placeholder_kernel_width", "kernel_width_policy", "perturbation_neighborhood", "neighborhood_distance_bandwidth_placeholder"),
        ("lime_placeholder_sample_perturbation", "perturbation_sampler", "continuous_features", "normal_perturbed_samples_placeholder"),
        ("lime_placeholder_feature_selection", "ridge_selection_policy", "top_k_features", "sparse_explanation_features_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for lid, etype, target, desc in lime_data:
        rows.append({
            "placeholder_id": lid,
            "explainer_type": etype,
            "target_entity": target,
            "description": desc,
            "is_placeholder_only": True,
            "lime_executed": False,
            "calculation_allowed": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_lime_placeholders(df)
    return df, summary


def summarize_lime_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize LIME placeholders."""
    return {
        "total_lime_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_lime_executed_false": bool((~df["lime_executed"]).all()) if not df.empty else True,
        "all_execution_blocked": bool(df["execution_blocked_by_policy"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
