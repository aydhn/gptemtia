# -*- coding: utf-8 -*-
"""Phase 143: Attribution Scope Policies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_attribution_scope_policy_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of attribution scope policies."""
    prof = profile or get_explainability_profile()

    scopes = [
        ("global_feature_importance", "global", "dataset_level_overall_importance", True, True),
        ("local_prediction_explanation", "local", "individual_sample_attribution", True, True),
        ("cohort_regime_explanation", "cohort", "macro_regime_subgroup_attribution", True, True),
        ("temporal_drift_explanation", "temporal", "time_sliced_attribution_drift", True, True),
    ]

    rows: List[Dict[str, Any]] = []
    for s_name, s_level, desc, req_review, non_sig in scopes:
        rows.append({
            "scope_name": s_name,
            "scope_level": s_level,
            "description": desc,
            "execution_blocked": True,
            "manual_review_required": req_review,
            "non_signal": non_sig,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_attribution_scope_policies(df)
    return df, summary


def summarize_attribution_scope_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize attribution scope policies."""
    return {
        "total_scope_policies": len(df),
        "all_execution_blocked": bool(df["execution_blocked"].all()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
