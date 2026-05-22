import pandas as pd
import numpy as np
from .factor_config import FactorResearchProfile

def calculate_distance_from_long_ma(close_df: pd.DataFrame, window: int = 252) -> pd.Series:
    """
    Value proxy based on mean reversion to a long-term moving average.
    """
    if len(close_df) < window:
        return pd.Series(np.nan, index=close_df.columns)

    ma = close_df.rolling(window=window).mean().iloc[-1]
    current = close_df.iloc[-1]

    # Avoid division by zero
    ma = ma.replace(0, np.nan)
    return (current - ma) / ma

def calculate_rolling_zscore_value_proxy(close_df: pd.DataFrame, window: int = 252) -> pd.Series:
    """
    Value proxy based on rolling Z-score.
    """
    if len(close_df) < window:
        return pd.Series(np.nan, index=close_df.columns)

    recent_window = close_df.iloc[-window:]
    mean = recent_window.mean()
    std = recent_window.std()
    current = recent_window.iloc[-1]

    std = std.replace(0, np.nan)
    return (current - mean) / std

def calculate_relative_to_synthetic_benchmark_value_proxy(close_df: pd.DataFrame, benchmark_level: pd.Series | None = None) -> pd.Series:
    if benchmark_level is None or benchmark_level.empty:
        return pd.Series(np.nan, index=close_df.columns)

    current_sym = close_df.iloc[-1]
    current_bench = benchmark_level.iloc[-1]

    return current_sym / current_bench

def build_value_proxy_factor_scores(
    close_df: pd.DataFrame,
    synthetic_index_map: dict[str, pd.DataFrame] | None,
    profile: FactorResearchProfile
) -> tuple[dict[str, pd.Series], dict]:

    summary = {"warnings": []}
    scores = {}

    if close_df.empty:
        summary["warnings"].append("Empty close_df for value proxy.")
        return scores, summary

    dist_ma = calculate_distance_from_long_ma(close_df, window=252)
    scores["value_proxy_distance_from_long_ma"] = dist_ma

    zscore = calculate_rolling_zscore_value_proxy(close_df, window=252)
    scores["value_proxy_zscore_from_rolling_mean"] = zscore

    # If len is short, warn
    if len(close_df) < 252:
         summary["warnings"].append("Insufficient data for 252-period value proxy.")

    return scores, summary
