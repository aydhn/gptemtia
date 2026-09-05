from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


QUOTE_PLACEHOLDERS = [
    {
        "placeholder_name": "quote_spread_rolling_mean",
        "family": "quote_microstructure",
        "windows": [5, 10, 20],
        "naming_pattern": "quote_spread_mean_w{window}",
        "description": "Bid-ask makas ortalaması placeholder gridi.",
    },
    {
        "placeholder_name": "quote_staleness",
        "family": "quote_microstructure",
        "windows": [5, 10, 20],
        "naming_pattern": "quote_staleness_w{window}",
        "description": "Kotasyon bayatlığı/hareketsizliği placeholder gridi.",
    },
    {
        "placeholder_name": "quote_mid_return",
        "family": "quote_microstructure",
        "windows": [1, 5, 10],
        "naming_pattern": "quote_mid_return_w{window}",
        "description": "Orta fiyat (mid-price) getirisi placeholder gridi.",
    },
]


def build_quote_feature_grid_placeholder_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []
    for p in QUOTE_PLACEHOLDERS:
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
