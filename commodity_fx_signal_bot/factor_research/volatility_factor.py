import pandas as pd
import numpy as np
from .factor_config import FactorResearchProfile

def calculate_realized_volatility(returns_df: pd.DataFrame, window: int) -> pd.Series:
    if len(returns_df) < window:
         return pd.Series(np.nan, index=returns_df.columns)

    recent_returns = returns_df.iloc[-window:]
    return recent_returns.std(skipna=True) * np.sqrt(252)

def calculate_inverse_volatility_factor(returns_df: pd.DataFrame, window: int) -> pd.Series:
    vol = calculate_realized_volatility(returns_df, window)
    vol = vol.replace(0, np.nan)
    return 1.0 / vol

def calculate_downside_volatility_factor(returns_df: pd.DataFrame, window: int) -> pd.Series:
    if len(returns_df) < window:
         return pd.Series(np.nan, index=returns_df.columns)

    recent_returns = returns_df.iloc[-window:]
    downside_returns = recent_returns[recent_returns < 0]

    # Avoid std calculation on empty or 1-item arrays returning NaN when not needed
    downside_vol = downside_returns.std(skipna=True) * np.sqrt(252)
    downside_vol = downside_vol.replace(0, np.nan)
    return 1.0 / downside_vol

def build_volatility_factor_scores(returns_df: pd.DataFrame, profile: FactorResearchProfile) -> tuple[dict[str, pd.Series], dict]:
    summary = {"warnings": []}
    scores = {}

    if returns_df.empty:
        summary["warnings"].append("Empty returns_df provided for volatility factor.")
        return scores, summary

    for w in profile.volatility_windows:
        factor_id = f"inverse_volatility_{w}"
        score = calculate_inverse_volatility_factor(returns_df, w)
        scores[factor_id] = score

    return scores, summary
