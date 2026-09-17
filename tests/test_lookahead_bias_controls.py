# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Lookahead Bias Controls."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.lookahead_bias_controls import (
    build_lookahead_bias_control_registry,
    validate_lookahead_bias_columns,
    LOOKAHEAD_CONTROLS,
)


def test_build_lookahead_bias_controls():
    profile = get_default_backtest_governance_profile()
    df, summary = build_lookahead_bias_control_registry(profile)

    assert not df.empty
    assert len(df) == 5
    assert "control_id" in df.columns
    assert "name" in df.columns
    assert (df["execution_allowed"] == False).all()
    assert (df["status"] == "ACTIVE").all()
    assert summary["total_controls"] == 5
    assert len(LOOKAHEAD_CONTROLS) == 5


def test_validate_lookahead_bias_columns():
    invalid_cols = ["timestamp", "close", "future_return_5d", "lead_return"]
    res_invalid = validate_lookahead_bias_columns(invalid_cols)
    assert res_invalid["is_clean"] is False
    assert res_invalid["is_blocked"] is True
    assert len(res_invalid["detected_leaks"]) > 0

    valid_cols = ["timestamp", "open", "high", "low", "close", "volume"]
    res_valid = validate_lookahead_bias_columns(valid_cols)
    assert res_valid["is_clean"] is True
    assert res_valid["is_blocked"] is False
    assert len(res_valid["detected_leaks"]) == 0
