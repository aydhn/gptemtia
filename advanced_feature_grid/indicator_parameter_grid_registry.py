import itertools
from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_models import IndicatorParameterGrid, build_indicator_parameter_grid_id


PARAMETER_GRID_CATALOG = [
    {
        "indicator_name": "sma",
        "indicator_family": "moving_average",
        "parameter_grid": {"window": [5, 10, 20, 50, 100, 200]},
        "output_naming_template": "sma_w{window}",
    },
    {
        "indicator_name": "ema",
        "indicator_family": "moving_average",
        "parameter_grid": {"window": [5, 10, 20, 50, 100, 200]},
        "output_naming_template": "ema_w{window}",
    },
    {
        "indicator_name": "wma",
        "indicator_family": "moving_average",
        "parameter_grid": {"window": [5, 10, 20, 50]},
        "output_naming_template": "wma_w{window}",
    },
    {
        "indicator_name": "rsi",
        "indicator_family": "momentum",
        "parameter_grid": {"window": [7, 14, 21, 28]},
        "output_naming_template": "rsi_w{window}",
    },
    {
        "indicator_name": "roc",
        "indicator_family": "momentum",
        "parameter_grid": {"window": [5, 10, 20, 30]},
        "output_naming_template": "roc_w{window}",
    },
    {
        "indicator_name": "atr",
        "indicator_family": "volatility",
        "parameter_grid": {"window": [7, 14, 20, 30]},
        "output_naming_template": "atr_w{window}",
    },
    {
        "indicator_name": "bollinger",
        "indicator_family": "range_channel",
        "parameter_grid": {
            "window": [10, 20, 30],
            "num_std": [1.5, 2.0, 2.5],
        },
        "output_naming_template": "bb_w{window}_std{num_std}",
    },
    {
        "indicator_name": "donchian",
        "indicator_family": "range_channel",
        "parameter_grid": {"window": [10, 20, 55]},
        "output_naming_template": "donchian_w{window}",
    },
    {
        "indicator_name": "rolling_zscore",
        "indicator_family": "mean_reversion",
        "parameter_grid": {"window": [10, 20, 50, 100]},
        "output_naming_template": "zscore_w{window}",
    },
    {
        "indicator_name": "realized_volatility",
        "indicator_family": "volatility",
        "parameter_grid": {"window": [5, 10, 20, 30, 60]},
        "output_naming_template": "realized_vol_w{window}",
    },
    {
        "indicator_name": "simple_return",
        "indicator_family": "return",
        "parameter_grid": {"window": [1, 3, 5, 10, 20]},
        "output_naming_template": "return_w{window}",
    },
]


def expand_parameter_grid(parameter_grid: Dict[str, List[Any]]) -> List[Dict[str, Any]]:
    if not parameter_grid:
        return [{}]

    keys = list(parameter_grid.keys())
    values = [parameter_grid[k] if isinstance(parameter_grid[k], list) else [parameter_grid[k]] for k in keys]

    expanded = []
    for combination in itertools.product(*values):
        expanded.append(dict(zip(keys, combination)))
    return expanded


def build_indicator_parameter_grid_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []

    for item in PARAMETER_GRID_CATALOG:
        expanded_combinations = expand_parameter_grid(item["parameter_grid"])
        expected_count = len(expanded_combinations)

        grid = IndicatorParameterGrid(
            grid_id=build_indicator_parameter_grid_id(item["indicator_name"], item["indicator_family"]),
            indicator_name=item["indicator_name"],
            indicator_family=item["indicator_family"],
            parameter_grid=item["parameter_grid"],
            output_naming_template=item["output_naming_template"],
            expected_output_count=expected_count,
            non_signal=True,
            manual_review_required=False,
        )
        rows.append(grid.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_indicator_parameter_grids(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_indicator_parameter_grids(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_grids": 0, "total_expected_features": 0, "status": "EMPTY"}

    total_expected = int(df["expected_output_count"].sum()) if "expected_output_count" in df.columns else 0
    return {
        "total_grids": len(df),
        "total_families": df["indicator_family"].nunique() if "indicator_family" in df.columns else 0,
        "total_expected_features": total_expected,
        "non_signal": True,
        "status": "READY",
    }
