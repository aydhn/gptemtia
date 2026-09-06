"""Tests for Regime Timestamp Order Acceptance."""

import pandas as pd
from advanced_regime_validation_acceptance.regime_timestamp_order_acceptance import (
    build_regime_timestamp_order_acceptance_report,
    validate_timestamp_monotonicity,
    validate_context_timestamp_not_future,
    summarize_regime_timestamp_order_acceptance,
)


def test_timestamp_order_acceptance():
    df, summary = build_regime_timestamp_order_acceptance_report()
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["timestamp_order_clean"] is True

    s_df = summarize_regime_timestamp_order_acceptance(df)
    assert s_df["all_passed"] is True

    # Monotonicity test
    mono_df = pd.DataFrame({"timestamp": ["2026-01-01", "2026-01-02", "2026-01-03"]})
    assert validate_timestamp_monotonicity(mono_df)["passed"] is True

    non_mono_df = pd.DataFrame({"timestamp": ["2026-01-01", "2026-01-03", "2026-01-02"]})
    res_mono = validate_timestamp_monotonicity(non_mono_df)
    assert res_mono["passed"] is False
    assert res_mono["violations_count"] > 0

    # Context timestamp not future
    valid_pair = pd.DataFrame({
        "base_timestamp": ["2026-01-05", "2026-01-06"],
        "context_timestamp": ["2026-01-04", "2026-01-05"],
    })
    assert validate_context_timestamp_not_future(valid_pair)["passed"] is True

    invalid_pair = pd.DataFrame({
        "base_timestamp": ["2026-01-05", "2026-01-06"],
        "context_timestamp": ["2026-01-07", "2026-01-05"],
    })
    res_pair = validate_context_timestamp_not_future(invalid_pair)
    assert res_pair["passed"] is False
    assert res_pair["future_violations"] == 1
