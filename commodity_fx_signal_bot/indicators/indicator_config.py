import os
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Tuple

import pandas as pd


@dataclass
class IndicatorSpec:
    name: str
    category: str
    function_name: str
    default_params: Dict[str, Any] = field(default_factory=dict)
    required_columns: Tuple[str, ...] = field(default_factory=tuple)
    output_columns: Tuple[str, ...] = field(default_factory=tuple)
    warmup_period: int = 0


# Registry of known indicators, their requirements and outputs
_INDICATOR_SPECS = [
    # Trend
    IndicatorSpec(
        "sma_20", "trend", "calculate_sma", {"window": 20}, ("close",), ("sma_20",), 20
    ),
    IndicatorSpec(
        "sma_50", "trend", "calculate_sma", {"window": 50}, ("close",), ("sma_50",), 50
    ),
    IndicatorSpec(
        "sma_200",
        "trend",
        "calculate_sma",
        {"window": 200},
        ("close",),
        ("sma_200",),
        200,
    ),
    IndicatorSpec(
        "ema_20", "trend", "calculate_ema", {"window": 20}, ("close",), ("ema_20",), 20
    ),
    IndicatorSpec(
        "ema_50", "trend", "calculate_ema", {"window": 50}, ("close",), ("ema_50",), 50
    ),
    IndicatorSpec(
        "macd_12_26_9",
        "trend",
        "calculate_macd",
        {"fast": 12, "slow": 26, "signal": 9},
        ("close",),
        ("macd_12_26_9", "macd_signal_12_26_9", "macd_hist_12_26_9"),
        35,  # 26 + 9
    ),
    IndicatorSpec(
        "compact_trend_features", "trend", "build_compact_trend_features", {}, ("open", "high", "low", "close", "volume"), (), 200
    ),
    IndicatorSpec(
        "full_trend_features", "trend", "build_trend_features", {}, ("open", "high", "low", "close", "volume"), (), 200
    ),
    # Volatility
    IndicatorSpec(
        "multi_true_range", "volatility", "calculate_multi_true_range", {}, ("open", "high", "low", "close"), (), 0
    ),
    IndicatorSpec(
        "multi_atr", "volatility", "calculate_multi_atr", {"windows": (7, 14, 21, 28)}, ("high", "low", "close"), (), 28
    ),
    IndicatorSpec(
        "atr_percent", "volatility", "calculate_atr_percent", {"windows": (7, 14, 21, 28)}, ("high", "low", "close"), (), 28
    ),
    IndicatorSpec(
        "multi_bollinger_bands", "volatility", "calculate_multi_bollinger_bands", {"windows": (20, 50), "num_std": 2.0}, ("close",), (), 50
    ),
    IndicatorSpec(
        "multi_keltner_channels", "volatility", "calculate_multi_keltner_channels", {"windows": (20, 50), "atr_window": 14, "multiplier": 2.0}, ("high", "low", "close"), (), 50
    ),
    IndicatorSpec(
        "multi_donchian_channels", "volatility", "calculate_multi_donchian_channels", {"windows": (20, 55)}, ("high", "low"), (), 55
    ),
    IndicatorSpec(
        "historical_volatility_multi", "volatility", "calculate_historical_volatility_multi", {"windows": (10, 20, 50, 100), "annualization": 252}, ("close",), (), 100
    ),
    IndicatorSpec(
        "parkinson_volatility", "volatility", "calculate_parkinson_volatility", {"window": 20, "annualization": 252}, ("high", "low"), (), 20
    ),
    IndicatorSpec(
        "garman_klass_volatility", "volatility", "calculate_garman_klass_volatility", {"window": 20, "annualization": 252}, ("open", "high", "low", "close"), (), 20
    ),
    IndicatorSpec(
        "range_percent", "volatility", "calculate_range_percent", {}, ("high", "low", "close"), (), 0
    ),
    IndicatorSpec(
        "gap_volatility", "volatility", "calculate_gap_volatility", {}, ("open", "close"), (), 1
    ),
    IndicatorSpec(
        "volatility_percentile", "volatility", "calculate_volatility_percentile", {"source_col": "atr_pct_14", "window": 120}, (), (), 120
    ),
    IndicatorSpec(
        "volatility_slope", "volatility", "calculate_volatility_slope", {"source_col": "atr_pct_14", "window": 5}, (), (), 5
    ),
    IndicatorSpec(
        "channel_position", "volatility", "calculate_channel_position", {"upper_col": "bb_upper_20_2", "lower_col": "bb_lower_20_2", "prefix": "bb20"}, ("close",), (), 0
    ),
    IndicatorSpec(
        "volatility_events", "volatility", "build_volatility_event_frame", {}, (), (), 120
    ),
    IndicatorSpec(
        "compact_volatility_features", "volatility", "build_compact_volatility_features", {}, ("open", "high", "low", "close"), (), 120
    ),
    IndicatorSpec(
        "full_volatility_features", "volatility", "build_volatility_features", {}, ("open", "high", "low", "close", "volume"), (), 120
    ),
    IndicatorSpec(
        "atr_14",
        "volatility",
        "calculate_atr",
        {"window": 14},
        ("high", "low", "close"),
        ("atr_14",),
        14,
    ),
    IndicatorSpec(
        "bollinger_20_2",
        "volatility",
        "calculate_bollinger_bands",
        {"window": 20, "num_std": 2.0},
        ("close",),
        (
            "bb_upper_20_2",
            "bb_mid_20_2",
            "bb_lower_20_2",
            "bb_width_20_2",
            "bb_percent_b_20_2",
        ),
        20,
    ),
    IndicatorSpec(
        "keltner_20",
        "volatility",
        "calculate_keltner_channels",
        {"window": 20, "atr_window": 10, "multiplier": 2.0},
        ("high", "low", "close"),
        ("keltner_upper_20", "keltner_mid_20", "keltner_lower_20"),
        20,
    ),
    IndicatorSpec(
        "donchian_20",
        "volatility",
        "calculate_donchian_channels",
        {"window": 20},
        ("high", "low"),
        ("donchian_high_20", "donchian_low_20", "donchian_mid_20"),
        20,
    ),
    IndicatorSpec(
        "historical_volatility_20",
        "volatility",
        "calculate_historical_volatility",
        {"window": 20, "annualization": 252},
        ("close",),
        ("hist_vol_20",),
        20,
    ),
    IndicatorSpec(
        "true_range",
        "volatility",
        "calculate_true_range",
        {},
        ("high", "low", "close"),
        ("true_range",),
        0,
    ),
    # Momentum
    IndicatorSpec(
        "rsi_14", "momentum", "calculate_rsi", {"window": 14}, ("close",), ("rsi_14",), 14
    ),
    IndicatorSpec(
        "stochastic_14_3_3",
        "momentum",
        "calculate_stochastic",
        {"k_window": 14, "d_window": 3, "smooth_k": 3},
        ("high", "low", "close"),
        ("stoch_k_14_3_3", "stoch_d_14_3_3"),
        17,  # 14 + 3
    ),
    IndicatorSpec(
        "williams_r_14",
        "momentum",
        "calculate_williams_r",
        {"window": 14},
        ("high", "low", "close"),
        ("williams_r_14",),
        14,
    ),
    IndicatorSpec(
        "cci_20",
        "momentum",
        "calculate_cci",
        {"window": 20},
        ("high", "low", "close"),
        ("cci_20",),
        20,
    ),
    IndicatorSpec(
        "roc_10", "momentum", "calculate_roc", {"window": 10}, ("close",), ("roc_10",), 10
    ),
    IndicatorSpec(
        "momentum_10",
        "momentum",
        "calculate_momentum",
        {"window": 10},
        ("close",),
        ("mom_10",),
        10,
    ),
    IndicatorSpec(
        "compact_momentum_features", "momentum", "build_compact_momentum_features", {}, ("open", "high", "low", "close", "volume"), (), 20
    ),
    IndicatorSpec(
        "full_momentum_features", "momentum", "build_momentum_features", {}, ("open", "high", "low", "close", "volume"), (), 20
    ),
    IndicatorSpec(
        "momentum_events", "momentum", "build_momentum_event_frame", {}, (), (), 20
    ),
    # Volume
    IndicatorSpec(
        "volume_sma_20",
        "volume",
        "calculate_volume_sma",
        {"window": 20},
        ("volume",),
        ("volume_sma_20",),
        20,
    ),
    IndicatorSpec(
        "vwap",
        "volume",
        "calculate_vwap",
        {},
        ("high", "low", "close", "volume"),
        ("vwap",),
        0,
    ),
    IndicatorSpec(
        "obv",
        "volume",
        "calculate_obv",
        {},
        ("close", "volume"),
        ("obv",),
        0,
    ),
    IndicatorSpec(
        "cmf",
        "volume",
        "calculate_cmf",
        {"window": 20},
        ("high", "low", "close", "volume"),
        ("cmf_20",),
        20,
    ),
    IndicatorSpec(
        "mfi",
        "volume",
        "calculate_mfi",
        {"window": 14},
        ("high", "low", "close", "volume"),
        ("mfi_14",),
        14,
    ),
    # Mean Reversion / Stat
    IndicatorSpec(
        "zscore_close_20",
        "mean_reversion",
        "calculate_zscore",
        {"window": 20, "column": "close"},
        ("close",),
        ("zscore_close_20",),
        20,
    ),
    IndicatorSpec(
        "distance_from_sma_20",
        "mean_reversion",
        "calculate_distance_from_ma",
        {"ma_column": "sma_20", "price_column": "close"},
        ("close", "sma_20"),  # Requires sma_20 to be computed first
        ("dist_close_sma_20",),
        0,
    ),
    # Price Action / Candles
    IndicatorSpec(
        "candle_body",
        "price_action",
        "calculate_candle_body",
        {},
        ("open", "close"),
        ("candle_body",),
        0,
    ),
    IndicatorSpec(
        "candle_range",
        "price_action",
        "calculate_candle_range",
        {},
        ("high", "low"),
        ("candle_range",),
        0,
    ),
    IndicatorSpec(
        "close_position_in_range",
        "price_action",
        "calculate_close_position",
        {},
        ("high", "low", "close"),
        ("close_position_in_range",),
        0,
    ),
    # Transforms / Basic Returns
    IndicatorSpec(
        "return_1",
        "transform",
        "calculate_return",
        {"window": 1},
        ("close",),
        ("return_1",),
        1,
    ),
    IndicatorSpec(
        "return_5",
        "transform",
        "calculate_return",
        {"window": 5},
        ("close",),
        ("return_5",),
        5,
    ),
    IndicatorSpec(
        "log_return_1",
        "transform",
        "calculate_log_return",
        {"window": 1},
        ("close",),
        ("log_return_1",),
        1,
    ),
    IndicatorSpec(
        "volume_zscore_20",
        "transform",
        "calculate_zscore",
        {"window": 20, "column": "volume"},
        ("volume",),
        ("volume_zscore_20",),
        20,
    ),
]


def list_indicator_specs() -> list[IndicatorSpec]:
    """Returns a list of all known indicator specifications."""
    return list(_INDICATOR_SPECS)


def get_indicator_spec(name: str) -> IndicatorSpec:
    """Gets the specification for a specific indicator by name."""
    for spec in _INDICATOR_SPECS:
        if spec.name == name:
            return spec
    raise ValueError(f"Indicator spec '{name}' not found.")


def validate_indicator_specs() -> list[str]:
    """
    Validates all indicator specs for common errors.
    Returns a list of error messages. Empty list means all specs are valid.
    """
    errors = []
    names = set()

    valid_categories = {
        "momentum",
        "trend",
        "volatility",
        "volume",
        "mean_reversion",
        "price_action",
        "transform",
    }

    for spec in _INDICATOR_SPECS:
        if spec.name in names:
            errors.append(f"Duplicate indicator name: {spec.name}")
        names.add(spec.name)

        if spec.category not in valid_categories:
            errors.append(
                f"Invalid category '{spec.category}' for indicator '{spec.name}'"
            )

        if not spec.function_name:
            errors.append(f"Missing function_name for indicator '{spec.name}'")

        if spec.warmup_period < 0:
            errors.append(f"Negative warmup period for indicator '{spec.name}'")

    return errors
