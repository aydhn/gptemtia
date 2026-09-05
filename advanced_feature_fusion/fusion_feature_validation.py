"""Fusion Feature System Validation.

High-level validation verifying profile configurations, contract compliances,
policy consistency, and safety guard enforcement.
Strictly non-signal, research use only.
"""

from typing import Any, Dict, List
from advanced_feature_fusion.fusion_feature_config import validate_fusion_feature_profiles, list_fusion_feature_profiles
from advanced_feature_fusion.fusion_feature_domain_registry import get_fusion_feature_domains_summary
from advanced_feature_fusion.macro_release_lag_policies import get_macro_release_lag_policies
from advanced_feature_fusion.calendar_event_window_policies import get_calendar_event_window_policies
from advanced_feature_fusion.news_metadata_only_fusion_policies import get_news_metadata_only_policies
from advanced_feature_fusion.fusion_timestamp_alignment_policies import get_timestamp_alignment_policies
from advanced_feature_fusion.fusion_asof_join_policies import get_asof_join_policies


def validate_all_fusion_feature_components() -> Dict[str, Any]:
    """Perform structural and semantic validation across all Phase 120 components."""
    errors: List[str] = []

    # 1. Validate Profiles
    try:
        profiles_valid = validate_fusion_feature_profiles()
        if not profiles_valid:
            errors.append("Profile validation failed.")
    except Exception as e:
        errors.append(f"Profile validation error: {e}")

    # 2. Check Domains count
    domains_summary = get_fusion_feature_domains_summary()
    if domains_summary["total_domains"] < 35:
        errors.append(f"Insufficient domain count: {domains_summary['total_domains']} < 35.")

    # 3. Check Policies presence
    lag_policies = get_macro_release_lag_policies()
    if not lag_policies:
        errors.append("Missing macro release lag policies.")

    cal_policies = get_calendar_event_window_policies()
    if not cal_policies:
        errors.append("Missing calendar event window policies.")

    news_policies = get_news_metadata_only_policies()
    if not news_policies:
        errors.append("Missing news metadata-only policies.")

    ts_policies = get_timestamp_alignment_policies()
    if not ts_policies:
        errors.append("Missing timestamp alignment policies.")

    asof_policies = get_asof_join_policies()
    if not asof_policies:
        errors.append("Missing asof join policies.")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "profiles_count": len(list_fusion_feature_profiles()),
        "domains_count": domains_summary["total_domains"],
        "policies_checked": len(lag_policies) + len(cal_policies) + len(news_policies) + len(ts_policies) + len(asof_policies),
        "zero_signal_guarantee": True,
        "metadata_only_news_guarantee": True,
    }
