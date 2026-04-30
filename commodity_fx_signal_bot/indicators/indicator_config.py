from dataclasses import dataclass


@dataclass(frozen=True)
class IndicatorSpec:
    name: str
    category: str
    function_name: str
    default_params: dict
    required_columns: tuple[str, ...]
    output_columns: tuple[str, ...]
    warmup_period: int
    enabled: bool = True
    tags: tuple[str, ...] = ()
    notes: str = ""


_BUILTIN_INDICATORS = [
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
        "stoch_14_3",
        "momentum",
        "calculate_stochastic",
        {"window": 14, "smooth_window": 3},
        ("high", "low", "close"),
        ("stoch_k_14_3", "stoch_d_14_3"),
        14,
    ),
    IndicatorSpec(
        "stoch_rsi_14",
        "momentum",
        "calculate_stoch_rsi",
        {"window": 14},
        ("close",),
        ("stoch_rsi_14",),
        14,
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
        ("momentum_10",),
        10,
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
        "ema_200",
        "trend",
        "calculate_ema",
        {"window": 200},
        ("close",),
        ("ema_200",),
        200,
    ),
    IndicatorSpec(
        "macd_12_26_9",
        "trend",
        "calculate_macd",
        {"fast": 12, "slow": 26, "signal": 9},
        ("close",),
        ("macd_12_26_9", "macd_signal_12_26_9", "macd_hist_12_26_9"),
        26,
    ),
    IndicatorSpec(
        "adx_14",
        "trend",
        "calculate_adx",
        {"window": 14},
        ("high", "low", "close"),
        ("adx_14", "plus_di_14", "minus_di_14"),
        14,
    ),
    IndicatorSpec(
        "aroon_25",
        "trend",
        "calculate_aroon",
        {"window": 25},
        ("high", "low"),
        ("aroon_up_25", "aroon_down_25"),
        25,
    ),
    IndicatorSpec(
        "ichimoku_basic",
        "trend",
        "calculate_ichimoku_basic",
        {},
        ("high", "low", "close"),
        ("ichimoku_tenkan", "ichimoku_kijun", "ichimoku_span_a", "ichimoku_span_b"),
        52,
    ),
    # Phase 9 Advanced Trend Specs
    IndicatorSpec(
        "multi_sma", "trend", "calculate_multi_sma", {"windows": (10, 20, 50, 100, 200)}, ("close",), ("sma_10", "sma_20", "sma_50", "sma_100", "sma_200"), 200
    ),
    IndicatorSpec(
        "multi_ema", "trend", "calculate_multi_ema", {"windows": (10, 20, 50, 100, 200)}, ("close",), ("ema_10", "ema_20", "ema_50", "ema_100", "ema_200"), 200
    ),
    IndicatorSpec(
        "wma_20", "trend", "calculate_wma", {"window": 20}, ("close",), ("wma_20",), 20
    ),
    IndicatorSpec(
        "multi_wma", "trend", "calculate_multi_wma", {"windows": (20, 50, 100)}, ("close",), ("wma_20", "wma_50", "wma_100"), 100
    ),
    IndicatorSpec(
        "hma_20", "trend", "calculate_hma", {"window": 20}, ("close",), ("hma_20",), 20
    ),
    IndicatorSpec(
        "multi_hma", "trend", "calculate_multi_hma", {"windows": (20, 50)}, ("close",), ("hma_20", "hma_50"), 50
    ),
    IndicatorSpec(
        "multi_macd", "trend", "calculate_multi_macd", {"configs": ((12, 26, 9), (8, 21, 5), (20, 50, 9))}, ("close",), ("macd_12_26_9", "macd_signal_12_26_9", "macd_hist_12_26_9", "macd_8_21_5", "macd_signal_8_21_5", "macd_hist_8_21_5", "macd_20_50_9", "macd_signal_20_50_9", "macd_hist_20_50_9"), 50
    ),
    IndicatorSpec(
        "dmi_adx_14", "trend", "calculate_dmi_adx", {"window": 14}, ("high", "low", "close"), ("adx_14", "plus_di_14", "minus_di_14"), 14
    ),
    IndicatorSpec(
        "multi_adx", "trend", "calculate_multi_adx", {"windows": (14, 21)}, ("high", "low", "close"), ("adx_14", "plus_di_14", "minus_di_14", "adx_21", "plus_di_21", "minus_di_21"), 21
    ),
    IndicatorSpec(
        "multi_aroon", "trend", "calculate_multi_aroon", {"windows": (14, 25)}, ("high", "low"), ("aroon_up_14", "aroon_down_14", "aroon_up_25", "aroon_down_25"), 25
    ),
    IndicatorSpec(
        "ichimoku_full", "trend", "calculate_ichimoku_full", {}, ("high", "low", "close"), ("ichimoku_tenkan", "ichimoku_kijun", "ichimoku_span_a", "ichimoku_span_b", "ichimoku_chikou"), 52
    ),
    IndicatorSpec(
        "price_ma_distances", "trend", "calculate_price_ma_distances", {"ma_columns": ["sma_20", "sma_50", "sma_200", "ema_20", "ema_50"]}, ("close",), ("dist_close_sma_20", "dist_close_sma_50", "dist_close_sma_200", "dist_close_ema_20", "dist_close_ema_50"), 0
    ),
    IndicatorSpec(
        "ma_slopes", "trend", "calculate_ma_slopes", {"ma_columns": ["sma_20", "ema_20"], "slope_window": 5}, (), ("slope_sma_20_5", "slope_ema_20_5"), 5
    ),
    IndicatorSpec(
        "ma_stack_state", "trend", "calculate_ma_stack_state", {"fast_col": "ema_20", "mid_col": "ema_50", "slow_col": "ema_200"}, (), ("ma_stack_bullish_20_50_200", "ma_stack_bearish_20_50_200"), 0
    ),
    IndicatorSpec(
        "trend_persistence", "trend", "calculate_trend_persistence", {"window": 10}, ("close",), ("trend_persistence_close_10",), 10
    ),
    IndicatorSpec(
        "trend_events", "trend", "build_trend_event_frame", {}, (), (), 0
    ),
    IndicatorSpec(
        "compact_trend_features", "trend", "build_compact_trend_features", {}, ("open", "high", "low", "close", "volume"), (), 200
    ),
    IndicatorSpec(
        "full_trend_features", "trend", "build_trend_features", {}, ("open", "high", "low", "close", "volume"), (), 200
    ),
    # Volatility
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
        1,
    ),
    # Volume
    IndicatorSpec(
        "obv", "volume", "calculate_obv", {}, ("close", "volume"), ("obv",), 1
    ),
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
        "volume_zscore_20",
        "volume",
        "calculate_volume_zscore",
        {"window": 20},
        ("volume",),
        ("volume_zscore_20",),
        20,
    ),
    IndicatorSpec(
        "mfi_14",
        "volume",
        "calculate_mfi",
        {"window": 14},
        ("high", "low", "close", "volume"),
        ("mfi_14",),
        14,
    ),
    IndicatorSpec(
        "cmf_20",
        "volume",
        "calculate_cmf",
        {"window": 20},
        ("high", "low", "close", "volume"),
        ("cmf_20",),
        20,
    ),
    # Mean Reversion
    IndicatorSpec(
        "zscore_close_20",
        "mean_reversion",
        "calculate_zscore_close",
        {"window": 20},
        ("close",),
        ("zscore_close_20",),
        20,
    ),
    IndicatorSpec(
        "distance_from_sma_20",
        "mean_reversion",
        "calculate_distance_from_sma",
        {"window": 20},
        ("close",),
        ("dist_sma_20",),
        20,
    ),
    IndicatorSpec(
        "distance_from_ema_20",
        "mean_reversion",
        "calculate_distance_from_ema",
        {"window": 20},
        ("close",),
        ("dist_ema_20",),
        20,
    ),
    IndicatorSpec(
        "bollinger_percent_b",
        "mean_reversion",
        "calculate_bollinger_percent_b",
        {"window": 20, "num_std": 2.0},
        ("close",),
        ("bb_percent_b_20_2",),
        20,
    ),
    IndicatorSpec(
        "bollinger_bandwidth",
        "mean_reversion",
        "calculate_bollinger_bandwidth",
        {"window": 20, "num_std": 2.0},
        ("close",),
        ("bb_bandwidth_20_2",),
        20,
    ),
    # Price Action
    IndicatorSpec(
        "candle_body",
        "price_action",
        "calculate_candle_body",
        {},
        ("open", "close"),
        ("candle_body", "candle_body_pct"),
        1,
    ),
    IndicatorSpec(
        "candle_range",
        "price_action",
        "calculate_candle_range",
        {},
        ("high", "low"),
        ("candle_range",),
        1,
    ),
    IndicatorSpec(
        "upper_wick",
        "price_action",
        "calculate_wicks",
        {},
        ("open", "high", "low", "close"),
        ("upper_wick", "lower_wick"),
        1,
    ),
    IndicatorSpec(
        "lower_wick",
        "price_action",
        "calculate_wicks",
        {},
        ("open", "high", "low", "close"),
        ("upper_wick", "lower_wick"),
        1,
    ),
    IndicatorSpec(
        "close_position_in_range",
        "price_action",
        "calculate_close_position_in_range",
        {},
        ("high", "low", "close"),
        ("close_pos_range",),
        1,
    ),
    IndicatorSpec(
        "gap_percent",
        "price_action",
        "calculate_gap_percent",
        {},
        ("open", "close"),
        ("gap_percent",),
        1,
    ),
    IndicatorSpec(
        "return_1",
        "price_action",
        "calculate_returns",
        {"periods": (1,)},
        ("close",),
        ("return_1",),
        1,
    ),
    IndicatorSpec(
        "return_5",
        "price_action",
        "calculate_returns",
        {"periods": (5,)},
        ("close",),
        ("return_5",),
        5,
    ),
    IndicatorSpec(
        "log_return_1",
        "price_action",
        "calculate_log_returns",
        {"periods": (1,)},
        ("close",),
        ("log_return_1",),
        1,
    ),
]

_INDICATOR_REGISTRY_MAP = {spec.name: spec for spec in _BUILTIN_INDICATORS}


def get_indicator_spec(name: str) -> IndicatorSpec:
    spec = _INDICATOR_REGISTRY_MAP.get(name)
    if not spec:
        raise ValueError(f"Indicator specification for '{name}' not found.")
    return spec


def list_indicator_specs(enabled_only: bool = True) -> list[IndicatorSpec]:
    if enabled_only:
        return [spec for spec in _BUILTIN_INDICATORS if spec.enabled]
    return _BUILTIN_INDICATORS


def list_indicator_specs_by_category(category: str) -> list[IndicatorSpec]:
    return [spec for spec in _BUILTIN_INDICATORS if spec.category == category]


def validate_indicator_specs() -> None:
    seen_names = set()
    valid_categories = {
        "momentum",
        "trend",
        "volatility",
        "volume",
        "mean_reversion",
        "price_action",
        "transform",
    }

    for spec in _BUILTIN_INDICATORS:
        if spec.name in seen_names:
            raise ValueError(f"Duplicate indicator name found: {spec.name}")
        seen_names.add(spec.name)

        if not spec.category:
            raise ValueError(f"Indicator {spec.name} is missing a category.")

        if spec.category not in valid_categories:
            raise ValueError(
                f"Indicator {spec.name} has an invalid category: {spec.category}. Must be one of {valid_categories}"
            )

        if not isinstance(spec.required_columns, tuple):
            raise ValueError(f"Indicator {spec.name} required_columns must be a tuple.")

        if not isinstance(spec.output_columns, tuple):
            raise ValueError(f"Indicator {spec.name} output_columns must be a tuple.")

        if spec.warmup_period < 0:
            raise ValueError(f"Indicator {spec.name} warmup_period cannot be negative.")


def summarize_indicator_specs() -> dict:
    categories = {}
    for spec in _BUILTIN_INDICATORS:
        categories[spec.category] = categories.get(spec.category, 0) + 1

    return {
        "total_indicators": len(_BUILTIN_INDICATORS),
        "enabled_indicators": sum(1 for spec in _BUILTIN_INDICATORS if spec.enabled),
        "categories": categories,
    }
