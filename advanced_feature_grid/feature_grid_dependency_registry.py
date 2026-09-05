from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


FEATURE_GRID_DEPENDENCIES = [
    {
        "grid_name": "sma_window_grid",
        "primary_input_fields": ["close"],
        "optional_input_fields": [],
        "intermediate_computations": ["rolling_mean"],
        "target_family": "moving_average",
    },
    {
        "grid_name": "ema_window_grid",
        "primary_input_fields": ["close"],
        "optional_input_fields": [],
        "intermediate_computations": ["exponential_moving_average"],
        "target_family": "moving_average",
    },
    {
        "grid_name": "rsi_window_grid",
        "primary_input_fields": ["close"],
        "optional_input_fields": [],
        "intermediate_computations": ["diff", "gain_loss_rolling_mean"],
        "target_family": "momentum",
    },
    {
        "grid_name": "roc_window_grid",
        "primary_input_fields": ["close"],
        "optional_input_fields": [],
        "intermediate_computations": ["shift", "percentage_change"],
        "target_family": "momentum",
    },
    {
        "grid_name": "atr_window_grid",
        "primary_input_fields": ["high", "low", "close"],
        "optional_input_fields": [],
        "intermediate_computations": ["true_range", "rolling_mean"],
        "target_family": "volatility",
    },
    {
        "grid_name": "bollinger_window_grid",
        "primary_input_fields": ["close"],
        "optional_input_fields": [],
        "intermediate_computations": ["rolling_mean", "rolling_std"],
        "target_family": "range_channel",
    },
    {
        "grid_name": "donchian_window_grid",
        "primary_input_fields": ["high", "low", "close"],
        "optional_input_fields": [],
        "intermediate_computations": ["rolling_max", "rolling_min"],
        "target_family": "range_channel",
    },
    {
        "grid_name": "rolling_zscore_window_grid",
        "primary_input_fields": ["close"],
        "optional_input_fields": [],
        "intermediate_computations": ["rolling_mean", "rolling_std"],
        "target_family": "mean_reversion",
    },
    {
        "grid_name": "realized_volatility_window_grid",
        "primary_input_fields": ["close"],
        "optional_input_fields": [],
        "intermediate_computations": ["log_returns", "rolling_std"],
        "target_family": "volatility",
    },
    {
        "grid_name": "return_window_grid",
        "primary_input_fields": ["close"],
        "optional_input_fields": [],
        "intermediate_computations": ["shift", "ratio"],
        "target_family": "return",
    },
]


def build_feature_grid_dependency_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    df = pd.DataFrame(FEATURE_GRID_DEPENDENCIES)
    summary = summarize_feature_grid_dependency_registry(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_feature_grid_dependency_registry(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_dependencies": 0, "status": "EMPTY"}

    return {
        "total_dependencies": len(df),
        "total_families": df["target_family"].nunique() if "target_family" in df.columns else 0,
        "input_types": ["price_fields", "volume_fields"],
        "no_forward_dependencies": True,
        "status": "READY",
    }
