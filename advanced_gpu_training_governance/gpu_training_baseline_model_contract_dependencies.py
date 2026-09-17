# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Baseline Model Contract Dependencies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_baseline_model_contract_dependency_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build baseline model contract dependencies registry referencing Phase 138 contracts."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    dependencies = [
        {
            "dependency_id": "BASE_DEP_001",
            "source_phase": 138,
            "contract_name": "baseline_model_contracts",
            "status": "SATISFIED",
            "enforces_zero_training": True,
            "non_signal": True,
            "description": "Requires baseline model contracts (logistic, ridge, tree, gbm, mlp, lstm).",
        },
        {
            "dependency_id": "BASE_DEP_002",
            "source_phase": 138,
            "contract_name": "dry_run_training_harness_contracts",
            "status": "SATISFIED",
            "enforces_zero_training": True,
            "non_signal": True,
            "description": "Requires baseline dry-run trainer stubs and interface contracts.",
        },
        {
            "dependency_id": "BASE_DEP_003",
            "source_phase": 138,
            "contract_name": "baseline_model_training_plans",
            "status": "SATISFIED",
            "enforces_zero_training": True,
            "non_signal": True,
            "description": "Requires declarative non-executing baseline training plans.",
        },
    ]

    df = pd.DataFrame(dependencies)
    summary = summarize_gpu_training_baseline_model_contract_dependencies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_baseline_model_contract_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline model dependencies DataFrame."""
    if df.empty:
        return {"total_dependencies": 0, "non_signal": True}
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "current_phase": 139,
        "non_signal": True,
    }
