"""Phase 135: Regime Acceptance Profile Registry.

Builds and summarizes the profile registry for Phase 135.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    PROFILES,
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    ACCEPTANCE_PASS,
    REGIME_ACCEPTANCE_PROFILE_DOMAIN,
)


def build_regime_acceptance_profile_registry(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of configured acceptance profiles."""
    active = profile or get_regime_acceptance_profile()
    rows = []
    for p in PROFILES.values():
        rows.append({
            "profile_name": p.profile_name,
            "description": p.description,
            "current_phase": p.current_phase,
            "target_final_phase": p.target_final_phase,
            "next_phase": p.next_phase,
            "dry_run_default": p.dry_run_default,
            "local_only": p.local_only,
            "non_production": p.non_production,
            "research_only": p.research_only,
            "min_score": p.min_score,
            "is_active": (p.profile_name == active.profile_name),
            "non_signal": True,
            "status_label": ACCEPTANCE_PASS,
        })
    df = pd.DataFrame(rows)
    summary: Dict[str, Any] = {
        "domain": REGIME_ACCEPTANCE_PROFILE_DOMAIN,
        "active_profile": active.profile_name,
        "total_profiles": len(rows),
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_regime_acceptance_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize a profile DataFrame."""
    return {
        "total_profiles": len(df),
        "profiles": df["profile_name"].tolist() if not df.empty and "profile_name" in df.columns else [],
        "non_signal": True,
    }
