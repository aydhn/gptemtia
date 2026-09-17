# -*- coding: utf-8 -*-
"""Phase 143: Surrogate Model Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_surrogate_model_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of surrogate model placeholders."""
    prof = profile or get_explainability_profile()

    surrogate_data = [
        ("surrogate_placeholder_shallow_tree", "decision_tree_regressor", "ensemble_predictions", "shallow_tree_depth3_surrogate_placeholder"),
        ("surrogate_placeholder_linear_gam", "generalized_additive_model", "candidate_complex_models", "interpretable_gam_surrogate_placeholder"),
        ("surrogate_placeholder_rule_fit", "rule_fit_generator", "tree_ensemble_models", "extracted_if_then_rules_placeholder"),
        ("surrogate_placeholder_fidelity_eval", "r2_fidelity_metric", "surrogate_vs_blackbox", "surrogate_fidelity_score_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for sid, mtype, target, desc in surrogate_data:
        rows.append({
            "placeholder_id": sid,
            "surrogate_type": mtype,
            "target_model": target,
            "description": desc,
            "is_placeholder_only": True,
            "surrogate_model_executed": False,
            "calculation_allowed": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_surrogate_model_placeholders(df)
    return df, summary


def summarize_surrogate_model_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize surrogate model placeholders."""
    return {
        "total_surrogate_model_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_surrogate_executed_false": bool((~df["surrogate_model_executed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
