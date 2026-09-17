# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Profile Registry.

Builds and manages configuration profiles for Phase 159 Final Hardening.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
    list_final_hardening_profiles,
)
from advanced_final_hardening.final_hardening_labels import (
    FINAL_HARDENING_PROFILE_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)


def build_final_hardening_profile_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build the final hardening profile registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()
    profiles = list_final_hardening_profiles(enabled_only=False)

    rows = []
    for p in profiles:
        rows.append({
            "profile_name": p.profile_name,
            "description": p.description,
            "current_phase": p.current_phase,
            "target_final_phase": p.target_final_phase,
            "next_phase": p.next_phase,
            "default_language": p.default_language,
            "dry_run_default": p.dry_run_default,
            "local_only": p.local_only,
            "non_production": p.non_production,
            "research_only": p.research_only,
            "allow_live_trading": p.allow_live_trading,
            "allow_broker_integration": p.allow_broker_integration,
            "allow_production_deployment": p.allow_production_deployment,
            "allow_release_deployment": p.allow_release_deployment,
            "min_readiness_score": p.min_readiness_score,
            "enabled": p.enabled,
            "domain": FINAL_HARDENING_PROFILE_DOMAIN,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "profile_count": len(rows),
        "active_profile": active_profile.profile_name,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "all_local_only": bool(df["local_only"].all()),
        "all_non_production": bool(df["non_production"].all()),
        "all_no_live_trading": bool((~df["allow_live_trading"]).all()),
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
