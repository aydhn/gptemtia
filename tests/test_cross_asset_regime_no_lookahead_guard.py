"""Tests for Cross-Asset Regime No-Lookahead Guard."""

import pandas as pd
from advanced_cross_asset_regime_context.cross_asset_regime_no_lookahead_guard import (
    LOOKAHEAD_GUARD_RULES,
    build_cross_asset_regime_no_lookahead_guard_registry,
    validate_no_future_cross_asset_join,
    validate_no_forbidden_cross_asset_columns,
    validate_no_negative_shift_usage,
)


def test_build_cross_asset_regime_no_lookahead_guard_registry():
    assert len(LOOKAHEAD_GUARD_RULES) >= 3
    df, summary = build_cross_asset_regime_no_lookahead_guard_registry()
    assert len(df) >= 3
    assert "guard_id" in df.columns
    assert summary["all_enforced"] is True
    assert summary["all_non_signal"] is True


def test_validate_no_future_cross_asset_join():
    left_df = pd.DataFrame({"base_ts": ["2026-01-02", "2026-01-03"]})
    right_df_valid = pd.DataFrame({"context_ts": ["2026-01-01", "2026-01-02"]})
    res_valid = validate_no_future_cross_asset_join(left_df, right_df_valid, "base_ts", "context_ts")
    assert res_valid["valid"] is True

    right_df_invalid = pd.DataFrame({"context_ts": ["2026-01-05", "2026-01-06"]})
    res_invalid = validate_no_future_cross_asset_join(left_df, right_df_invalid, "base_ts", "context_ts")
    assert res_invalid["valid"] is False


def test_validate_no_forbidden_cross_asset_columns():
    df_clean = pd.DataFrame({"regime_id": [1], "volatility": [0.2]})
    assert validate_no_forbidden_cross_asset_columns(df_clean)["valid"] is True

    df_forbidden = pd.DataFrame({"signal": [1], "volatility": [0.2]})
    assert validate_no_forbidden_cross_asset_columns(df_forbidden)["valid"] is False


def test_validate_no_negative_shift_usage():
    clean_code = "df['prior'] = df['close'].shift(1)"
    assert validate_no_negative_shift_usage(clean_code)["valid"] is True

    leaky_code = "df['future'] = df['close'].shift(-1)"
    assert validate_no_negative_shift_usage(leaky_code)["valid"] is False
