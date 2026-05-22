import pandas as pd
import numpy as np
from .factor_config import FactorResearchProfile

def calculate_rolling_beta_proxy(symbol_returns: pd.Series, factor_returns: pd.Series, window: int = 60) -> float | None:
    if len(symbol_returns) < window or len(factor_returns) < window:
        return None

    df = pd.DataFrame({'sym': symbol_returns, 'fac': factor_returns}).dropna()
    if len(df) < window:
        return None

    cov = df['sym'].tail(window).cov(df['fac'].tail(window))
    var = df['fac'].tail(window).var()

    if var == 0 or pd.isna(var):
        return None

    return cov / var

def calculate_usdtry_sensitivity_factor(returns_df: pd.DataFrame, usdtry_symbol: str = "USDTRY=X", window: int = 60) -> pd.Series:
    scores = pd.Series(np.nan, index=returns_df.columns)
    if usdtry_symbol not in returns_df.columns:
        return scores

    factor_ret = returns_df[usdtry_symbol]
    for col in returns_df.columns:
        if col != usdtry_symbol:
             beta = calculate_rolling_beta_proxy(returns_df[col], factor_ret, window)
             if beta is not None:
                 scores.loc[col] = beta

    return scores

def calculate_gold_relative_factor(returns_df: pd.DataFrame, gold_symbol: str = "GC=F", window: int = 60) -> pd.Series:
    scores = pd.Series(np.nan, index=returns_df.columns)
    if gold_symbol not in returns_df.columns:
         return scores

    gold_ret = returns_df[gold_symbol].tail(window).sum(skipna=True)
    for col in returns_df.columns:
         sym_ret = returns_df[col].tail(window).sum(skipna=True)
         scores.loc[col] = sym_ret - gold_ret

    return scores

def calculate_oil_relative_factor(returns_df: pd.DataFrame, oil_symbol: str = "CL=F", window: int = 60) -> pd.Series:
    scores = pd.Series(np.nan, index=returns_df.columns)
    if oil_symbol not in returns_df.columns:
         return scores

    oil_ret = returns_df[oil_symbol].tail(window).sum(skipna=True)
    for col in returns_df.columns:
         sym_ret = returns_df[col].tail(window).sum(skipna=True)
         scores.loc[col] = sym_ret - oil_ret

    return scores

def calculate_inflation_sensitivity_proxy(returns_df: pd.DataFrame, inflation_proxy_returns: pd.Series | None = None, window: int = 60) -> pd.Series:
    scores = pd.Series(np.nan, index=returns_df.columns)
    if inflation_proxy_returns is None or inflation_proxy_returns.empty:
         return scores

    for col in returns_df.columns:
         beta = calculate_rolling_beta_proxy(returns_df[col], inflation_proxy_returns, window)
         if beta is not None:
              scores.loc[col] = beta

    return scores

def build_macro_sensitivity_factor_scores(returns_df: pd.DataFrame, profile: FactorResearchProfile) -> tuple[dict[str, pd.Series], dict]:
    summary = {"warnings": []}
    scores = {}

    if returns_df.empty:
        summary["warnings"].append("Empty returns_df for macro sensitivity.")
        return scores, summary

    # We use hardcoded symbols for proxies, if they don't exist, we skip
    usdtry_sens = calculate_usdtry_sensitivity_factor(returns_df, "USDTRY=X", window=60)
    scores["usdtry_sensitivity_proxy"] = usdtry_sens

    gold_rel = calculate_gold_relative_factor(returns_df, "GC=F", window=60)
    scores["gold_relative_strength_factor"] = gold_rel

    oil_rel = calculate_oil_relative_factor(returns_df, "CL=F", window=60)
    scores["oil_relative_strength_factor"] = oil_rel

    # We don't have a direct inflation proxy series here, so we skip or use gold as proxy
    if "GC=F" in returns_df.columns:
         inf_sens = calculate_inflation_sensitivity_proxy(returns_df, returns_df["GC=F"], window=60)
         scores["inflation_sensitivity_proxy"] = inf_sens
    else:
         summary["warnings"].append("Missing GC=F for inflation proxy.")

    return scores, summary
