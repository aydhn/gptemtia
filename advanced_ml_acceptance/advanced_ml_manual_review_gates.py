# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Manual Review Gate Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    MANUAL_REVIEW_GATE_DOMAIN,
    ACCEPTANCE_MANUAL_REVIEW_REQUIRED,
)

MANUAL_REVIEW_GATES: List[Dict[str, Any]] = [
    {"gate_id": "MRG-136", "phase_ref": "Phase 136", "topic": "phase_136_runtime_review_gate", "requirement": "Inspect hardware discovery outputs and accelerator memory constraints.", "status": "PENDING_REVIEW"},
    {"gate_id": "MRG-137", "phase_ref": "Phase 137", "topic": "phase_137_dataset_contract_review_gate", "requirement": "Audit dataset schemas, experiment run plans, and feature namespaces.", "status": "PENDING_REVIEW"},
    {"gate_id": "MRG-138", "phase_ref": "Phase 138", "topic": "phase_138_baseline_contract_review_gate", "requirement": "Review baseline model family contracts and dry-run harness specifications.", "status": "PENDING_REVIEW"},
    {"gate_id": "MRG-139", "phase_ref": "Phase 139", "topic": "phase_139_resource_governance_review_gate", "requirement": "Verify device memory limits, timeout guards, and execution block rules.", "status": "PENDING_REVIEW"},
    {"gate_id": "MRG-140", "phase_ref": "Phase 140", "topic": "phase_140_ensemble_contract_review_gate", "requirement": "Inspect ensemble candidate models, eligibility gates, and weighting contracts.", "status": "PENDING_REVIEW"},
    {"gate_id": "MRG-141", "phase_ref": "Phase 141", "topic": "phase_141_calibration_uncertainty_review_gate", "requirement": "Review calibration scaling curves and uncertainty quantile intervals.", "status": "PENDING_REVIEW"},
    {"gate_id": "MRG-142", "phase_ref": "Phase 142", "topic": "phase_142_drift_monitoring_review_gate", "requirement": "Audit drift metrics, reference window sizes, and statistical thresholds.", "status": "PENDING_REVIEW"},
    {"gate_id": "MRG-143", "phase_ref": "Phase 143", "topic": "phase_143_explainability_review_gate", "requirement": "Verify SHAP/LIME explanation contracts and feature attribution schemas.", "status": "PENDING_REVIEW"},
    {"gate_id": "MRG-144", "phase_ref": "Phase 144", "topic": "phase_144_governance_model_card_review_gate", "requirement": "Examine model cards, risk registers, and approval boundary documentation.", "status": "PENDING_REVIEW"},
    {"gate_id": "MRG-146", "phase_ref": "Phase 146", "topic": "phase_146_backtest_boundary_review_gate", "requirement": "Validate transaction cost, slippage, and non-live backtest boundaries prior to Phase 146.", "status": "PENDING_REVIEW"},
]


def build_advanced_ml_manual_review_gate_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for manual review gates."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for g in MANUAL_REVIEW_GATES:
        row = dict(g)
        row["current_phase"] = active.current_phase
        row["target_final_phase"] = active.target_final_phase
        row["next_phase"] = active.next_phase
        row["manual_review_required"] = True
        row["status_label"] = ACCEPTANCE_MANUAL_REVIEW_REQUIRED
        row["non_signal"] = True
        row["production_ready"] = False
        row["broker_ready"] = False
        records.append(row)

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": MANUAL_REVIEW_GATE_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_gates": len(df),
        "pending_review_count": len(df),
        "manual_review_required": True,
        "non_signal": True,
        "status": "QUEUED",
    }
    return df, summary


def summarize_advanced_ml_manual_review_gates(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review gates DataFrame."""
    return {
        "gate_count": len(df),
        "gates": df["topic"].tolist() if not df.empty and "topic" in df.columns else [],
        "manual_review_required": True,
        "non_signal": True,
    }
