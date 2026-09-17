# -*- coding: utf-8 -*-
"""Phase 143: Feature Contribution Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_feature_contribution_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of feature contribution placeholders."""
    prof = profile or get_explainability_profile()

    placeholders_data = [
        ("feat_contrib_instance_additive", "additive_feature_contribution_placeholder", "sample_instance_core", "additive_placeholder"),
        ("feat_contrib_interaction_pairwise", "second_order_interaction_placeholder", "sample_instance_pairwise", "interaction_placeholder"),
        ("feat_contrib_group_macro", "macro_group_aggregate_contribution_placeholder", "macro_feature_group", "group_aggregate_placeholder"),
        ("feat_contrib_group_technical", "technical_group_aggregate_contribution_placeholder", "technical_feature_group", "group_aggregate_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for pid, ptype, target, metric in placeholders_data:
        rows.append({
            "placeholder_id": pid,
            "placeholder_type": ptype,
            "target_entity": target,
            "metric_type": metric,
            "is_placeholder_only": True,
            "calculation_executed": False,
            "calculation_allowed": False,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_feature_contribution_placeholders(df)
    return df, summary


def summarize_feature_contribution_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize feature contribution placeholders."""
    return {
        "total_feature_contribution_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_calculation_executed_false": bool((~df["calculation_executed"]).all()) if not df.empty else True,
        "all_feature_contribution_calculated_false": bool((~df["calculation_executed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }

