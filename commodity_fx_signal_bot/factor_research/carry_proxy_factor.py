import pandas as pd
import numpy as np
from .factor_config import FactorResearchProfile

def calculate_fx_try_carry_proxy(metadata_df: pd.DataFrame, returns_df: pd.DataFrame | None = None) -> pd.Series:
    """
    Very rough proxy for FX carry vs TRY.
    Assumes anything containing TRY has high yield.
    """
    scores = pd.Series(0.0, index=metadata_df["symbol"])

    for symbol in scores.index:
        if "TRY" in symbol:
             # Basic heuristic: if it's USDTRY, shorting USDTRY is positive carry
             scores.loc[symbol] = 1.0

    return scores

def calculate_commodity_carry_placeholder(metadata_df: pd.DataFrame) -> pd.Series:
    """
    Placeholder for commodity term structure.
    Real term structure data is not available from free sources natively.
    """
    scores = pd.Series(np.nan, index=metadata_df["symbol"])
    return scores

def calculate_roll_yield_proxy_from_price_trend(close_df: pd.DataFrame, window: int = 60) -> pd.Series:
    """
    A crude proxy estimating roll yield by comparing short and long-term trend divergence.
    """
    if len(close_df) <= window:
        return pd.Series(np.nan, index=close_df.columns)

    current = close_df.iloc[-1]
    past = close_df.iloc[-(window+1)]
    return (current - past) / past

def build_carry_proxy_factor_scores(
    metadata_df: pd.DataFrame,
    close_df: pd.DataFrame,
    returns_df: pd.DataFrame,
    profile: FactorResearchProfile
) -> tuple[dict[str, pd.Series], dict]:

    summary = {"warnings": []}
    scores = {}

    # Check if we have symbols to work with
    if metadata_df.empty:
         summary["warnings"].append("Empty metadata_df for carry proxy.")
         return scores, summary

    try_carry = calculate_fx_try_carry_proxy(metadata_df, returns_df)
    scores["carry_proxy_fx_try"] = try_carry

    commodity_carry = calculate_commodity_carry_placeholder(metadata_df)
    scores["carry_proxy_commodity_term_structure_placeholder"] = commodity_carry
    summary["warnings"].append("Commodity term structure carry is a placeholder.")

    return scores, summary
