from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_models import WindowGridContract, build_window_grid_contract_id


DEFAULT_WINDOW_SETS = {
    "short_grid": [3, 5, 8, 10],
    "medium_grid": [14, 20, 21, 30],
    "long_grid": [50, 100, 150, 200],
    "balanced_grid": [5, 10, 14, 20, 50, 100, 200],
    "volatility_grid": [5, 10, 20, 30, 60],
    "momentum_grid": [5, 10, 14, 20, 30],
    "mean_reversion_grid": [10, 20, 50, 100],
}

CONTRACT_DEFINITIONS = [
    {
        "grid_name": "sma_window_grid",
        "indicator_family": "moving_average",
        "indicator_name": "sma",
        "allowed_windows": [2, 3, 5, 8, 10, 14, 20, 21, 30, 50, 100, 150, 200, 250],
        "default_windows": [5, 10, 20, 50, 100, 200],
        "min_window": 2,
        "max_window": 500,
    },
    {
        "grid_name": "ema_window_grid",
        "indicator_family": "moving_average",
        "indicator_name": "ema",
        "allowed_windows": [2, 3, 5, 8, 10, 14, 20, 21, 30, 50, 100, 150, 200, 250],
        "default_windows": [5, 10, 20, 50, 100, 200],
        "min_window": 2,
        "max_window": 500,
    },
    {
        "grid_name": "wma_window_grid",
        "indicator_family": "moving_average",
        "indicator_name": "wma",
        "allowed_windows": [3, 5, 10, 14, 20, 30, 50],
        "default_windows": [5, 10, 20, 50],
        "min_window": 3,
        "max_window": 100,
    },
    {
        "grid_name": "rsi_window_grid",
        "indicator_family": "momentum",
        "indicator_name": "rsi",
        "allowed_windows": [5, 7, 9, 14, 21, 28, 30],
        "default_windows": [7, 14, 21, 28],
        "min_window": 2,
        "max_window": 100,
    },
    {
        "grid_name": "roc_window_grid",
        "indicator_family": "momentum",
        "indicator_name": "roc",
        "allowed_windows": [1, 3, 5, 10, 14, 20, 30],
        "default_windows": [5, 10, 20, 30],
        "min_window": 1,
        "max_window": 100,
    },
    {
        "grid_name": "atr_window_grid",
        "indicator_family": "volatility",
        "indicator_name": "atr",
        "allowed_windows": [5, 7, 10, 14, 20, 30, 50],
        "default_windows": [7, 14, 20, 30],
        "min_window": 2,
        "max_window": 100,
    },
    {
        "grid_name": "bollinger_window_grid",
        "indicator_family": "range_channel",
        "indicator_name": "bollinger",
        "allowed_windows": [10, 14, 20, 30, 50],
        "default_windows": [10, 20, 30],
        "min_window": 5,
        "max_window": 100,
    },
    {
        "grid_name": "donchian_window_grid",
        "indicator_family": "range_channel",
        "indicator_name": "donchian",
        "allowed_windows": [5, 10, 20, 30, 55, 100],
        "default_windows": [10, 20, 55],
        "min_window": 2,
        "max_window": 250,
    },
    {
        "grid_name": "zscore_window_grid",
        "indicator_family": "mean_reversion",
        "indicator_name": "rolling_zscore",
        "allowed_windows": [5, 10, 20, 30, 50, 100, 200],
        "default_windows": [10, 20, 50, 100],
        "min_window": 5,
        "max_window": 500,
    },
    {
        "grid_name": "realized_volatility_window_grid",
        "indicator_family": "volatility",
        "indicator_name": "realized_volatility",
        "allowed_windows": [5, 10, 20, 30, 60, 90],
        "default_windows": [5, 10, 20, 30, 60],
        "min_window": 3,
        "max_window": 250,
    },
    {
        "grid_name": "return_window_grid",
        "indicator_family": "return",
        "indicator_name": "simple_return",
        "allowed_windows": [1, 2, 3, 5, 10, 20, 50],
        "default_windows": [1, 3, 5, 10, 20],
        "min_window": 1,
        "max_window": 100,
    },
]


def validate_window_grid(
    windows: List[int], min_window: int = 2, max_window: int = 1000
) -> Dict[str, Any]:
    errors = []
    if not windows:
        errors.append("Window listesi boş olamaz.")
        return {"valid": False, "errors": errors, "sanitized_windows": []}

    sanitized = []
    for w in windows:
        if not isinstance(w, int):
            errors.append(f"Geçersiz window tipi: {w}, int bekleniyor.")
            continue
        if w < min_window:
            errors.append(f"Window {w} minimum window sınırı olan {min_window}'den küçük.")
        elif w > max_window:
            errors.append(f"Window {w} maksimum window sınırı olan {max_window}'den büyük.")
        else:
            sanitized.append(w)

    # Sort and remove duplicates
    sanitized = sorted(list(set(sanitized)))
    valid = len(errors) == 0 and len(sanitized) > 0

    return {
        "valid": valid,
        "errors": errors,
        "sanitized_windows": sanitized,
        "window_count": len(sanitized),
    }


def build_window_grid_contract_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []

    for c in CONTRACT_DEFINITIONS:
        contract = WindowGridContract(
            contract_id=build_window_grid_contract_id(c["grid_name"], c["indicator_name"]),
            grid_name=c["grid_name"],
            indicator_family=c["indicator_family"],
            indicator_name=c["indicator_name"],
            allowed_windows=c["allowed_windows"],
            default_windows=c["default_windows"],
            min_window=c["min_window"],
            max_window=c["max_window"],
            warmup_policy="preserve_warmup_nan",
            no_lookahead_policy="strictly_backward_looking",
            non_signal_usage_note="Research feature grid only. Not a trading signal or target label.",
            manual_review_required=False,
        )
        rows.append(contract.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_window_grid_contracts(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_window_grid_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_contracts": 0, "status": "EMPTY"}

    return {
        "total_contracts": len(df),
        "total_families": df["indicator_family"].nunique() if "indicator_family" in df.columns else 0,
        "avg_windows_per_contract": float(df["default_windows"].apply(len).mean()) if "default_windows" in df.columns else 0.0,
        "all_strictly_backward_looking": True,
        "non_signal": True,
        "status": "READY",
    }
