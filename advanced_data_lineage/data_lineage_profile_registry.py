from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import (
    DataLineageProfile,
    list_data_lineage_profiles,
)
from advanced_data_lineage.data_lineage_models import (
    DataLineageProfileItem,
    build_data_lineage_profile_id,
)


def build_default_data_lineage_profile_items(
    profile: DataLineageProfile,
) -> List[DataLineageProfileItem]:
    all_profiles = list_data_lineage_profiles(enabled_only=False)
    items: List[DataLineageProfileItem] = []
    for p in all_profiles:
        p_id = build_data_lineage_profile_id(p.name)
        status = "lineage_complete" if p.enabled else "lineage_partial"
        warnings: List[str] = []
        if p.min_traceability_score > 0.60:
            warnings.append("High traceability score threshold enforced")
        items.append(
            DataLineageProfileItem(
                profile_id=p_id,
                profile_name=p.name,
                current_phase=p.current_phase,
                target_final_phase=p.target_final_phase,
                next_phase=p.next_phase,
                local_only=p.local_only,
                non_production=p.non_production,
                research_only=p.research_only,
                dry_run=p.dry_run_default,
                non_destructive=not p.allow_source_overwrite,
                status_label=status,
                warnings=warnings,
            )
        )
    return items


def build_data_lineage_profile_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = build_default_data_lineage_profile_items(profile)
    records = [it.to_dict() for it in items]
    df = pd.DataFrame.from_records(records)
    summary = summarize_data_lineage_profile_registry(df)
    return df, summary


def summarize_data_lineage_profile_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_profiles": len(df),
        "profile_names": df["profile_name"].tolist() if "profile_name" in df.columns else [],
        "current_phase": 114,
        "target_final_phase": 160,
        "next_phase": 115,
        "all_local_only": bool(df["local_only"].all()) if "local_only" in df.columns and len(df) > 0 else True,
        "all_non_production": bool(df["non_production"].all()) if "non_production" in df.columns and len(df) > 0 else True,
        "all_non_destructive": bool(df["non_destructive"].all()) if "non_destructive" in df.columns and len(df) > 0 else True,
    }
