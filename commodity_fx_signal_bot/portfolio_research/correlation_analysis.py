import pandas as pd
import numpy as np
from portfolio_research.portfolio_config import PortfolioResearchProfile

def calculate_correlation_matrix(returns_df: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    if returns_df.empty:
        return pd.DataFrame()
    return returns_df.corr(method=method)

def calculate_rolling_average_correlation(returns_df: pd.DataFrame, window: int = 60) -> pd.DataFrame:
    if returns_df.empty or returns_df.shape[1] < 2:
        return pd.DataFrame()

    corr_series = {}
    cols = returns_df.columns
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            pair_name = f"{cols[i]}_{cols[j]}"
            corr_series[pair_name] = returns_df[cols[i]].rolling(window).corr(returns_df[cols[j]])

    if not corr_series:
        return pd.DataFrame()

    rolling_pairs = pd.DataFrame(corr_series)
    rolling_avg = rolling_pairs.mean(axis=1).to_frame(name="average_correlation")
    return rolling_avg

def calculate_pairwise_correlation_table(corr_df: pd.DataFrame) -> pd.DataFrame:
    if corr_df.empty:
        return pd.DataFrame()

    upper_tri = corr_df.where(np.triu(np.ones(corr_df.shape), k=1).astype(bool))

    stacked = upper_tri.stack(future_stack=True).dropna().reset_index()
    if stacked.empty:
        return pd.DataFrame(columns=["symbol_1", "symbol_2", "correlation"])

    stacked.columns = ['symbol_1', 'symbol_2', 'correlation']
    return stacked.sort_values(by="correlation", ascending=False).reset_index(drop=True)

def identify_high_correlation_pairs(pair_df: pd.DataFrame, threshold: float = 0.75) -> pd.DataFrame:
    if pair_df.empty:
        return pd.DataFrame()
    return pair_df[abs(pair_df['correlation']) >= threshold]

def calculate_average_correlation(corr_df: pd.DataFrame) -> float | None:
    if corr_df.empty or corr_df.shape[0] < 2:
        return None
    upper_tri = corr_df.where(np.triu(np.ones(corr_df.shape), k=1).astype(bool))
    return float(upper_tri.mean().mean())

def build_correlation_report(returns_df: pd.DataFrame, profile: PortfolioResearchProfile) -> tuple[dict[str, pd.DataFrame], dict]:
    corr_matrix = calculate_correlation_matrix(returns_df)
    rolling_corr = calculate_rolling_average_correlation(returns_df, window=profile.correlation_window)
    pair_table = calculate_pairwise_correlation_table(corr_matrix)
    high_corr = identify_high_correlation_pairs(pair_table)
    avg_corr = calculate_average_correlation(corr_matrix)

    tables = {
        "correlation_matrix": corr_matrix,
        "pairwise_correlation": pair_table,
        "high_correlation_pairs": high_corr,
        "rolling_average_correlation": rolling_corr,
    }

    summary = {
        "average_correlation": avg_corr,
        "high_correlation_pair_count": len(high_corr) if not high_corr.empty else 0,
        "correlation_window": profile.correlation_window,
        "warnings": [],
        "note": "Korelasyon analizi gecmis veri uzerinden yapilmis bir arastirma metrigidir."
    }

    return tables, summary
