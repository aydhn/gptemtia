# -*- coding: utf-8 -*-
"""Phase 144: Model Card Runtime Dependencies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

RUNTIME_DEPENDENCY_ITEMS: List[Dict[str, str]] = [
    {"rdep_id": "RDEP-01", "name": "gpu_ml_runtime_foundation", "phase_ref": "Phase 136", "role": "CUDA/DirectML hardware discovery and fallback abstraction."},
    {"rdep_id": "RDEP-02", "name": "gpu_resource_governance", "phase_ref": "Phase 139", "role": "VRAM budget limiters, memory monitoring, and timeout policies."},
    {"rdep_id": "RDEP-03", "name": "local_dry_run_environment", "phase_ref": "Phase 144", "role": "Offline mock execution harness with zero network requirements."},
]


def build_model_card_runtime_dependency_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card runtime dependencies."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in RUNTIME_DEPENDENCY_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["status"] = "SATISFIED"
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_card_runtime_dependencies(df)
    return df, summary


def summarize_model_card_runtime_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card runtime dependencies."""
    return {
        "total_runtime_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "non_signal": bool(df["non_signal"].all()),
    }
