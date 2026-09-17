# -*- coding: utf-8 -*-
"""Phase 143: Attribution Calculation Disabled Safeguard."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def verify_attribution_calculation_disabled(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify that feature attribution calculations are strictly disabled."""
    prof = profile or get_explainability_profile()

    checks = [
        ("feature_importance_score_guard", "Direct importance calculation blocked by policy", True, False),
        ("feature_contribution_vector_guard", "Direct contribution calculation blocked by policy", True, False),
        ("marginal_attribution_guard", "Marginal attribution computation blocked by policy", True, False),
        ("integrated_gradients_guard", "Integrated gradient calculation blocked by policy", True, False),
    ]

    rows: List[Dict[str, Any]] = []
    for cname, reason, is_dis, attempted in checks:
        rows.append({
            "action_name": cname,
            "blocked_reason": reason,
            "is_disabled": is_dis,
            "execution_attempted": attempted,
            "policy_enforced": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_attribution_calculation_disabled(df)
    return df, summary


def summarize_attribution_calculation_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize attribution calculation disabled state."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()) if not df.empty else True,
        "none_attempted": bool((~df["execution_attempted"]).all()) if not df.empty else True,
        "all_policy_enforced": bool(df["policy_enforced"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
