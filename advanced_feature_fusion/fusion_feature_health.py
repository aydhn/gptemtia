"""Fusion Feature Health Check.

Verifies the integrity, availability, and safety status of Phase 120 subsystems.
Strictly non-signal, research use only.
"""

from datetime import datetime, timezone
from typing import Any, Dict
from config.settings import get_settings
from advanced_feature_fusion.fusion_feature_config import list_fusion_feature_profiles
from advanced_feature_fusion.fusion_feature_domain_registry import get_fusion_feature_domains_summary
from advanced_feature_fusion.fusion_feature_metadata_registry import get_fusion_feature_metadata_summary
from advanced_feature_fusion.macro_feature_fusion_contracts import get_macro_timeseries_contracts
from advanced_feature_fusion.calendar_event_fusion_contracts import get_calendar_event_contracts
from advanced_feature_fusion.release_event_fusion_contracts import get_release_event_contracts
from advanced_feature_fusion.news_metadata_fusion_contracts import get_news_metadata_contracts


def check_fusion_feature_health() -> Dict[str, Any]:
    """Execute health verification for Phase 120."""
    checks = {}
    is_healthy = True

    # Check 1: Settings
    try:
        settings = get_settings()
        checks["settings_enabled"] = bool(getattr(settings, "advanced_feature_fusion_enabled", False))
        checks["local_only"] = bool(getattr(settings, "fusion_feature_local_only", True))
        checks["dry_run"] = bool(getattr(settings, "fusion_feature_dry_run_default", True))
    except Exception as e:
        checks["settings_enabled"] = False
        checks["settings_error"] = str(e)
        is_healthy = False

    # Check 2: Profiles
    try:
        profiles = list_fusion_feature_profiles()
        checks["profiles_count"] = len(profiles)
        checks["profiles_ok"] = len(profiles) >= 3
    except Exception as e:
        checks["profiles_ok"] = False
        checks["profiles_error"] = str(e)
        is_healthy = False

    # Check 3: Domains
    try:
        domains_summary = get_fusion_feature_domains_summary()
        checks["domains_count"] = domains_summary["total_domains"]
        checks["domains_ok"] = domains_summary["total_domains"] >= 35
    except Exception as e:
        checks["domains_ok"] = False
        checks["domains_error"] = str(e)
        is_healthy = False

    # Check 4: Metadata Features
    try:
        meta_summary = get_fusion_feature_metadata_summary()
        checks["metadata_features_count"] = meta_summary["total_features"]
        checks["metadata_ok"] = meta_summary["total_features"] > 0
    except Exception as e:
        checks["metadata_ok"] = False
        checks["metadata_error"] = str(e)
        is_healthy = False

    # Check 5: Contracts
    try:
        c_macro = len(get_macro_timeseries_contracts())
        c_cal = len(get_calendar_event_contracts())
        c_rel = len(get_release_event_contracts())
        c_news = len(get_news_metadata_contracts())
        checks["contracts_count"] = c_macro + c_cal + c_rel + c_news
        checks["contracts_ok"] = checks["contracts_count"] >= 4
    except Exception as e:
        checks["contracts_ok"] = False
        checks["contracts_error"] = str(e)
        is_healthy = False

    return {
        "status": "HEALTHY" if is_healthy else "UNHEALTHY",
        "phase": 120,
        "next_phase": 121,
        "checks": checks,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
