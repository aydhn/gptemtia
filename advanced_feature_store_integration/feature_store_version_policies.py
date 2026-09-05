"""Phase 124 Feature Store Version Policies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

VERSION_POLICIES = [
    {
        "policy_id": "VPOL_001",
        "policy_name": "immutable_snapshot_policy",
        "description": "Her sürüm değişmez bir snapshot olarak saklanır, önceki sürümler asla silinmez veya üzerine yazılmaz.",
        "destructive_overwrite_allowed": False,
        "production_release_tag_allowed": False,
        "immutable_snapshot_supported": True,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "policy_id": "VPOL_002",
        "policy_name": "metadata_audit_trail_policy",
        "description": "Tüm sürüm değişimleri lineage ve audit kayıtlarında tarih damgası ile izlenir.",
        "destructive_overwrite_allowed": False,
        "production_release_tag_allowed": False,
        "immutable_snapshot_supported": True,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "policy_id": "VPOL_003",
        "policy_name": "phase_bound_versioning_policy",
        "description": "Sürüm numaralandırması faz ilerlemesi ile uyumlu olup Phase 124 araştırma sınırını aşmaz.",
        "destructive_overwrite_allowed": False,
        "production_release_tag_allowed": False,
        "immutable_snapshot_supported": True,
        "non_signal": True,
        "source_preserved": True,
    },
]


def validate_store_version_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """Validate version policy for safety adherence."""
    issues = []
    if policy.get("destructive_overwrite_allowed", False):
        issues.append("Destructive overwrite is strictly prohibited.")
    if policy.get("production_release_tag_allowed", False):
        issues.append("Production release tags are strictly prohibited.")
    if not policy.get("source_preserved", True):
        issues.append("Source preservation must be True.")

    return {
        "policy_name": policy.get("policy_name", "unknown"),
        "is_safe": len(issues) == 0,
        "issues": issues,
        "non_signal": True,
    }


def build_feature_store_version_policy_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of version policies."""
    records = list(VERSION_POLICIES)
    df = pd.DataFrame(records)
    summary = {
        "total_version_policies": len(records),
        "destructive_overwrite_forbidden": True,
        "production_release_tag_forbidden": True,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_store_version_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize version policies."""
    return {
        "total_policies": len(df) if not df.empty else 0,
        "destructive_overwrite_forbidden": True,
        "non_signal": True,
    }
