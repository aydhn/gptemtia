import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_RUN_PLAN_PLACEHOLDERS = [
    {"placeholder_name": "baseline_model_contract_run_plan_ph", "experiment_family": "baseline_model_contract_experiment_placeholder"},
    {"placeholder_name": "regime_metadata_model_input_run_plan_ph", "experiment_family": "regime_metadata_model_input_experiment_placeholder"},
    {"placeholder_name": "featurestore_model_input_run_plan_ph", "experiment_family": "featurestore_model_input_experiment_placeholder"},
    {"placeholder_name": "phase_138_dry_run_harness_run_plan_ph", "experiment_family": "phase_138_dry_run_harness_experiment_placeholder"},
]

def build_ml_experiment_run_plan_placeholder_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for p in _RUN_PLAN_PLACEHOLDERS:
        rows.append({
            "placeholder_name": p["placeholder_name"],
            "experiment_family": p["experiment_family"],
            "execution_phase": 138,
            "run_plan_executed": False,
            "training_executed": False,
            "prediction_executed": False,
            "artifact_created": False,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_run_plans": len(rows),
        "current_phase": 137,
        "non_signal": True,
        "run_plan_executed": False,
        "executed": False,
        "status": "READY",
    }
    return df, summary

def summarize_ml_experiment_run_plan_placeholders(df: pd.DataFrame) -> Dict:
    return {
        "total_run_plans": len(df),
        "current_phase": 137,
        "non_signal": True,
        "run_plan_executed": False,
        "executed": False,
        "status": "READY",
    }
