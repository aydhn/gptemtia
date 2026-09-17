import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_WF_POLICIES = [
    {"policy_name": "walk_forward_validation_placeholder", "description": "Walk-forward validation contract placeholder. Not executed."},
    {"policy_name": "expanding_walk_forward_placeholder", "description": "Expanding walk-forward contract placeholder. Not executed."},
    {"policy_name": "rolling_walk_forward_placeholder", "description": "Rolling walk-forward contract placeholder. Not executed."},
]

def build_ml_dataset_walk_forward_split_policy_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for p in _WF_POLICIES:
        rows.append({
            "policy_name": p["policy_name"],
            "description": p["description"],
            "placeholder_only": True,
            "real_split_executed": False,
            "backtest_executed": False,
            "optimizer_executed": False,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_walk_forward_policies": len(rows),
        "total_wf_policies": len(rows),
        "current_phase": 137,
        "materialized": False,
        "backtest_executed": False,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary

def summarize_ml_dataset_walk_forward_split_policies(df: pd.DataFrame) -> Dict:
    return {
        "total_walk_forward_policies": len(df),
        "total_wf_policies": len(df),
        "current_phase": 137,
        "materialized": False,
        "backtest_executed": False,
        "non_signal": True,
        "status": "READY",
    }
