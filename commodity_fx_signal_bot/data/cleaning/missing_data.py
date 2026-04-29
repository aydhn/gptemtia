from typing import Any, Dict, Tuple

import pandas as pd

from core.logger import get_logger

logger = get_logger(__name__)


def calculate_missing_ratios(df: pd.DataFrame) -> Dict[str, float]:
    """Calculate the ratio of missing values for each column."""
    if df is None or df.empty:
        return {}

    ratios = {}
    total_rows = len(df)
    for col in df.columns:
        ratios[col] = float(df[col].isna().sum() / total_rows)
    return ratios


def detect_timestamp_gaps(df: pd.DataFrame, timeframe: str) -> pd.DataFrame:
    """
    Detect gaps in the DatetimeIndex based on the timeframe.
    Returns a DataFrame containing information about the gaps.
    """
    if df is None or len(df) < 2:
        return pd.DataFrame()

    # Create a simple gap series representing time difference
    diffs = df.index.to_series().diff()

    # Calculate expected timedelta
    expected_delta = pd.Timedelta(
        timeframe.upper() if timeframe.endswith("d") else timeframe
    )
    if pd.isna(expected_delta):
        # Fallback if timeframe string parsing fails
        expected_delta = diffs.median()

    # We only flag a gap if the difference is more than 1.5x expected
    # to account for slight timezone or trading session variations
    gap_threshold = expected_delta * 1.5

    # Also ignore typical weekend gaps for daily data (e.g., 3 days)
    if "d" in timeframe.lower():
        weekend_gap = pd.Timedelta(days=3.5)
        gap_mask = (diffs > gap_threshold) & (diffs < weekend_gap)
        large_gap_mask = diffs >= weekend_gap
    else:
        gap_mask = diffs > gap_threshold
        large_gap_mask = diffs > (expected_delta * 5)

    all_gaps = diffs[gap_mask | large_gap_mask]

    if all_gaps.empty:
        return pd.DataFrame()

    gaps_df = pd.DataFrame(
        {
            "gap_duration": all_gaps,
            "gap_start": df.index[df.index.get_indexer(all_gaps.index) - 1],
            "gap_end": all_gaps.index,
        }
    )

    return gaps_df


def summarize_gaps(gaps_df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the gaps detected in the timestamp index."""
    if gaps_df is None or gaps_df.empty:
        return {"total_gaps": 0, "max_gap": None, "mean_gap": None}

    return {
        "total_gaps": len(gaps_df),
        "max_gap": str(gaps_df["gap_duration"].max()),
        "mean_gap": str(gaps_df["gap_duration"].mean()),
    }


def fill_small_price_gaps(
    df: pd.DataFrame, max_gap: int = 2
) -> Tuple[pd.DataFrame, Dict[str, int]]:
    """
    Forward fill small price gaps (up to max_gap consecutive missing values).
    Only applies to OHLC columns.
    """
    if df is None or df.empty:
        return df, {}

    filled_df = df.copy()
    filled_counts = {}

    price_cols = [
        col
        for col in ["open", "high", "low", "close", "adj_close"]
        if col in df.columns
    ]

    for col in price_cols:
        missing_before = filled_df[col].isna().sum()
        if missing_before > 0:
            filled_df[col] = filled_df[col].ffill(limit=max_gap)
            missing_after = filled_df[col].isna().sum()
            filled_counts[col] = int(missing_before - missing_after)

    return filled_df, filled_counts


def mark_missing_data_flags(df: pd.DataFrame) -> pd.DataFrame:
    """Add boolean flag columns indicating missing data."""
    if df is None or df.empty:
        return df

    flagged_df = df.copy()

    price_cols = [col for col in ["open", "high", "low", "close"] if col in df.columns]
    if price_cols:
        flagged_df["has_missing_ohlc"] = flagged_df[price_cols].isna().any(axis=1)

    if "volume" in df.columns:
        flagged_df["has_missing_volume"] = flagged_df["volume"].isna()

    return flagged_df
