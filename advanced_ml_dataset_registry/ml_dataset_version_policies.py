import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_VERSION_POLICIES = [
    {"policy_name": "contract_version_only_policy", "description": "Only contract versioning is allowed. No dataset materialization versioning."},
    {"policy_name": "snapshot_placeholder_only_policy", "description": "Snapshot versioning is placeholder only. No real snapshot materialization."},
    {"policy_name": "append_only_metadata_policy", "description": "Append-only metadata versioning. No destructive overwrite."},
]


def build_ml_dataset_version_policy_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for p in _VERSION_POLICIES:
        rows.append({
            "policy_name": p["policy_name"],
            "description": p["description"],
            "destructive_overwrite_allowed": False,
            "production_tag_allowed": False,
            "broker_tag_allowed": False,
            "live_tag_allowed": False,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_version_policies": len(rows),
        "current_phase": 137,
        "destructive_overwrite_allowed": False,
        "production_tag_allowed": False,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_ml_dataset_version_policies(df: pd.DataFrame) -> Dict:
    return {
        "total_version_policies": len(df),
        "current_phase": 137,
        "destructive_overwrite_allowed": False,
        "production_tag_allowed": False,
        "non_signal": True,
        "status": "READY",
    }
