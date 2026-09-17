import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_TIME_INDEX_POLICIES = [
    {"policy_name": "chronological_time_index_policy", "description": "Chronological timestamp_utc required. No future timestamps. No naive timestamps."},
    {"policy_name": "strict_utc_no_future_policy", "description": "Strict UTC timezone required. Future timestamp forbidden."},
    {"policy_name": "no_lookahead_time_index_policy", "description": "Time index must be compatible with no-lookahead guard."},
]

def build_ml_dataset_time_index_policy_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for p in _TIME_INDEX_POLICIES:
        rows.append({
            "policy_name": p["policy_name"],
            "description": p["description"],
            "timestamp_utc_required": True,
            "naive_timestamp_forbidden": True,
            "future_timestamp_forbidden": True,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_time_index_policies": len(rows),
        "current_phase": 137,
        "timestamp_utc_required": True,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary

def validate_ml_dataset_time_index(df: pd.DataFrame, timestamp_field: str) -> Dict:
    issues = []
    if df is None or df.empty:
        return {"valid": False, "issues": ["DataFrame is empty"], "non_signal": True}
    if timestamp_field not in df.columns:
        issues.append(f"Missing timestamp field: {timestamp_field}")
    return {"valid": len(issues) == 0, "issues": issues, "non_signal": True}

def summarize_ml_dataset_time_index_policies(df: pd.DataFrame) -> Dict:
    return {
        "total_time_index_policies": len(df),
        "current_phase": 137,
        "timestamp_utc_required": True,
        "non_signal": True,
        "status": "READY",
    }
