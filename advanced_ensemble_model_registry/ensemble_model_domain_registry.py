# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Model Domain Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)
from advanced_ensemble_model_registry.ensemble_model_labels import ENSEMBLE_MODEL_DOMAIN_LABELS


def build_ensemble_model_domain_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build domain registry DataFrame and summary for Phase 140."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for domain in ENSEMBLE_MODEL_DOMAIN_LABELS:
        rows.append(
            {
                "domain_name": domain,
                "current_phase": 140,
                "target_final_phase": 160,
                "next_phase": 141,
                "status": "contract_registered",
                "execution_allowed": False,
                "non_signal": True,
                "source_preserved": True,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ensemble_model_domains(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_ensemble_model_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize ensemble model domain DataFrame."""
    if df.empty:
        return {
            "total_domains": 0,
            "all_non_signal": True,
            "execution_blocked": True,
        }
    return {
        "total_domains": len(df),
        "domains": list(df["domain_name"]),
        "all_non_signal": bool(df["non_signal"].all()),
        "all_source_preserved": bool(df["source_preserved"].all()),
        "execution_blocked": not bool(df["execution_allowed"].any()),
        "manual_review_required": bool(df["manual_review_required"].all()),
    }


def validate_ensemble_model_domain_registry(df: pd.DataFrame, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate ensemble model domain registry DataFrame and summary."""
    if df.empty:
        return False
    if not df["non_signal"].all():
        return False
    if df["execution_allowed"].any():
        return False
    return True

