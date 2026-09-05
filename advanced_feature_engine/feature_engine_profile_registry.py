from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import (
    FeatureEngineProfile,
    list_feature_engine_profiles,
)
from advanced_feature_engine.feature_engine_models import (
    FeatureEngineProfileItem,
    build_feature_engine_profile_id,
)


def build_feature_engine_profile_registry(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    profiles = list_feature_engine_profiles()
    items: List[Dict[str, Any]] = []

    for p in profiles:
        item = FeatureEngineProfileItem(
            profile_id=build_feature_engine_profile_id(p.name),
            profile_name=p.name,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            dry_run=p.dry_run_default,
            non_signal=True,
            status_label="feature_ready",
            warnings=[],
        )
        items.append(item.to_dict())

    df = pd.DataFrame.from_records(items)
    summary = summarize_feature_engine_profile_registry(df, profile)
    return df, summary


def summarize_feature_engine_profile_registry(
    df: pd.DataFrame,
    profile: FeatureEngineProfile,
) -> Dict[str, Any]:
    return {
        "total_profiles": len(df),
        "active_profile": profile.name,
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
    }
