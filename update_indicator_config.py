with open("commodity_fx_signal_bot/indicators/indicator_config.py", "r") as f:
    content = f.read()

new_specs = """    # Phase 9 Advanced Trend Specs
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
"""

if "multi_sma" not in content:
    content = content.replace(
        "    # Volatility",
        new_specs + "    # Volatility"
    )
    with open("commodity_fx_signal_bot/indicators/indicator_config.py", "w") as f:
        f.write(content)
