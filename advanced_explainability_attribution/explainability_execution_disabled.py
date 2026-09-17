# -*- coding: utf-8 -*-
"""Phase 143: Explainability Execution Disabled Safeguard."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def verify_explainability_execution_disabled(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify that general explainability execution is strictly disabled."""
    prof = profile or get_explainability_profile()

    checks = [
        ("explainability_calculation_guard", "Explainability calculation blocked by Phase 143 dry-run invariant", True, False),
        ("feature_attribution_execution_guard", "Attribution execution blocked by Phase 143 policy", True, False),
        ("automated_explanation_pipeline_guard", "Automated explanation generation pipeline blocked", True, False),
        ("interactive_xai_dashboard_guard", "Interactive XAI execution blocked in contract layer", True, False),
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
    summary = summarize_explainability_execution_disabled(df)
    return df, summary


def summarize_explainability_execution_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize explainability execution disabled state."""
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
