from advanced_feature_store_integration.feature_store_namespace_registry import (
    build_feature_store_namespace_registry,
    build_store_feature_key,
    validate_store_feature_key,
    summarize_feature_store_namespace_registry,
)

def test_namespace_registry_and_validation():
    df, s = build_feature_store_namespace_registry()
    assert not df.empty
    assert s["total_namespaces"] >= 8

    # Test valid key
    valid_key = build_store_feature_key("fx", "eurusd", "sma_20")
    assert valid_key == "fx__eurusd__sma_20"
    v1 = validate_store_feature_key(valid_key)
    assert v1["is_valid"] is True

    # Test key with forbidden word
    bad_key = "fx__eurusd__signal_buy"
    v2 = validate_store_feature_key(bad_key)
    assert v2["is_valid"] is False
    assert v2["non_signal"] is False
