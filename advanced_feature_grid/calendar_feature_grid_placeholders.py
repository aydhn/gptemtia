from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


CALENDAR_PLACEHOLDERS = [
    {
        "placeholder_name": "pre_event_window_flag",
        "family": "calendar_placeholder",
        "windows": [1, 3, 5],
        "naming_pattern": "cal_pre_event_d{window}",
        "description": "Ekonomik takvim etkinliği öncesi pencere bayrak gridi.",
    },
    {
        "placeholder_name": "post_event_window_flag",
        "family": "calendar_placeholder",
        "windows": [1, 3, 5],
        "naming_pattern": "cal_post_event_d{window}",
        "description": "Ekonomik takvim etkinliği sonrası pencere bayrak gridi.",
    },
    {
        "placeholder_name": "event_importance_rolling_count",
        "family": "calendar_placeholder",
        "windows": [5, 10, 20],
        "naming_pattern": "cal_high_impact_cnt_w{window}",
        "description": "Yüksek etkili etkinlik sayısı kayan pencere gridi.",
    },
]


def build_calendar_feature_grid_placeholder_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []
    for p in CALENDAR_PLACEHOLDERS:
        for w in p["windows"]:
            rows.append({
                "placeholder_name": p["placeholder_name"],
                "family": p["family"],
                "window": w,
                "column_name": p["naming_pattern"].format(window=w),
                "is_placeholder": True,
                "non_signal": True,
                "directional_claim": False,
            })

    df = pd.DataFrame(rows)
    summary = {
        "profile": active_profile.name,
        "total_placeholders": len(df),
        "non_signal": True,
        "status": "PLACEHOLDER_ONLY",
    }
    return df, summary
