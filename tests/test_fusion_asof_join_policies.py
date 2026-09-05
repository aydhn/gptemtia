"""Tests for Fusion AsOf Join Policies."""

import pandas as pd
from advanced_feature_fusion.fusion_asof_join_policies import (
    build_fusion_asof_join_policy_registry,
    get_asof_join_policies,
    safe_fusion_asof_join_backward,
)


def test_asof_join_policies():
    df, summary = build_fusion_asof_join_policy_registry()
    assert len(df) == 3
    assert summary["total_policies"] == 3
    assert summary["zero_future_data_enforced"] is True


def test_safe_fusion_asof_join_backward():
    left_times = pd.date_range("2025-01-01 10:00:00", periods=5, freq="1h", tz="UTC")
    left_df = pd.DataFrame({
        "timestamp": left_times,
        "price": [100.0, 101.0, 102.0, 103.0, 104.0],
    })

    right_times = pd.date_range("2025-01-01 09:30:00", periods=3, freq="2h", tz="UTC")
    right_df = pd.DataFrame({
        "release_timestamp": right_times,
        "macro_val": [1.5, 1.8, 2.0],
    })

    fused = safe_fusion_asof_join_backward(
        left_df=left_df,
        right_df=right_df,
        left_on="timestamp",
        right_on="release_timestamp",
    )
    assert len(fused) == len(left_df)
    assert "macro_val" in fused.columns
    # Check that right timestamp is always <= left timestamp
    valid_rows = fused.dropna(subset=["release_timestamp"])
    assert (valid_rows["release_timestamp"] <= valid_rows["timestamp"]).all()
    # Check source dataframes were not mutated
    assert "macro_val" not in left_df.columns
