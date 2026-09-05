from advanced_regime_matrix.regime_matrix_safety_boundary import (
    audit_regime_matrix_safety_boundary,
    is_safe_regime_matrix_operation,
)


def test_audit_regime_matrix_safety_boundary():
    df, s = audit_regime_matrix_safety_boundary()
    assert s["safety_status"] == "SECURE"
    assert s["no_go_count"] == 15
    assert s["safe_go_count"] == 7
    assert s["live_trading_prohibited"] is True
    assert s["model_training_prohibited"] is True
    assert s["source_mutation_prohibited"] is True


def test_is_safe_regime_matrix_operation():
    assert is_safe_regime_matrix_operation("read_feature_matrix") is True
    assert is_safe_regime_matrix_operation("live_trade_order") is False
    assert is_safe_regime_matrix_operation("train_hmm_model") is False
    assert is_safe_regime_matrix_operation("generate_buy_signal") is False
