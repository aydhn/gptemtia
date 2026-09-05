from advanced_feature_store_integration.feature_store_forbidden_column_policies import (
    build_feature_store_forbidden_column_policy_registry,
    validate_feature_store_forbidden_columns,
    summarize_feature_store_forbidden_column_policies,
)

def test_forbidden_column_policies():
    df, s = build_feature_store_forbidden_column_policy_registry()
    assert not df.empty
    assert s["total_forbidden_columns"] >= 15

    safe_cols = ["timestamp", "symbol", "sma_20", "atr_14", "rolling_mean"]
    res_safe = validate_feature_store_forbidden_columns(safe_cols)
    assert res_safe["is_safe"] is True

    bad_cols = ["timestamp", "signal", "buy_price", "target_return", "full_text", "embedding"]
    res_bad = validate_feature_store_forbidden_columns(bad_cols)
    assert res_bad["is_safe"] is False
    assert "signal" in res_bad["forbidden_detected"]
    assert "full_text" in res_bad["forbidden_detected"]
