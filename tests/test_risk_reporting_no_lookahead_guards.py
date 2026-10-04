# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting No-Lookahead Guards."""

import pandas as pd

from advanced_risk_reporting.risk_reporting_config import (
    get_default_risk_reporting_profile,
)
from advanced_risk_reporting.risk_reporting_no_lookahead_guards import (
    build_risk_reporting_no_lookahead_guard_registry,
    validate_risk_reporting_no_lookahead_columns,
    validate_no_future_risk_reporting_join,
)


def test_build_risk_reporting_no_lookahead_guard_registry():
    """Test registry builder for no-lookahead guards."""
    profile = get_default_risk_reporting_profile()
    df, summary = build_risk_reporting_no_lookahead_guard_registry(profile)

    assert not df.empty
    assert len(df) == 2

    # Check guard items
    guard_names = df["guard_name"].tolist()
    assert "risk_reporting_no_future_shift_guard" in guard_names
    assert "risk_reporting_asof_join_guard" in guard_names

    assert summary["guard_count"] == 2
    assert summary["all_active"] is True

    # Verify phase columns are added
    assert "current_phase" in df.columns
    assert "target_final_phase" in df.columns
    assert "next_phase" in df.columns


def test_validate_risk_reporting_no_lookahead_columns_valid():
    """Test column validation with valid columns."""
    valid_cols = ["date", "price", "return_1d", "volatility_20d", "signal"]
    result = validate_risk_reporting_no_lookahead_columns(valid_cols)

    assert result["is_valid"] is True
    assert len(result["violations"]) == 0
    assert result["action"] == "ALLOW"


def test_validate_risk_reporting_no_lookahead_columns_invalid():
    """Test column validation with invalid columns."""
    invalid_cols = [
        "date",
        "price",
        "future_return_1d",
        "lead_signal",
        "realized_future_pnl",
        "price_shift(-1)",
    ]
    result = validate_risk_reporting_no_lookahead_columns(invalid_cols)

    assert result["is_valid"] is False
    assert len(result["violations"]) == 4
    assert result["action"] == "BLOCK"

    # Check that the specific violations were caught
    assert "future_return_1d" in result["violations"]
    assert "lead_signal" in result["violations"]
    assert "realized_future_pnl" in result["violations"]
    assert "price_shift(-1)" in result["violations"]


def test_validate_no_future_risk_reporting_join_valid():
    """Test join validation with valid (backward-only) timestamps."""
    # Left (target) DataFrame
    left_df = pd.DataFrame(
        {"left_ts": pd.date_range("2023-01-05", periods=5), "val": range(5)}
    )

    # Right (source) DataFrame - earlier or equal timestamps
    right_df = pd.DataFrame(
        {"right_ts": pd.date_range("2023-01-01", periods=5), "feature": range(5)}
    )

    result = validate_no_future_risk_reporting_join(
        left_df, right_df, "left_ts", "right_ts"
    )

    assert result["is_valid"] is True
    assert result["violations_count"] == 0
    assert result["action"] == "ALLOW"


def test_validate_no_future_risk_reporting_join_empty():
    """Test join validation with empty DataFrames."""
    left_df = pd.DataFrame(columns=["left_ts", "val"])
    right_df = pd.DataFrame(
        {"right_ts": pd.date_range("2023-01-01", periods=5), "feature": range(5)}
    )

    result = validate_no_future_risk_reporting_join(
        left_df, right_df, "left_ts", "right_ts"
    )

    assert result["is_valid"] is True
    assert result["action"] == "ALLOW"


def test_validate_no_future_risk_reporting_join_missing_columns():
    """Test join validation with missing timestamp columns."""
    left_df = pd.DataFrame(
        {"timestamp": pd.date_range("2023-01-05", periods=5), "val": range(5)}
    )
    right_df = pd.DataFrame(
        {"right_ts": pd.date_range("2023-01-01", periods=5), "feature": range(5)}
    )

    # Missing left_ts
    result = validate_no_future_risk_reporting_join(
        left_df, right_df, "left_ts", "right_ts"
    )

    assert result["is_valid"] is True
    assert result["action"] == "ALLOW"


def test_validate_no_future_risk_reporting_join_invalid():
    """Test join validation with lookahead violation."""
    # Left (target) DataFrame - earlier timestamps
    left_df = pd.DataFrame(
        {"left_ts": pd.date_range("2023-01-01", periods=5), "val": range(5)}
    )

    # Right (source) DataFrame - future timestamps
    right_df = pd.DataFrame(
        {"right_ts": pd.date_range("2023-01-05", periods=5), "feature": range(5)}
    )

    result = validate_no_future_risk_reporting_join(
        left_df, right_df, "left_ts", "right_ts"
    )

    assert result["is_valid"] is False
    assert result["violations_count"] == 1
    assert result["action"] == "BLOCK"
