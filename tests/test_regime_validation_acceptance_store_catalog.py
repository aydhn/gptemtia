"""Tests for Phase 134 Regime Validation Acceptance Store Catalog."""

from advanced_regime_featurestore_integration.regime_validation_acceptance_store_catalog import (
    build_regime_validation_acceptance_store_catalog,
    summarize_regime_validation_acceptance_store_catalog,
)


def test_validation_acceptance_store_catalog():
    df, summary = build_regime_validation_acceptance_store_catalog()
    assert not df.empty
    assert len(df) == 3
    assert (df["non_signal"] == True).all()
    assert (df["source_preserved"] == True).all()
    assert summary["source_phase"] == 133

    s_res = summarize_regime_validation_acceptance_store_catalog(df)
    assert s_res["total_items"] == 3
    assert s_res["all_non_signal"] is True
