# -*- coding: utf-8 -*-
"""Phase 144: Model Governance Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

GOVERNANCE_CONTRACT_SPECS: List[Dict[str, Any]] = [
    {
        "contract_name": "baseline_model_governance_contract",
        "governance_family": "baseline_ml",
        "dataset_contract_ref": "phase_137_dataset_contracts",
        "baseline_model_ref": "phase_138_baseline_contracts",
        "candidate_model_ref": "none",
        "ensemble_ref": "none",
        "calibration_uncertainty_ref": "none",
        "drift_monitoring_ref": "phase_142_feature_drift_linkage",
        "explainability_ref": "phase_143_feature_attribution_contracts",
        "model_card_ref": "baseline_model_card_contract",
        "audit_trail_ref": "baseline_audit_trail_placeholder",
        "approval_boundary_ref": "production_approval_blocked_boundary",
        "required_no_lookahead_guard_ref": "governance_no_lookahead_guard",
        "required_metadata_only_news_guard_ref": "governance_metadata_only_news_guard",
        "required_source_preservation_guard_ref": "governance_source_preservation_guard",
    },
    {
        "contract_name": "candidate_model_governance_contract",
        "governance_family": "candidate_ml",
        "dataset_contract_ref": "phase_137_dataset_contracts",
        "baseline_model_ref": "phase_138_baseline_contracts",
        "candidate_model_ref": "phase_140_candidate_model_contracts",
        "ensemble_ref": "none",
        "calibration_uncertainty_ref": "phase_141_calibration_contracts",
        "drift_monitoring_ref": "phase_142_model_drift_monitoring_contracts",
        "explainability_ref": "phase_143_explainability_report_contracts",
        "model_card_ref": "candidate_model_card_contract",
        "audit_trail_ref": "candidate_audit_trail_placeholder",
        "approval_boundary_ref": "production_approval_blocked_boundary",
        "required_no_lookahead_guard_ref": "governance_no_lookahead_guard",
        "required_metadata_only_news_guard_ref": "governance_metadata_only_news_guard",
        "required_source_preservation_guard_ref": "governance_source_preservation_guard",
    },
    {
        "contract_name": "ensemble_model_governance_contract",
        "governance_family": "ensemble_ml",
        "dataset_contract_ref": "phase_137_dataset_contracts",
        "baseline_model_ref": "phase_138_baseline_contracts",
        "candidate_model_ref": "phase_140_candidate_model_contracts",
        "ensemble_ref": "phase_140_ensemble_strategy_contracts",
        "calibration_uncertainty_ref": "phase_141_uncertainty_estimation_contracts",
        "drift_monitoring_ref": "phase_142_uncertainty_drift_contracts",
        "explainability_ref": "phase_143_explainability_report_contracts",
        "model_card_ref": "ensemble_model_card_contract",
        "audit_trail_ref": "ensemble_audit_trail_placeholder",
        "approval_boundary_ref": "production_approval_blocked_boundary",
        "required_no_lookahead_guard_ref": "governance_no_lookahead_guard",
        "required_metadata_only_news_guard_ref": "governance_metadata_only_news_guard",
        "required_source_preservation_guard_ref": "governance_source_preservation_guard",
    },
    {
        "contract_name": "calibration_uncertainty_governance_contract",
        "governance_family": "calibration_uncertainty",
        "dataset_contract_ref": "phase_137_dataset_contracts",
        "baseline_model_ref": "phase_138_baseline_contracts",
        "candidate_model_ref": "phase_140_candidate_model_contracts",
        "ensemble_ref": "phase_140_ensemble_strategy_contracts",
        "calibration_uncertainty_ref": "phase_141_calibration_contracts",
        "drift_monitoring_ref": "phase_142_uncertainty_drift_contracts",
        "explainability_ref": "phase_143_explainability_report_contracts",
        "model_card_ref": "calibration_uncertainty_model_card_contract",
        "audit_trail_ref": "calibration_audit_trail_placeholder",
        "approval_boundary_ref": "production_approval_blocked_boundary",
        "required_no_lookahead_guard_ref": "governance_no_lookahead_guard",
        "required_metadata_only_news_guard_ref": "governance_metadata_only_news_guard",
        "required_source_preservation_guard_ref": "governance_source_preservation_guard",
    },
    {
        "contract_name": "drift_monitoring_governance_contract",
        "governance_family": "drift_monitoring",
        "dataset_contract_ref": "phase_137_dataset_contracts",
        "baseline_model_ref": "phase_138_baseline_contracts",
        "candidate_model_ref": "phase_140_candidate_model_contracts",
        "ensemble_ref": "phase_140_ensemble_strategy_contracts",
        "calibration_uncertainty_ref": "phase_141_calibration_contracts",
        "drift_monitoring_ref": "phase_142_model_drift_monitoring_contracts",
        "explainability_ref": "phase_143_explainability_report_contracts",
        "model_card_ref": "drift_monitoring_model_card_contract",
        "audit_trail_ref": "drift_audit_trail_placeholder",
        "approval_boundary_ref": "production_approval_blocked_boundary",
        "required_no_lookahead_guard_ref": "governance_no_lookahead_guard",
        "required_metadata_only_news_guard_ref": "governance_metadata_only_news_guard",
        "required_source_preservation_guard_ref": "governance_source_preservation_guard",
    },
    {
        "contract_name": "explainability_governance_contract",
        "governance_family": "explainability_attribution",
        "dataset_contract_ref": "phase_137_dataset_contracts",
        "baseline_model_ref": "phase_138_baseline_contracts",
        "candidate_model_ref": "phase_140_candidate_model_contracts",
        "ensemble_ref": "phase_140_ensemble_strategy_contracts",
        "calibration_uncertainty_ref": "phase_141_calibration_contracts",
        "drift_monitoring_ref": "phase_142_model_drift_monitoring_contracts",
        "explainability_ref": "phase_143_explainability_report_contracts",
        "model_card_ref": "explainability_model_card_contract",
        "audit_trail_ref": "explainability_audit_trail_placeholder",
        "approval_boundary_ref": "production_approval_blocked_boundary",
        "required_no_lookahead_guard_ref": "governance_no_lookahead_guard",
        "required_metadata_only_news_guard_ref": "governance_metadata_only_news_guard",
        "required_source_preservation_guard_ref": "governance_source_preservation_guard",
    },
    {
        "contract_name": "advanced_ml_acceptance_governance_contract",
        "governance_family": "advanced_ml_acceptance",
        "dataset_contract_ref": "phase_137_dataset_contracts",
        "baseline_model_ref": "phase_138_baseline_contracts",
        "candidate_model_ref": "phase_140_candidate_model_contracts",
        "ensemble_ref": "phase_140_ensemble_strategy_contracts",
        "calibration_uncertainty_ref": "phase_141_calibration_contracts",
        "drift_monitoring_ref": "phase_142_model_drift_monitoring_contracts",
        "explainability_ref": "phase_143_explainability_report_contracts",
        "model_card_ref": "advanced_ml_acceptance_model_card_contract",
        "audit_trail_ref": "acceptance_audit_trail_placeholder",
        "approval_boundary_ref": "production_approval_blocked_boundary",
        "required_no_lookahead_guard_ref": "governance_no_lookahead_guard",
        "required_metadata_only_news_guard_ref": "governance_metadata_only_news_guard",
        "required_source_preservation_guard_ref": "governance_source_preservation_guard",
    },
]


def build_model_governance_contract_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model governance contracts."""
    prof = profile or get_model_governance_profile()
    records = []
    for spec in GOVERNANCE_CONTRACT_SPECS:
        row = dict(spec)
        row["production_approval_allowed"] = prof.allow_production_approval
        row["broker_ready_approval_allowed"] = prof.allow_broker_ready_approval
        row["live_trading_approval_allowed"] = prof.allow_live_trading_approval
        row["deployment_allowed"] = prof.allow_model_deployment
        row["model_registry_write_allowed"] = prof.allow_model_registry_write
        row["artifact_persistence_allowed"] = prof.allow_artifact_persistence
        row["signal_generation_allowed"] = prof.allow_signal_generation
        row["non_signal_required"] = True
        row["manual_review_required"] = True
        row["phase"] = prof.current_phase
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_governance_contracts(df)
    return df, summary


def summarize_model_governance_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model governance contracts."""
    return {
        "total_contracts": len(df),
        "all_production_approval_blocked": not bool(df["production_approval_allowed"].any()),
        "all_deployment_blocked": not bool(df["deployment_allowed"].any()),
        "all_model_registry_write_blocked": not bool(df["model_registry_write_allowed"].any()),
        "all_signal_generation_blocked": not bool(df["signal_generation_allowed"].any()),
        "all_non_signal_required": bool(df["non_signal_required"].all()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
    }


def validate_model_governance_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a governance contract against safety invariants."""
    is_valid = True
    reasons = []

    if contract.get("production_approval_allowed", False):
        is_valid = False
        reasons.append("production_approval_allowed must be False")
    if contract.get("deployment_allowed", False):
        is_valid = False
        reasons.append("deployment_allowed must be False")
    if contract.get("model_registry_write_allowed", False):
        is_valid = False
        reasons.append("model_registry_write_allowed must be False")
    if contract.get("signal_generation_allowed", False):
        is_valid = False
        reasons.append("signal_generation_allowed must be False")
    if not contract.get("non_signal_required", True):
        is_valid = False
        reasons.append("non_signal_required must be True")

    return {
        "is_valid": is_valid,
        "contract_name": contract.get("contract_name", "unknown"),
        "reasons": reasons,
        "status": "VALID" if is_valid else "INVALID",
    }
