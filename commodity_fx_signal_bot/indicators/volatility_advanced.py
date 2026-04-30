import numpy as np
import pandas as pd

from .volatility import (
    calculate_true_range,
    calculate_atr,
    calculate_bollinger_bands,
    calculate_keltner_channels,
    calculate_donchian_channels,
    calculate_historical_volatility,
)

def calculate_multi_true_range(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate true range and preserve the original OHLCV input."""
    tr = calculate_true_range(df)
    return tr

def calculate_multi_atr(df: pd.DataFrame, windows: tuple[int, ...] = (7, 14, 21, 28)) -> pd.DataFrame:
    """Calculate ATR for multiple windows."""
    results = []
    for w in windows:
        res = calculate_atr(df, window=w)
        results.append(res)
    if results:
        return pd.concat(results, axis=1)
    return pd.DataFrame(index=df.index)

def calculate_atr_percent(df: pd.DataFrame, windows: tuple[int, ...] = (7, 14, 21, 28)) -> pd.DataFrame:
    """Calculate ATR as a percentage of close price."""
    atr_df = calculate_multi_atr(df, windows=windows)
    close = df["close"]

    pct_df = pd.DataFrame(index=df.index)
    for w in windows:
        col = f"atr_{w}"
        if col in atr_df.columns:
            pct_col = f"atr_pct_{w}"
            pct_df[pct_col] = atr_df[col] / close
            pct_df[pct_col] = pct_df[pct_col].replace([np.inf, -np.inf], np.nan)

    return pct_df

def calculate_multi_bollinger_bands(df: pd.DataFrame, windows: tuple[int, ...] = (20, 50), num_std: float = 2.0) -> pd.DataFrame:
    """Calculate Bollinger Bands for multiple windows."""
    results = []
    for w in windows:
        res = calculate_bollinger_bands(df, window=w, num_std=num_std)
        results.append(res)
    if results:
        return pd.concat(results, axis=1)
    return pd.DataFrame(index=df.index)

def calculate_multi_keltner_channels(df: pd.DataFrame, windows: tuple[int, ...] = (20, 50), atr_window: int = 14, multiplier: float = 2.0) -> pd.DataFrame:
    """Calculate Keltner Channels for multiple windows."""
    results = []
    for w in windows:
        res = calculate_keltner_channels(df, window=w, atr_window=atr_window, multiplier=multiplier)

        # Manually add the keltner_width calculation that isn't in the base implementation
        ema = res[f"keltner_mid_{w}"]
        upper = res[f"keltner_upper_{w}"]
        lower = res[f"keltner_lower_{w}"]
        width = (upper - lower) / ema
        res[f"keltner_width_{w}"] = width.replace([np.inf, -np.inf], np.nan)

        results.append(res)
    if results:
        return pd.concat(results, axis=1)
    return pd.DataFrame(index=df.index)

def calculate_multi_donchian_channels(df: pd.DataFrame, windows: tuple[int, ...] = (20, 55)) -> pd.DataFrame:
    """Calculate Donchian Channels for multiple windows."""
    results = []
    for w in windows:
        res = calculate_donchian_channels(df, window=w)

        # Add donchian_width calculation
        upper = res[f"donchian_high_{w}"]
        lower = res[f"donchian_low_{w}"]
        mid = res[f"donchian_mid_{w}"]
        width = (upper - lower) / mid
        res[f"donchian_width_{w}"] = width.replace([np.inf, -np.inf], np.nan)

        results.append(res)
    if results:
        return pd.concat(results, axis=1)
    return pd.DataFrame(index=df.index)

def calculate_historical_volatility_multi(df: pd.DataFrame, windows: tuple[int, ...] = (10, 20, 50, 100), annualization: int = 252) -> pd.DataFrame:
    """Calculate Historical Volatility for multiple windows."""
    results = []
    for w in windows:
        res = calculate_historical_volatility(df, window=w, annualization=annualization)
        results.append(res)
    if results:
        return pd.concat(results, axis=1)
    return pd.DataFrame(index=df.index)

def calculate_parkinson_volatility(df: pd.DataFrame, window: int = 20, annualization: int = 252) -> pd.DataFrame:
    """
    Calculate Parkinson Volatility using High/Low prices.
    Formula: sqrt( (1 / (4 * window * ln(2))) * sum(ln(High/Low)^2) ) * sqrt(annualization)
    """
    high_low_ratio = df["high"] / df["low"].replace(0, np.nan)
    hl_log_sq = np.log(high_low_ratio) ** 2

    constant = 1.0 / (4.0 * np.log(2.0))
    rolling_sum = hl_log_sq.rolling(window=window, min_periods=window).mean()

    parkinson = np.sqrt(constant * rolling_sum) * np.sqrt(annualization)

    return pd.DataFrame({f"parkinson_vol_{window}": parkinson})

def calculate_garman_klass_volatility(df: pd.DataFrame, window: int = 20, annualization: int = 252) -> pd.DataFrame:
    """
    Calculate Garman-Klass Volatility using Open, High, Low, Close prices.
    Formula includes overnight jumps and intraday volatility.
    """
    # Fix for log of 0 or negative
    close_open_ratio = df["close"] / df["open"].replace(0, np.nan)
    high_low_ratio = df["high"] / df["low"].replace(0, np.nan)

    hl_log_sq = np.log(high_low_ratio) ** 2
    co_log_sq = np.log(close_open_ratio) ** 2

    # Garman-Klass estimator components
    term1 = 0.5 * hl_log_sq
    term2 = (2.0 * np.log(2.0) - 1.0) * co_log_sq

    gk_sum = (term1 - term2).rolling(window=window, min_periods=window).mean()

    # Protect against negative values inside sqrt due to numerical precision
    gk_sum = gk_sum.clip(lower=0)

    garman_klass = np.sqrt(gk_sum) * np.sqrt(annualization)

    return pd.DataFrame({f"garman_klass_vol_{window}": garman_klass})

def calculate_range_percent(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate today's range as a percentage of close price."""
    high = df["high"]
    low = df["low"]
    close = df["close"].replace(0, np.nan)

    range_pct = (high - low) / close
    range_pct = range_pct.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({"range_pct": range_pct})

def calculate_gap_volatility(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate gap between previous close and current open."""
    open_p = df["open"]
    close_prev = df["close"].shift(1).replace(0, np.nan)

    gap_pct = (open_p - close_prev) / close_prev
    gap_pct = gap_pct.replace([np.inf, -np.inf], np.nan)
    abs_gap_pct = gap_pct.abs()

    return pd.DataFrame({
        "gap_pct": gap_pct,
        "abs_gap_pct": abs_gap_pct
    })

def calculate_volatility_percentile(feature_df: pd.DataFrame, source_col: str, window: int = 120) -> pd.DataFrame:
    """Calculate the rolling percentile rank of a volatility metric."""
    if source_col not in feature_df.columns:
        return pd.DataFrame(index=feature_df.index)

    series = feature_df[source_col]

    # Calculate rolling rank
    # rank() gives 1 to N. To get percentile, we divide by valid count
    percentile = series.rolling(window=window, min_periods=max(2, window//4)).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )

    return pd.DataFrame({f"percentile_{source_col}_{window}": percentile})

def calculate_volatility_slope(feature_df: pd.DataFrame, source_col: str, window: int = 5) -> pd.DataFrame:
    """Calculate the normalized slope of a volatility metric to detect rising/falling regimes."""
    if source_col not in feature_df.columns:
        return pd.DataFrame(index=feature_df.index)

    series = feature_df[source_col]

    # Simple linear regression slope using rolling
    # For a simple window, we can just look at (current - previous_N) / N
    # Normalizing by the average of the metric
    momentum = series - series.shift(window)
    avg_val = series.rolling(window=window).mean().replace(0, np.nan)

    slope = (momentum / window) / avg_val
    slope = slope.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({f"slope_{source_col}_{window}": slope})

def calculate_channel_position(df: pd.DataFrame, upper_col: str, lower_col: str, prefix: str) -> pd.DataFrame:
    """
    Calculate the position of current price within a channel (0 to 1).
    0 = at or below lower channel
    1 = at or above upper channel
    """
    if upper_col not in df.columns or lower_col not in df.columns:
        return pd.DataFrame(index=df.index)

    close = df["close"]
    upper = df[upper_col]
    lower = df[lower_col]

    width = upper - lower
    width = width.replace(0, np.nan)

    pos = (close - lower) / width
    pos = pos.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({f"channel_pos_{prefix}": pos})
