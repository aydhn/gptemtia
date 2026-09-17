import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_PURGED_POLICIES = [
    {"policy_name": "purged_k_fold_placeholder", "description": "Purged K-Fold contract placeholder. Embargo/purge values are metadata placeholders."},
    {"policy_name": "combinatorial_purged_cv_placeholder", "description": "Combinatorial purged CV contract placeholder. Not executed."},
]

def build_ml_dataset_purged_split_placeholder_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for p in _PURGED_POLICIES:
        rows.append({
            "policy_name": p["policy_name"],
            "description": p["description"],
            "placeholder_only": True,
            "real_purging_executed": False,
            "backtest_executed": False,
            "optimizer_executed": False,
            "embargo_value": "placeholder",
            "purge_value": "placeholder",
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_purged_split_placeholders": len(rows),
        "total_purged_policies": len(rows),
        "current_phase": 137,
        "non_signal": True,
        "materialized": False,
        "purging_execution_allowed": False,
        "status": "READY",
    }
    return df, summary

def summarize_ml_dataset_purged_split_placeholders(df: pd.DataFrame) -> Dict:
    return {
        "total_purged_split_placeholders": len(df),
        "total_purged_policies": len(df),
        "current_phase": 137,
        "non_signal": True,
        "materialized": False,
        "purging_execution_allowed": False,
        "status": "READY",
    }
