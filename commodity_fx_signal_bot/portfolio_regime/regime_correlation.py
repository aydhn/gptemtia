import pandas as pd
from typing import Tuple, Dict
from core.logger import get_logger

logger = get_logger(__name__)

def calculate_correlation_by_regime(returns_df: pd.DataFrame, regime_df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """Calculates correlation matrices by regime."""
    if returns_df.empty or regime_df.empty:
        return {}

    joined = returns_df.join(regime_df[['regime_label']], how='inner')
    results = {}

    for regime in joined['regime_label'].unique():
        regime_data = joined[joined['regime_label'] == regime].drop(columns=['regime_label'])
        if len(regime_data) > 10:  # Arbitrary min size
            results[regime] = regime_data.corr()

    return results

def calculate_average_correlation_by_regime(regime_corrs: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculates average pairwise correlation for each regime."""
    if not regime_corrs:
        return pd.DataFrame()

    results = []
    for regime, corr_df in regime_corrs.items():
        # Mask lower triangle to avoid duplicates and self-correlation
        import numpy as np
        mask = np.tril(np.ones(corr_df.shape), k=0).astype(bool)
        masked_corr = corr_df.mask(mask)
        avg_corr = masked_corr.mean().mean()

        results.append({
            'regime_label': regime,
            'avg_correlation': avg_corr
        })

    return pd.DataFrame(results)

def calculate_correlation_shift_table(regime_corrs: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculates shifts in correlation between regimes."""
    # Simplified placeholder
    return pd.DataFrame()

def identify_regime_correlation_spikes(avg_corr_df: pd.DataFrame, threshold: float = 0.70) -> pd.DataFrame:
    """Identifies regimes with unusually high correlation."""
    if avg_corr_df.empty:
        return pd.DataFrame()

    return avg_corr_df[avg_corr_df['avg_correlation'] > threshold]

def build_regime_correlation_report(returns_df: pd.DataFrame, regime_df: pd.DataFrame) -> Tuple[Dict[str, pd.DataFrame], dict]:
    """Builds a full regime correlation report."""
    logger.info("Building regime correlation report")

    regime_corrs = calculate_correlation_by_regime(returns_df, regime_df)
    avg_corr_df = calculate_average_correlation_by_regime(regime_corrs)
    spikes_df = identify_regime_correlation_spikes(avg_corr_df)

    summary = {
        "status": "success",
        "regimes_analyzed": len(regime_corrs),
        "spikes_detected": len(spikes_df)
    }

    tables = {
        "avg_correlation": avg_corr_df,
        "spikes": spikes_df
    }

    return tables, summary
