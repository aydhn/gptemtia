"""Tests for Fusion Timestamp Alignment Policies."""

import pandas as pd
from advanced_feature_fusion.fusion_timestamp_alignment_policies import (
    build_fusion_timestamp_alignment_policy_registry,
    get_timestamp_alignment_policies,
    validate_fusion_timestamp_order,
)


def test_timestamp_alignment_policies():
    df, summary = build_fusion_timestamp_alignment_policy_registry()
    assert len(df) == 3
    assert summary["total_policies"] == 3
    assert summary["zero_future_data_enforced"] is True


def test_validate_timestamp_order():
    # Monotonic increasing
    times = pd.date_range("2025-01-01 10:00:00", periods=5, freq="h", tz="UTC")
    df_sorted = pd.DataFrame({"timestamp": times})
    res_sorted = validate_fusion_timestamp_order(df_sorted)
    assert res_sorted["valid"] is True

    # Unsorted
    df_unsorted = pd.DataFrame({"timestamp": list(reversed(times))})
    res_unsorted = validate_fusion_timestamp_order(df_unsorted)
    assert res_unsorted["valid"] is False
