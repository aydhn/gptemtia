import numpy as np
import pandas as pd

from indicators.momentum import (
    calculate_rsi,
    calculate_roc,
    calculate_momentum,
    calculate_stochastic,
    calculate_williams_r,
)


def calculate_multi_rsi(
    df: pd.DataFrame, windows: tuple[int, ...] = (7, 14, 21, 28)
) -> pd.DataFrame:
    results = []
    for window in windows:
        rsi_df = calculate_rsi(df, window=window)
        results.append(rsi_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_multi_roc(
    df: pd.DataFrame, windows: tuple[int, ...] = (5, 10, 20)
) -> pd.DataFrame:
    results = []
    for window in windows:
        roc_df = calculate_roc(df, window=window)
        results.append(roc_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_multi_momentum(
    df: pd.DataFrame, windows: tuple[int, ...] = (5, 10, 20)
) -> pd.DataFrame:
    results = []
    for window in windows:
        mom_df = calculate_momentum(df, window=window)
        results.append(mom_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_multi_stochastic(
    df: pd.DataFrame, windows: tuple[int, ...] = (14, 21), smooth_window: int = 3
) -> pd.DataFrame:
    results = []
    for window in windows:
        stoch_df = calculate_stochastic(df, window=window, smooth_window=smooth_window)
        results.append(stoch_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_multi_williams_r(
    df: pd.DataFrame, windows: tuple[int, ...] = (14, 21)
) -> pd.DataFrame:
    results = []
    for window in windows:
        will_df = calculate_williams_r(df, window=window)
        results.append(will_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_cci(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    if not all(col in df.columns for col in ["high", "low", "close"]):
        raise ValueError("Missing required columns: high, low, close")

    typical_price = (df["high"] + df["low"] + df["close"]) / 3
    sma_tp = typical_price.rolling(window=window, min_periods=window).mean()

    mean_deviation = typical_price.rolling(window=window, min_periods=window).apply(
        lambda x: np.mean(np.abs(x - np.mean(x))), raw=True
    )

    cci = (typical_price - sma_tp) / (0.015 * mean_deviation)
    cci = cci.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({f"cci_{window}": cci}, index=df.index)


def calculate_multi_cci(
    df: pd.DataFrame, windows: tuple[int, ...] = (14, 20, 30)
) -> pd.DataFrame:
    results = []
    for window in windows:
        cci_df = calculate_cci(df, window=window)
        results.append(cci_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_momentum_slope(
    df: pd.DataFrame, source_col: str, window: int = 5
) -> pd.DataFrame:
    if source_col not in df.columns:
        raise ValueError(f"Source column {source_col} not found in dataframe.")

    slope = (df[source_col] - df[source_col].shift(window)) / window
    slope = slope.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({f"slope_{source_col}_{window}": slope}, index=df.index)


def calculate_momentum_acceleration(
    df: pd.DataFrame, source_col: str, window: int = 5
) -> pd.DataFrame:
    if source_col not in df.columns:
        raise ValueError(f"Source column {source_col} not found in dataframe.")

    slope_df = calculate_momentum_slope(df, source_col=source_col, window=window)
    slope_col = f"slope_{source_col}_{window}"

    accel = (slope_df[slope_col] - slope_df[slope_col].shift(window)) / window
    accel = accel.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({f"accel_{source_col}_{window}": accel}, index=df.index)


def calculate_relative_momentum_rank(
    feature_df: pd.DataFrame, columns: list[str]
) -> pd.DataFrame:
    missing = [c for c in columns if c not in feature_df.columns]
    if missing:
        raise ValueError(f"Missing columns for relative rank: {missing}")

    subset = feature_df[columns]
    rank_df = subset.rank(axis=1, pct=True)

    rank_df.columns = [f"rel_rank_{c}" for c in columns]
    return rank_df
