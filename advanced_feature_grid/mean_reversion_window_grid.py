from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


MEAN_REVERSION_GRIDS = [
    {
        "grid_name": "rolling_zscore_window_grid",
        "indicator_name": "rolling_zscore",
        "family": "mean_reversion",
        "windows": [10, 20, 50, 100],
        "naming_pattern": "zscore_w{window}",
        "description": "Fiyat standart sapma z-skoru pencere matrisi.",
    },
    {
        "grid_name": "distance_to_sma_window_grid",
        "indicator_name": "distance_to_sma",
        "family": "mean_reversion",
        "windows": [10, 20, 50, 100],
        "naming_pattern": "dist_sma_w{window}",
        "description": "Fiyatın SMA ortalamasına normalize mesafesi pencere matrisi.",
    },
    {
        "grid_name": "distance_to_ema_window_grid",
        "indicator_name": "distance_to_ema",
        "family": "mean_reversion",
        "windows": [10, 20, 50, 100],
        "naming_pattern": "dist_ema_w{window}",
        "description": "Fiyatın EMA ortalamasına normalize mesafesi pencere matrisi.",
    },
    {
        "grid_name": "percentile_rank_window_grid",
        "indicator_name": "rolling_percentile_rank_placeholder",
        "family": "mean_reversion",
        "windows": [50, 100, 200],
        "naming_pattern": "percentile_rank_w{window}",
        "description": "Rolling persentil sıralaması placeholder pencere matrisi.",
    },
]


def build_mean_reversion_window_grid_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []
    for g in MEAN_REVERSION_GRIDS:
        for w in g["windows"]:
            rows.append({
                "grid_name": g["grid_name"],
                "indicator_name": g["indicator_name"],
                "family": g["family"],
                "window": w,
                "column_name": g["naming_pattern"].format(window=w),
                "non_signal": True,
                "lookahead_free": True,
                "performance_tier": "standard",
            })

    df = pd.DataFrame(rows)
    summary = summarize_mean_reversion_window_grid(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_mean_reversion_window_grid(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_grid_features": 0, "status": "EMPTY"}

    return {
        "total_grid_features": len(df),
        "total_indicators": df["indicator_name"].nunique() if "indicator_name" in df.columns else 0,
        "non_signal": True,
        "status": "READY",
    }
