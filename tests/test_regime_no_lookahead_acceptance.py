"""Tests for Regime No-Lookahead Acceptance."""

import pandas as pd
from advanced_regime_validation_acceptance.regime_no_lookahead_acceptance import (
    build_regime_no_lookahead_acceptance_report,
    validate_no_future_join_records,
    validate_no_negative_shift_usage,
    summarize_regime_no_lookahead_acceptance,
)


def test_no_lookahead_acceptance():
    df, summary = build_regime_no_lookahead_acceptance_report()
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["lookahead_clean"] is True

    s_df = summarize_regime_no_lookahead_acceptance(df)
    assert s_df["lookahead_clean"] is True

    # Test negative shift detection
    clean_text = "df['ret'] = df['close'].pct_change(1).shift(1)"
    assert validate_no_negative_shift_usage(clean_text)["passed"] is True

    dirty_text = "df['future_ret'] = df['close'].pct_change(-1)"
    res_dirty = validate_no_negative_shift_usage(dirty_text)
    assert res_dirty["passed"] is False

    # Test future join detection
    valid_join_df = pd.DataFrame({
        "base_timestamp": ["2026-01-02", "2026-01-03"],
        "context_timestamp": ["2026-01-01", "2026-01-02"],
    })
    assert validate_no_future_join_records(valid_join_df)["passed"] is True

    invalid_join_df = pd.DataFrame({
        "base_timestamp": ["2026-01-02", "2026-01-03"],
        "context_timestamp": ["2026-01-05", "2026-01-02"],
    })
    res_join = validate_no_future_join_records(invalid_join_df)
    assert res_join["passed"] is False
    assert res_join["future_leak_count"] == 1
