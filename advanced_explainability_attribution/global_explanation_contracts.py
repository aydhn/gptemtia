# -*- coding: utf-8 -*-
"""Phase 143: Global Explanation Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_global_explanation_contract_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of global explanation contracts."""
    prof = profile or get_explainability_profile()

    global_contracts = [
        ("global_feature_importance_contract", "overall_feature_ranking", "dataset_train_validation_v1", "rank_stability_metric_v1"),
        ("global_treeshap_contract", "tree_ensemble_mean_abs_shap", "candidate_tree_models_v1", "attribution_stability_v1"),
        ("global_permutation_contract", "loss_degradation_permutation", "baseline_all_models_v1", "consistency_metric_v1"),
        ("global_surrogate_contract", "interpretable_decision_tree_surrogate", "ensemble_all_v1", "fidelity_metric_v1"),
        ("global_pdp_contract", "marginal_effect_pdp_grid", "featurestore_core_factors_v1", "coverage_metric_v1"),
        ("global_regime_interaction_contract", "regime_conditioned_global_importance", "regime_matrix_v1", "regime_stability_v1"),
    ]

    rows: List[Dict[str, Any]] = []
    for name, method, target_ref, metric_ref in global_contracts:
        rows.append({
            "contract_name": name,
            "method": method,
            "target_model_set_ref": target_ref,
            "evaluation_metric_ref": metric_ref,
            "scope": "global",
            "calculation_allowed": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "manual_review_required": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_global_explanation_contracts(df)
    return df, summary


def summarize_global_explanation_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize global explanation contracts statistics."""
    total_contracts = len(df)
    return {
        "total_global_contracts": total_contracts,
        "all_calculation_blocked": bool((~df["calculation_allowed"]).all()) if not df.empty else True,
        "all_zero_calculation": bool((~df["calculation_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }

