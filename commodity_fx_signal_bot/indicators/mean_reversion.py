import numpy as np
import pandas as pd


def calculate_zscore_close(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    close = df["close"]
    sma = close.rolling(window=window, min_periods=window).mean()
    std = close.rolling(window=window, min_periods=window).std()

    zscore = (close - sma) / std
    zscore = zscore.replace([np.inf, -np.inf], np.nan)
    return pd.DataFrame({f"zscore_close_{window}": zscore})


def calculate_distance_from_sma(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    close = df["close"]
    sma = close.rolling(window=window, min_periods=window).mean()
    dist = (close - sma) / sma
    dist = dist.replace([np.inf, -np.inf], np.nan)
    return pd.DataFrame({f"dist_sma_{window}": dist})


def calculate_distance_from_ema(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    close = df["close"]
    ema = close.ewm(span=window, adjust=False, min_periods=window).mean()
    dist = (close - ema) / ema
    dist = dist.replace([np.inf, -np.inf], np.nan)
    return pd.DataFrame({f"dist_ema_{window}": dist})


def calculate_bollinger_percent_b(
    df: pd.DataFrame, window: int = 20, num_std: float = 2.0
) -> pd.DataFrame:
    from indicators.volatility import calculate_bollinger_bands

    bb_df = calculate_bollinger_bands(df, window=window, num_std=num_std)
    # the func returns the column, we just pick it
    return pd.DataFrame(
        {
            f"bb_percent_b_{window}_{int(num_std)}": bb_df[
                f"bb_percent_b_{window}_{int(num_std)}"
            ]
        }
    )


def calculate_bollinger_bandwidth(
    df: pd.DataFrame, window: int = 20, num_std: float = 2.0
) -> pd.DataFrame:
    from indicators.volatility import calculate_bollinger_bands

    bb_df = calculate_bollinger_bands(df, window=window, num_std=num_std)
    return pd.DataFrame(
        {
            f"bb_bandwidth_{window}_{int(num_std)}": bb_df[
                f"bb_width_{window}_{int(num_std)}"
            ]
        }
    )
