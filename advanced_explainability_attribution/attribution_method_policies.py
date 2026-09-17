# -*- coding: utf-8 -*-
"""Phase 143: Attribution Method Policies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_attribution_method_policy_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of attribution method policies."""
    prof = profile or get_explainability_profile()

    methods = [
        ("tree_shap", "tree_shap_policy", "SHAP tree explainer policy requiring non-execution in dry-run"),
        ("kernel_shap", "kernel_shap_policy", "Kernel SHAP sampling policy requiring non-execution in dry-run"),
        ("lime_tabular", "lime_tabular_policy", "LIME tabular surrogate policy requiring non-execution in dry-run"),
        ("permutation_importance", "permutation_importance_policy", "Permutation feature importance policy requiring non-execution"),
        ("partial_dependence", "partial_dependence_policy", "Partial dependence profile policy requiring non-execution"),
        ("ice_individual_conditional", "ice_policy", "Individual conditional expectation policy requiring non-execution"),
        ("surrogate_interpretable_models", "surrogate_model_policy", "Interpretable surrogate model policy requiring non-execution"),
        ("counterfactual_recourse", "counterfactual_policy", "Counterfactual what-if recourse policy requiring non-execution"),
    ]

    rows: List[Dict[str, Any]] = []
    for method, pol_name, desc in methods:
        rows.append({
            "method_name": method,
            "policy_name": pol_name,
            "description": desc,
            "execution_blocked": True,
            "policy_status": "execution_blocked_by_policy",
            "non_signal": True,
            "manual_review_required": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_attribution_method_policies(df)
    return df, summary


def summarize_attribution_method_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize attribution method policies."""
    return {
        "total_method_policies": len(df),
        "all_execution_blocked": bool(df["execution_blocked"].all()) if not df.empty else True,
        "all_blocked_status": bool((df["policy_status"] == "execution_blocked_by_policy").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
