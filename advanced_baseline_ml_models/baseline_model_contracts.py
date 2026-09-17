# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Contracts Registry.

Defines formal baseline model contracts enforcing zero real training,
zero inference/predictions, zero target/label creation, and strict guard linkages.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_families import BASELINE_MODEL_FAMILIES_DATA

BASELINE_MODEL_CONTRACTS_SPEC = [
    {
        "contract_name": f"contract_{fam['family_id']}",
        "model_family": fam["family_id"],
        "dataset_contract_ref": "ds_contract_balanced_commodity_fx",
        "feature_snapshot_contract_ref": "snapshot_contract_multi_window_features",
        "experiment_registry_ref": "exp_template_baseline_benchmark_v1",
        "runtime_profile_ref": "balanced_local_gpu_ml_runtime_foundation",
        "required_no_lookahead_guard_ref": "guard_no_lookahead_timestamp_order",
        "required_metadata_only_news_guard_ref": "guard_metadata_only_news_strict",
        "required_source_preservation_guard_ref": "guard_source_preservation_immutability",
        "required_validation_dependency_ref": "val_dep_phase_137_dataset_validation",
        "required_quality_dependency_ref": "qual_dep_phase_123_quality_drift",
    }
    for fam in BASELINE_MODEL_FAMILIES_DATA
]


def build_baseline_model_contract_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build baseline model contracts DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for spec in BASELINE_MODEL_CONTRACTS_SPEC:
        rows.append({
            "contract_name": spec["contract_name"],
            "model_family": spec["model_family"],
            "dataset_contract_ref": spec["dataset_contract_ref"],
            "feature_snapshot_contract_ref": spec["feature_snapshot_contract_ref"],
            "experiment_registry_ref": spec["experiment_registry_ref"],
            "runtime_profile_ref": spec["runtime_profile_ref"],
            "required_no_lookahead_guard_ref": spec["required_no_lookahead_guard_ref"],
            "required_metadata_only_news_guard_ref": spec["required_metadata_only_news_guard_ref"],
            "required_source_preservation_guard_ref": spec["required_source_preservation_guard_ref"],
            "required_validation_dependency_ref": spec["required_validation_dependency_ref"],
            "required_quality_dependency_ref": spec["required_quality_dependency_ref"],
            "status": "baseline_contract_placeholder_only",
            "real_training_allowed": False,
            "model_fit_allowed": False,
            "model_predict_allowed": False,
            "inference_allowed": False,
            "target_label_generation_allowed": False,
            "artifact_persistence_allowed": False,
            "model_registry_write_allowed": False,
            "non_signal_required": True,
            "manual_review_required": True,
            "production_ready": False,
            "broker_ready": False,
            "official_approval": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_contracts(df)
    return df, summary


def validate_baseline_model_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a baseline model contract for safety violations."""
    violations = []
    if contract.get("real_training_allowed", False):
        violations.append("real_training_allowed must be False")
    if contract.get("model_fit_allowed", False):
        violations.append("model_fit_allowed must be False")
    if contract.get("model_predict_allowed", False):
        violations.append("model_predict_allowed must be False")
    if contract.get("inference_allowed", False):
        violations.append("inference_allowed must be False")
    if contract.get("target_label_generation_allowed", False):
        violations.append("target_label_generation_allowed must be False")
    if contract.get("artifact_persistence_allowed", False):
        violations.append("artifact_persistence_allowed must be False")
    if contract.get("model_registry_write_allowed", False):
        violations.append("model_registry_write_allowed must be False")
    if not contract.get("non_signal_required", True):
        violations.append("non_signal_required must be True")
    if not contract.get("manual_review_required", True):
        violations.append("manual_review_required must be True")

    return {
        "valid": len(violations) == 0,
        "violations": violations,
        "contract_name": contract.get("contract_name", "unknown"),
        "non_signal": True,
    }


def summarize_baseline_model_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline model contracts DataFrame."""
    return {
        "total_contracts": len(df),
        "unique_model_families": int(df["model_family"].nunique()) if not df.empty else 0,
        "all_real_training_blocked": bool((~df["real_training_allowed"]).all()) if not df.empty else True,
        "all_prediction_blocked": bool((~df["model_predict_allowed"]).all()) if not df.empty else True,
        "all_target_label_blocked": bool((~df["target_label_generation_allowed"]).all()) if not df.empty else True,
        "all_artifact_blocked": bool((~df["artifact_persistence_allowed"]).all()) if not df.empty else True,
        "all_registry_write_blocked": bool((~df["model_registry_write_allowed"]).all()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
