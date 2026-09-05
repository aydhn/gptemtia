from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import (
    DataNormalizationProfile,
    list_data_normalization_profiles,
)
from advanced_data_normalization.data_normalization_models import (
    DataNormalizationProfileItem,
    build_data_normalization_profile_id,
)


def build_default_data_normalization_profile_items(
    profile: DataNormalizationProfile,
) -> List[DataNormalizationProfileItem]:
    profiles = list_data_normalization_profiles(enabled_only=False)
    items = []
    for p in profiles:
        item = DataNormalizationProfileItem(
            profile_id=build_data_normalization_profile_id(p.name),
            profile_name=p.name,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            dry_run=p.dry_run_default,
            non_destructive=True,
            status_label="normalization_applied",
            warnings=[],
        )
        items.append(item)
    return items


def build_data_normalization_profile_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = build_default_data_normalization_profile_items(profile)
    records = [item.to_dict() for item in items]
    df = pd.DataFrame.from_records(records)
    summary = summarize_data_normalization_profile_registry(df)
    return df, summary


def summarize_data_normalization_profile_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_profiles": len(df),
        "profiles": df["profile_name"].tolist() if "profile_name" in df.columns else [],
        "all_non_destructive": bool(df["non_destructive"].all()) if "non_destructive" in df.columns else True,
        "all_dry_run": bool(df["dry_run"].all()) if "dry_run" in df.columns else True,
        "current_phase": 113,
        "target_final_phase": 160,
        "next_phase": 114,
    }
