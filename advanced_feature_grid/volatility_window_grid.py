from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


VOLATILITY_GRIDS = [
    {
        "grid_name": "atr_window_grid",
        "indicator_name": "atr",
        "family": "volatility",
        "windows": [7, 14, 20, 30],
        "naming_pattern": "atr_w{window}",
        "description": "Ortalama gerçek aralık (Average True Range) pencere matrisi.",
    },
    {
        "grid_name": "rolling_std_window_grid",
        "indicator_name": "rolling_std",
        "family": "volatility",
        "windows": [5, 10, 20, 30, 60],
        "naming_pattern": "rolling_std_w{window}",
        "description": "Fiyat standart sapması pencere matrisi.",
    },
    {
        "grid_name": "realized_volatility_window_grid",
        "indicator_name": "realized_volatility",
        "family": "volatility",
        "windows": [5, 10, 20, 30, 60],
        "naming_pattern": "realized_vol_w{window}",
        "description": "Gerçekleşen volatilite pencere matrisi.",
    },
    {
        "grid_name": "parkinson_volatility_window_grid",
        "indicator_name": "parkinson_volatility",
        "family": "volatility",
        "windows": [10, 20, 30],
        "naming_pattern": "parkinson_vol_w{window}",
        "description": "Parkinson yüksek-düşük volatilite pencere matrisi.",
    },
]


def build_volatility_window_grid_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []
    for g in VOLATILITY_GRIDS:
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
    summary = summarize_volatility_window_grid(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_volatility_window_grid(df: pd.DataFrame) -> Dict[str, Any]:
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
