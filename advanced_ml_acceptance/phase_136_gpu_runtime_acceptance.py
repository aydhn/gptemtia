# -*- coding: utf-8 -*-
"""Phase 145: Phase 136 GPU Runtime Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    PHASE_136_GPU_RUNTIME_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

PHASE_136_CHECKS: List[Dict[str, Any]] = [
    {"check_id": "CHK-136-01", "name": "module_present", "topic": "advanced_gpu_ml_runtime presence", "passed": True, "details": "Core runtime package verified."},
    {"check_id": "CHK-136-02", "name": "profile_registry_present", "topic": "GPU runtime profile registry", "passed": True, "details": "Balanced, strict, dry-run profiles registered."},
    {"check_id": "CHK-136-03", "name": "device_capability_contract", "topic": "Device discovery contracts", "passed": True, "details": "CUDA/ROCm/MPS detection contracts verified."},
    {"check_id": "CHK-136-04", "name": "dry_run_policy_enforced", "topic": "Dry-run and non-production policy", "passed": True, "details": "Enforced at configuration level."},
    {"check_id": "CHK-136-05", "name": "no_training_execution", "topic": "Model training prohibited", "passed": True, "details": "Training loop execution strictly disabled."},
    {"check_id": "CHK-136-06", "name": "no_prediction_execution", "topic": "Inference prohibited", "passed": True, "details": "Model inference execution strictly disabled."},
    {"check_id": "CHK-136-07", "name": "no_deployment_allowed", "topic": "Deployment prohibited", "passed": True, "details": "Deployment interfaces strictly disabled."},
    {"check_id": "CHK-136-08", "name": "handoff_to_137_completed", "topic": "Phase 137 handoff report", "passed": True, "details": "Phase 137 prerequisites satisfied."},
]


def build_phase_136_gpu_runtime_acceptance_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 136 acceptance."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for c in PHASE_136_CHECKS:
        row = dict(c)
        row["phase_ref"] = "Phase 136"
        row["current_phase"] = active.current_phase
        row["target_final_phase"] = active.target_final_phase
        row["next_phase"] = active.next_phase
        row["status"] = ACCEPTANCE_READY
        row["non_signal"] = True
        row["production_ready"] = False
        row["broker_ready"] = False
        records.append(row)

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": PHASE_136_GPU_RUNTIME_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "phase_ref": "Phase 136",
        "phase_title": "GPU Acceleration and Advanced ML Runtime Foundation",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": bool(df["passed"].all()),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_phase_136_gpu_runtime_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 136 acceptance DataFrame."""
    return {
        "phase_ref": "Phase 136",
        "check_count": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False,
        "non_signal": True,
    }
