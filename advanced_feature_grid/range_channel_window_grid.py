from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


RANGE_CHANNEL_GRIDS = [
    {
        "grid_name": "bollinger_window_grid",
        "indicator_name": "bollinger",
        "family": "range_channel",
        "windows": [10, 20, 30],
        "std_values": [1.5, 2.0, 2.5],
        "components": ["upper", "lower", "width", "pct_b"],
        "description": "Bollinger bantları ve genişlik matrisi.",
    },
    {
        "grid_name": "donchian_window_grid",
        "indicator_name": "donchian",
        "family": "range_channel",
        "windows": [10, 20, 55],
        "components": ["high", "low", "mid", "position"],
        "description": "Donchian kanalları tepe-dip pencere matrisi.",
    },
    {
        "grid_name": "rolling_range_window_grid",
        "indicator_name": "rolling_range",
        "family": "range_channel",
        "windows": [10, 20, 50],
        "components": ["range_abs", "range_pct"],
        "description": "Fiyat aralığı pencere matrisi.",
    },
    {
        "grid_name": "keltner_channel_window_grid",
        "indicator_name": "keltner_channel_placeholder",
        "family": "range_channel",
        "windows": [10, 20, 30],
        "components": ["upper", "lower"],
        "description": "Keltner kanalı placeholder pencere matrisi.",
    },
]


def build_range_channel_window_grid_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []

    for g in RANGE_CHANNEL_GRIDS:
        if g["indicator_name"] == "bollinger":
            for w in g["windows"]:
                for std in g["std_values"]:
                    std_str = str(std).replace(".", "_")
                    if std_str.endswith("_0"):
                        std_str = std_str[:-2]
                    for comp in g["components"]:
                        col_name = f"bb_{comp}_w{w}_std{std_str}"
                        rows.append({
                            "grid_name": g["grid_name"],
                            "indicator_name": g["indicator_name"],
                            "family": g["family"],
                            "window": w,
                            "component": comp,
                            "parameter": f"std={std}",
                            "column_name": col_name,
                            "non_signal": True,
                            "lookahead_free": True,
                        })
        else:
            for w in g["windows"]:
                for comp in g.get("components", ["val"]):
                    col_name = f"{g['indicator_name']}_{comp}_w{w}"
                    rows.append({
                        "grid_name": g["grid_name"],
                        "indicator_name": g["indicator_name"],
                        "family": g["family"],
                        "window": w,
                        "component": comp,
                        "parameter": "",
                        "column_name": col_name,
                        "non_signal": True,
                        "lookahead_free": True,
                    })

    df = pd.DataFrame(rows)
    summary = summarize_range_channel_window_grid(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_range_channel_window_grid(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_grid_features": 0, "status": "EMPTY"}

    return {
        "total_grid_features": len(df),
        "total_indicators": df["indicator_name"].nunique() if "indicator_name" in df.columns else 0,
        "non_signal": True,
        "status": "READY",
    }
