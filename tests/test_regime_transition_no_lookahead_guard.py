"""Tests for Regime Transition No-Lookahead Guards."""

import pandas as pd
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_no_lookahead_guard import (
    build_regime_transition_no_lookahead_guard_registry,
    validate_no_forbidden_transition_columns,
    validate_no_negative_shift_usage,
    summarize_transition_no_lookahead_guard,
)


def test_build_regime_transition_no_lookahead_guard_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_regime_transition_no_lookahead_guard_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "guard_key" in df.columns

    assert summary["total_guards"] == 3
    assert summary["all_strict_blocking"] is True


def test_validate_no_negative_shift_usage():
    code_clean = "df['roll_mean'] = df['close'].rolling(20).mean()"
    res_clean = validate_no_negative_shift_usage(code_clean)
    assert res_clean["is_valid"] is True

    code_bad = "df['next_close'] = df['close'].shift(-1)"
    res_bad = validate_no_negative_shift_usage(code_bad)
    assert res_bad["is_valid"] is False
    assert res_bad["violations_count"] > 0


def test_validate_no_forbidden_transition_columns():
    df_clean = pd.DataFrame([{"close": 100, "volume": 1000}])
    res_clean = validate_no_forbidden_transition_columns(df_clean)
    assert res_clean["is_valid"] is True

    df_bad = pd.DataFrame([{"close": 100, "buy_signal": 1}])
    res_bad = validate_no_forbidden_transition_columns(df_bad)
    assert res_bad["is_valid"] is False
