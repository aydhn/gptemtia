# -*- coding: utf-8 -*-
"""Phase 143: Explanation Stability Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_explanation_stability_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of explanation stability placeholders."""
    prof = profile or get_explainability_profile()

    stability_data = [
        ("stability_placeholder_lipschitz", "lipschitz_local_continuity", "local_attribution_perturbations", "local_lipschitz_continuity_score_placeholder"),
        ("stability_placeholder_jaccard_topk", "jaccard_top_k_overlap", "feature_ranking_stability", "top_k_feature_ranking_stability_placeholder"),
        ("stability_placeholder_spearman_rank", "spearman_rank_correlation", "temporal_subsamples", "rank_correlation_across_temporal_windows_placeholder"),
        ("stability_placeholder_noise_sensitivity", "gaussian_noise_sensitivity", "perturbed_instances", "attribution_variance_under_input_noise_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for sid, stype, target, desc in stability_data:
        rows.append({
            "placeholder_id": sid,
            "stability_type": stype,
            "target_eval": target,
            "description": desc,
            "is_placeholder_only": True,
            "stability_calculated": False,
            "calculation_allowed": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_explanation_stability_placeholders(df)
    return df, summary


def summarize_explanation_stability_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize explanation stability placeholders."""
    return {
        "total_stability_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_stability_calculated_false": bool((~df["stability_calculated"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
