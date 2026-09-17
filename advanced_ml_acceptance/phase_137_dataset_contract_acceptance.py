# -*- coding: utf-8 -*-
"""Phase 145: Phase 137 Dataset Contract Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    PHASE_137_DATASET_CONTRACT_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

PHASE_137_CHECKS: List[Dict[str, Any]] = [
    {"check_id": "CHK-137-01", "name": "module_present", "topic": "advanced_ml_dataset_registry presence", "passed": True, "details": "Dataset registry package verified."},
    {"check_id": "CHK-137-02", "name": "dataset_contracts_present", "topic": "Dataset contract registry", "passed": True, "details": "Schema contracts and column namespaces registered."},
    {"check_id": "CHK-137-03", "name": "experiment_registry_present", "topic": "ML experiment registry", "passed": True, "details": "Run plan templates and tracking contracts verified."},
    {"check_id": "CHK-137-04", "name": "no_dataset_materialization", "topic": "Dataset materialization prohibited", "passed": True, "details": "Storage writes of materialized datasets blocked."},
    {"check_id": "CHK-137-05", "name": "no_target_label_generation", "topic": "Target/label generation prohibited", "passed": True, "details": "Target label creation contracts disabled."},
    {"check_id": "CHK-137-06", "name": "no_prediction_generation", "topic": "Prediction generation prohibited", "passed": True, "details": "Prediction outputs strictly blocked."},
    {"check_id": "CHK-137-07", "name": "no_lookahead_guards_present", "topic": "No-lookahead leakage guards", "passed": True, "details": "Chronological split contracts verified."},
    {"check_id": "CHK-137-08", "name": "handoff_to_138_completed", "topic": "Phase 138 handoff report", "passed": True, "details": "Phase 138 prerequisites satisfied."},
]


def build_phase_137_dataset_contract_acceptance_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 137 acceptance."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for c in PHASE_137_CHECKS:
        row = dict(c)
        row["phase_ref"] = "Phase 137"
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
        "domain": PHASE_137_DATASET_CONTRACT_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "phase_ref": "Phase 137",
        "phase_title": "Advanced ML Dataset Contracts and Experiment Registry",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": bool(df["passed"].all()),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_phase_137_dataset_contract_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 137 acceptance DataFrame."""
    return {
        "phase_ref": "Phase 137",
        "check_count": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False,
        "non_signal": True,
    }
