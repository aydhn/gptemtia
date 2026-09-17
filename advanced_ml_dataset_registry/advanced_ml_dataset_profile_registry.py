"""
advanced_ml_dataset_profile_registry.py
Phase 137 — Advanced ML Dataset Contracts and Experiment Registry: Profile Registry Builder

current_phase=137 | target_final_phase=160 | next_phase=138
dry_run=True | local_only=True | non_production=True | research_only=True

Builds a registry DataFrame of all dataset profiles.
No data is persisted (save=False). No model training or materialization occurs.
All live/broker/signal/training/prediction flags=False.
"""

import pandas as pd
from typing import Dict, Tuple

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
    list_advanced_ml_dataset_profiles,
)


def build_advanced_ml_dataset_profile_registry(
    profile: AdvancedMlDatasetProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """
    Build an in-memory registry of all Advanced ML Dataset profiles.

    Parameters
    ----------
    profile : AdvancedMlDatasetProfile | None
        Active profile to report in the summary.  Defaults to the system default
        profile when not provided.

    Returns
    -------
    df : pd.DataFrame
        One row per registered profile with phase, guard, and flag metadata.
    summary : Dict
        High-level summary dictionary for the active session.

    Notes
    -----
    - save=False — no file I/O is performed.
    - All execution and materialization flags are hard-coded to False.
    - Status is always "dataset_contract_placeholder_only".
    """
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()

    profiles = list_advanced_ml_dataset_profiles(enabled_only=False)

    rows = []
    for p in profiles:
        p_name = getattr(p, "name", p.get("name", ""))
        p_desc = getattr(p, "description", p.get("description", ""))
        p_enabled = getattr(p, "enabled", p.get("enabled", True))
        rows.append(
            {
                "profile_name": p_name,
                "description": p_desc,
                "enabled": p_enabled,
                "current_phase": 137,
                "target_final_phase": 160,
                "next_phase": 138,
                "dry_run": True,
                "local_only": True,
                "non_production": True,
                "research_only": True,
                "non_signal": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
                "dataset_materialized": False,
                "feature_snapshot_materialized": False,
                "model_training_executed": False,
                "artifact_persisted": False,
                "status": "dataset_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)

    summary: Dict = {
        "total_profiles": len(rows),
        "active_profile": profile.name,
        "current_phase": 137,
        "target_final_phase": 160,
        "next_phase": 138,
        "non_signal": True,
        "dry_run": True,
        "local_only": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
        "dataset_materialized": False,
        "dataset_materialization_allowed": False,
        "model_training_executed": False,
        "model_training_allowed": False,
        "status": "READY",
    }

    return df, summary


def summarize_advanced_ml_dataset_profiles(
    df: pd.DataFrame | None = None,
) -> Dict:
    """Return a summary of advanced ML dataset profiles."""
    if df is None:
        df, summary = build_advanced_ml_dataset_profile_registry()
        return summary
    return {
        "total_profiles": len(df),
        "current_phase": 137,
        "target_final_phase": 160,
        "next_phase": 138,
        "non_signal": True,
        "dry_run": True,
        "local_only": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
        "dataset_materialized": False,
        "dataset_materialization_allowed": False,
        "model_training_executed": False,
        "model_training_allowed": False,
        "status": "READY",
    }
