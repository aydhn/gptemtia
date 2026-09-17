# -*- coding: utf-8 -*-
"""Phase 143: Reason Code Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_reason_code_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of reason code placeholders."""
    prof = profile or get_explainability_profile()

    rc_data = [
        ("rc_placeholder_top_positive_features", "top_k_positive_drivers", "local_prediction_context", "top_positive_attribution_reason_codes_placeholder"),
        ("rc_placeholder_top_negative_features", "top_k_negative_drivers", "local_prediction_context", "top_negative_attribution_reason_codes_placeholder"),
        ("rc_placeholder_regime_context_codes", "regime_specific_reason_codes", "macro_regime_features", "regime_contextual_reason_codes_placeholder"),
        ("rc_placeholder_uncertainty_caveat_codes", "uncertainty_flag_reason_codes", "calibration_uncertainty", "uncertainty_and_dispersion_caveats_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for rid, rtype, target, desc in rc_data:
        rows.append({
            "placeholder_id": rid,
            "reason_code_type": rtype,
            "target_context": target,
            "description": desc,
            "is_placeholder_only": True,
            "reason_codes_generated": False,
            "calculation_allowed": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_reason_code_placeholders(df)
    return df, summary


def summarize_reason_code_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize reason code placeholders."""
    return {
        "total_reason_code_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_reason_codes_generated_false": bool((~df["reason_codes_generated"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
