"""Phase 134: Regime FeatureStore Partition Policies.

Defines non-signal, governance-aware partitioning strategies for organizing
regime metadata in the DataLake / FeatureStore structure.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_FEATURESTORE_PARTITION_POLICY_DOMAIN,
    REGIME_STORE_READY,
)

CANONICAL_PARTITION_POLICIES: List[Dict[str, Any]] = [
    {
        "partition_type": "by_source_phase",
        "partition_key": "source_phase",
        "description": "Partition metadata by originating lifecycle phase index (e.g. 126..134).",
        "non_signal": True,
    },
    {
        "partition_type": "by_store_entity_type",
        "partition_key": "store_entity_type",
        "description": "Partition by canonical regime entity type (taxonomy, matrix, candidate_state, etc.).",
        "non_signal": True,
    },
    {
        "partition_type": "by_component_name",
        "partition_key": "component_name",
        "description": "Partition by originating subsystem package name.",
        "non_signal": True,
    },
    {
        "partition_type": "by_validation_acceptance_status",
        "partition_key": "validation_acceptance_status",
        "description": "Partition records by acceptance verification outcome.",
        "non_signal": True,
    },
    {
        "partition_type": "by_no_lookahead_status",
        "partition_key": "no_lookahead_accepted",
        "description": "Partition records verifying backward temporal integrity.",
        "non_signal": True,
    },
    {
        "partition_type": "by_metadata_only_news_status",
        "partition_key": "metadata_only_news_accepted",
        "description": "Partition news records verifying strict metadata-only purity.",
        "non_signal": True,
    },
    {
        "partition_type": "by_manual_review_required",
        "partition_key": "manual_review_required",
        "description": "Partition records isolating items requiring human auditor review.",
        "non_signal": True,
    },
    {
        "partition_type": "by_timestamp_bucket_placeholder",
        "partition_key": "timestamp_bucket",
        "description": "Non-directional UTC monthly/quarterly partitioning placeholder.",
        "non_signal": True,
    },
]


def build_regime_featurestore_partition_policy_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct tabular partition policy registry."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_PARTITION_POLICIES)
    summary = {
        "domain": REGIME_FEATURESTORE_PARTITION_POLICY_DOMAIN,
        "total_policies": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def summarize_regime_featurestore_partition_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize partition policy registry DataFrame."""
    return {
        "total_policies": len(df),
        "partition_types": df["partition_type"].tolist() if not df.empty else [],
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
