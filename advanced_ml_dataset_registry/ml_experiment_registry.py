import pandas as pd
from typing import Dict, List, Tuple, Union
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_EXPERIMENTS = [
    {"experiment_key": "baseline_model_contract_experiment_placeholder", "experiment_family": "baseline_model_contract_experiment_placeholder"},
    {"experiment_key": "regime_metadata_model_input_experiment_placeholder", "experiment_family": "regime_metadata_model_input_experiment_placeholder"},
    {"experiment_key": "featurestore_model_input_experiment_placeholder", "experiment_family": "featurestore_model_input_experiment_placeholder"},
    {"experiment_key": "cross_asset_feature_input_experiment_placeholder", "experiment_family": "cross_asset_feature_input_experiment_placeholder"},
    {"experiment_key": "macro_event_news_metadata_input_experiment_placeholder", "experiment_family": "macro_event_news_metadata_input_experiment_placeholder"},
    {"experiment_key": "phase_138_dry_run_harness_experiment_placeholder", "experiment_family": "phase_138_dry_run_harness_experiment_placeholder"},
]

def build_ml_experiment_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for e in _EXPERIMENTS:
        rows.append({
            "experiment_key": e["experiment_key"],
            "experiment_family": e["experiment_family"],
            "no_training_required": True,
            "no_prediction_required": True,
            "target_label_forbidden": True,
            "artifact_persistence_allowed": False,
            "model_registry_write_allowed": False,
            "manual_review_required": True,
            "non_signal": True,
            "status": "experiment_training_blocked",
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_experiments": len(rows),
        "current_phase": 137,
        "non_signal": True,
        "training_blocked": True,
        "prediction_blocked": True,
        "artifact_persistence_blocked": True,
        "status": "READY",
    }
    return df, summary

def validate_ml_experiment_registry_item(item: Dict) -> Dict:
    issues = []
    if not item.get("no_training_required", True):
        issues.append("no_training_required must be True")
    if not item.get("no_prediction_required", True):
        issues.append("no_prediction_required must be True")
    if not item.get("target_label_forbidden", True):
        issues.append("target_label_forbidden must be True")
    if item.get("artifact_persistence_allowed", False):
        issues.append("artifact_persistence_allowed must be False")
    if item.get("model_registry_write_allowed", False):
        issues.append("model_registry_write_allowed must be False")
    return {"valid": len(issues) == 0, "issues": issues, "non_signal": True}

def summarize_ml_experiment_registry(df: pd.DataFrame) -> Dict:
    return {
        "total_experiments": len(df),
        "current_phase": 137,
        "non_signal": True,
        "training_blocked": True,
        "prediction_blocked": True,
        "artifact_persistence_blocked": True,
        "status": "READY",
    }
