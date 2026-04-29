import numpy as np
import pandas as pd


def calculate_candle_body(df: pd.DataFrame) -> pd.DataFrame:
    body = df["close"] - df["open"]
    body_pct = body / df["open"]
    body_pct = body_pct.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({"candle_body": body, "candle_body_pct": body_pct})


def calculate_candle_range(df: pd.DataFrame) -> pd.DataFrame:
    candle_range = df["high"] - df["low"]
    return pd.DataFrame({"candle_range": candle_range})


def calculate_wicks(df: pd.DataFrame) -> pd.DataFrame:
    upper_wick = df["high"] - df[["open", "close"]].max(axis=1)
    lower_wick = df[["open", "close"]].min(axis=1) - df["low"]
    return pd.DataFrame({"upper_wick": upper_wick, "lower_wick": lower_wick})


def calculate_close_position_in_range(df: pd.DataFrame) -> pd.DataFrame:
    candle_range = df["high"] - df["low"]
    pos = (df["close"] - df["low"]) / candle_range
    pos = pos.replace([np.inf, -np.inf, np.nan], 0.5)  # defaults to 0.5 when doji
    return pd.DataFrame({"close_pos_range": pos})


def calculate_gap_percent(df: pd.DataFrame) -> pd.DataFrame:
    gap = (df["open"] - df["close"].shift(1)) / df["close"].shift(1)
    gap = gap.replace([np.inf, -np.inf], np.nan)
    return pd.DataFrame({"gap_percent": gap})


def calculate_returns(
    df: pd.DataFrame, periods: tuple[int, ...] = (1, 5, 10)
) -> pd.DataFrame:
    results = {}
    for p in periods:
        ret = df["close"].pct_change(periods=p)
        results[f"return_{p}"] = ret.replace([np.inf, -np.inf], np.nan)
    return pd.DataFrame(results)


def calculate_log_returns(
    df: pd.DataFrame, periods: tuple[int, ...] = (1, 5, 10)
) -> pd.DataFrame:
    results = {}
    for p in periods:
        log_ret = np.log(df["close"] / df["close"].shift(p))
        results[f"log_return_{p}"] = log_ret.replace([np.inf, -np.inf], np.nan)
    return pd.DataFrame(results)
