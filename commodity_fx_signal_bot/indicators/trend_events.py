from dataclasses import dataclass
from typing import Optional, Tuple

import pandas as pd


@dataclass
class TrendEventConfig:
    adx_threshold: float = 25.0
    strong_adx_threshold: float = 35.0
    ma_fast: str = "ema_20"
    ma_mid: str = "ema_50"
    ma_slow: str = "ema_200"
    macd_hist_col: str = "macd_hist_12_26_9"
    min_event_strength: float = 0.0


def detect_price_ma_position_events(
    features: pd.DataFrame, config: Optional[TrendEventConfig] = None
) -> pd.DataFrame:
    config = config or TrendEventConfig()
    result = {}
    close = features.get("close")

    if close is not None:
        if config.ma_fast in features.columns:
            fast = features[config.ma_fast]
            result[f"event_price_above_{config.ma_fast}"] = (close > fast).astype(int)
            result[f"event_price_below_{config.ma_fast}"] = (close < fast).astype(int)

        if config.ma_slow in features.columns:
            slow = features[config.ma_slow]
            result[f"event_price_above_{config.ma_slow}"] = (close > slow).astype(int)
            result[f"event_price_below_{config.ma_slow}"] = (close < slow).astype(int)

    return pd.DataFrame(result, index=features.index)


def detect_ma_cross_events(
    features: pd.DataFrame, config: Optional[TrendEventConfig] = None
) -> pd.DataFrame:
    config = config or TrendEventConfig()
    result = {}

    def _add_cross(fast_col, slow_col):
        if fast_col in features.columns and slow_col in features.columns:
            fast = features[fast_col]
            slow = features[slow_col]
            prev_fast = fast.shift(1)
            prev_slow = slow.shift(1)

            cross_above = (prev_fast <= prev_slow) & (fast > slow)
            cross_below = (prev_fast >= prev_slow) & (fast < slow)

            result[f"event_{fast_col}_cross_above_{slow_col}"] = cross_above.astype(int)
            result[f"event_{fast_col}_cross_below_{slow_col}"] = cross_below.astype(int)

    _add_cross(config.ma_fast, config.ma_mid)
    _add_cross(config.ma_mid, config.ma_slow)

    return pd.DataFrame(result, index=features.index)


def detect_ma_stack_events(
    features: pd.DataFrame, config: Optional[TrendEventConfig] = None
) -> pd.DataFrame:
    config = config or TrendEventConfig()
    result = {}

    if (
        config.ma_fast in features.columns
        and config.ma_mid in features.columns
        and config.ma_slow in features.columns
    ):
        fast = features[config.ma_fast]
        mid = features[config.ma_mid]
        slow = features[config.ma_slow]

        bullish = (fast > mid) & (mid > slow)
        bearish = (fast < mid) & (mid < slow)

        result["event_ma_stack_bullish"] = bullish.astype(int)
        result["event_ma_stack_bearish"] = bearish.astype(int)

    return pd.DataFrame(result, index=features.index)


def detect_macd_trend_events(
    features: pd.DataFrame, config: Optional[TrendEventConfig] = None
) -> pd.DataFrame:
    config = config or TrendEventConfig()
    result = {}

    if config.macd_hist_col in features.columns:
        hist = features[config.macd_hist_col]
        prev_hist = hist.shift(1)

        positive_shift = (prev_hist <= 0) & (hist > 0)
        negative_shift = (prev_hist >= 0) & (hist < 0)

        result["event_macd_hist_positive_shift"] = positive_shift.astype(int)
        result["event_macd_hist_negative_shift"] = negative_shift.astype(int)

    macd_line_col = config.macd_hist_col.replace("macd_hist", "macd")
    signal_line_col = config.macd_hist_col.replace("macd_hist", "macd_signal")

    if macd_line_col in features.columns and signal_line_col in features.columns:
        macd_line = features[macd_line_col]
        signal_line = features[signal_line_col]

        above = macd_line > signal_line
        below = macd_line < signal_line

        result["event_macd_line_above_signal"] = above.astype(int)
        result["event_macd_line_below_signal"] = below.astype(int)

    return pd.DataFrame(result, index=features.index)


def detect_adx_strength_events(
    features: pd.DataFrame, config: Optional[TrendEventConfig] = None
) -> pd.DataFrame:
    config = config or TrendEventConfig()
    result = {}

    for col in features.columns:
        if col.startswith("adx_"):
            adx = features[col]
            prev_adx = adx.shift(1)

            trend_strength = adx >= config.adx_threshold
            strong_trend = adx >= config.strong_adx_threshold
            rising = adx > prev_adx
            falling = adx < prev_adx

            result[f"event_{col}_trend_strength"] = trend_strength.astype(int)
            result[f"event_{col}_strong_trend"] = strong_trend.astype(int)
            result[f"event_{col}_rising"] = rising.astype(int)
            result[f"event_{col}_falling"] = falling.astype(int)

    return pd.DataFrame(result, index=features.index)


def detect_dmi_direction_events(
    features: pd.DataFrame, config: Optional[TrendEventConfig] = None
) -> pd.DataFrame:
    result = {}

    # Pair up plus_di and minus_di
    windows = []
    for col in features.columns:
        if col.startswith("plus_di_"):
            window = col.split("_")[-1]
            if f"minus_di_{window}" in features.columns:
                windows.append(window)

    for w in windows:
        plus_di = features[f"plus_di_{w}"]
        minus_di = features[f"minus_di_{w}"]

        bullish = plus_di > minus_di
        bearish = minus_di > plus_di

        result[f"event_dmi_bullish_direction_{w}"] = bullish.astype(int)
        result[f"event_dmi_bearish_direction_{w}"] = bearish.astype(int)

    return pd.DataFrame(result, index=features.index)


def detect_aroon_trend_events(
    features: pd.DataFrame, config: Optional[TrendEventConfig] = None
) -> pd.DataFrame:
    result = {}

    windows = []
    for col in features.columns:
        if col.startswith("aroon_up_"):
            window = col.split("_")[-1]
            if f"aroon_down_{window}" in features.columns:
                windows.append(window)

    for w in windows:
        aroon_up = features[f"aroon_up_{w}"]
        aroon_down = features[f"aroon_down_{w}"]

        bullish = aroon_up > aroon_down
        bearish = aroon_down > aroon_up

        result[f"event_aroon_bullish_{w}"] = bullish.astype(int)
        result[f"event_aroon_bearish_{w}"] = bearish.astype(int)

    return pd.DataFrame(result, index=features.index)


def detect_trend_slope_events(
    features: pd.DataFrame, config: Optional[TrendEventConfig] = None
) -> pd.DataFrame:
    result = {}

    for col in features.columns:
        if col.startswith("slope_"):
            slope = features[col]

            positive = slope > 0
            negative = slope < 0

            result[f"event_ma_slope_positive_{col}"] = positive.astype(int)
            result[f"event_ma_slope_negative_{col}"] = negative.astype(int)

    return pd.DataFrame(result, index=features.index)


def build_trend_event_frame(
    features: pd.DataFrame, config: Optional[TrendEventConfig] = None
) -> Tuple[pd.DataFrame, dict]:
    config = config or TrendEventConfig()

    df_list = []

    df_list.append(detect_price_ma_position_events(features, config))
    df_list.append(detect_ma_cross_events(features, config))
    df_list.append(detect_ma_stack_events(features, config))
    df_list.append(detect_macd_trend_events(features, config))
    df_list.append(detect_adx_strength_events(features, config))
    df_list.append(detect_dmi_direction_events(features, config))
    df_list.append(detect_aroon_trend_events(features, config))
    df_list.append(detect_trend_slope_events(features, config))

    # Filter out empty dataframes
    df_list = [df for df in df_list if not df.empty]

    if not df_list:
        event_df = pd.DataFrame(index=features.index)
    else:
        event_df = pd.concat(df_list, axis=1)

    event_columns = event_df.columns.tolist()

    summary = {
        "input_rows": len(features),
        "event_columns": event_columns,
        "total_event_count": int(event_df.sum().sum()) if not event_df.empty else 0,
        "event_count_by_column": {col: int(event_df[col].sum()) for col in event_columns} if not event_df.empty else {},
        "active_last_row_events": [],
        "warnings": [],
        "notes": "Events are candidate signals, not final buy/sell decisions.",
    }

    if not event_df.empty and len(event_df) > 0:
        last_row = event_df.iloc[-1]
        active = last_row[last_row == 1].index.tolist()
        summary["active_last_row_events"] = active

    return event_df, summary
