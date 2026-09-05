"""Unit tests for Phase 119 deterministic backward-only asof join engine."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.asof_join_policies import safe_asof_join_backward


def test_safe_asof_join_backward_basic():
    # Continuous price series
    left_df = pd.DataFrame({
        "timestamp_utc": ["2026-09-01T10:00:00Z", "2026-09-01T11:00:00Z", "2026-09-01T12:00:00Z"],
        "price": [100.0, 101.0, 102.0],
    })

    # Macro release that occurred at 10:30
    right_df = pd.DataFrame({
        "timestamp_utc": ["2026-09-01T10:30:00Z"],
        "macro_rate": [5.25],
    })

    result = safe_asof_join_backward(
        left_df=left_df,
        right_df=right_df,
        left_on="timestamp_utc",
        right_on="timestamp_utc",
    )

    assert len(result) == 3
    # At 10:00, macro was not yet released -> NaN
    assert pd.isna(result.loc[0, "macro_rate"])
    # At 11:00, macro had been released at 10:30 -> 5.25
    assert result.loc[1, "macro_rate"] == 5.25
    # At 12:00, macro remains 5.25
    assert result.loc[2, "macro_rate"] == 5.25


def test_safe_asof_join_backward_source_preserved():
    left_df = pd.DataFrame({
        "timestamp_utc": ["2026-09-01T10:00:00Z", "2026-09-01T11:00:00Z"],
        "val": [1, 2],
    })
    orig_left_cols = list(left_df.columns)
    right_df = pd.DataFrame({
        "timestamp_utc": ["2026-09-01T10:00:00Z"],
        "extra": [10],
    })

    _ = safe_asof_join_backward(left_df, right_df, "timestamp_utc", "timestamp_utc")

    # Verify left_df was not modified in-place
    assert list(left_df.columns) == orig_left_cols
    assert len(left_df) == 2


def test_safe_asof_join_backward_empty_handling():
    left_df = pd.DataFrame()
    right_df = pd.DataFrame({"ts": ["2026-09-01T00:00:00Z"], "val": [1]})
    res = safe_asof_join_backward(left_df, right_df, "ts", "ts")
    assert res.empty
