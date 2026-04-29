import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


def calculate_obv(df: pd.DataFrame) -> pd.DataFrame:
    if "volume" not in df.columns or df["volume"].sum() == 0:
        logger.warning("Volume data is missing or zero, returning NaN for OBV")
        return pd.DataFrame({"obv": pd.Series(np.nan, index=df.index)})

    close_diff = df["close"].diff()
    direction = pd.Series(0, index=df.index)
    direction[close_diff > 0] = 1
    direction[close_diff < 0] = -1

    obv = (df["volume"] * direction).cumsum()
    return pd.DataFrame({"obv": obv})


def calculate_volume_sma(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    if "volume" not in df.columns or df["volume"].sum() == 0:
        logger.warning(
            f"Volume data is missing or zero, returning NaN for volume_sma_{window}"
        )
        return pd.DataFrame({f"volume_sma_{window}": pd.Series(np.nan, index=df.index)})

    sma = df["volume"].rolling(window=window, min_periods=window).mean()
    return pd.DataFrame({f"volume_sma_{window}": sma})


def calculate_volume_zscore(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    if "volume" not in df.columns or df["volume"].sum() == 0:
        logger.warning(
            f"Volume data is missing or zero, returning NaN for volume_zscore_{window}"
        )
        return pd.DataFrame(
            {f"volume_zscore_{window}": pd.Series(np.nan, index=df.index)}
        )

    sma = df["volume"].rolling(window=window, min_periods=window).mean()
    std = df["volume"].rolling(window=window, min_periods=window).std()

    zscore = (df["volume"] - sma) / std
    zscore = zscore.replace([np.inf, -np.inf], np.nan)
    return pd.DataFrame({f"volume_zscore_{window}": zscore})


def calculate_mfi(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    if "volume" not in df.columns or df["volume"].sum() == 0:
        logger.warning(
            f"Volume data is missing or zero, returning NaN for mfi_{window}"
        )
        return pd.DataFrame({f"mfi_{window}": pd.Series(np.nan, index=df.index)})

    typical_price = (df["high"] + df["low"] + df["close"]) / 3
    raw_money_flow = typical_price * df["volume"]

    positive_flow = pd.Series(0.0, index=df.index)
    negative_flow = pd.Series(0.0, index=df.index)

    diff = typical_price.diff()
    positive_flow[diff > 0] = raw_money_flow[diff > 0]
    negative_flow[diff < 0] = raw_money_flow[diff < 0]

    positive_mf = positive_flow.rolling(window=window, min_periods=window).sum()
    negative_mf = negative_flow.rolling(window=window, min_periods=window).sum()

    mfi = 100 - (100 / (1 + (positive_mf / negative_mf)))
    mfi = mfi.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({f"mfi_{window}": mfi})


def calculate_cmf(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    if "volume" not in df.columns or df["volume"].sum() == 0:
        logger.warning(
            f"Volume data is missing or zero, returning NaN for cmf_{window}"
        )
        return pd.DataFrame({f"cmf_{window}": pd.Series(np.nan, index=df.index)})

    mf_multiplier = ((df["close"] - df["low"]) - (df["high"] - df["close"])) / (
        df["high"] - df["low"]
    )
    # Handle division by zero where high == low
    mf_multiplier = mf_multiplier.replace([np.inf, -np.inf, np.nan], 0)

    mf_volume = mf_multiplier * df["volume"]

    cmf = (
        mf_volume.rolling(window=window, min_periods=window).sum()
        / df["volume"].rolling(window=window, min_periods=window).sum()
    )
    cmf = cmf.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({f"cmf_{window}": cmf})
