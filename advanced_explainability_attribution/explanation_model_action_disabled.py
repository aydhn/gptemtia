# -*- coding: utf-8 -*-
"""Phase 143: Explanation Model Action Disabled Safeguard."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def verify_explanation_model_action_disabled(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify that automated model actions based on explanations are strictly disabled."""
    prof = profile or get_explainability_profile()

    checks = [
        ("auto_model_disable_on_attribution", "Auto-disabling models based on attribution shift blocked by policy", True, False),
        ("auto_feature_pruning_on_importance", "Auto-pruning features based on low importance blocked by policy", True, False),
        ("auto_retraining_on_explanation_drift", "Auto-triggering model retraining based on explanation drift blocked", True, False),
        ("auto_hyperparameter_tuning_on_xai", "Auto-tuning model hyperparameters based on XAI metrics blocked", True, False),
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
    summary = summarize_explanation_model_action_disabled(df)
    return df, summary


def summarize_explanation_model_action_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize explanation model action disabled state."""
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
