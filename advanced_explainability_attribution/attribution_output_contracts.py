# -*- coding: utf-8 -*-
"""Phase 143: Attribution Output Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_attribution_output_contract_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of attribution output contracts."""
    prof = profile or get_explainability_profile()

    outputs = [
        ("output_global_importance_schema", "schema_global_importance_report", "Global importance ranking schema placeholder"),
        ("output_local_attribution_schema", "schema_local_attribution_report", "Local feature attribution schema placeholder"),
        ("output_shap_values_schema", "schema_shap_values_contract", "SHAP values contract schema placeholder"),
        ("output_lime_explanations_schema", "schema_lime_explanations_contract", "LIME explanations contract schema placeholder"),
        ("output_pdp_ice_curves_schema", "schema_pdp_ice_curves_contract", "PDP and ICE curves contract schema placeholder"),
        ("output_surrogate_model_schema", "schema_surrogate_model_contract", "Surrogate model contract schema placeholder"),
        ("output_counterfactual_schema", "schema_counterfactual_contract", "Counterfactual explanation schema placeholder"),
        ("output_reason_codes_schema", "schema_reason_codes_contract", "Attribution reason codes contract schema placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for oname, sref, desc in outputs:
        rows.append({
            "output_name": oname,
            "output_schema_ref": sref,
            "description": desc,
            "contains_signal": False,
            "contains_real_attribution": False,
            "contains_prediction": False,
            "is_contract_only": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_attribution_output_contracts(df)
    return df, summary


def summarize_attribution_output_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize attribution output contracts."""
    return {
        "total_output_contracts": len(df),
        "all_no_signal": bool((~df["contains_signal"]).all()) if not df.empty else True,
        "all_no_real_attribution": bool((~df["contains_real_attribution"]).all()) if not df.empty else True,
        "all_no_prediction": bool((~df["contains_prediction"]).all()) if not df.empty else True,
        "all_contract_only": bool(df["is_contract_only"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
