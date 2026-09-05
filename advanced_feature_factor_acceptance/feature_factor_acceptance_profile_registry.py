"""Phase 125: Feature Factor Acceptance Profile Registry.

Builds and summarizes the registry of configured acceptance profiles.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    PROFILES,
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_models import (
    FeatureFactorAcceptanceProfileItem,
)


def build_feature_factor_acceptance_profile_registry(
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of acceptance profiles and summary."""
    active_profile = profile or get_default_feature_factor_acceptance_profile()
    rows = []
    for p in PROFILES.values():
        item = FeatureFactorAcceptanceProfileItem(
            profile_name=p.profile_name,
            description=p.description,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            dry_run_default=p.dry_run_default,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            min_score=p.min_score,
            non_signal=True,
            source_preserved=True,
            official_approval=False,
            production_ready=False,
            broker_ready=False,
        )
        rows.append(item.__dict__)

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_profiles": len(df),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_feature_factor_acceptance_profile_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize a profile registry DataFrame."""
    return {
        "total_profiles": len(df),
        "profiles": df["profile_name"].tolist() if "profile_name" in df.columns else [],
        "non_signal": True,
    }
