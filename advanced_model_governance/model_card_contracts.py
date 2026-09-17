# -*- coding: utf-8 -*-
"""Phase 144: Model Card Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

MODEL_CARD_CONTRACT_TYPES: List[Dict[str, str]] = [
    {
        "contract_name": "baseline_model_card_contract",
        "model_family": "baseline_models",
        "template_ref": "baseline_template",
        "limitations_ref": "baseline_limitations",
        "intended_use_ref": "research_only_intended_use",
        "prohibited_use_ref": "live_trading_prohibited_use",
        "risk_disclosure_ref": "baseline_risk_disclosure",
        "validation_evidence_ref": "baseline_validation_evidence",
        "data_dependency_ref": "ml_dataset_data_dependency",
        "feature_dependency_ref": "feature_store_dependency",
        "model_dependency_ref": "baseline_model_dependency",
        "runtime_dependency_ref": "cpu_runtime_dependency",
    },
    {
        "contract_name": "candidate_model_card_contract",
        "model_family": "candidate_models",
        "template_ref": "candidate_template",
        "limitations_ref": "candidate_limitations",
        "intended_use_ref": "research_only_intended_use",
        "prohibited_use_ref": "live_trading_prohibited_use",
        "risk_disclosure_ref": "candidate_risk_disclosure",
        "validation_evidence_ref": "candidate_validation_evidence",
        "data_dependency_ref": "ml_dataset_data_dependency",
        "feature_dependency_ref": "feature_store_dependency",
        "model_dependency_ref": "candidate_model_dependency",
        "runtime_dependency_ref": "gpu_runtime_dependency",
    },
    {
        "contract_name": "ensemble_model_card_contract",
        "model_family": "ensemble_models",
        "template_ref": "ensemble_template",
        "limitations_ref": "ensemble_limitations",
        "intended_use_ref": "research_only_intended_use",
        "prohibited_use_ref": "live_trading_prohibited_use",
        "risk_disclosure_ref": "ensemble_risk_disclosure",
        "validation_evidence_ref": "ensemble_validation_evidence",
        "data_dependency_ref": "ml_dataset_data_dependency",
        "feature_dependency_ref": "feature_store_dependency",
        "model_dependency_ref": "ensemble_model_dependency",
        "runtime_dependency_ref": "gpu_runtime_dependency",
    },
    {
        "contract_name": "calibration_uncertainty_model_card_contract",
        "model_family": "calibration_uncertainty",
        "template_ref": "calibration_template",
        "limitations_ref": "calibration_limitations",
        "intended_use_ref": "research_only_intended_use",
        "prohibited_use_ref": "live_trading_prohibited_use",
        "risk_disclosure_ref": "calibration_risk_disclosure",
        "validation_evidence_ref": "calibration_validation_evidence",
        "data_dependency_ref": "ml_dataset_data_dependency",
        "feature_dependency_ref": "feature_store_dependency",
        "model_dependency_ref": "calibration_dependency",
        "runtime_dependency_ref": "cpu_gpu_runtime_dependency",
    },
    {
        "contract_name": "drift_monitoring_model_card_contract",
        "model_family": "drift_monitoring",
        "template_ref": "drift_template",
        "limitations_ref": "drift_limitations",
        "intended_use_ref": "research_only_intended_use",
        "prohibited_use_ref": "live_trading_prohibited_use",
        "risk_disclosure_ref": "drift_risk_disclosure",
        "validation_evidence_ref": "drift_validation_evidence",
        "data_dependency_ref": "ml_dataset_data_dependency",
        "feature_dependency_ref": "feature_store_dependency",
        "model_dependency_ref": "drift_dependency",
        "runtime_dependency_ref": "cpu_runtime_dependency",
    },
    {
        "contract_name": "explainability_model_card_contract",
        "model_family": "explainability_attribution",
        "template_ref": "explainability_template",
        "limitations_ref": "explainability_limitations",
        "intended_use_ref": "research_only_intended_use",
        "prohibited_use_ref": "live_trading_prohibited_use",
        "risk_disclosure_ref": "explainability_risk_disclosure",
        "validation_evidence_ref": "explainability_validation_evidence",
        "data_dependency_ref": "ml_dataset_data_dependency",
        "feature_dependency_ref": "feature_store_dependency",
        "model_dependency_ref": "explainability_dependency",
        "runtime_dependency_ref": "cpu_gpu_runtime_dependency",
    },
    {
        "contract_name": "advanced_ml_acceptance_model_card_contract",
        "model_family": "advanced_ml_acceptance",
        "template_ref": "acceptance_template",
        "limitations_ref": "acceptance_limitations",
        "intended_use_ref": "research_only_intended_use",
        "prohibited_use_ref": "live_trading_prohibited_use",
        "risk_disclosure_ref": "acceptance_risk_disclosure",
        "validation_evidence_ref": "acceptance_validation_evidence",
        "data_dependency_ref": "ml_dataset_data_dependency",
        "feature_dependency_ref": "feature_store_dependency",
        "model_dependency_ref": "all_ml_components_dependency",
        "runtime_dependency_ref": "runtime_foundation_dependency",
    },
]


def build_model_card_contract_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card contracts."""
    prof = profile or get_model_governance_profile()
    records = []
    for spec in MODEL_CARD_CONTRACT_TYPES:
        row = dict(spec)
        row["production_ready_claim"] = prof.allow_production_ready_claim
        row["broker_ready_claim"] = prof.allow_broker_ready_claim
        row["official_approval_claim"] = prof.allow_official_approval_claim
        row["signal_claim"] = prof.allow_signal_generation
        row["non_signal_required"] = True
        row["manual_review_required"] = True
        row["phase"] = prof.current_phase
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_card_contracts(df)
    return df, summary


def summarize_model_card_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card contracts."""
    return {
        "total_contracts": len(df),
        "all_production_ready_claims_false": not bool(df["production_ready_claim"].any()),
        "all_broker_ready_claims_false": not bool(df["broker_ready_claim"].any()),
        "all_official_approval_claims_false": not bool(df["official_approval_claim"].any()),
        "all_non_signal_required": bool(df["non_signal_required"].all()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
    }


def validate_model_card_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate model card contract claims."""
    is_valid = True
    reasons = []

    if contract.get("production_ready_claim", False):
        is_valid = False
        reasons.append("production_ready_claim must be False")
    if contract.get("broker_ready_claim", False):
        is_valid = False
        reasons.append("broker_ready_claim must be False")
    if contract.get("official_approval_claim", False):
        is_valid = False
        reasons.append("official_approval_claim must be False")
    if contract.get("signal_claim", False):
        is_valid = False
        reasons.append("signal_claim must be False")

    return {
        "is_valid": is_valid,
        "contract_name": contract.get("contract_name", "unknown"),
        "reasons": reasons,
        "status": "VALID" if is_valid else "INVALID",
    }
