"""
advanced_ml_dataset_domain_registry.py
Phase 137 — Advanced ML Dataset Contracts and Experiment Registry: Domain Registry Builder

current_phase=137 | target_final_phase=160 | next_phase=138
dry_run=True | local_only=True | non_production=True | research_only=True

Builds a registry DataFrame of all dataset domain labels.
No data is persisted (save=False). No model training or materialization occurs.
All live/broker/signal/training/prediction flags=False.
"""

import pandas as pd
from typing import Dict, Tuple

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_labels import (
    ADVANCED_ML_DATASET_DOMAIN_LABELS,
)


def build_advanced_ml_dataset_domain_registry(
    profile: AdvancedMlDatasetProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """
    Build an in-memory registry of all Advanced ML Dataset domain labels.

    Parameters
    ----------
    profile : AdvancedMlDatasetProfile | None
        Active profile used for session context.  Defaults to the system default
        profile when not provided.

    Returns
    -------
    df : pd.DataFrame
        One row per domain label with phase, guard, and flag metadata.
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

    rows = []
    for label in ADVANCED_ML_DATASET_DOMAIN_LABELS:
        rows.append(
            {
                "domain_label": label,
                "current_phase": 137,
                "target_final_phase": 160,
                "next_phase": 138,
                "non_signal": True,
                "dry_run": True,
                "local_only": True,
                "non_production": True,
                "research_only": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
                "dataset_materialized": False,
                "model_training_executed": False,
                "artifact_persisted": False,
                "status": "dataset_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)

    summary: Dict = {
        "total_domains": len(rows),
        "current_phase": 137,
        "target_final_phase": 160,
        "next_phase": 138,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
        "status": "READY",
    }

    return df, summary


def summarize_advanced_ml_dataset_domains(
    df: pd.DataFrame | None = None,
) -> Dict:
    """Return a summary of advanced ML dataset domains."""
    if df is None:
        df, summary = build_advanced_ml_dataset_domain_registry()
        return summary
    return {
        "total_domains": len(df),
        "current_phase": 137,
        "target_final_phase": 160,
        "next_phase": 138,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
        "status": "READY",
    }
