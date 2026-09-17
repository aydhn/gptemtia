# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Runtime Dependencies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_runtime_dependency_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build runtime dependency registry referencing Phase 136 runtime foundation."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    dependencies = [
        {
            "dependency_id": "RUN_DEP_001",
            "source_phase": 136,
            "runtime_component": "local_hardware_discovery",
            "status": "SATISFIED",
            "non_signal": True,
            "description": "Hardware discovery probe verifying GPU, CPU, and RAM metrics without allocation.",
        },
        {
            "dependency_id": "RUN_DEP_002",
            "source_phase": 136,
            "runtime_component": "accelerator_backend_registry",
            "status": "SATISFIED",
            "non_signal": True,
            "description": "Accelerator registry mapping CUDA, CPU, and MPS backends.",
        },
        {
            "dependency_id": "RUN_DEP_003",
            "source_phase": 136,
            "runtime_component": "ml_runtime_safety_contracts",
            "status": "SATISFIED",
            "non_signal": True,
            "description": "Base runtime safety boundaries prohibiting unvetted training execution.",
        },
    ]

    df = pd.DataFrame(dependencies)
    summary = summarize_gpu_training_runtime_dependencies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_runtime_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize runtime dependencies DataFrame."""
    if df.empty:
        return {"total_dependencies": 0, "non_signal": True}
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "current_phase": 139,
        "non_signal": True,
    }
