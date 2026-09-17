# -*- coding: utf-8 -*-
"""Phase 140: Candidate Model Dataset Dependencies Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

DATASET_DEPENDENCIES = [
    {
        "dependency_name": "dataset_contracts_dependency",
        "source_phase": 137,
        "source_module": "advanced_ml_dataset_registry",
        "status": "DEPENDENCY_SATISFIED",
        "description": "Dataset schema and splitting contracts from Phase 137.",
    },
    {
        "dependency_name": "featurestore_catalog_dependency",
        "source_phase": 134,
        "source_module": "advanced_regime_featurestore_integration",
        "status": "DEPENDENCY_SATISFIED",
        "description": "Feature and factor schema definitions from Phase 134 FeatureStore.",
    },
]


def build_candidate_model_dataset_dependency_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build candidate model dataset dependency registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for dep in DATASET_DEPENDENCIES:
        rows.append(
            {
                "dependency_name": dep["dependency_name"],
                "source_phase": dep["source_phase"],
                "source_module": dep["source_module"],
                "status": dep["status"],
                "description": dep["description"],
                "non_signal": True,
                "source_preserved": True,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_candidate_model_dataset_dependencies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_candidate_model_dataset_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize dataset dependency registry DataFrame."""
    if df.empty:
        return {
            "total_dependencies": 0,
            "all_satisfied": True,
            "non_signal": True,
        }
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "DEPENDENCY_SATISFIED").all()),
        "all_non_signal": bool(df["non_signal"].all()),
        "non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


build_candidate_model_dataset_dependencies = build_candidate_model_dataset_dependency_registry
