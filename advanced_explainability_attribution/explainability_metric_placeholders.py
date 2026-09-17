# -*- coding: utf-8 -*-
"""Phase 143: Explainability Metric Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_explainability_metric_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of explainability metric placeholders."""
    prof = profile or get_explainability_profile()

    metrics = [
        ("metric_faithfulness_correlation", "faithfulness", "correlation_between_attribution_and_model_output_change_placeholder"),
        ("metric_monotonicity", "monotonicity", "monotonicity_of_increasing_feature_attributions_placeholder"),
        ("metric_infidelity_score", "infidelity", "infidelity_mean_squared_difference_placeholder"),
        ("metric_complexity_entropy", "complexity", "shannon_entropy_of_normalized_attribution_vector_placeholder"),
        ("metric_surrogate_r2_fidelity", "fidelity", "surrogate_model_r2_approximation_score_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for mid, mfamily, desc in metrics:
        rows.append({
            "metric_id": mid,
            "metric_family": mfamily,
            "description": desc,
            "is_placeholder_only": True,
            "metric_calculation_allowed": False,
            "metric_calculated": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_explainability_metric_placeholders(df)
    return df, summary


def summarize_explainability_metric_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize explainability metric placeholders."""
    return {
        "total_metric_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_metric_calculated_false": bool((~df["metric_calculated"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
