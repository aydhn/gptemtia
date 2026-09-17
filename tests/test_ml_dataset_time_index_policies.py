"""Test suite for Phase 137 ML Dataset Time Index Policies."""

import pytest
import pandas as pd
from advanced_ml_dataset_registry.ml_dataset_time_index_policies import (
    build_ml_dataset_time_index_policy_registry,
    validate_ml_dataset_time_index,
    summarize_ml_dataset_time_index_policies,
)


def test_build_time_index_policies():
    df, summary = build_ml_dataset_time_index_policy_registry()
    assert not df.empty
    assert summary["total_time_index_policies"] >= 3
    assert summary["timestamp_utc_required"] is True


def test_validate_time_index():
    good_df = pd.DataFrame({"timestamp_utc": pd.to_datetime(["2025-01-01", "2025-01-02"], utc=True)})
    v_good = validate_ml_dataset_time_index(good_df, "timestamp_utc")
    assert v_good["valid"] is True

    bad_df = pd.DataFrame({"time": [1, 2]})
    v_bad = validate_ml_dataset_time_index(bad_df, "timestamp_utc")
    assert v_bad["valid"] is False
