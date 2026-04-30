import numpy as np
import pandas as pd


def calculate_multi_zscore_close(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50, 100)
) -> pd.DataFrame:
    close = df["close"]
    res = {}
    for w in windows:
        sma = close.rolling(window=w, min_periods=w).mean()
        std = close.rolling(window=w, min_periods=w).std()
        z = (close - sma) / std
        # Replace inf with nan
        z = z.replace([np.inf, -np.inf], np.nan)
        res[f"zscore_close_{w}"] = z
    return pd.DataFrame(res, index=df.index)


def calculate_multi_rolling_mean_distance(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50, 100)
) -> pd.DataFrame:
    close = df["close"]
    res = {}
    for w in windows:
        sma = close.rolling(window=w, min_periods=w).mean()
        dist = (close - sma) / sma
        dist = dist.replace([np.inf, -np.inf], np.nan)
        res[f"rolling_mean_dist_{w}"] = dist
    return pd.DataFrame(res, index=df.index)


def calculate_multi_sma_distance(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50, 100, 200)
) -> pd.DataFrame:
    close = df["close"]
    res = {}
    for w in windows:
        sma = close.rolling(window=w, min_periods=w).mean()
        dist = (close - sma) / sma
        dist = dist.replace([np.inf, -np.inf], np.nan)
        res[f"dist_sma_{w}"] = dist
    return pd.DataFrame(res, index=df.index)


def calculate_multi_ema_distance(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50, 100, 200)
) -> pd.DataFrame:
    close = df["close"]
    res = {}
    for w in windows:
        ema = close.ewm(span=w, adjust=False, min_periods=w).mean()
        dist = (close - ema) / ema
        dist = dist.replace([np.inf, -np.inf], np.nan)
        res[f"dist_ema_{w}"] = dist
    return pd.DataFrame(res, index=df.index)


def calculate_rolling_percentile_rank(
    df: pd.DataFrame, source_col: str = "close", window: int = 120
) -> pd.DataFrame:
    if source_col not in df.columns:
        return pd.DataFrame(index=df.index)

    s = df[source_col]
    rank = s.rolling(window=window, min_periods=window).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )
    return pd.DataFrame({f"percentile_{source_col}_{window}": rank}, index=df.index)


def calculate_multi_percentile_rank(
    df: pd.DataFrame, windows: tuple[int, ...] = (60, 120, 252)
) -> pd.DataFrame:
    res = pd.DataFrame(index=df.index)
    for w in windows:
        p = calculate_rolling_percentile_rank(df, source_col="close", window=w)
        res = pd.concat([res, p], axis=1)
    return res


def calculate_rolling_minmax_position(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50, 100)
) -> pd.DataFrame:
    close = df["close"]
    res = {}
    for w in windows:
        low_min = close.rolling(window=w, min_periods=w).min()
        high_max = close.rolling(window=w, min_periods=w).max()
        pos = (close - low_min) / (high_max - low_min)
        pos = pos.replace([np.inf, -np.inf], np.nan)
        res[f"minmax_pos_{w}"] = pos
    return pd.DataFrame(res, index=df.index)


def calculate_bollinger_reversion_features(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50), num_std: float = 2.0
) -> pd.DataFrame:
    from indicators.volatility import calculate_bollinger_bands

    res = pd.DataFrame(index=df.index)
    close = df["close"]

    for w in windows:
        bb = calculate_bollinger_bands(df, window=w, num_std=num_std)
        # Using the returned dataframe, calculate what we need
        upper = bb[f"bb_upper_{w}_{int(num_std)}"]
        lower = bb[f"bb_lower_{w}_{int(num_std)}"]
        mid = bb[f"bb_mid_{w}_{int(num_std)}"]

        # bb_percent_b is already returned but let's recalculate or pull it
        pct_b = bb[f"bb_percent_b_{w}_{int(num_std)}"]

        # extensions
        lower_ext = (lower - close) / close
        lower_ext = lower_ext.clip(lower=0)  # Only positive when extended below

        upper_ext = (close - upper) / close
        upper_ext = upper_ext.clip(lower=0)  # Only positive when extended above

        # z-score equivalent for BB
        std = df["close"].rolling(window=w, min_periods=w).std()
        z = (close - mid) / std

        # reentry pressure
        reentry = (
            pct_b - 0.5
        ) * -1  # negative when high pct_b, positive when low pct_b

        res[f"bb_reversion_z_{w}_{int(num_std)}"] = z
        res[f"bb_percent_b_{w}_{int(num_std)}"] = pct_b
        res[f"bb_lower_extension_{w}_{int(num_std)}"] = lower_ext
        res[f"bb_upper_extension_{w}_{int(num_std)}"] = upper_ext
        res[f"bb_reentry_pressure_{w}_{int(num_std)}"] = reentry

    res = res.replace([np.inf, -np.inf], np.nan)
    return res


def calculate_channel_deviation_features(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 55)
) -> pd.DataFrame:
    res = {}
    close = df["close"]
    for w in windows:
        donchian_high = df["high"].rolling(window=w, min_periods=w).max()
        donchian_low = df["low"].rolling(window=w, min_periods=w).min()
        donchian_mid = (donchian_high + donchian_low) / 2

        # Deviation from channel midline
        dev = (close - donchian_mid) / (donchian_high - donchian_low)
        dev = dev.replace([np.inf, -np.inf], np.nan)
        res[f"channel_dev_{w}"] = dev
    return pd.DataFrame(res, index=df.index)


def calculate_overextension_score(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    # A composite score using RSI and distance from SMA
    from indicators.momentum import calculate_rsi

    rsi_df = calculate_rsi(df, window=window)
    dist_df = calculate_distance_from_sma(df, window=window)

    rsi = rsi_df[f"rsi_{window}"]
    # Scale RSI to roughly -1 to 1 around 50
    rsi_scaled = (rsi - 50) / 50

    # Scale dist roughly
    dist = dist_df[f"dist_close_sma_{window}"]
    # Using z-score of dist might be better, but we can do a simple combination
    dist_z = (
        dist - dist.rolling(window=window, min_periods=window).mean()
    ) / dist.rolling(window=window, min_periods=window).std()

    score = rsi_scaled + dist_z
    score = score.replace([np.inf, -np.inf], np.nan)
    return pd.DataFrame({f"overextension_score_{window}": score}, index=df.index)


def calculate_distance_from_sma(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    # helper for overextension
    close = df["close"]
    sma = close.rolling(window=window, min_periods=window).mean()
    dist = (close - sma) / sma
    return pd.DataFrame({f"dist_close_sma_{window}": dist}, index=df.index)


def calculate_snapback_pressure(
    df: pd.DataFrame, zscore_col: str = "zscore_close_20"
) -> pd.DataFrame:
    # Needs a zscore to be calculated first. If not present in df, we calculate it here
    if zscore_col not in df.columns:
        # try to parse window
        try:
            window = int(zscore_col.split("_")[-1])
        except:
            window = 20
        z_df = calculate_multi_zscore_close(df, windows=(window,))
        z = z_df[f"zscore_close_{window}"]
    else:
        z = df[zscore_col]

    # Snapback pressure: when z-score is high but starting to mean-revert
    # pressure is negative when z is high and falling, positive when z is low and rising
    z_diff = z.diff()
    pressure = -z * z_diff
    pressure = pressure.replace([np.inf, -np.inf], np.nan)
    return pd.DataFrame({f"snapback_pressure_{zscore_col}": pressure}, index=df.index)


def calculate_reversion_half_life_proxy(
    df: pd.DataFrame, window: int = 50
) -> pd.DataFrame:
    # A proxy for half-life of mean reversion.
    # Autocorrelation of price changes
    close = df["close"]
    diff = close.diff()

    # We'll use a simple proxy: rolling autocorrelation with lag 1
    # Negative autocorrelation -> faster mean reversion
    autocorr = diff.rolling(window=window, min_periods=window).apply(
        lambda x: pd.Series(x).autocorr(lag=1), raw=False
    )

    # Half life proxy: smaller values mean faster reversion
    # Invert and scale
    hl_proxy = (1 + autocorr) * window / 2
    hl_proxy = hl_proxy.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({f"half_life_proxy_{window}": hl_proxy}, index=df.index)


def calculate_range_position_features(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50, 100)
) -> pd.DataFrame:
    res = {}
    close = df["close"]
    for w in windows:
        recent_max = df["high"].rolling(window=w, min_periods=w).max()
        recent_min = df["low"].rolling(window=w, min_periods=w).min()
        rng = recent_max - recent_min

        pos = (close - recent_min) / rng
        pos = pos.replace([np.inf, -np.inf], np.nan)
        res[f"range_pos_{w}"] = pos
    return pd.DataFrame(res, index=df.index)
