"""Unit tests for Phase 119 no-lookahead alignment guard and forbidden column detection."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.no_lookahead_alignment_guard import (
    validate_no_future_timestamps,
    validate_no_forbidden_alignment_columns,
    validate_no_negative_shift_usage,
    validate_alignment_no_lookahead,
    build_no_lookahead_alignment_guard_registry,
)


def test_validate_no_future_timestamps():
    df = pd.DataFrame({
        "timestamp_utc": ["2026-09-01T00:00:00Z", "2026-09-02T00:00:00Z"],
    })
    res = validate_no_future_timestamps(df, "timestamp_utc", "2026-09-03T00:00:00Z")
    assert res["is_valid"] is True

    # Future row present
    res_bad = validate_no_future_timestamps(df, "timestamp_utc", "2026-09-01T12:00:00Z")
    assert res_bad["is_valid"] is False


def test_validate_no_forbidden_alignment_columns():
    df_clean = pd.DataFrame({"timestamp_utc": ["2026-09-01"], "fx_feature": [1.0]})
    assert validate_no_forbidden_alignment_columns(df_clean)["is_valid"] is True

    df_dirty = pd.DataFrame({"timestamp_utc": ["2026-09-01"], "target_return": [0.05]})
    assert validate_no_forbidden_alignment_columns(df_dirty)["is_valid"] is False


def test_validate_no_negative_shift_usage():
    safe_code = "df['ret'] = df['close'].pct_change()"
    assert validate_no_negative_shift_usage(safe_code)["is_valid"] is True

    bad_code = "df['future'] = df['close'].shift(-1)"
    assert validate_no_negative_shift_usage(bad_code)["is_valid"] is False


def test_build_guard_registry():
    df, summary = build_no_lookahead_alignment_guard_registry()
    assert len(df) == 5
    assert summary["all_enforced"] is True
    assert summary["status"] == "READY"
