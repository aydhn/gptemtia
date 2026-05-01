from dataclasses import dataclass
import pandas as pd
import numpy as np


@dataclass
class MTFContextSummary:
    symbol: str
    base_timeframe: str
    context_timeframes: tuple[str, ...]
    rows: int
    columns: int
    trend_alignment_score: float
    momentum_alignment_score: float
    volatility_context_score: float
    conflict_score: float
    stale_context_ratio: float
    warnings: list[str]


def _calculate_score(mtf_df: pd.DataFrame, prefix_pattern: str) -> pd.Series:
    # Dummy implementation, creates a series of 0s
    return pd.Series(0.0, index=mtf_df.index)


def calculate_trend_alignment_score(mtf_df: pd.DataFrame) -> pd.Series:
    return _calculate_score(mtf_df, "trend")


def calculate_momentum_alignment_score(mtf_df: pd.DataFrame) -> pd.Series:
    return _calculate_score(mtf_df, "momentum")


def calculate_volatility_context_score(mtf_df: pd.DataFrame) -> pd.Series:
    return _calculate_score(mtf_df, "volatility")


def calculate_mean_reversion_context_score(mtf_df: pd.DataFrame) -> pd.Series:
    return _calculate_score(mtf_df, "mean_reversion")


def calculate_event_cluster_score(mtf_df: pd.DataFrame) -> pd.Series:
    return _calculate_score(mtf_df, "event")


def calculate_mtf_conflict_score(mtf_df: pd.DataFrame) -> pd.Series:
    return _calculate_score(mtf_df, "conflict")


def add_mtf_context_columns(mtf_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    df = mtf_df.copy()
    warnings = []

    df["mtf_trend_alignment_score"] = calculate_trend_alignment_score(df)
    df["mtf_momentum_alignment_score"] = calculate_momentum_alignment_score(df)
    df["mtf_volatility_context_score"] = calculate_volatility_context_score(df)
    df["mtf_mean_reversion_context_score"] = calculate_mean_reversion_context_score(df)
    df["mtf_event_cluster_score"] = calculate_event_cluster_score(df)
    df["mtf_conflict_score"] = calculate_mtf_conflict_score(df)

    # Check stale ratio
    stale_cols = [c for c in df.columns if "context_age_bars" in c]
    if stale_cols:
        # E.g. count how many are > 5
        # Simplified:
        df["mtf_stale_context_ratio"] = 0.0
    else:
        df["mtf_stale_context_ratio"] = 0.0

    return df, {"warnings": warnings}


def summarize_mtf_context(
    symbol: str,
    base_timeframe: str,
    context_timeframes: tuple[str, ...],
    mtf_df: pd.DataFrame,
) -> MTFContextSummary:
    return MTFContextSummary(
        symbol=symbol,
        base_timeframe=base_timeframe,
        context_timeframes=context_timeframes,
        rows=len(mtf_df),
        columns=len(mtf_df.columns),
        trend_alignment_score=(
            float(mtf_df["mtf_trend_alignment_score"].mean())
            if "mtf_trend_alignment_score" in mtf_df
            else 0.0
        ),
        momentum_alignment_score=(
            float(mtf_df["mtf_momentum_alignment_score"].mean())
            if "mtf_momentum_alignment_score" in mtf_df
            else 0.0
        ),
        volatility_context_score=(
            float(mtf_df["mtf_volatility_context_score"].mean())
            if "mtf_volatility_context_score" in mtf_df
            else 0.0
        ),
        conflict_score=(
            float(mtf_df["mtf_conflict_score"].mean())
            if "mtf_conflict_score" in mtf_df
            else 0.0
        ),
        stale_context_ratio=(
            float(mtf_df["mtf_stale_context_ratio"].mean())
            if "mtf_stale_context_ratio" in mtf_df
            else 0.0
        ),
        warnings=[],
    )
