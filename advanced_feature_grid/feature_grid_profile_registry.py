from typing import Tuple, Dict, Any
import pandas as pd

from advanced_feature_grid.feature_grid_config import (
    FeatureGridProfile,
    FEATURE_GRID_PROFILES,
    get_default_feature_grid_profile,
)
from advanced_feature_grid.feature_grid_models import (
    FeatureGridProfileItem,
    build_feature_grid_profile_id,
)


def build_feature_grid_profile_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    items = []

    for name, prof in FEATURE_GRID_PROFILES.items():
        warnings = []
        if not prof.research_only:
            warnings.append("Research only kuralı ihlal edilmiş.")
        if not prof.non_production:
            warnings.append("Non-production kuralı ihlal edilmiş.")
        if not prof.local_only:
            warnings.append("Local only kuralı ihlal edilmiş.")

        status = "feature_grid_ready" if not warnings else "feature_grid_ready_with_warnings"

        item = FeatureGridProfileItem(
            profile_id=build_feature_grid_profile_id(prof.name),
            profile_name=prof.name,
            current_phase=prof.current_phase,
            target_final_phase=prof.target_final_phase,
            next_phase=prof.next_phase,
            local_only=prof.local_only,
            non_production=prof.non_production,
            research_only=prof.research_only,
            dry_run=prof.dry_run_default,
            non_signal=True,
            status_label=status,
            warnings=warnings,
        )
        items.append(item.to_dict())

    df = pd.DataFrame(items)
    summary = {
        "active_profile": active_profile.name,
        "total_profiles": len(df),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "local_only": active_profile.local_only,
        "research_only": active_profile.research_only,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary
