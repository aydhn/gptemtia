# -*- coding: utf-8 -*-
"""Phase 144: Model Card Validation Evidence Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

VALIDATION_EVIDENCE_ITEMS: List[Dict[str, Any]] = [
    {"evidence_id": "EVD-136", "source_phase": 136, "component": "GPU ML Runtime Foundation", "evidence_type": "device_enumeration_contract", "status": "VERIFIED"},
    {"evidence_id": "EVD-137", "source_phase": 137, "component": "ML Dataset Contracts", "evidence_type": "schema_and_leakage_guards", "status": "VERIFIED"},
    {"evidence_id": "EVD-138", "source_phase": 138, "component": "Baseline ML Model Contracts", "evidence_type": "interface_stubs_and_disabled_execution", "status": "VERIFIED"},
    {"evidence_id": "EVD-139", "source_phase": 139, "component": "GPU Resource Governance", "evidence_type": "memory_budget_and_timeout_policies", "status": "VERIFIED"},
    {"evidence_id": "EVD-140", "source_phase": 140, "component": "Ensemble & Candidate Registry", "evidence_type": "strategy_contracts_and_eligibility_gates", "status": "VERIFIED"},
    {"evidence_id": "EVD-141", "source_phase": 141, "component": "Calibration & Uncertainty Contracts", "evidence_type": "calibration_curves_and_conformal_stubs", "status": "VERIFIED"},
    {"evidence_id": "EVD-142", "source_phase": 142, "component": "Model Drift Monitoring", "evidence_type": "statistical_test_contracts_and_linkage", "status": "VERIFIED"},
    {"evidence_id": "EVD-143", "source_phase": 143, "component": "Explainability & Attribution", "evidence_type": "xai_report_contracts_and_stability_stubs", "status": "VERIFIED"},
]


def build_model_card_validation_evidence_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card validation evidence."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in VALIDATION_EVIDENCE_ITEMS:
        row = dict(item)
        row["current_phase"] = prof.current_phase
        row["is_valid"] = True
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_card_validation_evidence(df)
    return df, summary


def summarize_model_card_validation_evidence(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card validation evidence."""
    return {
        "total_evidence_items": len(df),
        "all_verified": bool((df["status"] == "VERIFIED").all()),
        "covered_phases": sorted(list(df["source_phase"].unique())),
        "non_signal": bool(df["non_signal"].all()),
    }
