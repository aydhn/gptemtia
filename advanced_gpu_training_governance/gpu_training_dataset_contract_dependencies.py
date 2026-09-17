# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Dataset Contract Dependencies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_dataset_contract_dependency_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dataset contract dependencies registry referencing Phase 137 contracts."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    dependencies = [
        {
            "dependency_id": "DS_DEP_001",
            "source_phase": 137,
            "contract_name": "advanced_ml_dataset_schema_contracts",
            "status": "SATISFIED",
            "enforces_no_materialization": True,
            "non_signal": True,
            "description": "Requires dataset schema definitions without disk materialization.",
        },
        {
            "dependency_id": "DS_DEP_002",
            "source_phase": 137,
            "contract_name": "purged_walk_forward_split_contracts",
            "status": "SATISFIED",
            "enforces_no_materialization": True,
            "non_signal": True,
            "description": "Requires walk-forward and purged time-series splitting contracts.",
        },
        {
            "dependency_id": "DS_DEP_003",
            "source_phase": 137,
            "contract_name": "feature_snapshot_manifest_placeholders",
            "status": "SATISFIED",
            "enforces_no_materialization": True,
            "non_signal": True,
            "description": "Requires feature snapshot manifest placeholders with zero payload writing.",
        },
    ]

    df = pd.DataFrame(dependencies)
    summary = summarize_gpu_training_dataset_contract_dependencies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_dataset_contract_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize dataset dependencies DataFrame."""
    if df.empty:
        return {"total_dependencies": 0, "non_signal": True}
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "current_phase": 139,
        "non_signal": True,
    }
