import pandas as pd
from typing import Dict, List, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

ALLOWED_ACTIONS = [
    "create_experiment_metadata",
    "create_dataset_contract_reference",
    "create_feature_snapshot_contract_reference",
    "create_run_plan_placeholder",
    "create_safety_governance_report",
]

BLOCKED_ACTIONS = [
    "materialize_dataset",
    "create_target_label",
    "fit_model",
    "train_model",
    "predict",
    "inference",
    "transform",
    "persist_artifact",
    "write_model_registry",
    "run_backtest",
    "generate_signal",
]

_TEMPLATES = [
    {"template_name": "baseline_model_contract_template", "experiment_family": "baseline_model_contract_experiment_placeholder"},
    {"template_name": "regime_metadata_model_input_template", "experiment_family": "regime_metadata_model_input_experiment_placeholder"},
    {"template_name": "featurestore_model_input_template", "experiment_family": "featurestore_model_input_experiment_placeholder"},
    {"template_name": "cross_asset_feature_input_template", "experiment_family": "cross_asset_feature_input_experiment_placeholder"},
    {"template_name": "phase_138_dry_run_harness_template", "experiment_family": "phase_138_dry_run_harness_experiment_placeholder"},
]

def build_ml_experiment_template_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for t in _TEMPLATES:
        rows.append({
            "template_name": t["template_name"],
            "experiment_family": t["experiment_family"],
            "allowed_actions": ", ".join(ALLOWED_ACTIONS),
            "blocked_actions": ", ".join(BLOCKED_ACTIONS),
            "handoff_phase": 138,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {"total_templates": len(rows), "current_phase": 137, "non_signal": True, "status": "READY"}
    return df, summary

def summarize_ml_experiment_templates(df: pd.DataFrame) -> Dict:
    return {"total_templates": len(df), "current_phase": 137, "non_signal": True, "status": "READY"}
