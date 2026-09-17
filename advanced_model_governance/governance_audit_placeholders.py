# -*- coding: utf-8 -*-
"""Phase 144: Governance Audit Placeholders Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

GOVERNANCE_AUDIT_PLACEHOLDERS: List[Dict[str, str]] = [
    {
        "governance_audit_id_placeholder": "GAUD-001",
        "model_card_contract_ref": "baseline_model_card_contract",
        "governance_contract_ref": "baseline_model_governance_contract",
        "approval_boundary_ref": "production_approval_blocked_boundary",
        "validation_evidence_ref": "baseline_validation_evidence",
        "risk_register_ref": "REG-01",
        "control_checklist_ref": "CHK-01",
    },
    {
        "governance_audit_id_placeholder": "GAUD-002",
        "model_card_contract_ref": "candidate_model_card_contract",
        "governance_contract_ref": "candidate_model_governance_contract",
        "approval_boundary_ref": "broker_ready_approval_blocked_boundary",
        "validation_evidence_ref": "candidate_validation_evidence",
        "risk_register_ref": "REG-02",
        "control_checklist_ref": "CHK-02",
    },
    {
        "governance_audit_id_placeholder": "GAUD-003",
        "model_card_contract_ref": "ensemble_model_card_contract",
        "governance_contract_ref": "ensemble_model_governance_contract",
        "approval_boundary_ref": "live_trading_approval_blocked_boundary",
        "validation_evidence_ref": "ensemble_validation_evidence",
        "risk_register_ref": "REG-04",
        "control_checklist_ref": "CHK-04",
    },
    {
        "governance_audit_id_placeholder": "GAUD-004",
        "model_card_contract_ref": "calibration_uncertainty_model_card_contract",
        "governance_contract_ref": "calibration_uncertainty_governance_contract",
        "approval_boundary_ref": "release_approval_blocked_boundary",
        "validation_evidence_ref": "calibration_validation_evidence",
        "risk_register_ref": "REG-05",
        "control_checklist_ref": "CHK-05",
    },
    {
        "governance_audit_id_placeholder": "GAUD-005",
        "model_card_contract_ref": "drift_monitoring_model_card_contract",
        "governance_contract_ref": "drift_monitoring_governance_contract",
        "approval_boundary_ref": "official_approval_claim_blocked_boundary",
        "validation_evidence_ref": "drift_validation_evidence",
        "risk_register_ref": "REG-06",
        "control_checklist_ref": "CHK-06",
    },
    {
        "governance_audit_id_placeholder": "GAUD-006",
        "model_card_contract_ref": "explainability_model_card_contract",
        "governance_contract_ref": "explainability_governance_contract",
        "approval_boundary_ref": "manual_review_required_boundary",
        "validation_evidence_ref": "explainability_validation_evidence",
        "risk_register_ref": "REG-07",
        "control_checklist_ref": "CHK-07",
    },
    {
        "governance_audit_id_placeholder": "GAUD-007",
        "model_card_contract_ref": "advanced_ml_acceptance_model_card_contract",
        "governance_contract_ref": "advanced_ml_acceptance_governance_contract",
        "approval_boundary_ref": "production_approval_blocked_boundary",
        "validation_evidence_ref": "acceptance_validation_evidence",
        "risk_register_ref": "REG-08",
        "control_checklist_ref": "CHK-08",
    },
]


def build_governance_audit_placeholder_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance audit placeholders."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in GOVERNANCE_AUDIT_PLACEHOLDERS:
        row = dict(item)
        row["dry_run_only"] = True
        row["real_audit_log"] = False
        row["production_approved"] = False
        row["broker_ready_approved"] = False
        row["live_trading_approved"] = False
        row["model_registry_written"] = False
        row["artifact_persisted"] = False
        row["model_deployed"] = False
        row["manual_review_required"] = True
        row["phase"] = prof.current_phase
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_audit_placeholders(df)
    return df, summary


def summarize_governance_audit_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance audit placeholders."""
    return {
        "total_audit_placeholders": len(df),
        "all_dry_run_only": bool(df["dry_run_only"].all()),
        "all_real_audit_log_false": not bool(df["real_audit_log"].any()),
        "all_production_approved_false": not bool(df["production_approved"].any()),
        "all_broker_ready_approved_false": not bool(df["broker_ready_approved"].any()),
        "all_live_trading_approved_false": not bool(df["live_trading_approved"].any()),
        "all_model_registry_written_false": not bool(df["model_registry_written"].any()),
        "all_artifact_persisted_false": not bool(df["artifact_persisted"].any()),
        "all_model_deployed_false": not bool(df["model_deployed"].any()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "status": "GOVERNANCE_AUDIT_PLACEHOLDERS_READY",
    }
