"""Tests for No-Lookahead Fusion Guard."""

import pytest
import pandas as pd
from advanced_feature_fusion.no_lookahead_fusion_guard import (
    build_no_lookahead_fusion_guard_registry,
    validate_no_future_fusion_join,
    validate_no_forbidden_fusion_columns,
    validate_no_full_article_columns,
    validate_no_negative_shift_usage,
)


def test_guard_registry():
    df, summary = build_no_lookahead_fusion_guard_registry()
    assert len(df) >= 4
    assert summary["status"] == "READY"


def test_future_join_validation():
    # Valid
    df_valid = pd.DataFrame({
        "timestamp": pd.to_datetime(["2025-01-01 12:00:00"], utc=True),
        "release_timestamp": pd.to_datetime(["2025-01-01 11:00:00"], utc=True),
    })
    res = validate_no_future_fusion_join(df_valid, base_timestamp_col="timestamp", release_timestamp_col="release_timestamp")
    assert res["valid"] is True

    # Invalid: future leak
    df_invalid = pd.DataFrame({
        "timestamp": pd.to_datetime(["2025-01-01 10:00:00"], utc=True),
        "release_timestamp": pd.to_datetime(["2025-01-01 11:00:00"], utc=True),
    })
    with pytest.raises(ValueError):
        validate_no_future_fusion_join(df_invalid, base_timestamp_col="timestamp", release_timestamp_col="release_timestamp")


def test_forbidden_columns_validation():
    clean_df = pd.DataFrame({"timestamp": [1], "volatility": [0.2]})
    res = validate_no_forbidden_fusion_columns(clean_df)
    assert res["valid"] is True

    bad_df = pd.DataFrame({"timestamp": [1], "buy_signal": [1]})
    res_bad = validate_no_forbidden_fusion_columns(bad_df)
    assert res_bad["valid"] is False


def test_negative_shift_validation():
    res_clean = validate_no_negative_shift_usage("df['val'].shift(1)")
    assert res_clean["valid"] is True

    res_bad = validate_no_negative_shift_usage("df['val'].shift(-1)")
    assert res_bad["valid"] is False
