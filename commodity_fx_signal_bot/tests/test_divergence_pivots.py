import numpy as np
import pandas as pd
import pytest

from indicators.divergence_pivots import (
    PivotConfig,
    find_pivot_highs,
    find_pivot_lows,
    build_pivot_frame,
    get_last_two_pivots,
    calculate_pivot_slope,
)


@pytest.fixture
def synthetic_series():
    # A simple series: 0 1 2 3 2 1 0 1 2 1 0
    # Pivot High at index 3 (val 3) and index 8 (val 2)
    # Pivot Low at index 6 (val 0)
    data = [0.0, 1.0, 2.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 1.0, 0.0]
    return pd.Series(data)


@pytest.fixture
def synthetic_df(synthetic_series):
    return pd.DataFrame(
        {"close": synthetic_series, "rsi_14": synthetic_series * 10}  # Just dummy data
    )


def test_find_pivot_highs(synthetic_series):
    config = PivotConfig(left=2, right=2)
    highs = find_pivot_highs(synthetic_series, config)

    assert highs.sum() == 2
    assert highs.iloc[3] == True
    assert highs.iloc[8] == True


def test_find_pivot_lows(synthetic_series):
    config = PivotConfig(left=2, right=2)
    lows = find_pivot_lows(synthetic_series, config)

    assert lows.sum() == 1
    assert lows.iloc[6] == True


def test_build_pivot_frame(synthetic_df):
    config = PivotConfig(left=2, right=2)
    df_out = build_pivot_frame(
        synthetic_df, price_col="close", indicator_cols=["rsi_14"], config=config
    )

    assert "pivot_high_close" in df_out.columns
    assert "pivot_low_close" in df_out.columns
    assert "pivot_high_rsi_14" in df_out.columns
    assert "pivot_slope_close_high" in df_out.columns

    assert df_out["pivot_high_close"].iloc[3] == 3.0
    assert df_out["pivot_high_rsi_14"].iloc[3] == 30.0
    assert pd.isna(df_out["pivot_high_close"].iloc[4])


def test_get_last_two_pivots(synthetic_series):
    config = PivotConfig(left=2, right=2)
    highs = find_pivot_highs(synthetic_series, config)

    # At index 9, we should see both pivots
    prev_val, curr_val, prev_idx, curr_idx = get_last_two_pivots(
        synthetic_series, highs, 9
    )
    assert prev_idx == 3
    assert curr_idx == 8
    assert prev_val == 3.0
    assert curr_val == 2.0


def test_calculate_pivot_slope(synthetic_series):
    config = PivotConfig(left=2, right=2)
    highs = find_pivot_highs(synthetic_series, config)

    slope = calculate_pivot_slope(synthetic_series, highs)

    # Slope at index 8 = (2.0 - 3.0) / (8 - 3) = -1.0 / 5 = -0.2
    assert slope.iloc[8] == -0.2
    assert pd.isna(slope.iloc[3])
