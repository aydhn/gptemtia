import pandas as pd
import numpy as np
from .factor_config import FactorResearchProfile

def calculate_return_momentum_score(returns_df: pd.DataFrame, window: int) -> pd.Series:
    if len(returns_df) < window:
         return pd.Series(np.nan, index=returns_df.columns)

    # Cumulate log returns or compound simple returns
    recent_returns = returns_df.iloc[-window:]
    return recent_returns.sum(skipna=True)

def calculate_risk_adjusted_momentum_score(returns_df: pd.DataFrame, window: int) -> pd.Series:
    if len(returns_df) < window:
         return pd.Series(np.nan, index=returns_df.columns)

    recent_returns = returns_df.iloc[-window:]
    ret = recent_returns.sum(skipna=True)
    vol = recent_returns.std(skipna=True) * np.sqrt(252) # Annualized vol proxy

    # Avoid division by zero
    vol = vol.replace(0, np.nan)
    return ret / vol

def calculate_multi_window_momentum_factor(returns_df: pd.DataFrame, windows: tuple[int, ...]) -> pd.Series:
    scores = []
    for w in windows:
        s = calculate_return_momentum_score(returns_df, w)
        scores.append(s)

    if not scores:
         return pd.Series(np.nan, index=returns_df.columns)

    df = pd.DataFrame(scores).T
    return df.mean(axis=1, skipna=True)

def build_momentum_factor_scores(returns_df: pd.DataFrame, profile: FactorResearchProfile) -> tuple[dict[str, pd.Series], dict]:
    summary = {"warnings": []}
    scores = {}

    if returns_df.empty:
        summary["warnings"].append("Empty returns_df provided for momentum factor.")
        return scores, summary

    for w in profile.momentum_windows:
        factor_id = f"momentum_{w}"
        score = calculate_return_momentum_score(returns_df, w)
        scores[factor_id] = score

    return scores, summary
