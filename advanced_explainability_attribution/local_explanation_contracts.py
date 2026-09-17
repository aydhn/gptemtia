# -*- coding: utf-8 -*-
"""Phase 143: Local Explanation Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_local_explanation_contract_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of local explanation contracts."""
    prof = profile or get_explainability_profile()

    local_contracts = [
        ("local_shap_waterfall_contract", "instance_treeshap_waterfall", "candidate_sample_instances_v1", "local_stability_v1"),
        ("local_lime_tabular_contract", "instance_sparse_linear_surrogate", "candidate_sample_instances_v1", "local_fidelity_v1"),
        ("local_ice_contract", "instance_conditional_expectation", "candidate_sample_instances_v1", "local_coverage_v1"),
        ("local_counterfactual_contract", "instance_minimal_perturbation", "candidate_sample_instances_v1", "proximity_metric_v1"),
        ("local_reason_code_contract", "instance_top_contributing_factors", "candidate_sample_instances_v1", "interpretability_score_v1"),
        ("local_drift_instance_contract", "instance_drift_attribution_alignment", "drift_window_instances_v1", "drift_linkage_score_v1"),
    ]

    rows: List[Dict[str, Any]] = []
    for name, method, target_ref, metric_ref in local_contracts:
        rows.append({
            "contract_name": name,
            "method": method,
            "target_instance_set_ref": target_ref,
            "evaluation_metric_ref": metric_ref,
            "scope": "local",
            "calculation_allowed": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "manual_review_required": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_local_explanation_contracts(df)
    return df, summary


def summarize_local_explanation_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize local explanation contracts statistics."""
    total_contracts = len(df)
    return {
        "total_local_contracts": total_contracts,
        "all_calculation_blocked": bool((~df["calculation_allowed"]).all()) if not df.empty else True,
        "all_zero_calculation": bool((~df["calculation_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }

