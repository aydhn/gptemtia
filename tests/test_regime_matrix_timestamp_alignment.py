import pandas as pd
from advanced_regime_matrix.regime_matrix_timestamp_alignment import (
    build_regime_matrix_timestamp_alignment_registry,
    validate_regime_matrix_timestamp_order,
    summarize_regime_matrix_timestamp_alignment,
)


def test_build_regime_matrix_timestamp_alignment_registry():
    df, s = build_regime_matrix_timestamp_alignment_registry()
    assert len(df) == 5
    assert s["total_rules"] == 5
    assert s["all_enforced"] is True
    assert s["all_non_signal"] is True


def test_validate_regime_matrix_timestamp_order():
    valid_df = pd.DataFrame({
        "base_ts": pd.to_datetime(["2026-01-02 10:00:00", "2026-01-03 10:00:00"], utc=True),
        "ctx_ts": pd.to_datetime(["2026-01-01 10:00:00", "2026-01-02 10:00:00"], utc=True),
    })
    res_valid = validate_regime_matrix_timestamp_order(valid_df, "base_ts", "ctx_ts")
    assert res_valid["is_valid"] is True
    assert res_valid["leak_count"] == 0

    future_df = pd.DataFrame({
        "base_ts": pd.to_datetime(["2026-01-02 10:00:00", "2026-01-03 10:00:00"], utc=True),
        "ctx_ts": pd.to_datetime(["2026-01-05 10:00:00", "2026-01-06 10:00:00"], utc=True),
    })
    res_future = validate_regime_matrix_timestamp_order(future_df, "base_ts", "ctx_ts")
    assert res_future["is_valid"] is False
    assert res_future["leak_count"] == 2
