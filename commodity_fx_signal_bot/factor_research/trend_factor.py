import pandas as pd
import numpy as np
from .factor_config import FactorResearchProfile

def calculate_price_trend_score(close_df: pd.DataFrame, window: int) -> pd.Series:
    if len(close_df) <= window:
         return pd.Series(np.nan, index=close_df.columns)

    current_close = close_df.iloc[-1]
    past_close = close_df.iloc[-(window + 1)]
    return (current_close - past_close) / past_close

def calculate_ma_slope_score(close_df: pd.DataFrame, window: int) -> pd.Series:
    if len(close_df) <= window:
         return pd.Series(np.nan, index=close_df.columns)

    ma = close_df.rolling(window=window).mean()
    current_ma = ma.iloc[-1]
    past_ma = ma.iloc[-5] if len(ma) >= 5 else ma.iloc[-(len(ma))]

    return (current_ma - past_ma) / past_ma

def calculate_multi_window_trend_score(close_df: pd.DataFrame, windows: tuple[int, ...]) -> pd.Series:
    scores = []
    for w in windows:
        s = calculate_price_trend_score(close_df, w)
        scores.append(s)

    if not scores:
         return pd.Series(np.nan, index=close_df.columns)

    df = pd.DataFrame(scores).T
    # Simple average of available trend scores
    return df.mean(axis=1, skipna=True)

def build_trend_factor_scores(close_df: pd.DataFrame, profile: FactorResearchProfile) -> tuple[dict[str, pd.Series], dict]:
    summary = {"warnings": []}
    scores = {}

    if close_df.empty:
        summary["warnings"].append("Empty close_df provided for trend factor.")
        return scores, summary

    for w in profile.trend_windows:
        factor_id = f"trend_{w}"
        score = calculate_price_trend_score(close_df, w)
        scores[factor_id] = score

    return scores, summary
