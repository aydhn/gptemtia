import pandas as pd
from typing import Tuple, Dict, Optional
from core.logger import get_logger

logger = get_logger(__name__)

def join_returns_with_regimes(returns_df: pd.DataFrame, regime_df: pd.DataFrame) -> pd.DataFrame:
    """Joins returns with regime labels."""
    if returns_df.empty or regime_df.empty:
        return pd.DataFrame()
    return returns_df.join(regime_df[['regime_label']], how='inner')

def calculate_regime_conditioned_symbol_returns(returns_df: pd.DataFrame, regime_df: pd.DataFrame) -> pd.DataFrame:
    """Calculates symbol returns conditioned on regimes."""
    joined = join_returns_with_regimes(returns_df, regime_df)
    if joined.empty:
        return pd.DataFrame()

    results = []
    for regime in joined['regime_label'].unique():
        regime_data = joined[joined['regime_label'] == regime].drop(columns=['regime_label'])
        for col in regime_data.columns:
            series = regime_data[col].dropna()
            if len(series) == 0:
                continue

            results.append({
                'symbol': col,
                'regime_label': regime,
                'mean_return': series.mean(),
                'median_return': series.median(),
                'volatility': series.std(),
                'hit_rate_positive': (series > 0).mean(),
                'worst_return': series.min(),
                'best_return': series.max(),
                'observation_count': len(series)
            })

    return pd.DataFrame(results)

def calculate_regime_conditioned_basket_returns(basket_returns: Dict[str, pd.Series], regime_df: pd.DataFrame) -> pd.DataFrame:
    """Calculates basket returns conditioned on regimes."""
    if not basket_returns or regime_df.empty:
        return pd.DataFrame()

    combined_returns = pd.DataFrame(basket_returns)
    joined = join_returns_with_regimes(combined_returns, regime_df)

    if joined.empty:
        return pd.DataFrame()

    results = []
    for regime in joined['regime_label'].unique():
        regime_data = joined[joined['regime_label'] == regime].drop(columns=['regime_label'])
        for col in regime_data.columns:
            series = regime_data[col].dropna()
            if len(series) == 0:
                continue

            results.append({
                'basket_id': col,
                'regime_label': regime,
                'mean_return': series.mean(),
                'median_return': series.median(),
                'volatility': series.std(),
                'hit_rate_positive': (series > 0).mean(),
                'worst_return': series.min(),
                'best_return': series.max(),
                'observation_count': len(series)
            })

    return pd.DataFrame(results)

def summarize_regime_conditioned_returns(conditioned_df: pd.DataFrame) -> dict:
    """Summarizes conditioned returns."""
    if conditioned_df.empty:
        return {"status": "empty"}

    return {
        "status": "success",
        "regimes_analyzed": len(conditioned_df['regime_label'].unique()),
        "total_observations": int(conditioned_df['observation_count'].sum())
    }

def build_regime_conditioned_returns_report(
    returns_df: pd.DataFrame,
    regime_df: pd.DataFrame,
    basket_returns: Optional[Dict[str, pd.Series]] = None
) -> Tuple[Dict[str, pd.DataFrame], dict]:
    """Builds a full conditioned returns report."""
    logger.info("Building regime conditioned returns report")
    summary = {"warnings": []}

    symbol_df = calculate_regime_conditioned_symbol_returns(returns_df, regime_df)
    summary['symbol_summary'] = summarize_regime_conditioned_returns(symbol_df)

    tables = {"symbol_returns": symbol_df}

    if basket_returns:
        basket_df = calculate_regime_conditioned_basket_returns(basket_returns, regime_df)
        summary['basket_summary'] = summarize_regime_conditioned_returns(basket_df)
        tables["basket_returns"] = basket_df

    return tables, summary
