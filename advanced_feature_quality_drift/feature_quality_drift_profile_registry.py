"""Phase 123 Feature Quality and Drift Profile Registry.

Builds immutable DataFrame and metadata summary of configured diagnostic profiles.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
    list_feature_quality_drift_profiles,
)


def build_feature_quality_drift_profile_registry(
    profile: FeatureQualityDriftProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of all available profiles."""
    active_profile = profile or get_default_feature_quality_drift_profile()
    profiles = list_feature_quality_drift_profiles(enabled_only=False)

    records = []
    for p in profiles:
        records.append({
            "profile_name": p.name,
            "description": p.description,
            "current_phase": p.current_phase,
            "target_final_phase": p.target_final_phase,
            "next_phase": p.next_phase,
            "dry_run_default": p.dry_run_default,
            "local_only": p.local_only,
            "non_production": p.non_production,
            "research_only": p.research_only,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "enabled": p.enabled,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_profiles": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "local_only": active_profile.local_only,
        "research_only": active_profile.research_only,
    }
    return df, summary
