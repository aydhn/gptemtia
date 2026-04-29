import numpy as np
import pandas as pd

from data.cleaning.missing_data import (
    calculate_missing_ratios,
    detect_timestamp_gaps,
    fill_small_price_gaps,
    summarize_gaps,
)


def test_calculate_missing_ratios():
    df = pd.DataFrame({"open": [1, np.nan, 3], "close": [1, 2, 3]})
    ratios = calculate_missing_ratios(df)
    assert ratios["open"] == 1 / 3
    assert ratios["close"] == 0.0


def test_detect_timestamp_gaps():
    df = pd.DataFrame(
        {"close": [100, 101, 102]},
        index=pd.DatetimeIndex(["2024-01-01", "2024-01-02", "2024-01-05"]),
    )
    gaps = detect_timestamp_gaps(df, "1d")
    assert len(gaps) == 1
    # We use 1.5x expected as gap threshold, so gap > 1.5 days.
    # 2024-01-02 to 2024-01-05 is 3 days gap.


def test_summarize_gaps():
    df = pd.DataFrame(
        {"close": [100, 101, 102]},
        index=pd.DatetimeIndex(["2024-01-01", "2024-01-02", "2024-01-05"]),
    )
    gaps = detect_timestamp_gaps(df, "1d")
    summary = summarize_gaps(gaps)
    assert summary["total_gaps"] == 1


def test_fill_small_price_gaps():
    df = pd.DataFrame(
        {"close": [100, np.nan, np.nan, 103, np.nan, np.nan, np.nan, 107]}
    )
    filled, counts = fill_small_price_gaps(df, max_gap=2)

    # First gap is 2 NaNs, should be filled
    assert filled["close"].iloc[1] == 100
    assert filled["close"].iloc[2] == 100

    # Second gap is 3 NaNs, should NOT be filled (max_gap=2 limit applies per gap?
    # Actually pandas .ffill(limit=2) fills the first 2 of the 3 NaN gap)
    assert filled["close"].iloc[4] == 103
    assert filled["close"].iloc[5] == 103
    assert np.isnan(filled["close"].iloc[6])  # 3rd NaN remains
