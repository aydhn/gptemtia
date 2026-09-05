from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


MACRO_PLACEHOLDERS = [
    {
        "placeholder_name": "macro_value_change",
        "family": "macro_placeholder",
        "windows": [1, 3, 6, 12],
        "naming_pattern": "macro_chg_m{window}",
        "description": "Makro ekonomik gösterge periyodik değişim placeholder gridi.",
    },
    {
        "placeholder_name": "macro_rolling_change",
        "family": "macro_placeholder",
        "windows": [3, 6, 12],
        "naming_pattern": "macro_rolling_chg_m{window}",
        "description": "Makro veri kayan pencere ortalama değişim placeholder gridi.",
    },
    {
        "placeholder_name": "macro_revision_flag_count",
        "family": "macro_placeholder",
        "windows": [3, 6, 12],
        "naming_pattern": "macro_rev_cnt_m{window}",
        "description": "Makro revizyon sayısı kayan pencere placeholder gridi.",
    },
]


def build_macro_feature_grid_placeholder_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []
    for p in MACRO_PLACEHOLDERS:
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
