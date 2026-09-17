# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Weighting Policy Placeholders Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

WEIGHTING_POLICIES = [
    {
        "policy_id": "uniform_weighting_policy",
        "weighting_type": "uniform",
        "description": "Equal weight allocation placeholder across candidate models (calculation blocked).",
    },
    {
        "policy_id": "validation_loss_weighting_policy",
        "weighting_type": "inverse_validation_loss",
        "description": "Inverse validation error weighting placeholder contract (calculation blocked).",
    },
    {
        "policy_id": "information_ratio_weighting_policy",
        "weighting_type": "metric_scaled",
        "description": "Cross-validation stability weighting placeholder contract (calculation blocked).",
    },
]


def build_ensemble_weighting_policy_placeholder_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build weighting policy placeholder registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for wp in WEIGHTING_POLICIES:
        rows.append(
            {
                "policy_id": wp["policy_id"],
                "weighting_type": wp["weighting_type"],
                "description": wp["description"],
                "calculation_blocked": True,
                "weights_calculated": False,
                "non_signal": True,
                "source_preserved": True,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ensemble_weighting_policy_placeholders(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_ensemble_weighting_policy_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize weighting policy placeholders DataFrame."""
    if df.empty:
        return {
            "total_weighting_policies": 0,
            "all_calculations_blocked": True,
            "zero_weights_calculated": True,
            "non_signal": True,
        }
    return {
        "total_weighting_policies": len(df),
        "all_calculations_blocked": bool(df["calculation_blocked"].all()),
        "zero_weights_calculated": not bool(df["weights_calculated"].any()),
        "non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_ensemble_weighting_policy_placeholders(placeholders: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate ensemble weighting policy placeholders."""
    if isinstance(placeholders, tuple):
        df = placeholders[0]
    elif isinstance(placeholders, pd.DataFrame):
        df = placeholders
    elif isinstance(placeholders, dict):
        return all(not p.get("weights_calculated", False) for p in placeholders.values())
    else:
        return False
    if df.empty:
        return False
    if df["weights_calculated"].any():
        return False
    if not df["non_signal"].all():
        return False
    return True


build_ensemble_weighting_policy_placeholders = build_ensemble_weighting_policy_placeholder_registry

