from typing import Tuple, Dict, Any
import pandas as pd

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
    list_fusion_feature_profiles,
)
from advanced_feature_fusion.fusion_feature_models import (
    FusionFeatureProfileItem,
    build_fusion_feature_profile_id,
)


def build_fusion_feature_profile_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    profiles = list_fusion_feature_profiles(enabled_only=False)

    rows = []
    for p in profiles:
        item = FusionFeatureProfileItem(
            profile_id=build_fusion_feature_profile_id(p.name),
            profile_name=p.name,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            dry_run=p.dry_run_default,
            non_signal=p.non_signal,
            metadata_only_news=p.metadata_only_news,
            status_label="fusion_ready" if p.enabled else "fusion_placeholder_only",
            warnings=[] if p.enabled else ["Profile disabled"],
        )
        rows.append(item.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_fusion_feature_profiles(df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["status"] = "READY"
    return df, summary


def summarize_fusion_feature_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_profiles": 0, "status": "EMPTY"}
    return {
        "total_profiles": len(df),
        "active_profiles": int((df["status_label"] == "fusion_ready").sum()),
        "non_signal_verified": bool(df["non_signal"].all()),
        "metadata_only_verified": bool(df["metadata_only_news"].all()),
        "dry_run_mandate": bool(df["dry_run"].all()),
        "non_signal_mandate": bool(df["non_signal"].all()),
        "default_profile": "balanced_local_macro_calendar_news_fusion",
        "current_phase": 120,
        "target_final_phase": 160,
        "next_phase": 121,
        "status": "READY",
    }


def get_fusion_feature_profiles_registry() -> pd.DataFrame:
    """Return DataFrame of profile registry."""
    df, _ = build_fusion_feature_profile_registry()
    return df


def get_fusion_feature_profiles_summary() -> Dict[str, Any]:
    """Return summary dictionary of profile registry."""
    _, summary = build_fusion_feature_profile_registry()
    return summary
