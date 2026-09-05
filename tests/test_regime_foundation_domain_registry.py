from advanced_regime_foundation.regime_foundation_domain_registry import (
    build_regime_foundation_domain_registry,
)


def test_regime_foundation_domain_registry():
    df, summary = build_regime_foundation_domain_registry()
    assert not df.empty
    assert len(df) >= 20
    assert summary["all_non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False

    domain_names = list(df["domain_name"])
    assert "Market Behavior Taxonomy" in domain_names
    assert "Regime State Taxonomy" in domain_names
    assert "Regime Families" in domain_names
    assert "Phase 127 Regime Feature Matrix Handoff" in domain_names
