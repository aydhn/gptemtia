# -*- coding: utf-8 -*-
"""Phase 143: Permutation Importance Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_permutation_importance_placeholder_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of permutation importance placeholders."""
    prof = profile or get_explainability_profile()

    perm_data = [
        ("perm_placeholder_single_pass", "single_feature_shuffling", "validation_set", "metric_drop_placeholder"),
        ("perm_placeholder_grouped", "correlated_group_shuffling", "featurestore_groups", "group_metric_drop_placeholder"),
        ("perm_placeholder_multi_repeat", "k_repeat_shuffling", "baseline_candidates", "mean_std_drop_placeholder"),
        ("perm_placeholder_regime_slice", "regime_sliced_shuffling", "regime_validation_splits", "regime_loss_increase_placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for pid, stype, target, desc in perm_data:
        rows.append({
            "placeholder_id": pid,
            "shuffling_type": stype,
            "target_dataset": target,
            "description": desc,
            "is_placeholder_only": True,
            "permutation_importance_executed": False,
            "calculation_allowed": False,
            "execution_blocked_by_policy": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_permutation_importance_placeholders(df)
    return df, summary


def summarize_permutation_importance_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize permutation importance placeholders."""
    return {
        "total_permutation_importance_placeholders": len(df),
        "all_placeholder_only": bool(df["is_placeholder_only"].all()) if not df.empty else True,
        "all_permutation_executed_false": bool((~df["permutation_importance_executed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
