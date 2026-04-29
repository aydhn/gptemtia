import numpy as np
import pandas as pd


def rolling_zscore(series: pd.Series, window: int) -> pd.Series:
    sma = series.rolling(window=window, min_periods=window).mean()
    std = series.rolling(window=window, min_periods=window).std()
    zscore = (series - sma) / std
    return zscore.replace([np.inf, -np.inf], np.nan)


def rolling_minmax(series: pd.Series, window: int) -> pd.Series:
    roll_min = series.rolling(window=window, min_periods=window).min()
    roll_max = series.rolling(window=window, min_periods=window).max()
    res = (series - roll_min) / (roll_max - roll_min)
    return res.replace([np.inf, -np.inf, np.nan], 0.5)


def percent_rank(series: pd.Series, window: int) -> pd.Series:
    def rank_func(x):
        return pd.Series(x).rank(pct=True).iloc[-1]

    return series.rolling(window=window, min_periods=window).apply(rank_func)


def safe_pct_change(series: pd.Series, periods: int = 1) -> pd.Series:
    pct = series.pct_change(periods=periods)
    return pct.replace([np.inf, -np.inf], np.nan)


def safe_log_return(series: pd.Series, periods: int = 1) -> pd.Series:
    log_ret = np.log(series / series.shift(periods))
    return log_ret.replace([np.inf, -np.inf], np.nan)


def winsorize_series(
    series: pd.Series, lower: float = 0.01, upper: float = 0.99
) -> pd.Series:
    # Use quantile to bound values
    s = series.copy()
    lower_bound = s.quantile(lower)
    upper_bound = s.quantile(upper)

    s = s.clip(lower=lower_bound, upper=upper_bound)
    return s
