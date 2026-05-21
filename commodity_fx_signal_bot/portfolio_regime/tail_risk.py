import pandas as pd
import numpy as np
from typing import Dict, Optional
from portfolio_regime.regime_config import PortfolioRegimeProfile

def calculate_historical_var(series: pd.Series, quantile: float = 0.05) -> Optional[float]:
    """Calculates historical Value at Risk (VaR)."""
    if len(series) < 30:
        return None
    return series.quantile(quantile)

def calculate_historical_cvar(series: pd.Series, quantile: float = 0.05) -> Optional[float]:
    """Calculates historical Conditional Value at Risk (CVaR / Expected Shortfall)."""
    if len(series) < 30:
        return None
    var = calculate_historical_var(series, quantile)
    if var is None:
        return None
    return series[series <= var].mean()

def calculate_tail_loss_frequency(series: pd.Series, threshold: Optional[float] = None, quantile: float = 0.05) -> Optional[float]:
    """Calculates frequency of tail losses below threshold or quantile."""
    if len(series) < 30:
        return None

    if threshold is None:
        threshold = calculate_historical_var(series, quantile)

    if threshold is None:
        return None

    return (series < threshold).mean()

def build_tail_risk_table(basket_returns: Dict[str, pd.Series], profile: PortfolioRegimeProfile) -> pd.DataFrame:
    """Builds tail risk table for multiple baskets."""
    if not basket_returns:
        return pd.DataFrame()

    results = []
    for basket_id, returns in basket_returns.items():
        results.append({
            'basket_id': basket_id,
            'historical_var_95': calculate_historical_var(returns, 0.05),
            'historical_var_99': calculate_historical_var(returns, 0.01),
            'historical_cvar_95': calculate_historical_cvar(returns, 0.05),
            'historical_cvar_99': calculate_historical_cvar(returns, 0.01),
            'tail_loss_freq_95': calculate_tail_loss_frequency(returns, quantile=0.05)
        })

    return pd.DataFrame(results)

def summarize_tail_risk(tail_df: pd.DataFrame) -> dict:
    """Summarizes tail risk."""
    if tail_df.empty:
        return {"status": "empty"}

    return {
        "status": "success",
        "baskets_analyzed": len(tail_df),
        "worst_cvar_95": tail_df['historical_cvar_95'].min() if 'historical_cvar_95' in tail_df.columns else None
    }
