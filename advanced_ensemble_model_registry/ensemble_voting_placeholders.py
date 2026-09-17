# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Voting Placeholders Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

VOTING_PLACEHOLDERS = [
    {
        "placeholder_id": "hard_voting_placeholder",
        "voting_type": "majority_vote",
        "description": "Majority vote aggregation contract placeholder (execution blocked).",
    },
    {
        "placeholder_id": "soft_voting_placeholder",
        "voting_type": "probability_average",
        "description": "Continuous probability mean voting contract placeholder (execution blocked).",
    },
    {
        "placeholder_id": "trimmed_voting_placeholder",
        "voting_type": "trimmed_mean",
        "description": "Outlier-resistant trimmed mean voting contract placeholder (execution blocked).",
    },
]


def build_ensemble_voting_placeholder_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build voting placeholder registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for vp in VOTING_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_id": vp["placeholder_id"],
                "voting_type": vp["voting_type"],
                "description": vp["description"],
                "execution_blocked": True,
                "voting_executed": False,
                "non_signal": True,
                "source_preserved": True,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ensemble_voting_placeholders(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_ensemble_voting_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize voting placeholders DataFrame."""
    if df.empty:
        return {
            "total_voting_placeholders": 0,
            "all_execution_blocked": True,
            "zero_voting_executed": True,
            "non_signal": True,
        }
    return {
        "total_voting_placeholders": len(df),
        "all_execution_blocked": bool(df["execution_blocked"].all()),
        "zero_voting_executed": not bool(df["voting_executed"].any()),
        "non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_ensemble_voting_placeholders(placeholders: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate ensemble voting placeholders."""
    if isinstance(placeholders, tuple):
        df = placeholders[0]
    elif isinstance(placeholders, pd.DataFrame):
        df = placeholders
    elif isinstance(placeholders, dict):
        return all(not p.get("voting_executed", False) for p in placeholders.values())
    else:
        return False
    if df.empty:
        return False
    if df["voting_executed"].any():
        return False
    if not df["non_signal"].all():
        return False
    return True


build_ensemble_voting_placeholders = build_ensemble_voting_placeholder_registry

