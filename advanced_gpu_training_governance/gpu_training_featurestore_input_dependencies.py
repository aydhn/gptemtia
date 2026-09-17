# -*- coding: utf-8 -*-
"""Phase 139 GPU Training FeatureStore Input Dependencies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_featurestore_input_dependency_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build FeatureStore input dependency registry referencing catalog contracts."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    dependencies = [
        {
            "dependency_id": "FS_DEP_001",
            "source_phase": 134,
            "catalog_name": "featurestore_read_contracts",
            "status": "SATISFIED",
            "non_signal": True,
            "description": "Read-only access contracts for FeatureStore technical and macro factors.",
        },
        {
            "dependency_id": "FS_DEP_002",
            "source_phase": 135,
            "catalog_name": "regime_classification_acceptance_catalog",
            "status": "SATISFIED",
            "non_signal": True,
            "description": "Accepted regime state metadata without predictive labels.",
        },
        {
            "dependency_id": "FS_DEP_003",
            "source_phase": 121,
            "catalog_name": "feature_validation_matrix_manifest",
            "status": "SATISFIED",
            "non_signal": True,
            "description": "Validated feature matrix schema without infinite or lookahead values.",
        },
    ]

    df = pd.DataFrame(dependencies)
    summary = summarize_gpu_training_featurestore_input_dependencies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_featurestore_input_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize FeatureStore input dependencies DataFrame."""
    if df.empty:
        return {"total_dependencies": 0, "non_signal": True}
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "current_phase": 139,
        "non_signal": True,
    }
