import pandas as pd
from typing import Dict, List, Tuple, Union
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

PERMISSION_BLOCKED_KEYWORDS = [
    "fit", "train", "predict", "inference", "transform",
    "materialize", "save_model", "model_registry",
    "target", "label", "future_return", "forward_return", "next_return",
    "signal", "buy", "sell", "long", "short",
    "backtest", "optimize",
]

_PERMISSIONS = [
    {"permission_name": "create_experiment_metadata_allowed", "description": "Creating experiment metadata is allowed.", "allowed": True},
    {"permission_name": "create_dataset_contract_reference_allowed", "description": "Creating dataset contract reference is allowed.", "allowed": True},
    {"permission_name": "create_feature_snapshot_contract_reference_allowed", "description": "Creating feature snapshot contract reference is allowed.", "allowed": True},
    {"permission_name": "create_run_plan_placeholder_allowed", "description": "Creating run plan placeholder is allowed.", "allowed": True},
    {"permission_name": "create_safety_governance_report_allowed", "description": "Creating safety/governance report is allowed.", "allowed": True},
    {"permission_name": "materialize_dataset_blocked", "description": "Materializing dataset is blocked.", "allowed": False},
    {"permission_name": "create_target_label_blocked", "description": "Creating target label is blocked.", "allowed": False},
    {"permission_name": "fit_model_blocked", "description": "Fitting model is blocked.", "allowed": False},
    {"permission_name": "train_model_blocked", "description": "Training model is blocked.", "allowed": False},
    {"permission_name": "predict_blocked", "description": "Prediction is blocked.", "allowed": False},
    {"permission_name": "persist_artifact_blocked", "description": "Persisting artifact is blocked.", "allowed": False},
    {"permission_name": "write_model_registry_blocked", "description": "Writing model registry is blocked.", "allowed": False},
    {"permission_name": "run_backtest_blocked", "description": "Running backtest is blocked.", "allowed": False},
    {"permission_name": "generate_signal_blocked", "description": "Generating signal is blocked.", "allowed": False},
]

def build_ml_experiment_permission_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for p in _PERMISSIONS:
        rows.append({
            "permission_name": p["permission_name"],
            "description": p["description"],
            "allowed": p["allowed"],
            "non_signal": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_permissions": len(rows),
        "current_phase": 137,
        "training_blocked": True,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary

def validate_ml_experiment_permission_request(request: Union[Dict, str]) -> Dict:
    text = str(request).lower()
    issues = []
    for kw in PERMISSION_BLOCKED_KEYWORDS:
        if kw in text:
            issues.append(f"Blocked keyword detected in request: {kw}")
    return {"valid": len(issues) == 0, "issues": issues, "non_signal": True}

def summarize_ml_experiment_permissions(df: pd.DataFrame) -> Dict:
    return {
        "total_permissions": len(df),
        "current_phase": 137,
        "training_blocked": True,
        "non_signal": True,
        "status": "READY",
    }
