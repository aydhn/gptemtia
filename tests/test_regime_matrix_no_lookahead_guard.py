import pandas as pd
from advanced_regime_matrix.regime_matrix_no_lookahead_guard import (
    audit_dataframe_no_lookahead,
    validate_code_no_negative_shift,
)


def test_audit_dataframe_no_lookahead_clean():
    clean_df = pd.DataFrame({
        "timestamp": pd.date_range("2026-01-01", periods=3, tz="UTC"),
        "entity_id": ["BRENT", "BRENT", "BRENT"],
        "regime_matrix__volatility_atr_14": [1.0, 1.1, 1.2],
    })
    audit = audit_dataframe_no_lookahead(clean_df)
    assert audit["guard_passed"] is True
    assert len(audit["violations"]) == 0


def test_audit_dataframe_no_lookahead_catches_forbidden_columns():
    dirty_df = pd.DataFrame({
        "timestamp": pd.date_range("2026-01-01", periods=3, tz="UTC"),
        "target_return_5d": [0.01, -0.02, 0.03],
        "future_price": [100, 101, 102],
    })
    audit = audit_dataframe_no_lookahead(dirty_df)
    assert audit["guard_passed"] is False
    assert len(audit["violations"]) >= 2


def test_validate_code_no_negative_shift():
    safe_code = "df['lag_1'] = df['close'].shift(1)"
    unsafe_code = "df['future_ret'] = df['close'].shift(-1)"
    assert validate_code_no_negative_shift(safe_code) is True
    assert validate_code_no_negative_shift(unsafe_code) is False
