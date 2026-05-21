import pandas as pd
from typing import Dict, Optional

def calculate_basket_regime_exposure(basket_returns: Dict[str, pd.Series], regime_df: pd.DataFrame) -> pd.DataFrame:
    """Calculates risk regime exposure for baskets."""
    from portfolio_regime.regime_conditioned_returns import calculate_regime_conditioned_basket_returns

    if not basket_returns or regime_df.empty:
        return pd.DataFrame()

    df = calculate_regime_conditioned_basket_returns(basket_returns, regime_df)

    if df.empty:
        return pd.DataFrame()

    df['exposure_score'] = 1.0 # placeholder
    df['avg_return_in_regime'] = df['mean_return']
    df['volatility_in_regime'] = df['volatility']
    df['drawdown_in_regime'] = df['worst_return']
    df['warning_label'] = 'normal'

    return df[['basket_id', 'regime_label', 'exposure_score', 'avg_return_in_regime', 'volatility_in_regime', 'drawdown_in_regime', 'warning_label']]

def calculate_asset_class_regime_exposure(weights: Dict[str, float], metadata_df: pd.DataFrame, regime_label: Optional[str] = None) -> pd.DataFrame:
    """Calculates asset class exposure to a regime."""
    # Placeholder
    return pd.DataFrame()

def build_risk_regime_exposure_table(baskets_df: pd.DataFrame, regime_df: pd.DataFrame, metadata_df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
    """Builds the full exposure table."""
    # Assume baskets_df contains returns for now (simplification)
    basket_returns = {col: baskets_df[col] for col in baskets_df.columns}
    return calculate_basket_regime_exposure(basket_returns, regime_df)

def summarize_risk_regime_exposure(exposure_df: pd.DataFrame) -> dict:
    """Summarizes exposure."""
    if exposure_df.empty:
        return {"status": "empty"}

    return {
        "status": "success",
        "baskets_analyzed": len(exposure_df['basket_id'].unique()),
        "regimes_analyzed": len(exposure_df['regime_label'].unique())
    }
