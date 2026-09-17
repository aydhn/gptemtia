# -*- coding: utf-8 -*-
"""Phase 140: Candidate Model Compatibility Matrix Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)
from advanced_ensemble_model_registry.candidate_model_families import CANDIDATE_MODEL_FAMILIES


def build_candidate_model_compatibility_matrix_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build candidate model compatibility matrix registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for fam in CANDIDATE_MODEL_FAMILIES:
        matrix_id = f"compat_{fam['family_id']}"
        rows.append(
            {
                "matrix_id": matrix_id,
                "candidate_family": fam["family_id"],
                "compatible_dataset_family_placeholder": "timeseries_purged_walk_forward_datasets",
                "compatible_runtime_backend_placeholder": "local_cpu_or_gpu_runtime_foundation",
                "compatible_resource_policy_placeholder": "bounded_memory_timeout_resource_policy",
                "compatible_ensemble_strategy_placeholder": "voting_blending_stacking_strategies",
                "compatibility_score_placeholder": 1.0,
                "compatibility_score_is_signal": False,
                "compatibility_score_is_performance": False,
                "manual_review_required": True,
                "non_signal": True,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_candidate_model_compatibility_matrix(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_candidate_model_compatibility_matrix(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize candidate compatibility matrix DataFrame."""
    if df.empty:
        return {
            "total_compatibility_records": 0,
            "all_scores_non_signal": True,
            "all_scores_non_performance": True,
            "non_signal": True,
        }
    return {
        "total_compatibility_records": len(df),
        "all_scores_non_signal": not bool(df["compatibility_score_is_signal"].any()),
        "all_scores_non_performance": not bool(df["compatibility_score_is_performance"].any()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "non_signal": bool(df["non_signal"].all()),
        "all_non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_candidate_compatibility_matrix(matrix: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate candidate compatibility matrix."""
    if isinstance(matrix, tuple):
        df = matrix[0]
    elif isinstance(matrix, pd.DataFrame):
        df = matrix
    elif isinstance(matrix, dict):
        return all(m.get("non_signal", False) for m in matrix.values())
    else:
        return False
    if df.empty:
        return False
    if df["compatibility_score_is_signal"].any() or df["compatibility_score_is_performance"].any():
        return False
    if not df["non_signal"].all():
        return False
    return True


build_candidate_compatibility_matrix = build_candidate_model_compatibility_matrix_registry
summarize_candidate_compatibility_matrix = summarize_candidate_model_compatibility_matrix

