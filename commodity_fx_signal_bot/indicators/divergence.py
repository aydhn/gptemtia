import logging
from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np
import pandas as pd

from config.settings import settings
from indicators.divergence_pivots import (
    PivotConfig,
    find_pivot_highs,
    find_pivot_lows,
    get_last_two_pivots,
)

logger = logging.getLogger(__name__)


@dataclass
class DivergenceConfig:
    pivot_left: int = settings.default_divergence_pivot_left
    pivot_right: int = settings.default_divergence_pivot_right
    lookback: int = settings.default_divergence_lookback
    min_price_move_pct: float = settings.default_divergence_min_price_move_pct
    min_indicator_move: float = settings.default_divergence_min_indicator_move
    indicator_columns: tuple[str, ...] = settings.default_divergence_indicator_columns
    include_hidden_divergence: bool = True
    include_regular_divergence: bool = True


def _get_pivot_config(config: DivergenceConfig) -> PivotConfig:
    return PivotConfig(
        left=config.pivot_left,
        right=config.pivot_right,
        min_move_pct=0.0,  # Handled locally
        allow_equal=False,
    )


def _detect_divergence(
    df: pd.DataFrame,
    indicator_col: str,
    direction: str,
    divergence_type: str,
    config: Optional[DivergenceConfig] = None,
) -> pd.Series:
    if config is None:
        config = DivergenceConfig()

    result = pd.Series(0, index=df.index, dtype=int)

    if "close" not in df.columns or indicator_col not in df.columns:
        return result

    price = df["close"]
    indicator = df[indicator_col]

    pivot_config = _get_pivot_config(config)

    if direction == "bullish":
        # Bullish looks at pivot lows
        pivots = find_pivot_lows(price, pivot_config)
    else:
        # Bearish looks at pivot highs
        pivots = find_pivot_highs(price, pivot_config)

    pivot_indices = np.where(pivots)[0]

    for i in range(1, len(pivot_indices)):
        prev_idx = pivot_indices[i - 1]
        curr_idx = pivot_indices[i]

        # Lookback check
        if curr_idx - prev_idx > config.lookback:
            continue

        p1 = price.iloc[prev_idx]
        p2 = price.iloc[curr_idx]

        i1 = indicator.iloc[prev_idx]
        i2 = indicator.iloc[curr_idx]

        if pd.isna(p1) or pd.isna(p2) or pd.isna(i1) or pd.isna(i2):
            continue

        # Check price move pct if min_price_move_pct is set
        if config.min_price_move_pct > 0:
            pct_change = abs(p2 - p1) / p1
            if pct_change < config.min_price_move_pct:
                continue

        # Check indicator move if min_indicator_move is set
        if config.min_indicator_move > 0:
            ind_change = abs(i2 - i1)
            if ind_change < config.min_indicator_move:
                continue

        is_divergence = False

        if divergence_type == "regular":
            if direction == "bullish":
                # Lower Low in Price, Higher Low in Indicator
                if p2 < p1 and i2 > i1:
                    is_divergence = True
            elif direction == "bearish":
                # Higher High in Price, Lower High in Indicator
                if p2 > p1 and i2 < i1:
                    is_divergence = True
        elif divergence_type == "hidden":
            if direction == "bullish":
                # Higher Low in Price, Lower Low in Indicator
                if p2 > p1 and i2 < i1:
                    is_divergence = True
            elif direction == "bearish":
                # Lower High in Price, Higher High in Indicator
                if p2 < p1 and i2 > i1:
                    is_divergence = True

        if is_divergence:
            result.iloc[curr_idx] = 1

    return result


def detect_regular_bullish_divergence(
    df: pd.DataFrame, indicator_col: str, config: Optional[DivergenceConfig] = None
) -> pd.Series:
    return _detect_divergence(df, indicator_col, "bullish", "regular", config)


def detect_regular_bearish_divergence(
    df: pd.DataFrame, indicator_col: str, config: Optional[DivergenceConfig] = None
) -> pd.Series:
    return _detect_divergence(df, indicator_col, "bearish", "regular", config)


def detect_hidden_bullish_divergence(
    df: pd.DataFrame, indicator_col: str, config: Optional[DivergenceConfig] = None
) -> pd.Series:
    return _detect_divergence(df, indicator_col, "bullish", "hidden", config)


def detect_hidden_bearish_divergence(
    df: pd.DataFrame, indicator_col: str, config: Optional[DivergenceConfig] = None
) -> pd.Series:
    return _detect_divergence(df, indicator_col, "bearish", "hidden", config)


def calculate_divergence_strength(
    df: pd.DataFrame,
    indicator_col: str,
    direction: str,
    config: Optional[DivergenceConfig] = None,
) -> pd.Series:
    """
    Calculates the strength of a divergence.
    Here, a simple heuristic is used: the product of the absolute percentage change in price
    and the absolute change in the indicator between the two pivots.
    """
    if config is None:
        config = DivergenceConfig()

    result = pd.Series(0.0, index=df.index)

    if "close" not in df.columns or indicator_col not in df.columns:
        return result

    price = df["close"]
    indicator = df[indicator_col]

    pivot_config = _get_pivot_config(config)

    if direction == "bullish":
        pivots = find_pivot_lows(price, pivot_config)
    else:
        pivots = find_pivot_highs(price, pivot_config)

    pivot_indices = np.where(pivots)[0]

    for i in range(1, len(pivot_indices)):
        prev_idx = pivot_indices[i - 1]
        curr_idx = pivot_indices[i]

        p1 = price.iloc[prev_idx]
        p2 = price.iloc[curr_idx]
        i1 = indicator.iloc[prev_idx]
        i2 = indicator.iloc[curr_idx]

        if pd.isna(p1) or pd.isna(p2) or pd.isna(i1) or pd.isna(i2) or p1 == 0:
            continue

        price_change_pct = abs(p2 - p1) / p1
        ind_change = abs(i2 - i1)

        strength = price_change_pct * ind_change
        result.iloc[curr_idx] = strength

    return result


def build_divergence_feature_frame(
    df: pd.DataFrame, config: Optional[DivergenceConfig] = None
) -> Tuple[pd.DataFrame, dict]:
    if config is None:
        config = DivergenceConfig()

    out = pd.DataFrame(index=df.index)
    summary = {
        "input_rows": len(df),
        "indicator_columns_used": [],
        "missing_indicator_columns": [],
        "divergence_columns": [],
        "total_divergence_count": 0,
        "divergence_count_by_column": {},
        "active_last_row_divergences": [],
        "warnings": [],
        "notes": [
            "Warning: Pivot detection uses 'right' parameter which introduces lookahead bias equal to 'right' bars.",
            "Divergence values are recorded at the pivot index, but can only be confirmed after 'right' bars.",
        ],
    }

    if "close" not in df.columns:
        summary["warnings"].append(
            "Missing 'close' column, cannot calculate divergence."
        )
        return out, summary

    for ind_col in config.indicator_columns:
        if ind_col not in df.columns:
            summary["missing_indicator_columns"].append(ind_col)
            continue

        summary["indicator_columns_used"].append(ind_col)

        # Regular
        if config.include_regular_divergence:
            bull_col = f"div_regular_bullish_{ind_col}"
            bear_col = f"div_regular_bearish_{ind_col}"

            out[bull_col] = detect_regular_bullish_divergence(df, ind_col, config)
            out[bear_col] = detect_regular_bearish_divergence(df, ind_col, config)

            summary["divergence_columns"].extend([bull_col, bear_col])

        # Hidden
        if config.include_hidden_divergence:
            bull_col = f"div_hidden_bullish_{ind_col}"
            bear_col = f"div_hidden_bearish_{ind_col}"

            out[bull_col] = detect_hidden_bullish_divergence(df, ind_col, config)
            out[bear_col] = detect_hidden_bearish_divergence(df, ind_col, config)

            summary["divergence_columns"].extend([bull_col, bear_col])

        # Strength
        str_bull_col = f"div_strength_bullish_{ind_col}"
        str_bear_col = f"div_strength_bearish_{ind_col}"
        out[str_bull_col] = calculate_divergence_strength(
            df, ind_col, "bullish", config
        )
        out[str_bear_col] = calculate_divergence_strength(
            df, ind_col, "bearish", config
        )
        summary["divergence_columns"].extend([str_bull_col, str_bear_col])

    # Stats
    for col in out.columns:
        if col.startswith("div_") and not col.startswith("div_strength"):
            count = out[col].sum()
            summary["total_divergence_count"] += count
            summary["divergence_count_by_column"][col] = int(count)

            if len(out) > 0 and out[col].iloc[-1] > 0:
                summary["active_last_row_divergences"].append(col)

    return out, summary
