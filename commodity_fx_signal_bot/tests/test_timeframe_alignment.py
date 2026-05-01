import pytest
import pandas as pd
import numpy as np
from mtf.timeframe_alignment import prefix_columns_for_timeframe, align_context_to_base


def test_prefix_columns():
    df = pd.DataFrame({"close": [1, 2], "volume": [10, 20]})
    res = prefix_columns_for_timeframe(df, "1d")
    assert list(res.columns) == ["tf_1d_close", "tf_1d_volume"]
    assert "close" not in res.columns


def test_align_context_to_base_strict_no_lookahead():
    # Create base
    dates_base = pd.date_range("2023-01-01 00:00:00", periods=5, freq="1h")
    base_df = pd.DataFrame({"close": [1, 2, 3, 4, 5]}, index=dates_base)

    # Create context
    dates_context = pd.date_range("2023-01-01 01:00:00", periods=2, freq="2h")
    context_df = pd.DataFrame({"ctx_close": [10, 20]}, index=dates_context)

    res = align_context_to_base(
        base_df, context_df, "1h", "2h", forward_fill=True, strict_no_lookahead=True
    )

    df = res.dataframe
    assert len(df) == 5
    assert "tf_2h_ctx_close" in df.columns
    # Check that at 2023-01-01 00:00:00 context is NaN (because context first row is at 01:00:00)
    assert pd.isna(df.iloc[0]["tf_2h_ctx_close"])
    # At 01:00:00 it should be 10
    assert df.iloc[1]["tf_2h_ctx_close"] == 10
    # At 02:00:00 it should be 10 (forward filled)
    assert df.iloc[2]["tf_2h_ctx_close"] == 10
    # At 03:00:00 it should be 20
    assert df.iloc[3]["tf_2h_ctx_close"] == 20


def test_stale_context_count():
    dates_base = pd.date_range("2023-01-01 00:00:00", periods=10, freq="1h")
    base_df = pd.DataFrame({"close": range(10)}, index=dates_base)

    dates_context = pd.date_range("2023-01-01 00:00:00", periods=1, freq="1d")
    context_df = pd.DataFrame({"ctx_close": [10]}, index=dates_context)

    # max age = 5
    res = align_context_to_base(base_df, context_df, "1h", "1d", max_context_age_bars=5)

    df = res.dataframe
    # base bars: 0..9.
    # At index 0 context is 0 bars old.
    # At index 6, context is 6 bars old -> stale
    # Total bars = 10, so indices 6, 7, 8, 9 are stale (4 bars)
    assert res.stale_context_count == 4
    assert "tf_1d_context_age_bars" in df.columns
