from typing import Tuple, Dict, Any
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import (
    TechnicalIndicatorProfile,
    list_technical_indicator_profiles,
)
from advanced_technical_indicators.technical_indicator_models import (
    TechnicalIndicatorProfileItem,
    build_technical_indicator_profile_id,
)


def build_technical_indicator_profile_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    profiles = list_technical_indicator_profiles(enabled_only=False)
    items = []
    for p in profiles:
        item = TechnicalIndicatorProfileItem(
            profile_id=build_technical_indicator_profile_id(p.name),
            profile_name=p.name,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            dry_run=p.dry_run_default,
            non_signal=not p.allow_indicator_as_signal,
            status_label="indicator_ready",
            warnings=[],
        )
        items.append(item.to_dict())

    df = pd.DataFrame(items)
    summary = {
        "total_profiles": len(df),
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
        "default_profile": profile.name,
        "non_signal_guaranteed": True,
        "local_only": profile.local_only,
        "status": "READY",
    }
    return df, summary
