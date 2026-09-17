# -*- coding: utf-8 -*-
"""Phase 140: Candidate Model Contracts Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)
from advanced_ensemble_model_registry.candidate_model_families import CANDIDATE_MODEL_FAMILIES


def build_candidate_model_contract_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build candidate model contract registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for fam in CANDIDATE_MODEL_FAMILIES:
        contract_name = f"{fam['family_id']}_contract"
        rows.append(
            {
                "contract_name": contract_name,
                "candidate_family": fam["family_id"],
                "baseline_contract_ref": fam["baseline_contract_ref"],
                "dataset_contract_ref": fam["dataset_contract_ref"],
                "feature_snapshot_contract_ref": "feature_snapshot_contract_v137",
                "experiment_registry_ref": "experiment_registry_v137",
                "gpu_resource_policy_ref": "gpu_training_resource_policy_v139",
                "required_no_lookahead_guard_ref": "ensemble_no_lookahead_guard",
                "required_metadata_only_news_guard_ref": "ensemble_metadata_only_news_guard",
                "required_source_preservation_guard_ref": "ensemble_source_preservation_guard",
                "required_validation_dependency_ref": "ensemble_validation_dependency",
                "required_quality_dependency_ref": "ensemble_quality_dependency",
                "real_training_allowed": False,
                "model_fit_allowed": False,
                "model_predict_allowed": False,
                "inference_allowed": False,
                "ensemble_execution_allowed": False,
                "calibration_allowed": False,
                "target_label_generation_allowed": False,
                "artifact_persistence_allowed": False,
                "model_registry_write_allowed": False,
                "non_signal_required": True,
                "manual_review_required": True,
                "status": "ensemble_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_candidate_model_contracts(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_candidate_model_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a candidate model contract against non-execution and non-signal rules."""
    violations = []
    if contract.get("real_training_allowed", False):
        violations.append("real_training_allowed must be False")
    if contract.get("model_fit_allowed", False):
        violations.append("model_fit_allowed must be False")
    if contract.get("model_predict_allowed", False):
        violations.append("model_predict_allowed must be False")
    if contract.get("inference_allowed", False):
        violations.append("inference_allowed must be False")
    if contract.get("ensemble_execution_allowed", False):
        violations.append("ensemble_execution_allowed must be False")
    if contract.get("calibration_allowed", False):
        violations.append("calibration_allowed must be False")
    if contract.get("target_label_generation_allowed", False):
        violations.append("target_label_generation_allowed must be False")
    if contract.get("artifact_persistence_allowed", False):
        violations.append("artifact_persistence_allowed must be False")
    if contract.get("model_registry_write_allowed", False):
        violations.append("model_registry_write_allowed must be False")
    if not contract.get("non_signal_required", True):
        violations.append("non_signal_required must be True")

    is_valid = len(violations) == 0
    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": is_valid,
        "violations": violations,
        "status": "VALID_CONTRACT" if is_valid else "INVALID_CONTRACT",
        "non_signal": True,
        "manual_review_required": True,
    }


def summarize_candidate_model_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize candidate model contracts DataFrame."""
    if df.empty:
        return {
            "total_contracts": 0,
            "all_training_disabled": True,
            "all_prediction_disabled": True,
            "all_non_signal_required": True,
            "all_manual_review_required": True,
        }
    return {
        "total_contracts": len(df),
        "all_training_disabled": not bool(df["real_training_allowed"].any()),
        "all_prediction_disabled": not bool(df["model_predict_allowed"].any()),
        "all_ensemble_disabled": not bool(df["ensemble_execution_allowed"].any()),
        "all_non_signal_required": bool(df["non_signal_required"].all()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_candidate_model_contracts(contracts: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate candidate model contracts."""
    if isinstance(contracts, tuple):
        df = contracts[0]
    elif isinstance(contracts, pd.DataFrame):
        df = contracts
    elif isinstance(contracts, dict):
        return all(validate_candidate_model_contract(c).get("is_valid", False) for c in contracts.values())
    else:
        return False
    if df.empty:
        return False
    if df["real_training_allowed"].any() or df["model_predict_allowed"].any() or df["ensemble_execution_allowed"].any():
        return False
    if not df["non_signal_required"].all():
        return False
    return True


build_candidate_model_contracts = build_candidate_model_contract_registry

