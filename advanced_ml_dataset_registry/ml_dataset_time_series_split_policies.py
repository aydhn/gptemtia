import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_SPLIT_POLICIES = [
    {"policy_name": "chronological_train_validation_test_placeholder", "split_type": "chronological"},
    {"policy_name": "expanding_window_placeholder", "split_type": "expanding_window"},
    {"policy_name": "rolling_window_placeholder", "split_type": "rolling_window"},
    {"policy_name": "blocked_time_series_split_placeholder", "split_type": "blocked"},
]

def build_ml_dataset_time_series_split_policy_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for p in _SPLIT_POLICIES:
        rows.append({
            "policy_name": p["policy_name"],
            "split_type": p["split_type"],
            "placeholder_only": True,
            "real_split_executed": False,
            "target_label_generated": False,
            "train_test_dataset_produced": False,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_split_policies": len(rows),
        "current_phase": 137,
        "all_placeholder_only": True,
        "materialized": False,
        "train_test_split_executed": False,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary

def summarize_ml_dataset_time_series_split_policies(df: pd.DataFrame) -> Dict:
    return {
        "total_split_policies": len(df),
        "current_phase": 137,
        "all_placeholder_only": True,
        "materialized": False,
        "train_test_split_executed": False,
        "non_signal": True,
        "status": "READY",
    }
