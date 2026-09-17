import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_PARTITION_POLICIES = [
    {"policy_name": "by_dataset_family", "description": "Partition by dataset family (regime_metadata, featurestore, etc.)"},
    {"policy_name": "by_source_phase", "description": "Partition by source phase reference"},
    {"policy_name": "by_entity_type", "description": "Partition by entity type (commodity, fx, etc.)"},
    {"policy_name": "by_time_bucket_placeholder", "description": "Placeholder partition by time bucket. Not materialized."},
    {"policy_name": "by_validation_acceptance_status", "description": "Partition by validation acceptance status"},
    {"policy_name": "by_no_lookahead_status", "description": "Partition by no-lookahead guard status"},
    {"policy_name": "by_metadata_only_news_status", "description": "Partition by metadata-only news guard status"},
    {"policy_name": "by_manual_review_required", "description": "Partition by manual review required flag"},
]


def build_ml_dataset_partition_policy_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for p in _PARTITION_POLICIES:
        rows.append({
            "policy_name": p["policy_name"],
            "description": p["description"],
            "materialized": False,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {"total_partition_policies": len(rows), "current_phase": 137, "non_signal": True, "status": "READY"}
    return df, summary


def summarize_ml_dataset_partition_policies(df: pd.DataFrame) -> Dict:
    return {"total_partition_policies": len(df), "current_phase": 137, "non_signal": True, "status": "READY"}
