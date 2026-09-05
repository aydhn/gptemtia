from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


RETURN_GRIDS = [
    {
        "grid_name": "simple_return_window_grid",
        "indicator_name": "simple_return",
        "family": "return",
        "windows": [1, 3, 5, 10, 20],
        "naming_pattern": "simple_return_w{window}",
        "description": "Basit periyodik getiri pencere matrisi.",
    },
    {
        "grid_name": "log_return_window_grid",
        "indicator_name": "log_return",
        "family": "return",
        "windows": [1, 3, 5, 10, 20],
        "naming_pattern": "log_return_w{window}",
        "description": "Logaritmik getiri pencere matrisi.",
    },
    {
        "grid_name": "cumulative_return_window_grid",
        "indicator_name": "cumulative_return",
        "family": "return",
        "windows": [5, 10, 20, 50],
        "naming_pattern": "cum_return_w{window}",
        "description": "Kümülatif getiri pencere matrisi.",
    },
    {
        "grid_name": "rolling_return_sum_window_grid",
        "indicator_name": "rolling_return_sum",
        "family": "return",
        "windows": [5, 10, 20, 50],
        "naming_pattern": "return_sum_w{window}",
        "description": "Rolling getiri toplamı pencere matrisi.",
    },
]


def build_return_window_grid_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []
    for g in RETURN_GRIDS:
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
    summary = summarize_return_window_grid(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_return_window_grid(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_grid_features": 0, "status": "EMPTY"}

    return {
        "total_grid_features": len(df),
        "total_indicators": df["indicator_name"].nunique() if "indicator_name" in df.columns else 0,
        "non_signal": True,
        "status": "READY",
    }
