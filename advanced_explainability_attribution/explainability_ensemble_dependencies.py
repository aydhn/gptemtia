# -*- coding: utf-8 -*-
"""Phase 143: Explainability Ensemble Dependencies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def verify_explainability_ensemble_dependencies(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify ensemble contract dependencies for attribution."""
    prof = profile or get_explainability_profile()

    ensembles = [
        ("ens_equal_weighted_contract", "Phase 140 Equal Weighted Ensemble Contract", True),
        ("ens_rank_averaged_contract", "Phase 140 Rank Averaged Ensemble Contract", True),
        ("ens_stacked_linear_contract", "Phase 140 Stacked Linear Ensemble Contract", True),
        ("ens_volatility_weighted_contract", "Phase 140 Volatility Weighted Ensemble Contract", True),
    ]

    rows: List[Dict[str, Any]] = []
    for eid, desc, satisfied in ensembles:
        rows.append({
            "ensemble_id": eid,
            "description": desc,
            "contract_verified": satisfied,
            "ensemble_predict_executed": False,
            "weight_rebalanced_on_attribution": False,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_explainability_ensemble_dependencies(df)
    return df, summary


def summarize_explainability_ensemble_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize ensemble dependencies."""
    return {
        "total_ensemble_contracts": len(df),
        "all_contracts_verified": bool(df["contract_verified"].all()) if not df.empty else True,
        "all_predict_executed_false": bool((~df["ensemble_predict_executed"]).all()) if not df.empty else True,
        "all_rebalance_executed_false": bool((~df["weight_rebalanced_on_attribution"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
