# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Model Profile Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    PROFILES,
    get_default_ensemble_model_profile,
)


def build_ensemble_model_profile_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for registered Phase 140 profiles."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for name, prof in PROFILES.items():
        rows.append(
            {
                "profile_name": prof.name,
                "description": prof.description,
                "current_phase": prof.current_phase,
                "target_final_phase": prof.target_final_phase,
                "next_phase": prof.next_phase,
                "dry_run_default": prof.dry_run_default,
                "local_only": prof.local_only,
                "non_production": prof.non_production,
                "research_only": prof.research_only,
                "allow_live_trading": prof.allow_live_trading,
                "allow_real_model_training": prof.allow_real_model_training,
                "allow_ensemble_execution": prof.allow_ensemble_execution,
                "allow_calibration_execution": prof.allow_calibration_execution,
                "allow_target_label_generation": prof.allow_target_label_generation,
                "allow_prediction_generation": prof.allow_prediction_generation,
                "allow_artifact_persistence": prof.allow_artifact_persistence,
                "allow_model_registry_write": prof.allow_model_registry_write,
                "non_signal": True,
                "source_preserved": True,
                "production_ready": False,
                "broker_ready": False,
                "official_approval": False,
                "is_active": (prof.name == active_profile.name),
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ensemble_model_profiles(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_ensemble_model_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize profile registry DataFrame."""
    if df.empty:
        return {
            "total_profiles": 0,
            "all_dry_run": True,
            "all_non_signal": True,
            "real_training_allowed": False,
            "ensemble_execution_allowed": False,
        }
    return {
        "total_profiles": len(df),
        "profiles": list(df["profile_name"]),
        "all_dry_run": bool(df["dry_run_default"].all()),
        "all_local_only": bool(df["local_only"].all()),
        "all_non_signal": bool(df["non_signal"].all()),
        "real_training_allowed": bool(df["allow_real_model_training"].any()),
        "ensemble_execution_allowed": bool(df["allow_ensemble_execution"].any()),
        "production_ready": False,
        "broker_ready": False,
        "official_approval": False,
    }


def validate_ensemble_model_profile_registry(df: pd.DataFrame, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate ensemble model profile registry DataFrame and summary."""
    if df.empty:
        return False
    if not df["non_signal"].all():
        return False
    if df["allow_real_model_training"].any() or df["allow_ensemble_execution"].any():
        return False
    if not df["dry_run_default"].all() or not df["local_only"].all():
        return False
    return True

