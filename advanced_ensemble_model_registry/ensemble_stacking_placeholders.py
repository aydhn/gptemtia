# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Stacking Placeholders Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

STACKING_PLACEHOLDERS = [
    {
        "placeholder_id": "oof_stacking_placeholder",
        "stacking_type": "out_of_fold",
        "description": "Out-of-fold cross-validated meta-feature stacking placeholder contract (execution blocked).",
    },
    {
        "placeholder_id": "multi_level_stacking_placeholder",
        "stacking_type": "hierarchical_stacking",
        "description": "Two-level hierarchical candidate stacking placeholder contract (execution blocked).",
    },
]


def build_ensemble_stacking_placeholder_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build stacking placeholder registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for sp in STACKING_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_id": sp["placeholder_id"],
                "stacking_type": sp["stacking_type"],
                "description": sp["description"],
                "execution_blocked": True,
                "stacking_executed": False,
                "non_signal": True,
                "source_preserved": True,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ensemble_stacking_placeholders(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_ensemble_stacking_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize stacking placeholders DataFrame."""
    if df.empty:
        return {
            "total_stacking_placeholders": 0,
            "all_execution_blocked": True,
            "zero_stacking_executed": True,
            "non_signal": True,
        }
    return {
        "total_stacking_placeholders": len(df),
        "all_execution_blocked": bool(df["execution_blocked"].all()),
        "zero_stacking_executed": not bool(df["stacking_executed"].any()),
        "non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_ensemble_stacking_placeholders(placeholders: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate ensemble stacking placeholders."""
    if isinstance(placeholders, tuple):
        df = placeholders[0]
    elif isinstance(placeholders, pd.DataFrame):
        df = placeholders
    elif isinstance(placeholders, dict):
        return all(not p.get("stacking_executed", False) for p in placeholders.values())
    else:
        return False
    if df.empty:
        return False
    if df["stacking_executed"].any():
        return False
    if not df["non_signal"].all():
        return False
    return True


build_ensemble_stacking_placeholders = build_ensemble_stacking_placeholder_registry

