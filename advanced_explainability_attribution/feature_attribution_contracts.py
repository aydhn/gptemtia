# -*- coding: utf-8 -*-
"""Phase 143: Feature Attribution Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_feature_attribution_contract_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of feature attribution contracts."""
    prof = profile or get_explainability_profile()

    contracts_data = [
        ("global_feature_attribution_contract", "shap_tree_kernel_placeholder", "global", "featurestore_core_factors_v1"),
        ("local_feature_attribution_contract", "lime_tabular_placeholder", "local", "featurestore_sample_instances_v1"),
        ("tree_based_attribution_contract", "treeshap_placeholder", "global_local", "featurestore_tree_factors_v1"),
        ("linear_kernel_attribution_contract", "kernelshap_placeholder", "global_local", "featurestore_linear_factors_v1"),
        ("permutation_attribution_contract", "permutation_importance_placeholder", "global", "featurestore_validation_split_v1"),
        ("pdp_ice_attribution_contract", "pdp_ice_placeholder", "feature_subspace", "featurestore_selected_pairs_v1"),
        ("surrogate_attribution_contract", "surrogate_decision_tree_placeholder", "global_surrogate", "featurestore_surrogate_v1"),
        ("counterfactual_attribution_contract", "counterfactual_distance_placeholder", "local_counterfactual", "featurestore_instance_v1"),
    ]

    rows: List[Dict[str, Any]] = []
    for name, method, scope, feat_ref in contracts_data:
        rows.append({
            "contract_name": name,
            "method_name": method,
            "attribution_scope": scope,
            "target_feature_set_ref": feat_ref,
            "attribution_calculation_allowed": False,
            "shap_execution_allowed": False,
            "lime_execution_allowed": False,
            "permutation_importance_allowed": False,
            "non_signal_required": True,
            "manual_review_required": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_feature_attribution_contracts(df)
    return df, summary


def validate_feature_attribution_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single feature attribution contract dictionary."""
    is_valid = True
    issues: List[str] = []

    if not contract.get("contract_name"):
        is_valid = False
        issues.append("contract_name is required")

    if contract.get("attribution_calculation_allowed", True):
        is_valid = False
        issues.append("attribution_calculation_allowed must be False")

    if contract.get("shap_execution_allowed", True):
        is_valid = False
        issues.append("shap_execution_allowed must be False")

    if contract.get("lime_execution_allowed", True):
        is_valid = False
        issues.append("lime_execution_allowed must be False")

    if contract.get("permutation_importance_allowed", True):
        is_valid = False
        issues.append("permutation_importance_allowed must be False")

    if not contract.get("non_signal_required", False):
        is_valid = False
        issues.append("non_signal_required must be True")

    if contract.get("production_ready", False) or contract.get("broker_ready", False):
        is_valid = False
        issues.append("production_ready and broker_ready must be False")

    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": is_valid,
        "issues": issues,
        "non_signal": True,
    }


def summarize_feature_attribution_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize feature attribution contracts statistics."""
    total_contracts = len(df)
    all_zero_calc = bool((~df["attribution_calculation_allowed"]).all()) if not df.empty else True
    all_zero_shap = bool((~df["shap_execution_allowed"]).all()) if not df.empty else True
    all_zero_lime = bool((~df["lime_execution_allowed"]).all()) if not df.empty else True

    return {
        "total_contracts": total_contracts,
        "total_attribution_contracts": total_contracts,
        "all_zero_calculation": all_zero_calc,
        "all_zero_shap": all_zero_shap,
        "all_zero_lime": all_zero_lime,
        "all_non_signal": bool(df["non_signal_required"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }


# Convenience alias
build_feature_attribution_contracts = build_feature_attribution_contract_registry
