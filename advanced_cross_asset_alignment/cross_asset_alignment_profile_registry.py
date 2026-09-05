from typing import Tuple, Dict, Any
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    list_cross_asset_alignment_profiles,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.cross_asset_alignment_models import (
    CrossAssetAlignmentProfileItem,
    build_cross_asset_alignment_profile_id,
)


def build_cross_asset_alignment_profile_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    profiles = list_cross_asset_alignment_profiles(enabled_only=False)

    rows = []
    for p in profiles:
        item = CrossAssetAlignmentProfileItem(
            profile_id=build_cross_asset_alignment_profile_id(p.name),
            profile_name=p.name,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            dry_run=p.dry_run_default,
            non_signal=True,
            status_label="alignment_ready" if p.enabled else "alignment_placeholder_only",
            warnings=[] if p.enabled else ["Profile is disabled"],
        )
        row_dict = item.to_dict()
        row_dict["dry_run_default"] = p.dry_run_default
        rows.append(row_dict)

    df = pd.DataFrame(rows)
    summary = summarize_cross_asset_alignment_profiles(df)
    summary["active_profile"] = active_profile.name
    summary["dry_run"] = active_profile.dry_run_default
    summary["dry_run_default"] = active_profile.dry_run_default
    return df, summary


def summarize_cross_asset_alignment_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_profiles": len(df),
        "current_phase": 119,
        "target_final_phase": 160,
        "next_phase": 120,
        "local_only": True,
        "research_only": True,
        "non_signal": True,
        "status": "READY" if not df.empty else "EMPTY",
    }

