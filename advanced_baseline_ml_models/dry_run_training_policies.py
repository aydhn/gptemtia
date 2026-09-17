# -*- coding: utf-8 -*-
"""Phase 138 Dry-Run Training Policies Registry and Request Validator.

Enforces strict non-execution policies on any incoming training requests.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

DRY_RUN_POLICIES = [
    {"policy_id": "policy_zero_real_training", "policy_name": "Zero Real Training Enforcement", "enforced": True, "description": "Blocks actual model training on real/market data"},
    {"policy_id": "policy_zero_model_fit", "policy_name": "Zero Model Fit Enforcement", "enforced": True, "description": "Blocks calling .fit() or optimizer loops"},
    {"policy_id": "policy_zero_prediction", "policy_name": "Zero Prediction Enforcement", "enforced": True, "description": "Blocks calling .predict() or generating directional signals"},
    {"policy_id": "policy_zero_target_label", "policy_name": "Zero Target/Label Generation", "enforced": True, "description": "Blocks computing target labels or future returns"},
    {"policy_id": "policy_zero_artifact_persistence", "policy_name": "Zero Artifact Persistence", "enforced": True, "description": "Blocks saving model weights or pickles"},
    {"policy_id": "policy_zero_registry_write", "policy_name": "Zero Model Registry Write", "enforced": True, "description": "Blocks writing to model registries or MLflow"},
]


def build_dry_run_training_policy_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dry-run training policy registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for p in DRY_RUN_POLICIES:
        rows.append({
            "policy_id": p["policy_id"],
            "policy_name": p["policy_name"],
            "enforced": p["enforced"],
            "description": p["description"],
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_dry_run_training_policies(df)
    return df, summary


def validate_dry_run_training_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate incoming training request and reject real training/fit attempts."""
    violations = []
    request_str = str(request).lower()

    forbidden_triggers = [
        "fit", "train", "predict", "inference", "transform",
        "materialize", "save_model", "pickle", "joblib.dump",
        "model_registry", "mlflow", "target", "label", "future_return",
        "forward_return", "next_return", "signal", "buy", "sell",
        "long", "short", "backtest", "optimize",
    ]

    for trigger in forbidden_triggers:
        if trigger in request_str:
            violations.append(f"Forbidden trigger detected: '{trigger}'")

    is_blocked = len(violations) > 0
    return {
        "blocked": is_blocked,
        "violations": violations,
        "status": "execution_blocked_by_safety" if is_blocked else "dry_run_contract_validated",
        "real_training_executed": False,
        "model_fit_executed": False,
        "model_predict_executed": False,
        "target_label_generated": False,
        "artifact_persisted": False,
        "manual_review_required": True,
        "non_signal": True,
    }


def summarize_dry_run_training_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize policy registry."""
    return {
        "total_policies": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
