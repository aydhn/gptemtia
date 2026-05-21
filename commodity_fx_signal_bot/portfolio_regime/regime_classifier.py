import pandas as pd
import numpy as np
from typing import Tuple, Optional, Dict
from portfolio_regime.regime_config import PortfolioRegimeProfile
from core.logger import get_logger

logger = get_logger(__name__)

def calculate_portfolio_proxy_return(returns_df: pd.DataFrame, weights: Optional[Dict[str, float]] = None) -> pd.Series:
    """Calculates proxy portfolio returns."""
    if returns_df.empty:
        return pd.Series(dtype=float)

    if weights is None:
        # Equal weights fallback
        cols = returns_df.columns
        weights = {col: 1.0 / len(cols) for col in cols}

    aligned_weights = pd.Series(weights)
    aligned_weights = aligned_weights.reindex(returns_df.columns).fillna(0.0)

    # Normalize weights just in case
    weight_sum = aligned_weights.sum()
    if weight_sum > 0:
        aligned_weights = aligned_weights / weight_sum

    return returns_df.dot(aligned_weights)

def calculate_rolling_volatility(series: pd.Series, window: int = 20) -> pd.Series:
    """Calculates rolling volatility (annualized assuming daily)."""
    return series.rolling(window=window).std() * np.sqrt(252)

def calculate_rolling_trend(series: pd.Series, window: int = 50) -> pd.Series:
    """Calculates rolling trend (simple momentum)."""
    return series.rolling(window=window).mean()

def calculate_rolling_drawdown(equity_curve: pd.Series) -> pd.Series:
    """Calculates rolling drawdown from peak."""
    rolling_max = equity_curve.cummax()
    drawdown = (equity_curve - rolling_max) / rolling_max
    return drawdown

def classify_volatility_state(value: float, low_threshold: float, high_threshold: float) -> str:
    """Classifies volatility into state labels."""
    if pd.isna(value):
        return "unknown"
    if value < low_threshold:
        return "low_volatility"
    if value > high_threshold:
        return "high_volatility"
    return "normal_volatility"

def classify_trend_state(value: float) -> str:
    """Classifies trend into state labels."""
    if pd.isna(value):
        return "unknown"
    if value > 0.001:
        return "positive_trend"
    if value < -0.001:
        return "negative_trend"
    return "sideways_trend"

def classify_drawdown_state(value: float) -> str:
    """Classifies drawdown state."""
    if pd.isna(value):
        return "unknown"
    if value < -0.10:
        return "deep_drawdown"
    if value < -0.05:
        return "moderate_drawdown"
    return "normal_drawdown"

def classify_portfolio_regimes(
    returns_df: pd.DataFrame,
    profile: PortfolioRegimeProfile,
    weights: Optional[Dict[str, float]] = None
) -> Tuple[pd.DataFrame, dict]:
    """Classifies risk regimes based on proxy portfolio returns."""
    logger.info("Classifying portfolio regimes")
    summary = {"status": "success", "warnings": []}

    if returns_df.empty:
        summary["warnings"].append("Empty returns dataframe. Cannot classify regimes.")
        return pd.DataFrame(), summary

    proxy_returns = calculate_portfolio_proxy_return(returns_df, weights)
    equity_curve = (1 + proxy_returns).cumprod()

    vol = calculate_rolling_volatility(proxy_returns, profile.volatility_window)
    trend = calculate_rolling_trend(proxy_returns, profile.trend_window)
    drawdown = calculate_rolling_drawdown(equity_curve)

    # Calculate dynamic thresholds
    vol_q25 = vol.quantile(0.25)
    vol_q75 = vol.quantile(0.75)

    regime_df = pd.DataFrame(index=returns_df.index)
    regime_df['rolling_volatility'] = vol
    regime_df['rolling_trend'] = trend
    regime_df['rolling_drawdown'] = drawdown

    # Apply classifications
    regime_df['volatility_state'] = vol.apply(lambda x: classify_volatility_state(x, vol_q25, vol_q75))
    regime_df['trend_state'] = trend.apply(classify_trend_state)
    regime_df['drawdown_state'] = drawdown.apply(classify_drawdown_state)

    # Dummy correlation state
    regime_df['correlation_state'] = "normal_correlation"

    # Combine into regime_label
    def get_regime_label(row):
        if row['drawdown_state'] == 'deep_drawdown' and row['volatility_state'] == 'high_volatility':
            return "stress_regime"
        elif row['trend_state'] == 'negative_trend' and row['volatility_state'] == 'high_volatility':
            return "risk_off_regime"
        elif row['trend_state'] == 'positive_trend' and row['volatility_state'] == 'low_volatility':
            return "risk_on_regime"
        elif row['trend_state'] == 'sideways_trend':
            return "sideways_regime"
        return "unknown_regime"

    regime_df['regime_label'] = regime_df.apply(get_regime_label, axis=1)
    regime_df['regime_score'] = 0.5  # placeholder
    regime_df['confidence_score'] = 0.5 # placeholder

    return regime_df, summary
