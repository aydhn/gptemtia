"""Phase 122 Factor Metadata Profile Registry.

Constructs registry records for active factor metadata profiles.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
    list_factor_metadata_profiles,
)
from advanced_factor_metadata.factor_metadata_models import (
    FactorMetadataProfileItem,
    build_factor_metadata_profile_id,
)


def build_factor_metadata_profile_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Metadata Profile Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()
    profiles = list_factor_metadata_profiles(enabled_only=False)

    items: List[Dict[str, Any]] = []
    for p in profiles:
        item = FactorMetadataProfileItem(
            profile_id=build_factor_metadata_profile_id(p.name),
            profile_name=p.name,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            dry_run=p.dry_run_default,
            non_signal=True,
            status_label="factor_ready",
            warnings=[],
        )
        items.append(item.to_dict())

    df = pd.DataFrame(items)
    summary = {
        "active_profile": active_profile.name,
        "total_profiles": len(items),
        "current_phase": 122,
        "target_final_phase": 160,
        "next_phase": 123,
        "dry_run_default": active_profile.dry_run_default,
        "non_signal": True,
        "status": "factor_ready",
    }
    return df, summary
