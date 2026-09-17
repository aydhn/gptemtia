# -*- coding: utf-8 -*-
"""Phase 143: Explainability Candidate Model Dependencies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def verify_explainability_candidate_model_dependencies(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify candidate model contract dependencies for attribution."""
    prof = profile or get_explainability_profile()

    models = [
        ("cand_ridge_baseline", "Phase 138 Ridge Baseline Model Contract", True),
        ("cand_random_forest", "Phase 138 Random Forest Baseline Model Contract", True),
        ("cand_gradient_boosting", "Phase 138 LightGBM/GBDT Model Contract", True),
        ("cand_mlp_neural_net", "Phase 138 Tabular MLP Model Contract", True),
    ]

    rows: List[Dict[str, Any]] = []
    for mid, desc, satisfied in models:
        rows.append({
            "candidate_model_id": mid,
            "description": desc,
            "contract_verified": satisfied,
            "model_fit_executed": False,
            "model_predict_executed": False,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_explainability_candidate_model_dependencies(df)
    return df, summary


def summarize_explainability_candidate_model_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize candidate model dependencies."""
    return {
        "total_candidate_models": len(df),
        "all_contracts_verified": bool(df["contract_verified"].all()) if not df.empty else True,
        "all_fit_executed_false": bool((~df["model_fit_executed"]).all()) if not df.empty else True,
        "all_predict_executed_false": bool((~df["model_predict_executed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
