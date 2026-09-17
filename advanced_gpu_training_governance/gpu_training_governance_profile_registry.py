# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Governance Profile Registry Builder."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    PROFILES,
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_governance_profile_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for GPU training governance profiles."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    rows = []
    for name, p in PROFILES.items():
        rows.append(
            {
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
                "non_signal": True,
                "real_training_allowed": p.allow_real_model_training,
                "prediction_allowed": p.allow_model_predict,
                "artifact_persistence_allowed": p.allow_artifact_persistence,
                "model_registry_write_allowed": p.allow_model_registry_write,
                "min_readiness_score": p.min_readiness_score,
                "tags": ",".join(p.tags),
                "is_active": (p.name == active_profile.name),
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "total_profiles": len(df),
        "active_profile": active_profile.name,
        "all_dry_run": bool((df["dry_run_default"] == True).all()),
        "all_no_real_training": bool((df["real_training_allowed"] == False).all()),
        "all_no_prediction": bool((df["prediction_allowed"] == False).all()),
        "all_no_artifact_persistence": bool((df["artifact_persistence_allowed"] == False).all()),
        "all_no_registry_write": bool((df["model_registry_write_allowed"] == False).all()),
        "current_phase": 139,
        "target_final_phase": 160,
        "next_phase": 140,
        "non_signal": True,
    }
    return df, summary


def summarize_gpu_training_governance_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize a GPU training governance profiles DataFrame."""
    if df.empty:
        return {"total_profiles": 0, "non_signal": True}
    return {
        "total_profiles": len(df),
        "active_profiles": int(df["enabled"].sum()) if "enabled" in df.columns else len(df),
        "all_dry_run": bool((df["dry_run_default"] == True).all()) if "dry_run_default" in df.columns else True,
        "non_signal": True,
    }
