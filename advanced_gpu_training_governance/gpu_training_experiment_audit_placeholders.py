# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Experiment Audit Placeholders."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_experiment_audit_placeholder_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build experiment audit placeholder registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    placeholders = [
        {
            "experiment_audit_id": "EXP_AUDIT_PH_001",
            "experiment_name": "dry_run_baseline_experiment_sim",
            "model_family": "logistic_regression",
            "run_status": "CONTRACT_ONLY_NOT_EXECUTED",
            "dry_run": True,
            "real_training_executed": False,
            "real_prediction_logged": False,
            "performance_claim_included": False,
            "non_signal": True,
            "description": "Simulated experiment audit record for baseline linear family.",
            "status": "gpu_governance_ready",
        },
        {
            "experiment_audit_id": "EXP_AUDIT_PH_002",
            "experiment_name": "dry_run_gradient_boosting_experiment_sim",
            "model_family": "gradient_boosting",
            "run_status": "CONTRACT_ONLY_NOT_EXECUTED",
            "dry_run": True,
            "real_training_executed": False,
            "real_prediction_logged": False,
            "performance_claim_included": False,
            "non_signal": True,
            "description": "Simulated experiment audit record for baseline tree-based family.",
            "status": "gpu_governance_ready",
        },
        {
            "experiment_audit_id": "EXP_AUDIT_PH_003",
            "experiment_name": "dry_run_neural_network_experiment_sim",
            "model_family": "mlp_lstm_sequence",
            "run_status": "CONTRACT_ONLY_NOT_EXECUTED",
            "dry_run": True,
            "real_training_executed": False,
            "real_prediction_logged": False,
            "performance_claim_included": False,
            "non_signal": True,
            "description": "Simulated experiment audit record for deep sequence family.",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(placeholders)
    summary = summarize_gpu_training_experiment_audit_placeholders(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_experiment_audit_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize experiment audit placeholders DataFrame."""
    if df.empty:
        return {"total_placeholders": 0, "non_signal": True}
    return {
        "total_placeholders": len(df),
        "all_dry_run": bool((df["dry_run"] == True).all()),
        "all_training_disabled": bool((df["real_training_executed"] == False).all()),
        "all_performance_claims_disabled": bool((df["performance_claim_included"] == False).all()),
        "current_phase": 139,
        "non_signal": True,
    }
