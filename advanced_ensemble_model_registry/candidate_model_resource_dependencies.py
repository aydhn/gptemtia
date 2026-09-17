# -*- coding: utf-8 -*-
"""Phase 140: Candidate Model Resource Dependencies Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

RESOURCE_DEPENDENCIES = [
    {
        "dependency_name": "gpu_runtime_foundation_dependency",
        "source_phase": 136,
        "source_module": "advanced_gpu_ml_runtime",
        "status": "DEPENDENCY_SATISFIED",
        "description": "Hardware and execution environment capability from Phase 136.",
    },
    {
        "dependency_name": "gpu_resource_governance_dependency",
        "source_phase": 139,
        "source_module": "advanced_gpu_training_governance",
        "status": "DEPENDENCY_SATISFIED",
        "description": "Memory bounds and timeout governance from Phase 139.",
    },
]


def build_candidate_model_resource_dependency_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build candidate model resource dependency registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for dep in RESOURCE_DEPENDENCIES:
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
    summary = summarize_candidate_model_resource_dependencies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_candidate_model_resource_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize resource dependency registry DataFrame."""
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


build_candidate_model_resource_dependencies = build_candidate_model_resource_dependency_registry
