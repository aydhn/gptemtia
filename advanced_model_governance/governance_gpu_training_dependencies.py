# -*- coding: utf-8 -*-
"""Phase 144: Governance GPU Training Dependencies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

GPU_TRAINING_DEP_SPECS: List[Dict[str, str]] = [
    {"dependency_name": "phase_139_gpu_resource_policies", "source": "Phase 139", "scope": "VRAM budget control and device limiters", "status": "SATISFIED"},
    {"dependency_name": "phase_139_timeout_policies", "source": "Phase 139", "scope": "Execution execution timeouts", "status": "SATISFIED"},
    {"dependency_name": "phase_139_audit_placeholders", "source": "Phase 139", "scope": "GPU audit placeholders", "status": "SATISFIED"},
]


def build_governance_gpu_training_dependency_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for GPU training dependencies."""
    prof = profile or get_model_governance_profile()
    records = []
    for spec in GPU_TRAINING_DEP_SPECS:
        row = dict(spec)
        row["phase"] = prof.current_phase
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_gpu_training_dependencies(df)
    return df, summary


def summarize_governance_gpu_training_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize GPU training dependencies."""
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "non_signal": bool(df["non_signal"].all()),
    }
