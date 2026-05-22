import pandas as pd
import numpy as np
import logging
from synthetic_indices.index_config import SyntheticIndexProfile
from synthetic_indices.index_models import RelativeStrengthRecord

logger = logging.getLogger(__name__)

def calculate_relative_return(symbol_returns: pd.Series, benchmark_returns: pd.Series, window: int) -> float | None:
    if len(symbol_returns) < window or len(benchmark_returns) < window:
        return None

    s_ret = symbol_returns.iloc[-window:].sum() # Assuming log returns
    b_ret = benchmark_returns.iloc[-window:].sum()

    return float(s_ret - b_ret)

def calculate_relative_strength_table(returns_df: pd.DataFrame, benchmark_returns: pd.Series, windows: tuple[int, ...]) -> pd.DataFrame:
    records = []

    for symbol in returns_df.columns:
        row = {"symbol": symbol}
        for window in windows:
            rel_ret = calculate_relative_return(returns_df[symbol], benchmark_returns, window)
            row[f"relative_return_{window}"] = rel_ret
        records.append(row)

    return pd.DataFrame(records)

def rank_relative_strength(rs_df: pd.DataFrame) -> pd.DataFrame:
    if rs_df.empty:
        return rs_df

    df = rs_df.copy()

    # We will rank based on the average relative return across windows
    ret_cols = [c for c in df.columns if c.startswith("relative_return_")]

    if not ret_cols:
        return df

    df["avg_relative_return"] = df[ret_cols].mean(axis=1)

    # Rank descending (highest return is rank 1)
    df["relative_rank"] = df["avg_relative_return"].rank(ascending=False, method="min").astype("Int64")

    # Calculate percentile (0 to 1, where 1 is highest)
    df["relative_percentile"] = df["avg_relative_return"].rank(pct=True)

    # Add label
    df["relative_strength_label"] = df["relative_percentile"].apply(infer_relative_strength_label)

    return df

def infer_relative_strength_label(percentile: float | None) -> str:
    if pd.isna(percentile):
        return "insufficient_data"
    if percentile >= 0.8:
        return "strong_leader"
    elif percentile >= 0.6:
        return "moderate_leader"
    elif percentile >= 0.4:
        return "neutral_relative_strength"
    elif percentile >= 0.2:
        return "moderate_laggard"
    else:
        return "strong_laggard"

def build_relative_strength_report(returns_df: pd.DataFrame, benchmark_returns: pd.Series, profile: SyntheticIndexProfile) -> tuple[pd.DataFrame, dict]:
    summary = {"warnings": [], "symbols_processed": 0}

    if returns_df.empty or benchmark_returns.empty:
        summary["warnings"].append("Empty returns or benchmark data.")
        return pd.DataFrame(), summary

    rs_df = calculate_relative_strength_table(returns_df, benchmark_returns, profile.relative_strength_windows)
    ranked_df = rank_relative_strength(rs_df)

    # Sort by rank
    if "relative_rank" in ranked_df.columns:
         ranked_df = ranked_df.sort_values("relative_rank")

    summary["symbols_processed"] = len(ranked_df)

    return ranked_df, summary
