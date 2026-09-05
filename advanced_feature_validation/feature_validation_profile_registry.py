"""Profile Registry for Phase 121 Feature Validation Layer.

Constructs DataFrame and metadata summary of all available validation profiles.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
    list_feature_validation_profiles,
)
from advanced_feature_validation.feature_validation_models import (
    FeatureValidationProfileItem,
    build_feature_validation_profile_id,
)


def build_feature_validation_profile_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all registered feature validation profiles."""
    active_profile = profile or get_default_feature_validation_profile()
    all_profiles = list_feature_validation_profiles(enabled_only=False)

    records = []
    for p in all_profiles:
        p_id = build_feature_validation_profile_id(p.name)
        warnings = []
        if not p.enable_no_lookahead_rules:
            warnings.append("no_lookahead_disabled")
        if not p.enable_forbidden_column_rules:
            warnings.append("forbidden_column_rules_disabled")

        item = FeatureValidationProfileItem(
            profile_id=p_id,
            profile_name=p.name,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            dry_run=p.dry_run_default,
            non_signal=True,
            no_leakage_required=True,
            status_label="validation_pass" if p.enabled else "validation_placeholder_only",
            warnings=warnings,
        )
        records.append(item.to_dict())

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "default_profile": active_profile.name,
        "total_profiles": len(records),
        "enabled_profiles": sum(1 for p in all_profiles if p.enabled),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "dry_run_mandate": active_profile.dry_run_default,
        "non_signal_mandate": True,
        "no_leakage_required": True,
    }
    return df, summary


def get_feature_validation_profile(name: str = "default") -> FeatureValidationProfile:
    """Return FeatureValidationProfile instance by name."""
    norm_name = name.lower()
    if "strict" in norm_name:
        return FeatureValidationProfile(
            name="strict",
            profile_name="strict",
            description="Strict validation profile",
            non_signal=True,
        )
    elif "lenient" in norm_name:
        return FeatureValidationProfile(
            name="lenient",
            profile_name="lenient",
            description="Lenient validation profile",
            non_signal=True,
        )
    else:
        return FeatureValidationProfile(
            name="default",
            profile_name="default",
            description="Default validation profile",
            non_signal=True,
        )


def get_feature_validation_profiles_registry(
    profile: FeatureValidationProfile | None = None,
) -> Dict[str, FeatureValidationProfile]:
    """Return dictionary of available validation profiles."""
    return {
        "default": get_feature_validation_profile("default"),
        "strict": get_feature_validation_profile("strict"),
        "lenient": get_feature_validation_profile("lenient"),
    }


def get_feature_validation_profiles_summary(
    profile: FeatureValidationProfile | None = None,
) -> Dict[str, Any]:
    """Return summary of validation profile registry."""
    profiles = get_feature_validation_profiles_registry(profile)
    return {
        "total_profiles": len(profiles),
        "default_profile": "balanced_local_feature_validation",
        "current_phase": 121,
        "target_final_phase": 160,
        "next_phase": 122,
        "dry_run_mandate": True,
        "non_signal_mandate": True,
    }


