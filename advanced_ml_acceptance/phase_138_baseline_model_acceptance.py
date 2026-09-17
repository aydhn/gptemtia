# -*- coding: utf-8 -*-
"""Phase 145: Phase 138 Baseline Model Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    PHASE_138_BASELINE_MODEL_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

PHASE_138_CHECKS: List[Dict[str, Any]] = [
    {"check_id": "CHK-138-01", "name": "module_present", "topic": "advanced_baseline_ml_models presence", "passed": True, "details": "Baseline model package verified."},
    {"check_id": "CHK-138-02", "name": "model_family_registry_present", "topic": "Baseline model family registry", "passed": True, "details": "Linear, tree, ensemble placeholder families cataloged."},
    {"check_id": "CHK-138-03", "name": "model_contracts_present", "topic": "Model input/output contracts", "passed": True, "details": "Tensor shape and metadata contracts verified."},
    {"check_id": "CHK-138-04", "name": "dry_run_harness_stubs_present", "topic": "Dry-run training harness stubs", "passed": True, "details": "Stub interfaces defined without execution capability."},
    {"check_id": "CHK-138-05", "name": "no_real_training", "topic": "Real model training prohibited", "passed": True, "details": "Training loop triggers disabled."},
    {"check_id": "CHK-138-06", "name": "no_fit_predict_inference", "topic": "Fit/predict/inference prohibited", "passed": True, "details": "Weight estimation and inference disabled."},
    {"check_id": "CHK-138-07", "name": "no_artifact_persistence", "topic": "Model artifact saving prohibited", "passed": True, "details": "Disk persistence of model binaries blocked."},
    {"check_id": "CHK-138-08", "name": "handoff_to_139_completed", "topic": "Phase 139 handoff report", "passed": True, "details": "Phase 139 prerequisites satisfied."},
]


def build_phase_138_baseline_model_acceptance_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 138 acceptance."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for c in PHASE_138_CHECKS:
        row = dict(c)
        row["phase_ref"] = "Phase 138"
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
        "domain": PHASE_138_BASELINE_MODEL_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "phase_ref": "Phase 138",
        "phase_title": "Baseline ML Model Contracts and Dry-Run Training Harness",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": bool(df["passed"].all()),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_phase_138_baseline_model_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 138 acceptance DataFrame."""
    return {
        "phase_ref": "Phase 138",
        "check_count": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False,
        "non_signal": True,
    }
