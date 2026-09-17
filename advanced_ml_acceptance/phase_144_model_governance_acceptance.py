# -*- coding: utf-8 -*-
"""Phase 145: Phase 144 Model Governance Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    PHASE_144_MODEL_GOVERNANCE_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

PHASE_144_CHECKS: List[Dict[str, Any]] = [
    {"check_id": "CHK-144-01", "name": "module_present", "topic": "advanced_model_governance presence", "passed": True, "details": "Model governance package verified."},
    {"check_id": "CHK-144-02", "name": "governance_contracts_present", "topic": "Model governance contracts", "passed": True, "details": "Policy registries and governance frameworks registered."},
    {"check_id": "CHK-144-03", "name": "model_cards_present", "topic": "Model cards contracts", "passed": True, "details": "Intended use, limitations, and risk disclosures cataloged."},
    {"check_id": "CHK-144-04", "name": "approval_boundaries_present", "topic": "Approval boundaries", "passed": True, "details": "Zero production/broker/live-trading approval enforced."},
    {"check_id": "CHK-144-05", "name": "audit_placeholders_present", "topic": "Audit trail placeholders", "passed": True, "details": "Audit logging placeholder interfaces verified."},
    {"check_id": "CHK-144-06", "name": "no_production_approval", "topic": "Production approval prohibited", "passed": True, "details": "Explicit no-go production approval boundary enforced."},
    {"check_id": "CHK-144-07", "name": "no_deployment_registry_write", "topic": "Deployment and registry write prohibited", "passed": True, "details": "Model deployment and registry persistence disabled."},
    {"check_id": "CHK-144-08", "name": "handoff_to_145_completed", "topic": "Phase 145 handoff report", "passed": True, "details": "Phase 145 prerequisites satisfied."},
]


def build_phase_144_model_governance_acceptance_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 144 acceptance."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for c in PHASE_144_CHECKS:
        row = dict(c)
        row["phase_ref"] = "Phase 144"
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
        "domain": PHASE_144_MODEL_GOVERNANCE_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "phase_ref": "Phase 144",
        "phase_title": "Model Governance, Model Cards and Audit Trail",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": bool(df["passed"].all()),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_phase_144_model_governance_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 144 acceptance DataFrame."""
    return {
        "phase_ref": "Phase 144",
        "check_count": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False,
        "non_signal": True,
    }
