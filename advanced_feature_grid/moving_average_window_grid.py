from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


MOVING_AVERAGE_GRIDS = [
    {
        "grid_name": "sma_window_grid",
        "indicator_name": "sma",
        "family": "moving_average",
        "windows": [5, 10, 20, 50, 100, 200],
        "naming_pattern": "sma_w{window}",
        "description": "Basit hareketli ortalama çoklu pencere matrisi.",
    },
    {
        "grid_name": "ema_window_grid",
        "indicator_name": "ema",
        "family": "moving_average",
        "windows": [5, 10, 20, 50, 100, 200],
        "naming_pattern": "ema_w{window}",
        "description": "Üstel hareketli ortalama çoklu pencere matrisi.",
    },
    {
        "grid_name": "wma_window_grid",
        "indicator_name": "wma",
        "family": "moving_average",
        "windows": [5, 10, 20, 50],
        "naming_pattern": "wma_w{window}",
        "description": "Ağırlıklı hareketli ortalama pencere matrisi.",
    },
    {
        "grid_name": "dema_window_grid",
        "indicator_name": "dema",
        "family": "moving_average",
        "windows": [10, 20, 50],
        "naming_pattern": "dema_w{window}",
        "description": "Çift üstel hareketli ortalama pencere matrisi.",
    },
    {
        "grid_name": "tema_window_grid",
        "indicator_name": "tema",
        "family": "moving_average",
        "windows": [10, 20, 50],
        "naming_pattern": "tema_w{window}",
        "description": "Üçlü üstel hareketli ortalama pencere matrisi.",
    },
]


def build_moving_average_window_grid_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []
    for g in MOVING_AVERAGE_GRIDS:
        for w in g["windows"]:
            rows.append({
                "grid_name": g["grid_name"],
                "indicator_name": g["indicator_name"],
                "family": g["family"],
                "window": w,
                "column_name": g["naming_pattern"].format(window=w),
                "non_signal": True,
                "lookahead_free": True,
                "performance_tier": "light" if w <= 50 else "standard",
            })

    df = pd.DataFrame(rows)
    summary = summarize_moving_average_window_grid(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_moving_average_window_grid(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_grid_features": 0, "status": "EMPTY"}

    return {
        "total_grid_features": len(df),
        "total_indicators": df["indicator_name"].nunique() if "indicator_name" in df.columns else 0,
        "max_window": int(df["window"].max()) if "window" in df.columns else 0,
        "min_window": int(df["window"].min()) if "window" in df.columns else 0,
        "non_signal": True,
        "status": "READY",
    }
