"""Phase 134: Regime FeatureStore Version Policies.

Enforces append-only or immutable snapshot versioning for regime metadata.
Prohibits destructive overwrites, production release tags, and broker readiness tags.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_FEATURESTORE_VERSION_POLICY_DOMAIN,
    REGIME_STORE_READY,
)

CANONICAL_VERSION_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_name": "metadata_snapshot_policy",
        "versioning_mode": "snapshot",
        "allow_append": False,
        "allow_overwrite": False,
        "allow_production_release_tag": False,
        "allow_broker_readiness_tag": False,
        "description": "Immutable time-stamped snapshot of regime metadata states.",
        "non_signal": True,
    },
    {
        "policy_name": "metadata_append_policy",
        "versioning_mode": "append_only",
        "allow_append": True,
        "allow_overwrite": False,
        "allow_production_release_tag": False,
        "allow_broker_readiness_tag": False,
        "description": "Strict append-only logging of regime catalog entries without altering historical records.",
        "non_signal": True,
    },
    {
        "policy_name": "audit_ledger_version_policy",
        "versioning_mode": "append_only",
        "allow_append": True,
        "allow_overwrite": False,
        "allow_production_release_tag": False,
        "allow_broker_readiness_tag": False,
        "description": "Tamper-evident audit ledger tracking changes and manual review queue additions.",
        "non_signal": True,
    },
]


def build_regime_featurestore_version_policy_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct tabular version policy registry."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_VERSION_POLICIES)
    summary = {
        "domain": REGIME_FEATURESTORE_VERSION_POLICY_DOMAIN,
        "total_policies": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "all_overwrites_forbidden": bool((df["allow_overwrite"] == False).all()),
        "all_production_tags_forbidden": bool((df["allow_production_release_tag"] == False).all()),
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def validate_regime_featurestore_version_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that version policy prohibits destructive overwrites and production tags."""
    errors = []
    if policy.get("allow_overwrite", False):
        errors.append("Version policy must not allow destructive overwrites")
    if policy.get("allow_production_release_tag", False):
        errors.append("Version policy must not allow production release tags")
    if policy.get("allow_broker_readiness_tag", False):
        errors.append("Version policy must not allow broker readiness tags")

    return {
        "policy_name": policy.get("policy_name", "unknown"),
        "is_valid": len(errors) == 0,
        "errors": errors,
        "non_signal": True,
    }


def summarize_regime_featurestore_version_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize version policy registry DataFrame."""
    return {
        "total_policies": len(df),
        "policy_names": df["policy_name"].tolist() if not df.empty else [],
        "all_overwrites_prohibited": bool((df["allow_overwrite"] == False).all()) if not df.empty else True,
    }
