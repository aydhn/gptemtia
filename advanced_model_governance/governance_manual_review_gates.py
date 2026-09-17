# -*- coding: utf-8 -*-
"""Phase 144: Governance Manual Review Gates Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

MANUAL_REVIEW_GATE_DEFINITIONS: List[Dict[str, str]] = [
    {"gate_id": "GATE-01", "gate_name": "dataset_contract_review_gate", "scope": "Phase 137 ML Dataset Contracts", "criterion": "Verify time index integrity, purged splits, and absence of target labels."},
    {"gate_id": "GATE-02", "gate_name": "baseline_model_contract_review_gate", "scope": "Phase 138 Baseline Model Contracts", "criterion": "Ensure baseline models are dry-run interface stubs with no trained weights."},
    {"gate_id": "GATE-03", "gate_name": "ensemble_contract_review_gate", "scope": "Phase 140 Ensemble Model Contracts", "criterion": "Verify candidate eligibility and confirm ensemble weights are non-materialized."},
    {"gate_id": "GATE-04", "gate_name": "calibration_uncertainty_review_gate", "scope": "Phase 141 Calibration & Uncertainty", "criterion": "Check calibration curves and guarantee uncertainty outputs are non-signal."},
    {"gate_id": "GATE-05", "gate_name": "drift_monitoring_review_gate", "scope": "Phase 142 Drift Monitoring", "criterion": "Validate statistical drift thresholds and linkage to FeatureStore."},
    {"gate_id": "GATE-06", "gate_name": "explainability_review_gate", "scope": "Phase 143 Explainability & Attribution", "criterion": "Ensure XAI stability contracts and zero automated model action policies."},
    {"gate_id": "GATE-07", "gate_name": "model_card_review_gate", "scope": "Phase 144 Model Cards", "criterion": "Audit limitations, intended use, prohibited use, and risk disclosures."},
    {"gate_id": "GATE-08", "gate_name": "audit_placeholder_review_gate", "scope": "Phase 144 Audit Trail", "criterion": "Confirm audit trail items are marked dry_run_only and non-production."},
    {"gate_id": "GATE-09", "gate_name": "release_boundary_review_gate", "scope": "Phase 144 Release Boundaries", "criterion": "Confirm 100% block on production deployment and live trading."},
]


def build_governance_manual_review_gate_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance manual review gates."""
    prof = profile or get_model_governance_profile()
    records = []
    for g in MANUAL_REVIEW_GATE_DEFINITIONS:
        row = dict(g)
        row["requires_signoff"] = True
        row["status"] = "REVIEW_PENDING"
        row["phase"] = prof.current_phase
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_manual_review_gates(df)
    return df, summary


def summarize_governance_manual_review_gates(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance manual review gates."""
    return {
        "total_gates": len(df),
        "all_require_signoff": bool(df["requires_signoff"].all()),
        "status": "ALL_GATES_ENFORCED",
    }
