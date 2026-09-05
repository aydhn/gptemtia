from advanced_regime_matrix.regime_matrix_non_signal_policies import (
    scan_text_for_signal_claims,
    validate_feature_columns_non_signal,
    build_regime_matrix_non_signal_policies,
)


def test_scan_text_for_signal_claims():
    clean_text = "Feature matrix containing historical volatility and momentum indicators."
    signal_text = "Strong BUY signal triggered for Brent crude oil targeting higher returns."
    assert scan_text_for_signal_claims(clean_text) == []
    assert len(scan_text_for_signal_claims(signal_text)) > 0


def test_validate_feature_columns_non_signal():
    clean_cols = ["timestamp", "entity_id", "regime_matrix__volatility_atr_14"]
    dirty_cols = ["timestamp", "regime_matrix__buy_signal", "target_price"]
    assert validate_feature_columns_non_signal(clean_cols) is True
    assert validate_feature_columns_non_signal(dirty_cols) is False


def test_build_regime_matrix_non_signal_policies():
    df, s = build_regime_matrix_non_signal_policies()
    assert len(df) == 6
    assert s["total_policies"] == 6
    assert s["all_enforced"] is True
