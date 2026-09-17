# -*- coding: utf-8 -*-
"""Phase 138 Baseline ML Model Profile Registry.

Builds and summarizes the profile registry for baseline ML models.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    PROFILES,
    get_default_baseline_ml_model_profile,
)


def build_baseline_ml_model_profile_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary dictionary for baseline ML model profiles."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for p_name, p in PROFILES.items():
        rows.append({
            "profile_name": p.name,
            "description": p.description,
            "enabled": p.enabled,
            "current_phase": p.current_phase,
            "target_final_phase": p.target_final_phase,
            "next_phase": p.next_phase,
            "dry_run_default": p.dry_run_default,
            "local_only": p.local_only,
            "non_production": p.non_production,
            "research_only": p.research_only,
            "allow_real_model_training": p.allow_real_model_training,
            "allow_model_predict": p.allow_model_predict,
            "allow_target_label_generation": p.allow_target_label_generation,
            "allow_artifact_persistence": p.allow_artifact_persistence,
            "allow_model_registry_write": p.allow_model_registry_write,
            "non_signal": True,
            "source_preserved": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_ml_model_profiles(df)
    return df, summary


def summarize_baseline_ml_model_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline ML model profile registry DataFrame."""
    return {
        "total_profiles": len(df),
        "enabled_profiles": int(df["enabled"].sum()) if not df.empty else 0,
        "all_dry_run": bool(df["dry_run_default"].all()) if not df.empty else True,
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "zero_real_training": bool((~df["allow_real_model_training"]).all()) if not df.empty else True,
        "zero_prediction": bool((~df["allow_model_predict"]).all()) if not df.empty else True,
        "zero_artifact_persistence": bool((~df["allow_artifact_persistence"]).all()) if not df.empty else True,
        "zero_model_registry_write": bool((~df["allow_model_registry_write"]).all()) if not df.empty else True,
        "non_signal": True,
        "source_preserved": True,
        "production_ready": False,
        "broker_ready": False,
    }
