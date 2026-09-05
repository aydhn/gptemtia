from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


MOMENTUM_GRIDS = [
    {
        "grid_name": "rsi_window_grid",
        "indicator_name": "rsi",
        "family": "momentum",
        "windows": [7, 14, 21, 28],
        "naming_pattern": "rsi_w{window}",
        "description": "Göreceli güç endeksi çoklu pencere matrisi.",
    },
    {
        "grid_name": "roc_window_grid",
        "indicator_name": "roc",
        "family": "momentum",
        "windows": [5, 10, 20, 30],
        "naming_pattern": "roc_w{window}",
        "description": "Değişim oranı (Rate of Change) pencere matrisi.",
    },
    {
        "grid_name": "momentum_window_grid",
        "indicator_name": "momentum",
        "family": "momentum",
        "windows": [5, 10, 20, 30],
        "naming_pattern": "momentum_w{window}",
        "description": "Fiyat momentumu pencere matrisi.",
    },
    {
        "grid_name": "cmo_window_grid",
        "indicator_name": "cmo",
        "family": "momentum",
        "windows": [7, 14, 21],
        "naming_pattern": "cmo_w{window}",
        "description": "Chande momentum osilatörü pencere matrisi.",
    },
]


def build_momentum_window_grid_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []
    for g in MOMENTUM_GRIDS:
        for w in g["windows"]:
            rows.append({
                "grid_name": g["grid_name"],
                "indicator_name": g["indicator_name"],
                "family": g["family"],
                "window": w,
                "column_name": g["naming_pattern"].format(window=w),
                "non_signal": True,
                "lookahead_free": True,
                "performance_tier": "light",
            })

    df = pd.DataFrame(rows)
    summary = summarize_momentum_window_grid(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_momentum_window_grid(df: pd.DataFrame) -> Dict[str, Any]:
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
