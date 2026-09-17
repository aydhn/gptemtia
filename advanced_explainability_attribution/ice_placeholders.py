# -*- coding: utf-8 -*-
"""Phase 143: Individual Conditional Expectation (ICE) Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_ice_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of ICE placeholders."""
    prof = profile or get_explainability_profile()

    ice_data = [
        ("ice_placeholder_individual_curves", "standard_ice_curve", "instance_subset_core", "per_instance_conditional_curve_placeholder"),
        ("ice_placeholder_centered", "centered_ice_curve", "instance_subset_core", "baseline_anchored_ice_curve_placeholder"),
        ("ice_placeholder_derivative", "derivative_ice", "instance_subset_continuous", "rate_of_change_conditional_placeholder"),
        ("ice_placeholder_heterogeneity", "ice_variance_dispersion", "instance_subset_all", "heterogeneity_spread_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for pid, ctype, target, desc in ice_data:
        rows.append({
            "placeholder_id": pid,
            "curve_type": ctype,
            "target_instances": target,
            "description": desc,
            "is_placeholder_only": True,
            "ice_executed": False,
            "calculation_allowed": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_ice_placeholders(df)
    return df, summary


def summarize_ice_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize ICE placeholders."""
    return {
        "total_ice_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_ice_executed_false": bool((~df["ice_executed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
