# -*- coding: utf-8 -*-
"""Phase 140: Candidate Model GPU Governance Dependencies Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

GPU_GOVERNANCE_DEPENDENCIES = [
    {
        "dependency_name": "gpu_device_selection_dependency",
        "source_phase": 139,
        "source_module": "advanced_gpu_training_governance",
        "status": "DEPENDENCY_SATISFIED",
        "description": "Deterministic GPU device selection with CPU fallback from Phase 139.",
    },
    {
        "dependency_name": "gpu_memory_budget_dependency",
        "source_phase": 139,
        "source_module": "advanced_gpu_training_governance",
        "status": "DEPENDENCY_SATISFIED",
        "description": "GPU memory allocation budget and cap policies from Phase 139.",
    },
    {
        "dependency_name": "training_timeout_dependency",
        "source_phase": 139,
        "source_module": "advanced_gpu_training_governance",
        "status": "DEPENDENCY_SATISFIED",
        "description": "Training execution timeout policy and watchdog guards from Phase 139.",
    },
]


def build_candidate_model_gpu_governance_dependency_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build candidate model GPU governance dependency registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for dep in GPU_GOVERNANCE_DEPENDENCIES:
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
    summary = summarize_candidate_model_gpu_governance_dependencies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_candidate_model_gpu_governance_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize GPU governance dependency registry DataFrame."""
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


build_candidate_model_gpu_governance_dependencies = build_candidate_model_gpu_governance_dependency_registry

