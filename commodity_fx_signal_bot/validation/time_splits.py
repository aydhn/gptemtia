"""
Time splits generator for in-sample/out-of-sample and walk-forward validation.
"""

import logging
from typing import Optional
import pandas as pd

from validation.validation_models import TimeSplit, build_split_id

logger = logging.getLogger(__name__)


def create_train_test_split(index: pd.DatetimeIndex, train_ratio: float = 0.70) -> dict:
    """
    Creates a simple train/test split from a DatetimeIndex.
    """
    if len(index) == 0:
        logger.warning("Empty index provided for train/test split.")
        return {}

    split_idx = int(len(index) * train_ratio)
    if split_idx == 0 or split_idx == len(index):
        logger.warning("Insufficient data for train/test split.")
        return {}

    train_index = index[:split_idx]
    test_index = index[split_idx:]

    return {
        "train_start": train_index[0].isoformat(),
        "train_end": train_index[-1].isoformat(),
        "test_start": test_index[0].isoformat(),
        "test_end": test_index[-1].isoformat(),
        "train_bars": len(train_index),
        "test_bars": len(test_index),
    }


def create_walk_forward_splits(
    index: pd.DatetimeIndex,
    train_window_bars: int,
    test_window_bars: int,
    step_bars: int,
    expanding_window: bool = False,
    min_train_bars: Optional[int] = None,
    min_test_bars: Optional[int] = None,
) -> list[TimeSplit]:
    """
    Creates walk-forward splits from a DatetimeIndex.
    """
    if not isinstance(index, pd.DatetimeIndex):
        logger.error("index must be a pandas DatetimeIndex.")
        return []

    if not index.is_monotonic_increasing:
        logger.warning("Index is not monotonic increasing. Duplicate or unsorted dates may exist.")

    total_bars = len(index)
    if total_bars < (train_window_bars + test_window_bars):
        logger.warning(f"Insufficient data for walk-forward. Have {total_bars}, need at least {train_window_bars + test_window_bars}")
        return []

    if min_train_bars is None:
        min_train_bars = train_window_bars // 2
    if min_test_bars is None:
        min_test_bars = test_window_bars // 2

    splits = []
    split_index = 0
    current_train_start_idx = 0

    while True:
        if expanding_window:
            train_start_idx = 0
        else:
            train_start_idx = current_train_start_idx

        train_end_idx = current_train_start_idx + train_window_bars
        test_start_idx = train_end_idx
        test_end_idx = test_start_idx + test_window_bars

        # Check if we have enough data for the test window
        if test_start_idx >= total_bars:
            break

        # Adjust test_end_idx if it exceeds total bars, but only if we still meet min_test_bars
        actual_test_end_idx = min(test_end_idx, total_bars)
        actual_test_bars = actual_test_end_idx - test_start_idx
        actual_train_bars = train_end_idx - train_start_idx

        if actual_test_bars < min_test_bars:
            break

        if actual_train_bars < min_train_bars:
            # Move to next step without breaking, in case future windows have more data
            current_train_start_idx += step_bars
            continue

        train_idx = index[train_start_idx:train_end_idx]
        test_idx = index[test_start_idx:actual_test_end_idx]

        split = TimeSplit(
            split_id=build_split_id("generic", "generic", split_index),
            train_start=train_idx[0].isoformat(),
            train_end=train_idx[-1].isoformat(),
            test_start=test_idx[0].isoformat(),
            test_end=test_idx[-1].isoformat(),
            train_bars=len(train_idx),
            test_bars=len(test_idx),
            split_index=split_index,
        )
        splits.append(split)

        split_index += 1
        current_train_start_idx += step_bars

    return splits


def validate_time_splits(splits: list[TimeSplit]) -> dict:
    """
    Validates a list of TimeSplits.
    Ensures train comes before test, and test periods do not overlap.
    """
    if not splits:
        return {"valid": False, "reason": "Empty splits list."}

    for split in splits:
        if split.train_end >= split.test_start:
            return {"valid": False, "reason": f"Train end ({split.train_end}) >= test start ({split.test_start}) in split {split.split_index}"}

    # Check for test period overlaps
    for i in range(len(splits) - 1):
        if splits[i].test_end > splits[i+1].test_start:
             return {"valid": False, "reason": f"Test overlap: split {i} end ({splits[i].test_end}) > split {i+1} start ({splits[i+1].test_start})"}

    return {"valid": True, "reason": ""}


def filter_dataframe_by_split(df: pd.DataFrame, split: TimeSplit, label: str) -> pd.DataFrame:
    """
    Filters a DataFrame for a specific split period (train or test).
    """
    if df is None or df.empty:
        return df

    if label == "train":
        start_time = pd.to_datetime(split.train_start)
        end_time = pd.to_datetime(split.train_end)
    elif label == "test":
        start_time = pd.to_datetime(split.test_start)
        end_time = pd.to_datetime(split.test_end)
    else:
        raise ValueError(f"Invalid label for split filtering: {label}. Use 'train' or 'test'.")

    # If df has datetime index, use it directly
    if isinstance(df.index, pd.DatetimeIndex):
        mask = (df.index >= start_time) & (df.index <= end_time)
        return df.loc[mask]

    # If there's an exit_time or entry_time column (for trades)
    if 'exit_time' in df.columns:
        mask = (pd.to_datetime(df['exit_time']) >= start_time) & (pd.to_datetime(df['exit_time']) <= end_time)
        return df.loc[mask]
    elif 'entry_time' in df.columns:
         mask = (pd.to_datetime(df['entry_time']) >= start_time) & (pd.to_datetime(df['entry_time']) <= end_time)
         return df.loc[mask]

    # If there's a timestamp column
    if 'timestamp' in df.columns:
        mask = (pd.to_datetime(df['timestamp']) >= start_time) & (pd.to_datetime(df['timestamp']) <= end_time)
        return df.loc[mask]

    logger.warning("Could not determine time column for filtering. Returning original DataFrame.")
    return df
