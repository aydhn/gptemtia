"""Tests for Phase 134 Regime Quality Dependency Store."""

from advanced_regime_featurestore_integration.regime_quality_dependency_store import (
    build_regime_quality_dependency_store_registry,
    summarize_regime_quality_dependency_store,
)


def test_quality_dependency_store():
    df, summary = build_regime_quality_dependency_store_registry()
    assert not df.empty
    assert len(df) >= 4
    assert (df["dependency_status"] == "SATISFIED").all()
    assert (df["non_signal"] == True).all()

    s_res = summarize_regime_quality_dependency_store(df)
    assert s_res["all_satisfied"] is True
    assert s_res["all_non_signal"] is True
