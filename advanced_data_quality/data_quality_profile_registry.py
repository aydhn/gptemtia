from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import (
    DataQualityProfile,
    list_data_quality_profiles,
)
from advanced_data_quality.data_quality_models import (
    DataQualityProfileItem,
    build_data_quality_profile_id,
)


def build_default_data_quality_profile_items(profile: DataQualityProfile) -> List[DataQualityProfileItem]:
    profiles = list_data_quality_profiles(enabled_only=False)
    items = []
    for p in profiles:
        item = DataQualityProfileItem(
            profile_id=build_data_quality_profile_id(p.name),
            profile_name=p.name,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            dry_run=p.dry_run,
            status_label="quality_pass" if p.enabled else "quality_not_applicable",
            warnings=[]
        )
        items.append(item)
    return items


def build_data_quality_profile_registry(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = build_default_data_quality_profile_items(profile)
    records = [i.to_dict() for i in items]
    df = pd.DataFrame.from_records(records)
    summary = summarize_data_quality_profile_registry(df)
    return df, summary


def summarize_data_quality_profile_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_profiles": len(df),
        "profiles": df["profile_name"].tolist() if "profile_name" in df.columns else [],
        "dry_run_all": bool(df["dry_run"].all()) if "dry_run" in df.columns and len(df) > 0 else True,
        "local_only_all": bool(df["local_only"].all()) if "local_only" in df.columns and len(df) > 0 else True,
        "non_production_all": bool(df["non_production"].all()) if "non_production" in df.columns and len(df) > 0 else True,
        "current_phase": 112,
        "target_final_phase": 160,
    }
