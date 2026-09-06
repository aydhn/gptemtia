"""Tests for Phase 134 Regime Lineage References."""

from advanced_regime_featurestore_integration.regime_lineage_references import (
    build_regime_lineage_reference_registry,
    summarize_regime_lineage_references,
)


def test_lineage_references():
    df, summary = build_regime_lineage_reference_registry()
    assert not df.empty
    assert len(df) == 9
    assert (df["traceability_status"] == "VERIFIED").all()
    assert (df["non_signal"] == True).all()

    s_res = summarize_regime_lineage_references(df)
    assert s_res["total_lineage_steps"] == 9
    assert s_res["all_verified"] is True
