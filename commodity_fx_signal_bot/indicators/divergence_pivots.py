import logging
from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


@dataclass
class PivotConfig:
    left: int = 3
    right: int = 3
    min_move_pct: float = 0.0
    allow_equal: bool = False


def find_pivot_highs(
    series: pd.Series, config: Optional[PivotConfig] = None
) -> pd.Series:
    """
    Finds pivot highs in a pandas Series.
    A pivot high is a point that is strictly higher (or equal if allow_equal is True)
    than 'left' points before it and 'right' points after it.

    Warning: The 'right' parameter introduces a lookahead bias equal to 'right' bars.
    This means a pivot at index T can only be confirmed at index T + right.
    """
    if config is None:
        config = PivotConfig()

    result = pd.Series(False, index=series.index)

    # Need enough data
    if len(series) < config.left + config.right + 1:
        return result

    arr = series.values
    left = config.left
    right = config.right

    for i in range(left, len(arr) - right):
        val = arr[i]

        if pd.isna(val):
            continue

        # Check left
        left_window = arr[i - left : i]
        if config.allow_equal:
            if not np.all(left_window <= val):
                continue
        else:
            if not np.all(left_window < val):
                continue

        # Check right
        right_window = arr[i + 1 : i + right + 1]
        if config.allow_equal:
            if not np.all(right_window <= val):
                continue
        else:
            if not np.all(right_window < val):
                continue

        # Check min_move_pct
        if config.min_move_pct > 0:
            left_min = np.nanmin(left_window)
            if left_min > 0 and (val - left_min) / left_min < config.min_move_pct:
                continue

        result.iloc[i] = True

    return result


def find_pivot_lows(
    series: pd.Series, config: Optional[PivotConfig] = None
) -> pd.Series:
    """
    Finds pivot lows in a pandas Series.
    A pivot low is a point that is strictly lower (or equal if allow_equal is True)
    than 'left' points before it and 'right' points after it.

    Warning: The 'right' parameter introduces a lookahead bias equal to 'right' bars.
    This means a pivot at index T can only be confirmed at index T + right.
    """
    if config is None:
        config = PivotConfig()

    result = pd.Series(False, index=series.index)

    # Need enough data
    if len(series) < config.left + config.right + 1:
        return result

    arr = series.values
    left = config.left
    right = config.right

    for i in range(left, len(arr) - right):
        val = arr[i]

        if pd.isna(val):
            continue

        # Check left
        left_window = arr[i - left : i]
        if config.allow_equal:
            if not np.all(left_window >= val):
                continue
        else:
            if not np.all(left_window > val):
                continue

        # Check right
        right_window = arr[i + 1 : i + right + 1]
        if config.allow_equal:
            if not np.all(right_window >= val):
                continue
        else:
            if not np.all(right_window > val):
                continue

        # Check min_move_pct
        if config.min_move_pct > 0:
            left_max = np.nanmax(left_window)
            if val > 0 and (left_max - val) / val < config.min_move_pct:
                continue

        result.iloc[i] = True

    return result


def build_pivot_frame(
    df: pd.DataFrame,
    price_col: str = "close",
    indicator_cols: Optional[list[str]] = None,
    config: Optional[PivotConfig] = None,
) -> pd.DataFrame:
    """
    Builds a DataFrame containing pivot values for the price column and optional indicator columns.
    For each index where a pivot occurs, the column will contain the value at that pivot.
    Otherwise, it will be NaN.
    """
    if config is None:
        config = PivotConfig()

    if indicator_cols is None:
        indicator_cols = []

    # Make sure we don't mutate input
    out = pd.DataFrame(index=df.index)

    if price_col not in df.columns:
        logger.warning(f"Price column '{price_col}' not found for pivot calculation.")
        return out

    # Find price pivots
    highs = find_pivot_highs(df[price_col], config)
    lows = find_pivot_lows(df[price_col], config)

    # Set price pivot values
    out[f"pivot_high_{price_col}"] = np.where(highs, df[price_col], np.nan)
    out[f"pivot_low_{price_col}"] = np.where(lows, df[price_col], np.nan)

    # Calculate slope and change pct for price pivots
    out[f"pivot_slope_{price_col}_high"] = calculate_pivot_slope(df[price_col], highs)
    out[f"pivot_slope_{price_col}_low"] = calculate_pivot_slope(df[price_col], lows)
    out[f"pivot_change_pct_{price_col}_high"] = calculate_pivot_change_pct(
        df[price_col], highs
    )
    out[f"pivot_change_pct_{price_col}_low"] = calculate_pivot_change_pct(
        df[price_col], lows
    )

    # For indicators, we generally want to see their value at the exact bar the price pivot occurred
    # Some methodologies find indicator pivots independently and check if they align with price pivots
    # Here, we will record the indicator value at the price pivot
    for ind_col in indicator_cols:
        if ind_col in df.columns:
            out[f"pivot_high_{ind_col}"] = np.where(highs, df[ind_col], np.nan)
            out[f"pivot_low_{ind_col}"] = np.where(lows, df[ind_col], np.nan)
        else:
            logger.debug(f"Indicator column '{ind_col}' not found for pivot recording.")

    return out


def get_last_two_pivots(
    series: pd.Series, pivot_mask: pd.Series, current_index_pos: Optional[int] = None
) -> Tuple[Optional[float], Optional[float], Optional[int], Optional[int]]:
    """
    Returns the values and integer index positions of the last two pivots
    before or at current_index_pos.
    Returns (prev_val, curr_val, prev_idx, curr_idx)
    """
    if current_index_pos is None:
        current_index_pos = len(series) - 1

    # Get mask up to current pos
    sub_mask = pivot_mask.iloc[: current_index_pos + 1]

    # Get indices where mask is True
    pivot_indices = np.where(sub_mask.values)[0]

    if len(pivot_indices) < 2:
        return None, None, None, None

    curr_idx = pivot_indices[-1]
    prev_idx = pivot_indices[-2]

    return series.iloc[prev_idx], series.iloc[curr_idx], prev_idx, curr_idx


def calculate_pivot_slope(series: pd.Series, pivot_mask: pd.Series) -> pd.Series:
    """
    Calculates the slope (change in value per bar) between the current pivot and the previous pivot.
    The result is placed at the index of the current pivot.
    """
    result = pd.Series(np.nan, index=series.index)

    pivot_indices = np.where(pivot_mask.values)[0]

    for i in range(1, len(pivot_indices)):
        prev_idx = pivot_indices[i - 1]
        curr_idx = pivot_indices[i]

        bars_between = curr_idx - prev_idx
        if bars_between > 0:
            val_diff = series.iloc[curr_idx] - series.iloc[prev_idx]
            result.iloc[curr_idx] = val_diff / bars_between

    return result


def calculate_pivot_change_pct(series: pd.Series, pivot_mask: pd.Series) -> pd.Series:
    """
    Calculates the percentage change between the current pivot and the previous pivot.
    The result is placed at the index of the current pivot.
    """
    result = pd.Series(np.nan, index=series.index)

    pivot_indices = np.where(pivot_mask.values)[0]

    for i in range(1, len(pivot_indices)):
        prev_idx = pivot_indices[i - 1]
        curr_idx = pivot_indices[i]

        prev_val = series.iloc[prev_idx]
        if prev_val and prev_val != 0 and not pd.isna(prev_val):
            val_diff = series.iloc[curr_idx] - prev_val
            result.iloc[curr_idx] = val_diff / abs(prev_val)

    return result
