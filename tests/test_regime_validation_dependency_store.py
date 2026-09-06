"""Tests for Phase 134 Regime Validation Dependency Store."""

from advanced_regime_featurestore_integration.regime_validation_dependency_store import (
    build_regime_validation_dependency_store_registry,
    summarize_regime_validation_dependency_store,
)


def test_validation_dependency_store():
    df, summary = build_regime_validation_dependency_store_registry()
    assert not df.empty
    assert len(df) >= 7
    assert (df["validation_status"] == "SATISFIED").all()
    assert (df["non_signal"] == True).all()

    s_res = summarize_regime_validation_dependency_store(df)
    assert s_res["all_satisfied"] is True
    assert s_res["all_non_signal"] is True
