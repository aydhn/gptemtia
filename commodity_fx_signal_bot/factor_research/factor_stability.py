import pandas as pd
import numpy as np

def calculate_rank_stability(current_rank_df: pd.DataFrame, previous_rank_df: pd.DataFrame | None) -> pd.DataFrame:
    if current_rank_df.empty or previous_rank_df is None or previous_rank_df.empty:
        return pd.DataFrame()

    records = []

    # Merge on symbol and factor_id
    merged = pd.merge(current_rank_df, previous_rank_df, on=["symbol", "factor_id"], suffixes=('_curr', '_prev'))

    if merged.empty:
        return pd.DataFrame()

    for factor_id, group in merged.groupby("factor_id"):
        rank_delta = (group['rank_curr'] - group['rank_prev']).abs().mean()
        corr = group['rank_curr'].corr(group['rank_prev'])

        records.append({
            "factor_id": factor_id,
            "mean_rank_delta": float(rank_delta),
            "rank_correlation": float(corr) if not pd.isna(corr) else None
        })

    return pd.DataFrame(records)

def calculate_factor_score_stability(score_history_df: pd.DataFrame) -> pd.DataFrame:
    # Requires panel data over time. Returns empty for now.
    return pd.DataFrame()

def calculate_bucket_turnover(score_history_df: pd.DataFrame) -> pd.DataFrame:
    # Requires panel data over time. Returns empty for now.
    return pd.DataFrame()

def build_factor_stability_report(score_history_df: pd.DataFrame, previous_rank_df: pd.DataFrame | None = None) -> tuple[dict[str, pd.DataFrame], dict]:
    summary = {"warnings": ["Stability report is a placeholder"]}
    tables = {}
    return tables, summary
