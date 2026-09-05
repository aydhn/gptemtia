"""Phase 128: Regime Rule-Free Profile Registry.

Constructs DataFrame and summary metadata for Phase 128 operational profiles.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    REGIME_RULE_FREE_PROFILES,
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import RegimeRuleFreeProfileItem


def build_regime_rule_free_profile_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for Phase 128 profile registry."""
    active_profile = profile or get_default_regime_rule_free_profile()

    items = []
    for name, p in REGIME_RULE_FREE_PROFILES.items():
        is_active = (name == active_profile.profile_name)
        item = RegimeRuleFreeProfileItem(
            profile_name=p.profile_name,
            description=p.description,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            is_active=is_active,
            dry_run_default=p.dry_run_default,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            non_signal=True,
            source_preserved=True,
            clustering_allowed=p.allow_clustering_execution,
            model_training_allowed=p.allow_model_training,
            min_readiness_score=p.min_readiness_score,
        )
        items.append(item.__dict__)

    df = pd.DataFrame(items)

    summary = {
        "active_profile": active_profile.profile_name,
        "total_profiles": len(items),
        "current_phase": active_profile.current_phase,
        "next_phase": active_profile.next_phase,
        "target_final_phase": active_profile.target_final_phase,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "all_clustering_disallowed": bool((~df["clustering_allowed"]).all()) if not df.empty else True,
        "all_model_training_disallowed": bool((~df["model_training_allowed"]).all()) if not df.empty else True,
    }

    return df, summary
