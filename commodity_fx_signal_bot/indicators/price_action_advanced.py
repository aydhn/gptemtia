import numpy as np
import pandas as pd


def calculate_candle_anatomy(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate basic candle anatomy elements."""
    # df format check
    if not all(col in df.columns for col in ["open", "high", "low", "close"]):
        raise ValueError("Missing required OHLC columns")

    res = pd.DataFrame(index=df.index)
    res["candle_body"] = df["close"] - df["open"]
    res["candle_body_abs"] = res["candle_body"].abs()

    # pct (relative to open)
    res["candle_body_pct"] = res["candle_body"] / df["open"]
    res["candle_body_pct"] = res["candle_body_pct"].replace([np.inf, -np.inf], np.nan)

    res["candle_range"] = df["high"] - df["low"]
    res["candle_range_pct"] = res["candle_range"] / df["low"]
    res["candle_range_pct"] = res["candle_range_pct"].replace([np.inf, -np.inf], np.nan)

    res["upper_wick"] = df["high"] - df[["open", "close"]].max(axis=1)
    res["lower_wick"] = df[["open", "close"]].min(axis=1) - df["low"]

    res["upper_wick_pct"] = res["upper_wick"] / df["high"]
    res["lower_wick_pct"] = res["lower_wick"] / df["low"]
    res["upper_wick_pct"] = res["upper_wick_pct"].replace([np.inf, -np.inf], np.nan)
    res["lower_wick_pct"] = res["lower_wick_pct"].replace([np.inf, -np.inf], np.nan)

    return res


def calculate_candle_ratios(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate ratios of candle parts."""
    anatomy = calculate_candle_anatomy(df)
    res = pd.DataFrame(index=df.index)

    res["body_to_range_ratio"] = anatomy["candle_body_abs"] / anatomy["candle_range"]
    res["upper_wick_to_range_ratio"] = anatomy["upper_wick"] / anatomy["candle_range"]
    res["lower_wick_to_range_ratio"] = anatomy["lower_wick"] / anatomy["candle_range"]

    res = res.replace([np.inf, -np.inf], np.nan)
    return res


def calculate_close_location_features(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate where close/open are relative to the range."""
    res = pd.DataFrame(index=df.index)
    candle_range = df["high"] - df["low"]

    close_pos = (df["close"] - df["low"]) / candle_range
    open_pos = (df["open"] - df["low"]) / candle_range

    res["close_pos_range"] = close_pos.replace([np.inf, -np.inf, np.nan], 0.5)
    res["open_pos_range"] = open_pos.replace([np.inf, -np.inf, np.nan], 0.5)

    res["close_above_open"] = (df["close"] > df["open"]).astype(int)
    res["close_below_open"] = (df["close"] < df["open"]).astype(int)

    return res


def calculate_range_features(
    df: pd.DataFrame, windows: tuple[int, ...] = (5, 10, 20, 50)
) -> pd.DataFrame:
    """Calculate moving averages and z-scores of candle range."""
    res = pd.DataFrame(index=df.index)
    candle_range = df["high"] - df["low"]

    for w in windows:
        res[f"range_sma_{w}"] = candle_range.rolling(window=w).mean()

    if 20 in windows:
        roll_mean = candle_range.rolling(window=20).mean()
        roll_std = candle_range.rolling(window=20).std()
        res["range_zscore_20"] = (candle_range - roll_mean) / roll_std
        res["range_zscore_20"] = res["range_zscore_20"].replace(
            [np.inf, -np.inf], np.nan
        )

    return res


def calculate_body_features(
    df: pd.DataFrame, windows: tuple[int, ...] = (5, 10, 20, 50)
) -> pd.DataFrame:
    """Calculate moving averages and z-scores of candle body."""
    res = pd.DataFrame(index=df.index)
    body_abs = (df["close"] - df["open"]).abs()

    for w in windows:
        res[f"body_sma_{w}"] = body_abs.rolling(window=w).mean()

    if 20 in windows:
        roll_mean = body_abs.rolling(window=20).mean()
        roll_std = body_abs.rolling(window=20).std()
        res["body_zscore_20"] = (body_abs - roll_mean) / roll_std
        res["body_zscore_20"] = res["body_zscore_20"].replace([np.inf, -np.inf], np.nan)

    return res


def calculate_wick_features(
    df: pd.DataFrame, windows: tuple[int, ...] = (5, 10, 20)
) -> pd.DataFrame:
    """Calculate wick imbalance and rolling metrics."""
    res = pd.DataFrame(index=df.index)
    anatomy = calculate_candle_anatomy(df)

    # Wick imbalance: positive means upper wick > lower wick
    res["wick_imbalance"] = anatomy["upper_wick"] - anatomy["lower_wick"]

    return res


def calculate_gap_features(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate gap between previous close and current open."""
    res = pd.DataFrame(index=df.index)
    prev_close = df["close"].shift(1)

    gap = df["open"] - prev_close
    res["gap_pct"] = gap / prev_close
    res["gap_pct"] = res["gap_pct"].replace([np.inf, -np.inf], np.nan)
    res["abs_gap_pct"] = res["gap_pct"].abs()

    res["gap_direction"] = np.sign(gap)
    res["gap_direction"] = res["gap_direction"].fillna(0)

    return res


def calculate_inside_outside_bars(df: pd.DataFrame) -> pd.DataFrame:
    """Detect inside and outside bars."""
    res = pd.DataFrame(index=df.index)
    prev_high = df["high"].shift(1)
    prev_low = df["low"].shift(1)

    is_inside = (df["high"] <= prev_high) & (df["low"] >= prev_low)
    # Exclude exact match to prevent identical bars being both inside and outside
    is_inside = is_inside & ~((df["high"] == prev_high) & (df["low"] == prev_low))

    is_outside = (df["high"] > prev_high) & (df["low"] < prev_low)

    res["inside_bar"] = is_inside.astype(int)
    res["outside_bar"] = is_outside.astype(int)

    return res


def calculate_breakout_levels(
    df: pd.DataFrame, windows: tuple[int, ...] = (10, 20, 55)
) -> pd.DataFrame:
    """Calculate breakout levels (Donchian channels roughly without shift)."""
    res = pd.DataFrame(index=df.index)

    for w in windows:
        # We look at the past N days, EXCLUDING current day
        # Shift(1) so current bar is compared to past W bars
        res[f"breakout_high_{w}"] = df["high"].shift(1).rolling(window=w).max()
        res[f"breakout_low_{w}"] = df["low"].shift(1).rolling(window=w).min()

    return res


def calculate_breakout_distance(
    df: pd.DataFrame, windows: tuple[int, ...] = (10, 20, 55)
) -> pd.DataFrame:
    """Calculate distance to breakout levels."""
    levels = calculate_breakout_levels(df, windows)
    res = pd.DataFrame(index=df.index)

    for w in windows:
        if f"breakout_high_{w}" in levels.columns:
            res[f"dist_to_breakout_high_{w}"] = (
                levels[f"breakout_high_{w}"] - df["close"]
            ) / df["close"]
            res[f"dist_to_breakout_low_{w}"] = (
                df["close"] - levels[f"breakout_low_{w}"]
            ) / df["close"]

    res = res.replace([np.inf, -np.inf], np.nan)
    return res


def calculate_false_breakout_features(
    df: pd.DataFrame, windows: tuple[int, ...] = (10, 20, 55)
) -> pd.DataFrame:
    """Detect if price broke out but closed back inside."""
    levels = calculate_breakout_levels(df, windows)
    res = pd.DataFrame(index=df.index)

    for w in windows:
        if f"breakout_high_{w}" in levels.columns:
            # High goes above the breakout high, but close is below it
            fb_upper = (df["high"] > levels[f"breakout_high_{w}"]) & (
                df["close"] < levels[f"breakout_high_{w}"]
            )
            # Low goes below the breakout low, but close is above it
            fb_lower = (df["low"] < levels[f"breakout_low_{w}"]) & (
                df["close"] > levels[f"breakout_low_{w}"]
            )

            res[f"false_breakout_upper_{w}"] = fb_upper.astype(int)
            res[f"false_breakout_lower_{w}"] = fb_lower.astype(int)

    return res


def calculate_range_compression_expansion(
    df: pd.DataFrame, window: int = 20, percentile_window: int = 120
) -> pd.DataFrame:
    """Calculate range compression and expansion signals."""
    res = pd.DataFrame(index=df.index)
    candle_range = df["high"] - df["low"]

    roll_mean = candle_range.rolling(window=window).mean()
    # If range is very small compared to past N days
    res[f"range_compression_{window}"] = (candle_range < (roll_mean * 0.5)).astype(int)
    # If range is very large compared to past N days
    res[f"range_expansion_{window}"] = (candle_range > (roll_mean * 2.0)).astype(int)

    return res


def calculate_candle_percentiles(
    df: pd.DataFrame, percentile_window: int = 120
) -> pd.DataFrame:
    """Calculate the percentile rank of the current candle's range/body."""
    res = pd.DataFrame(index=df.index)
    candle_range = df["high"] - df["low"]
    body_abs = (df["close"] - df["open"]).abs()

    # We use rolling rank
    if len(df) > 0:
        res[f"candle_range_percentile_{percentile_window}"] = candle_range.rolling(
            window=percentile_window
        ).apply(
            lambda x: (
                pd.Series(x).rank(pct=True).iloc[-1] if not pd.isna(x).all() else np.nan
            ),
            raw=False,
        )
        res[f"candle_body_percentile_{percentile_window}"] = body_abs.rolling(
            window=percentile_window
        ).apply(
            lambda x: (
                pd.Series(x).rank(pct=True).iloc[-1] if not pd.isna(x).all() else np.nan
            ),
            raw=False,
        )
    else:
        res[f"candle_range_percentile_{percentile_window}"] = np.nan
        res[f"candle_body_percentile_{percentile_window}"] = np.nan

    return res


def calculate_consecutive_candle_features(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate consecutive up/down closes and higher highs/lower lows."""
    res = pd.DataFrame(index=df.index)

    # Consecutive up closes
    is_up = df["close"] > df["close"].shift(1)
    res["consecutive_up_closes"] = is_up.groupby((~is_up).cumsum()).cumsum()

    # Consecutive down closes
    is_down = df["close"] < df["close"].shift(1)
    res["consecutive_down_closes"] = is_down.groupby((~is_down).cumsum()).cumsum()

    # Consecutive higher highs
    is_hh = df["high"] > df["high"].shift(1)
    res["consecutive_higher_highs"] = is_hh.groupby((~is_hh).cumsum()).cumsum()

    # Consecutive lower lows
    is_ll = df["low"] < df["low"].shift(1)
    res["consecutive_lower_lows"] = is_ll.groupby((~is_ll).cumsum()).cumsum()

    return res


def calculate_price_action_context(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50)
) -> pd.DataFrame:
    """Calculate macro price action context (position within larger ranges)."""
    res = pd.DataFrame(index=df.index)

    for w in windows:
        roll_high = df["high"].rolling(window=w).max()
        roll_low = df["low"].rolling(window=w).min()
        roll_range = roll_high - roll_low

        pos = (df["close"] - roll_low) / roll_range
        res[f"pa_context_range_position_{w}"] = pos.replace([np.inf, -np.inf], np.nan)

    return res
