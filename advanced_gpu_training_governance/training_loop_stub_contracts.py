# -*- coding: utf-8 -*-
"""Phase 139 Training Loop Stub Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)

FORBIDDEN_TRAINING_LOOP_METHODS: List[str] = [
    "fit",
    "train",
    "predict",
    "inference",
    "transform",
    "backward",
    "optimizer_step",
    "save_model",
    "write_model_registry",
    "generate_signal",
]


def build_training_loop_stub_contract_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build training loop stub contracts registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    contracts = [
        {
            "contract_id": "LOOP_STUB_001",
            "contract_name": "no_op_training_loop_contract",
            "allowed_execution": False,
            "blocked_keywords": ",".join(FORBIDDEN_TRAINING_LOOP_METHODS),
            "dry_run_only": True,
            "non_signal": True,
            "description": "Complete no-op stub contract returning immediate success without executing any iterations.",
            "status": "execution_contract_only",
        },
        {
            "contract_id": "LOOP_STUB_002",
            "contract_name": "resource_check_only_training_loop_contract",
            "allowed_execution": False,
            "blocked_keywords": ",".join(FORBIDDEN_TRAINING_LOOP_METHODS),
            "dry_run_only": True,
            "non_signal": True,
            "description": "Simulates pre-training hardware and memory checks and immediately exits.",
            "status": "execution_contract_only",
        },
        {
            "contract_id": "LOOP_STUB_003",
            "contract_name": "safety_validation_only_training_loop_contract",
            "allowed_execution": False,
            "blocked_keywords": ",".join(FORBIDDEN_TRAINING_LOOP_METHODS),
            "dry_run_only": True,
            "non_signal": True,
            "description": "Runs parameter and guard validations without invoking backward or optimization steps.",
            "status": "execution_contract_only",
        },
        {
            "contract_id": "LOOP_STUB_004",
            "contract_name": "blocked_execution_training_loop_contract",
            "allowed_execution": False,
            "blocked_keywords": ",".join(FORBIDDEN_TRAINING_LOOP_METHODS),
            "dry_run_only": True,
            "non_signal": True,
            "description": "Explicitly blocks any forward pass, gradient calculation, or weight modification.",
            "status": "execution_blocked_no_real_training",
        },
        {
            "contract_id": "LOOP_STUB_005",
            "contract_name": "phase_140_candidate_model_registry_contract",
            "allowed_execution": False,
            "blocked_keywords": ",".join(FORBIDDEN_TRAINING_LOOP_METHODS),
            "dry_run_only": True,
            "non_signal": True,
            "description": "Interface boundary contract preparing structure for Phase 140 candidate registry registration.",
            "status": "execution_contract_only",
        },
    ]

    df = pd.DataFrame(contracts)
    summary = summarize_training_loop_stub_contracts(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_training_loop_stub_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that a stub contract does not permit execution of forbidden methods."""
    violations = []
    if contract.get("allowed_execution", False):
        violations.append("allowed_execution must be False")
    if not contract.get("dry_run_only", False):
        violations.append("dry_run_only must be True")

    blocked_keywords = contract.get("blocked_keywords", "")
    if isinstance(blocked_keywords, str):
        keywords_list = [k.strip() for k in blocked_keywords.split(",") if k.strip()]
    else:
        keywords_list = list(blocked_keywords)

    for forbidden in FORBIDDEN_TRAINING_LOOP_METHODS:
        if forbidden not in keywords_list:
            violations.append(f"missing forbidden keyword: {forbidden}")

    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": len(violations) == 0,
        "violations": violations,
        "non_signal": True,
    }


def summarize_training_loop_stub_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize training loop stub contracts DataFrame."""
    if df.empty:
        return {"total_contracts": 0, "non_signal": True}
    return {
        "total_contracts": len(df),
        "all_execution_disabled": bool((df["allowed_execution"] == False).all()),
        "all_dry_run": bool((df["dry_run_only"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
