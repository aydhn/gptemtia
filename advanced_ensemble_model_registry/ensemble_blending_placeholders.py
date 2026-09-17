# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Blending Placeholders Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

BLENDING_PLACEHOLDERS = [
    {
        "placeholder_id": "holdout_blending_placeholder",
        "blending_type": "holdout_split",
        "description": "Holdout validation split blending placeholder contract (execution blocked).",
    },
    {
        "placeholder_id": "walk_forward_blending_placeholder",
        "blending_type": "walk_forward_split",
        "description": "Purged walk-forward temporal split blending placeholder contract (execution blocked).",
    },
]


def build_ensemble_blending_placeholder_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build blending placeholder registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for bp in BLENDING_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_id": bp["placeholder_id"],
                "blending_type": bp["blending_type"],
                "description": bp["description"],
                "execution_blocked": True,
                "blending_executed": False,
                "non_signal": True,
                "source_preserved": True,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ensemble_blending_placeholders(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_ensemble_blending_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize blending placeholders DataFrame."""
    if df.empty:
        return {
            "total_blending_placeholders": 0,
            "all_execution_blocked": True,
            "zero_blending_executed": True,
            "non_signal": True,
        }
    return {
        "total_blending_placeholders": len(df),
        "all_execution_blocked": bool(df["execution_blocked"].all()),
        "zero_blending_executed": not bool(df["blending_executed"].any()),
        "non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_ensemble_blending_placeholders(placeholders: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate ensemble blending placeholders."""
    if isinstance(placeholders, tuple):
        df = placeholders[0]
    elif isinstance(placeholders, pd.DataFrame):
        df = placeholders
    elif isinstance(placeholders, dict):
        return all(not p.get("blending_executed", False) for p in placeholders.values())
    else:
        return False
    if df.empty:
        return False
    if df["blending_executed"].any():
        return False
    if not df["non_signal"].all():
        return False
    return True


build_ensemble_blending_placeholders = build_ensemble_blending_placeholder_registry

