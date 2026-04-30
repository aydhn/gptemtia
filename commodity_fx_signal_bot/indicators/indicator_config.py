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
        "compact_trend_features",
        "trend",
        "build_compact_trend_features",
        {},
        ("open", "high", "low", "close", "volume"),
        (),
        200,
    ),
    IndicatorSpec(
        "full_trend_features",
        "trend",
        "build_trend_features",
        {},
        ("open", "high", "low", "close", "volume"),
        (),
        200,
    ),
    # Phase 9 Advanced Trend Specs
    IndicatorSpec(
        "multi_sma",
        "trend",
        "calculate_multi_sma",
        {"windows": (10, 20, 50, 100, 200)},
        ("close",),
        ("sma_10", "sma_20", "sma_50", "sma_100", "sma_200"),
        200,
    ),
    IndicatorSpec(
        "multi_ema",
        "trend",
        "calculate_multi_ema",
        {"windows": (10, 20, 50, 100, 200)},
        ("close",),
        ("ema_10", "ema_20", "ema_50", "ema_100", "ema_200"),
        200,
    ),
    IndicatorSpec(
        "wma_20", "trend", "calculate_wma", {"window": 20}, ("close",), ("wma_20",), 20
    ),
    IndicatorSpec(
        "multi_wma",
        "trend",
        "calculate_multi_wma",
        {"windows": (20, 50, 100)},
        ("close",),
        ("wma_20", "wma_50", "wma_100"),
        100,
    ),
    IndicatorSpec(
        "hma_20", "trend", "calculate_hma", {"window": 20}, ("close",), ("hma_20",), 20
    ),
    IndicatorSpec(
        "multi_hma",
        "trend",
        "calculate_multi_hma",
        {"windows": (20, 50)},
        ("close",),
        ("hma_20", "hma_50"),
        50,
    ),
    IndicatorSpec(
        "multi_macd",
        "trend",
        "calculate_multi_macd",
        {"configs": ((12, 26, 9), (8, 21, 5), (20, 50, 9))},
        ("close",),
        (
            "macd_12_26_9",
            "macd_signal_12_26_9",
            "macd_hist_12_26_9",
            "macd_8_21_5",
            "macd_signal_8_21_5",
            "macd_hist_8_21_5",
            "macd_20_50_9",
            "macd_signal_20_50_9",
            "macd_hist_20_50_9",
        ),
        50,
    ),
    IndicatorSpec(
        "dmi_adx_14",
        "trend",
        "calculate_dmi_adx",
        {"window": 14},
        ("high", "low", "close"),
        ("adx_14", "plus_di_14", "minus_di_14"),
        14,
    ),
    IndicatorSpec(
        "multi_adx",
        "trend",
        "calculate_multi_adx",
        {"windows": (14, 21)},
        ("high", "low", "close"),
        ("adx_14", "plus_di_14", "minus_di_14", "adx_21", "plus_di_21", "minus_di_21"),
        21,
    ),
    IndicatorSpec(
        "multi_aroon",
        "trend",
        "calculate_multi_aroon",
        {"windows": (14, 25)},
        ("high", "low"),
        ("aroon_up_14", "aroon_down_14", "aroon_up_25", "aroon_down_25"),
        25,
    ),
    IndicatorSpec(
        "ichimoku_full",
        "trend",
        "calculate_ichimoku_full",
        {},
        ("high", "low", "close"),
        (
            "ichimoku_tenkan",
            "ichimoku_kijun",
            "ichimoku_span_a",
            "ichimoku_span_b",
            "ichimoku_chikou",
        ),
        52,
    ),
    IndicatorSpec(
        "price_ma_distances",
        "trend",
        "calculate_price_ma_distances",
        {"ma_columns": ["sma_20", "sma_50", "sma_200", "ema_20", "ema_50"]},
        ("close",),
        (
            "dist_close_sma_20",
            "dist_close_sma_50",
            "dist_close_sma_200",
            "dist_close_ema_20",
            "dist_close_ema_50",
        ),
        0,
    ),
    IndicatorSpec(
        "ma_slopes",
        "trend",
        "calculate_ma_slopes",
        {"ma_columns": ["sma_20", "ema_20"], "slope_window": 5},
        (),
        ("slope_sma_20_5", "slope_ema_20_5"),
        5,
    ),
    IndicatorSpec(
        "ma_stack_state",
        "trend",
        "calculate_ma_stack_state",
        {"fast_col": "ema_20", "mid_col": "ema_50", "slow_col": "ema_200"},
        (),
        ("ma_stack_bullish_20_50_200", "ma_stack_bearish_20_50_200"),
        0,
    ),
    IndicatorSpec(
        "trend_persistence",
        "trend",
        "calculate_trend_persistence",
        {"window": 10},
        ("close",),
        ("trend_persistence_close_10",),
        10,
    ),
    # Volatility
    IndicatorSpec(
        "multi_true_range",
        "volatility",
        "calculate_multi_true_range",
        {},
        ("open", "high", "low", "close"),
        (),
        0,
    ),
    IndicatorSpec(
        "multi_atr",
        "volatility",
        "calculate_multi_atr",
        {"windows": (7, 14, 21, 28)},
        ("high", "low", "close"),
        (),
        28,
    ),
    IndicatorSpec(
        "atr_percent",
        "volatility",
        "calculate_atr_percent",
        {"windows": (7, 14, 21, 28)},
        ("high", "low", "close"),
        (),
        28,
    ),
    IndicatorSpec(
        "multi_bollinger_bands",
        "volatility",
        "calculate_multi_bollinger_bands",
        {"windows": (20, 50), "num_std": 2.0},
        ("close",),
        (),
        50,
    ),
    IndicatorSpec(
        "multi_keltner_channels",
        "volatility",
        "calculate_multi_keltner_channels",
        {"windows": (20, 50), "atr_window": 14, "multiplier": 2.0},
        ("high", "low", "close"),
        (),
        50,
    ),
    IndicatorSpec(
        "multi_donchian_channels",
        "volatility",
        "calculate_multi_donchian_channels",
        {"windows": (20, 55)},
        ("high", "low"),
        (),
        55,
    ),
    IndicatorSpec(
        "historical_volatility_multi",
        "volatility",
        "calculate_historical_volatility_multi",
        {"windows": (10, 20, 50, 100), "annualization": 252},
        ("close",),
        (),
        100,
    ),
    IndicatorSpec(
        "parkinson_volatility",
        "volatility",
        "calculate_parkinson_volatility",
        {"window": 20, "annualization": 252},
        ("high", "low"),
        (),
        20,
    ),
    IndicatorSpec(
        "garman_klass_volatility",
        "volatility",
        "calculate_garman_klass_volatility",
        {"window": 20, "annualization": 252},
        ("open", "high", "low", "close"),
        (),
        20,
    ),
    IndicatorSpec(
        "range_percent",
        "volatility",
        "calculate_range_percent",
        {},
        ("high", "low", "close"),
        (),
        0,
    ),
    IndicatorSpec(
        "gap_volatility",
        "volatility",
        "calculate_gap_volatility",
        {},
        ("open", "close"),
        (),
        1,
    ),
    IndicatorSpec(
        "volatility_percentile",
        "volatility",
        "calculate_volatility_percentile",
        {"source_col": "atr_pct_14", "window": 120},
        (),
        (),
        120,
    ),
    IndicatorSpec(
        "volatility_slope",
        "volatility",
        "calculate_volatility_slope",
        {"source_col": "atr_pct_14", "window": 5},
        (),
        (),
        5,
    ),
    IndicatorSpec(
        "channel_position",
        "volatility",
        "calculate_channel_position",
        {"upper_col": "bb_upper_20_2", "lower_col": "bb_lower_20_2", "prefix": "bb20"},
        ("close",),
        (),
        0,
    ),
    IndicatorSpec(
        "volatility_events",
        "volatility",
        "build_volatility_event_frame",
        {},
        (),
        (),
        120,
    ),
    IndicatorSpec(
        "compact_volatility_features",
        "volatility",
        "build_compact_volatility_features",
        {},
        ("open", "high", "low", "close"),
        (),
        120,
    ),
    IndicatorSpec(
        "full_volatility_features",
        "volatility",
        "build_volatility_features",
        {},
        ("open", "high", "low", "close", "volume"),
        (),
        120,
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
        "rsi_14",
        "momentum",
        "calculate_rsi",
        {"window": 14},
        ("close",),
        ("rsi_14",),
        14,
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
        "roc_10",
        "momentum",
        "calculate_roc",
        {"window": 10},
        ("close",),
        ("roc_10",),
        10,
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
        "compact_momentum_features",
        "momentum",
        "build_compact_momentum_features",
        {},
        ("open", "high", "low", "close", "volume"),
        (),
        20,
    ),
    IndicatorSpec(
        "full_momentum_features",
        "momentum",
        "build_momentum_features",
        {},
        ("open", "high", "low", "close", "volume"),
        (),
        20,
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
    # Phase 12: Advanced Mean Reversion
    IndicatorSpec(
        "multi_zscore_close",
        "mean_reversion",
        "calculate_multi_zscore_close",
        {"windows": (20, 50, 100)},
        ("close",),
        (),
        100,
    ),
    IndicatorSpec(
        "multi_rolling_mean_distance",
        "mean_reversion",
        "calculate_multi_rolling_mean_distance",
        {"windows": (20, 50, 100)},
        ("close",),
        (),
        100,
    ),
    IndicatorSpec(
        "multi_sma_distance",
        "mean_reversion",
        "calculate_multi_sma_distance",
        {"windows": (20, 50, 100, 200)},
        ("close",),
        (),
        200,
    ),
    IndicatorSpec(
        "multi_ema_distance",
        "mean_reversion",
        "calculate_multi_ema_distance",
        {"windows": (20, 50, 100, 200)},
        ("close",),
        (),
        200,
    ),
    IndicatorSpec(
        "rolling_percentile_rank",
        "mean_reversion",
        "calculate_rolling_percentile_rank",
        {"source_col": "close", "window": 120},
        ("close",),
        (),
        120,
    ),
    IndicatorSpec(
        "multi_percentile_rank",
        "mean_reversion",
        "calculate_multi_percentile_rank",
        {"windows": (60, 120, 252)},
        ("close",),
        (),
        252,
    ),
    IndicatorSpec(
        "rolling_minmax_position",
        "mean_reversion",
        "calculate_rolling_minmax_position",
        {"windows": (20, 50, 100)},
        ("close",),
        (),
        100,
    ),
    IndicatorSpec(
        "bollinger_reversion_features",
        "mean_reversion",
        "calculate_bollinger_reversion_features",
        {"windows": (20, 50), "num_std": 2.0},
        ("close",),
        (),
        50,
    ),
    IndicatorSpec(
        "channel_deviation_features",
        "mean_reversion",
        "calculate_channel_deviation_features",
        {"windows": (20, 55)},
        ("high", "low", "close"),
        (),
        55,
    ),
    IndicatorSpec(
        "overextension_score",
        "mean_reversion",
        "calculate_overextension_score",
        {"window": 20},
        ("close",),
        (),
        20,
    ),
    IndicatorSpec(
        "snapback_pressure",
        "mean_reversion",
        "calculate_snapback_pressure",
        {"zscore_col": "zscore_close_20"},
        (),
        (),
        1,
    ),
    IndicatorSpec(
        "reversion_half_life_proxy",
        "mean_reversion",
        "calculate_reversion_half_life_proxy",
        {"window": 50},
        ("close",),
        (),
        50,
    ),
    IndicatorSpec(
        "range_position_features",
        "mean_reversion",
        "calculate_range_position_features",
        {"windows": (20, 50, 100)},
        ("high", "low", "close"),
        (),
        100,
    ),
    IndicatorSpec(
        "mean_reversion_event_frame",
        "mean_reversion",
        "build_mean_reversion_event_frame",
        {},
        (),
        (),
        120,
    ),
    IndicatorSpec(
        "compact_mean_reversion_feature_set",
        "mean_reversion",
        "build_compact_mean_reversion_features",
        {},
        ("open", "high", "low", "close"),
        (),
        120,
    ),
    IndicatorSpec(
        "full_mean_reversion_feature_set",
        "mean_reversion",
        "build_mean_reversion_features",
        {},
        ("open", "high", "low", "close"),
        (),
        252,
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
