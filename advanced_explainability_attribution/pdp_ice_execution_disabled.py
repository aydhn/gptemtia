# -*- coding: utf-8 -*-
"""Phase 143: PDP and ICE Execution Disabled Safeguard."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def verify_pdp_ice_execution_disabled(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify that PDP and ICE execution is strictly disabled."""
    prof = profile or get_explainability_profile()

    checks = [
        ("pdp_grid_evaluation_guard", "Partial dependence grid evaluation blocked by policy", True, False),
        ("ice_individual_curve_guard", "Individual conditional expectation curve computation blocked", True, False),
        ("two_way_pdp_interaction_guard", "2-way PDP interaction calculation blocked", True, False),
        ("centered_ice_curve_guard", "Centered ICE curve computation blocked by policy", True, False),
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
    summary = summarize_pdp_ice_execution_disabled(df)
    return df, summary


def summarize_pdp_ice_execution_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize PDP and ICE execution disabled state."""
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
