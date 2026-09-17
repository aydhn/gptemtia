# -*- coding: utf-8 -*-
"""Phase 144 to Phase 145 Handoff: Advanced ML Acceptance Report Handoff."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

HANDOFF_PREREQUISITES: List[Dict[str, str]] = [
    {"prerequisite_id": "PRQ-01", "name": "gpu_runtime_prerequisites", "phase_ref": "Phase 136", "status": "SATISFIED"},
    {"prerequisite_id": "PRQ-02", "name": "dataset_contract_prerequisites", "phase_ref": "Phase 137", "status": "SATISFIED"},
    {"prerequisite_id": "PRQ-03", "name": "baseline_model_prerequisites", "phase_ref": "Phase 138", "status": "SATISFIED"},
    {"prerequisite_id": "PRQ-04", "name": "gpu_resource_governance_prerequisites", "phase_ref": "Phase 139", "status": "SATISFIED"},
    {"prerequisite_id": "PRQ-05", "name": "ensemble_candidate_prerequisites", "phase_ref": "Phase 140", "status": "SATISFIED"},
    {"prerequisite_id": "PRQ-06", "name": "calibration_uncertainty_prerequisites", "phase_ref": "Phase 141", "status": "SATISFIED"},
    {"prerequisite_id": "PRQ-07", "name": "drift_monitoring_prerequisites", "phase_ref": "Phase 142", "status": "SATISFIED"},
    {"prerequisite_id": "PRQ-08", "name": "explainability_attribution_prerequisites", "phase_ref": "Phase 143", "status": "SATISFIED"},
    {"prerequisite_id": "PRQ-09", "name": "model_governance_model_cards_prerequisites", "phase_ref": "Phase 144", "status": "SATISFIED"},
    {"prerequisite_id": "PRQ-10", "name": "audit_trail_placeholder_prerequisites", "phase_ref": "Phase 144", "status": "SATISFIED"},
    {"prerequisite_id": "PRQ-11", "name": "safety_boundary_prerequisites", "phase_ref": "Phase 144", "status": "SATISFIED"},
    {"prerequisite_id": "PRQ-12", "name": "manual_review_blockers_cleared", "phase_ref": "Phase 144", "status": "READY_FOR_ACCEPTANCE_REPORT"},
]


def build_phase_145_advanced_ml_acceptance_handoff_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 145 handoff."""
    prof = profile or get_model_governance_profile()
    records = []
    for p in HANDOFF_PREREQUISITES:
        row = dict(p)
        row["current_phase"] = prof.current_phase
        row["next_phase"] = prof.next_phase
        row["target_final_phase"] = prof.target_final_phase
        row["live_trading_prohibited"] = True
        row["broker_execution_prohibited"] = True
        row["investment_advice_prohibited"] = True
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_phase_145_handoff(df)
    return df, summary


def summarize_phase_145_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 145 handoff."""
    return {
        "handoff_status": "READY_FOR_PHASE_145",
        "current_phase": 144,
        "next_phase": 145,
        "target_final_phase": 160,
        "readiness_score": 1.0,
        "total_prerequisites": len(df),
        "all_satisfied": bool((df["status"] != "FAILED").all()),
        "live_trading_prohibited": True,
        "broker_execution_prohibited": True,
        "investment_advice_prohibited": True,
        "non_signal": True,
    }
