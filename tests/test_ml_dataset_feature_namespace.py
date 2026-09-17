"""Test suite for Phase 137 ML Dataset Feature Namespace."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_feature_namespace import (
    build_ml_dataset_feature_namespace_registry,
    build_ml_dataset_feature_key,
    validate_ml_dataset_feature_key,
    summarize_ml_dataset_feature_namespace,
)


def test_build_feature_namespace():
    df, summary = build_ml_dataset_feature_namespace_registry()
    assert not df.empty
    assert summary["total_namespaces"] >= 5


def test_feature_key_construction_and_validation():
    key = build_ml_dataset_feature_key("regime", "volatility_score")
    assert key == "ml_feature_regime_volatility_score"
    v = validate_ml_dataset_feature_key(key)
    assert v["valid"] is True

    bad_key = "ml_feature_regime_buy_signal"
    v_bad = validate_ml_dataset_feature_key(bad_key)
    assert v_bad["valid"] is False
