# -*- coding: utf-8 -*-
"""Phase 138 Dry-Run Training Harness Contracts Registry.

Defines the contract rules for the dry-run training harness.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

DRY_RUN_HARNESS_SPECIFICATIONS = [
    {
        "harness_id": "harness_contract_standard_linear",
        "harness_name": "Standard Linear Baseline Dry-Run Harness",
        "target_family_group": "linear_models",
        "simulation_mode": "no_op_dry_run",
        "allowed_mode": "contract_only",
    },
    {
        "harness_id": "harness_contract_tree_ensemble",
        "harness_name": "Tree Ensemble Baseline Dry-Run Harness",
        "target_family_group": "tree_ensembles",
        "simulation_mode": "no_op_dry_run",
        "allowed_mode": "contract_only",
    },
    {
        "harness_id": "harness_contract_gradient_boosting",
        "harness_name": "Gradient Boosting Baseline Dry-Run Harness",
        "target_family_group": "gradient_boosting",
        "simulation_mode": "no_op_dry_run",
        "allowed_mode": "contract_only",
    },
    {
        "harness_id": "harness_contract_neural_baseline",
        "harness_name": "Neural Baseline Dry-Run Harness",
        "target_family_group": "neural_networks",
        "simulation_mode": "no_op_dry_run",
        "allowed_mode": "contract_only",
    },
    {
        "harness_id": "harness_contract_unsupervised_baseline",
        "harness_name": "Unsupervised Baseline Dry-Run Harness",
        "target_family_group": "unsupervised",
        "simulation_mode": "no_op_dry_run",
        "allowed_mode": "contract_only",
    },
]

DRY_RUN_HARNESS_CONTRACTS_DATA = DRY_RUN_HARNESS_SPECIFICATIONS


def build_dry_run_training_harness_contract_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dry-run training harness contract registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for item in DRY_RUN_HARNESS_SPECIFICATIONS:
        rows.append({
            "harness_id": item["harness_id"],
            "harness_name": item["harness_name"],
            "target_family_group": item["target_family_group"],
            "allowed_mode": item["allowed_mode"],
            "simulation_mode": item["simulation_mode"],
            "real_training_allowed": False,
            "model_fit_allowed": False,
            "model_predict_allowed": False,
            "artifact_persistence_allowed": False,
            "model_registry_write_allowed": False,
            "manual_review_required": True,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_dry_run_training_harness_contracts(df)
    return df, summary


def validate_dry_run_training_harness_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a harness contract for zero-training safety."""
    violations = []
    if contract.get("real_training_allowed", False):
        violations.append("real_training_allowed must be False")
    if contract.get("model_fit_allowed", False):
        violations.append("model_fit_allowed must be False")
    if contract.get("model_predict_allowed", False):
        violations.append("model_predict_allowed must be False")
    if contract.get("artifact_persistence_allowed", False):
        violations.append("artifact_persistence_allowed must be False")
    if contract.get("model_registry_write_allowed", False):
        violations.append("model_registry_write_allowed must be False")
    if contract.get("allowed_mode") != "contract_only":
        violations.append("allowed_mode must be contract_only")

    return {
        "valid": len(violations) == 0,
        "violations": violations,
        "harness_id": contract.get("harness_id", "unknown"),
        "non_signal": True,
    }


def summarize_dry_run_training_harness_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize harness contracts."""
    return {
        "total_harness_contracts": len(df),
        "all_real_training_blocked": bool((~df["real_training_allowed"]).all()) if not df.empty else True,
        "all_model_fit_blocked": bool((~df["model_fit_allowed"]).all()) if not df.empty else True,
        "all_predict_blocked": bool((~df["model_predict_allowed"]).all()) if not df.empty else True,
        "all_artifact_blocked": bool((~df["artifact_persistence_allowed"]).all()) if not df.empty else True,
        "all_registry_write_blocked": bool((~df["model_registry_write_allowed"]).all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
