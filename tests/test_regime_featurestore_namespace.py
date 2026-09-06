"""Tests for Phase 134 Regime FeatureStore Namespace."""

from advanced_regime_featurestore_integration.regime_featurestore_namespace import (
    build_regime_featurestore_namespace_registry,
    build_regime_store_key,
    validate_regime_store_key,
    summarize_regime_featurestore_namespace,
)


def test_namespace_registry():
    df, summary = build_regime_featurestore_namespace_registry()
    assert not df.empty
    assert len(df) >= 5
    assert (df["non_signal"] == True).all()


def test_build_and_validate_keys():
    key = build_regime_store_key("taxonomy", "growth_1", "foundation")
    assert key.startswith("regime_store_")
    res = validate_regime_store_key(key)
    assert res["is_valid"] is True
    assert res["non_signal"] is True

    bad_key1 = "invalid_prefix_key"
    assert validate_regime_store_key(bad_key1)["is_valid"] is False

    bad_key2 = "regime_store_buy_signal_action"
    res2 = validate_regime_store_key(bad_key2)
    assert res2["is_valid"] is False
    assert res2["non_signal"] is False
