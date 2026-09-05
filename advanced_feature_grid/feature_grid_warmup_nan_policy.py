from typing import Tuple, Dict, Any
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


WARMUP_POLICIES = [
    {
        "family": "moving_average",
        "indicator_name": "sma",
        "policy": "preserve_warmup_nan",
        "rationale": "SMA pencere genişliği kadar (window - 1) başlangıç NaN üretir, silinmez.",
        "auto_drop": False,
        "forward_fill": False,
    },
    {
        "family": "moving_average",
        "indicator_name": "ema",
        "policy": "preserve_warmup_nan",
        "rationale": "EMA başlangıç ağırlık adaptasyonu gerektirir, ilk satırlar korunur.",
        "auto_drop": False,
        "forward_fill": False,
    },
    {
        "family": "momentum",
        "indicator_name": "rsi",
        "policy": "preserve_warmup_nan",
        "rationale": "RSI ilk pencere boyunca ortalama kazanç/kayıp birikimi gerektirir.",
        "auto_drop": False,
        "forward_fill": False,
    },
    {
        "family": "volatility",
        "indicator_name": "atr",
        "policy": "preserve_warmup_nan",
        "rationale": "ATR true range ortalaması için window kadar geçmiş arar.",
        "auto_drop": False,
        "forward_fill": False,
    },
    {
        "family": "range_channel",
        "indicator_name": "bollinger",
        "policy": "preserve_warmup_nan",
        "rationale": "Bollinger Bands standart sapma hesaplaması için pencere tamamlanmalıdır.",
        "auto_drop": False,
        "forward_fill": False,
    },
    {
        "family": "range_channel",
        "indicator_name": "donchian",
        "policy": "preserve_warmup_nan",
        "rationale": "Donchian channel rolling min/max için window tamamlanmalıdır.",
        "auto_drop": False,
        "forward_fill": False,
    },
    {
        "family": "mean_reversion",
        "indicator_name": "rolling_zscore",
        "policy": "preserve_warmup_nan",
        "rationale": "Rolling z-score rolling mean ve std gerektirir.",
        "auto_drop": False,
        "forward_fill": False,
    },
    {
        "family": "volatility",
        "indicator_name": "realized_volatility",
        "policy": "preserve_warmup_nan",
        "rationale": "Realized volatility getiri standart sapması için pencere gerektirir.",
        "auto_drop": False,
        "forward_fill": False,
    },
    {
        "family": "return",
        "indicator_name": "simple_return",
        "policy": "preserve_warmup_nan",
        "rationale": "Periyodik getiri window kadar başlangıç NaN değeri üretir.",
        "auto_drop": False,
        "forward_fill": False,
    },
]


def estimate_grid_warmup_nan_count(indicator_name: str, parameters: Dict[str, Any]) -> int:
    name = indicator_name.lower().strip()
    window = parameters.get("window") or parameters.get("period") or parameters.get("w") or 14

    if name in ("sma", "rolling_std", "rolling_high_low_range", "donchian", "rolling_range"):
        return max(0, window - 1)
    elif name in ("ema", "wma", "dema", "tema"):
        return max(0, window - 1)
    elif name in ("rsi", "cmo", "atr"):
        return max(0, window)
    elif name in ("roc", "momentum", "simple_return", "log_return"):
        return max(0, window)
    elif name in ("bollinger", "rolling_zscore", "realized_volatility"):
        return max(0, window - 1)
    return max(0, window - 1)


def build_feature_grid_warmup_nan_policy_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    df = pd.DataFrame(WARMUP_POLICIES)
    summary = summarize_feature_grid_warmup_nan_policy(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_feature_grid_warmup_nan_policy(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_policies": 0, "status": "EMPTY"}

    return {
        "total_policies": len(df),
        "auto_drop_allowed": False,
        "forward_fill_allowed": False,
        "policy": "preserve_warmup_nan",
        "status": "READY",
    }
