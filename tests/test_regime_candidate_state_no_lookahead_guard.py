import pandas as pd
from advanced_regime_rule_free.regime_candidate_state_no_lookahead_guard import (
    validate_no_future_candidate_state_join,
    validate_no_forbidden_candidate_state_columns,
    validate_no_negative_shift_usage,
    build_regime_candidate_state_no_lookahead_guard_registry,
    summarize_candidate_state_no_lookahead_guard,
)


def test_validate_no_future_candidate_state_join():
    base_df = pd.DataFrame({"timestamp_utc": ["2025-01-01T10:00:00Z", "2025-01-01T11:00:00Z"]})
    valid_ctx_df = pd.DataFrame({"context_timestamp_utc": ["2025-01-01T09:00:00Z", "2025-01-01T11:00:00Z"]})
    res_valid = validate_no_future_candidate_state_join(base_df, valid_ctx_df)
    assert res_valid["is_valid"] is True
    assert res_valid["future_leak_count"] == 0

    leaky_ctx_df = pd.DataFrame({"context_timestamp_utc": ["2025-01-01T12:00:00Z", "2025-01-01T11:00:00Z"]})
    res_leak = validate_no_future_candidate_state_join(base_df, leaky_ctx_df)
    assert res_leak["is_valid"] is False
    assert res_leak["future_leak_count"] == 1


def test_validate_no_forbidden_candidate_state_columns():
    clean_df = pd.DataFrame({"timestamp_utc": [1], "volatility_score": [0.5]})
    assert validate_no_forbidden_candidate_state_columns(clean_df)["is_valid"] is True

    forbidden_df = pd.DataFrame({"timestamp_utc": [1], "target_return": [0.02]})
    res_f = validate_no_forbidden_candidate_state_columns(forbidden_df)
    assert res_f["is_valid"] is False
    assert "target_return" in res_f["forbidden_columns"]


def test_validate_no_negative_shift_usage():
    clean_code = "df['ret'] = df['close'].pct_change()"
    assert validate_no_negative_shift_usage(clean_code)["is_valid"] is True

    bad_code = "df['next'] = df['close'].shift(-1)"
    res_bad = validate_no_negative_shift_usage(bad_code)
    assert res_bad["is_valid"] is False


def test_build_regime_candidate_state_no_lookahead_guard_registry():
    df, summary = build_regime_candidate_state_no_lookahead_guard_registry()
    assert len(df) == 4
    assert summary["all_enforced"] is True
    assert summary["guard_status"] == "ACTIVE"
