import numpy as np
import pandas as pd


def calculate_multi_sma(
    df: pd.DataFrame, windows: tuple[int, ...] = (10, 20, 50, 100, 200)
) -> pd.DataFrame:
    result = {}
    for w in windows:
        result[f"sma_{w}"] = df["close"].rolling(window=w, min_periods=w).mean()
    return pd.DataFrame(result, index=df.index)


def calculate_multi_ema(
    df: pd.DataFrame, windows: tuple[int, ...] = (10, 20, 50, 100, 200)
) -> pd.DataFrame:
    result = {}
    for w in windows:
        result[f"ema_{w}"] = (
            df["close"].ewm(span=w, adjust=False, min_periods=w).mean()
        )
    return pd.DataFrame(result, index=df.index)


def calculate_wma(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    weights = np.arange(1, window + 1)

    def wma_apply(x):
        return np.dot(x, weights) / weights.sum()

    wma = df["close"].rolling(window=window, min_periods=window).apply(wma_apply, raw=True)
    return pd.DataFrame({f"wma_{window}": wma}, index=df.index)


def calculate_multi_wma(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50, 100)
) -> pd.DataFrame:
    result = {}
    for w in windows:
        weights = np.arange(1, w + 1)
        def wma_apply(x, wt=weights):
            return np.dot(x, wt) / wt.sum()
        result[f"wma_{w}"] = df["close"].rolling(window=w, min_periods=w).apply(wma_apply, raw=True)
    return pd.DataFrame(result, index=df.index)


def calculate_hma(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    half_window = window // 2
    sqrt_window = int(np.sqrt(window))

    weights_half = np.arange(1, half_window + 1)
    def wma_half(x):
        return np.dot(x, weights_half) / weights_half.sum()

    weights_full = np.arange(1, window + 1)
    def wma_full(x):
        return np.dot(x, weights_full) / weights_full.sum()

    wma1 = df["close"].rolling(window=half_window, min_periods=half_window).apply(wma_half, raw=True)
    wma2 = df["close"].rolling(window=window, min_periods=window).apply(wma_full, raw=True)

    diff = 2 * wma1 - wma2

    weights_sqrt = np.arange(1, sqrt_window + 1)
    def wma_sqrt(x):
        return np.dot(x, weights_sqrt) / weights_sqrt.sum()

    hma = diff.rolling(window=sqrt_window, min_periods=sqrt_window).apply(wma_sqrt, raw=True)
    return pd.DataFrame({f"hma_{window}": hma}, index=df.index)


def calculate_multi_hma(
    df: pd.DataFrame, windows: tuple[int, ...] = (20, 50)
) -> pd.DataFrame:
    result = {}
    for w in windows:
        hma_df = calculate_hma(df, window=w)
        result.update(hma_df.to_dict("series"))
    return pd.DataFrame(result, index=df.index)


def calculate_multi_macd(
    df: pd.DataFrame,
    configs: tuple[tuple[int, int, int], ...] = ((12, 26, 9), (8, 21, 5), (20, 50, 9)),
) -> pd.DataFrame:
    result = {}
    for fast, slow, signal in configs:
        ema_fast = df["close"].ewm(span=fast, adjust=False, min_periods=fast).mean()
        ema_slow = df["close"].ewm(span=slow, adjust=False, min_periods=slow).mean()

        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal, adjust=False, min_periods=signal).mean()
        macd_hist = macd_line - signal_line

        result[f"macd_{fast}_{slow}_{signal}"] = macd_line
        result[f"macd_signal_{fast}_{slow}_{signal}"] = signal_line
        result[f"macd_hist_{fast}_{slow}_{signal}"] = macd_hist

    return pd.DataFrame(result, index=df.index)


def calculate_dmi_adx(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    high = df["high"]
    low = df["low"]
    close = df["close"]

    plus_dm = high.diff()
    minus_dm = low.diff()

    plus_dm[plus_dm < 0] = 0
    plus_dm[plus_dm < -minus_dm] = 0

    minus_dm = -minus_dm
    minus_dm[minus_dm < 0] = 0
    minus_dm[minus_dm < plus_dm] = 0

    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    atr = tr.rolling(window=window, min_periods=window).mean()
    atr = atr.replace(0, np.nan) # Prevent division by zero

    plus_di = 100 * (plus_dm.rolling(window=window, min_periods=window).mean() / atr)
    minus_di = 100 * (minus_dm.rolling(window=window, min_periods=window).mean() / atr)

    dx = 100 * ((plus_di - minus_di).abs() / (plus_di + minus_di + 1e-9))
    adx = dx.rolling(window=window, min_periods=window).mean()

    return pd.DataFrame(
        {
            f"adx_{window}": adx,
            f"plus_di_{window}": plus_di,
            f"minus_di_{window}": minus_di,
        },
        index=df.index
    )


def calculate_multi_adx(
    df: pd.DataFrame, windows: tuple[int, ...] = (14, 21)
) -> pd.DataFrame:
    result = {}
    for w in windows:
        adx_df = calculate_dmi_adx(df, window=w)
        result.update(adx_df.to_dict("series"))
    return pd.DataFrame(result, index=df.index)


def calculate_multi_aroon(
    df: pd.DataFrame, windows: tuple[int, ...] = (14, 25)
) -> pd.DataFrame:
    result = {}
    high = df["high"]
    low = df["low"]

    for w in windows:
        aroon_up = high.rolling(window=w, min_periods=w).apply(
            lambda x: float(np.argmax(x)) / (w - 1) * 100 if w > 1 else 0
        )
        aroon_down = low.rolling(window=w, min_periods=w).apply(
            lambda x: float(np.argmin(x)) / (w - 1) * 100 if w > 1 else 0
        )
        result[f"aroon_up_{w}"] = aroon_up
        result[f"aroon_down_{w}"] = aroon_down

    return pd.DataFrame(result, index=df.index)


def calculate_ichimoku_full(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the full Ichimoku Cloud.
    WARNING: The Chikou Span (Lagging Span) requires shifting the close price backwards,
    which introduces future data (leakage). It should be used with extreme caution in
    strategy and ML backtesting.
    """
    high = df["high"]
    low = df["low"]
    close = df["close"]

    # Tenkan-sen (Conversion Line): (9-period high + 9-period low)/2
    period9_high = high.rolling(window=9, min_periods=9).max()
    period9_low = low.rolling(window=9, min_periods=9).min()
    tenkan_sen = (period9_high + period9_low) / 2

    # Kijun-sen (Base Line): (26-period high + 26-period low)/2
    period26_high = high.rolling(window=26, min_periods=26).max()
    period26_low = low.rolling(window=26, min_periods=26).min()
    kijun_sen = (period26_high + period26_low) / 2

    # Senkou Span A (Leading Span A): (Conversion Line + Base Line)/2
    senkou_span_a = ((tenkan_sen + kijun_sen) / 2).shift(26)

    # Senkou Span B (Leading Span B): (52-period high + 52-period low)/2
    period52_high = high.rolling(window=52, min_periods=52).max()
    period52_low = low.rolling(window=52, min_periods=52).min()
    senkou_span_b = ((period52_high + period52_low) / 2).shift(26)

    # Chikou Span (Lagging Span): Close shifted backwards by 26 periods
    chikou_span = close.shift(-26)

    return pd.DataFrame(
        {
            "ichimoku_tenkan": tenkan_sen,
            "ichimoku_kijun": kijun_sen,
            "ichimoku_span_a": senkou_span_a,
            "ichimoku_span_b": senkou_span_b,
            "ichimoku_chikou": chikou_span,
        },
        index=df.index
    )


def calculate_price_ma_distances(
    df: pd.DataFrame, ma_columns: list[str]
) -> pd.DataFrame:
    result = {}
    close = df.get("close")
    if close is None:
        return pd.DataFrame(index=df.index)

    for col in ma_columns:
        if col in df.columns:
            ma = df[col]
            ma = ma.replace(0, np.nan) # prevent div by zero
            # percentage distance
            result[f"dist_close_{col}"] = (close - ma) / ma

    return pd.DataFrame(result, index=df.index)


def calculate_ma_slopes(
    feature_df: pd.DataFrame, ma_columns: list[str], slope_window: int = 5
) -> pd.DataFrame:
    result = {}
    for col in ma_columns:
        if col in feature_df.columns:
            ma = feature_df[col]
            # Difference over window relative to previous MA value
            prev_ma = ma.shift(slope_window)
            prev_ma = prev_ma.replace(0, np.nan)
            slope = (ma - prev_ma) / prev_ma
            result[f"slope_{col}_{slope_window}"] = slope

    return pd.DataFrame(result, index=feature_df.index)


def calculate_ma_stack_state(
    feature_df: pd.DataFrame, fast_col: str, mid_col: str, slow_col: str
) -> pd.DataFrame:
    result = {}
    if (
        fast_col in feature_df.columns
        and mid_col in feature_df.columns
        and slow_col in feature_df.columns
    ):
        fast = feature_df[fast_col]
        mid = feature_df[mid_col]
        slow = feature_df[slow_col]

        bullish = (fast > mid) & (mid > slow)
        bearish = (fast < mid) & (mid < slow)

        # Convert to 0/1 integers for events/states
        suffix = f"{fast_col.split('_')[-1]}_{mid_col.split('_')[-1]}_{slow_col.split('_')[-1]}"
        result[f"ma_stack_bullish_{suffix}"] = bullish.astype(int)
        result[f"ma_stack_bearish_{suffix}"] = bearish.astype(int)

    return pd.DataFrame(result, index=feature_df.index)


def calculate_trend_persistence(series: pd.Series, window: int = 10) -> pd.Series:
    """
    Calculate trend persistence.
    Ratio of consecutive up/down moves within the window.
    """
    diffs = series.diff()
    up_moves = (diffs > 0).astype(int).rolling(window=window, min_periods=window).sum()
    down_moves = (diffs < 0).astype(int).rolling(window=window, min_periods=window).sum()

    total_moves = up_moves + down_moves
    total_moves = total_moves.replace(0, np.nan)

    persistence = (up_moves - down_moves) / total_moves

    col_name = "trend_persistence"
    if hasattr(series, "name") and series.name:
         col_name = f"trend_persistence_{series.name}_{window}"

    return pd.Series(persistence, name=col_name, index=series.index)
