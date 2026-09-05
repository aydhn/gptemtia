from advanced_regime_foundation.regime_factor_dependencies import (
    build_regime_factor_dependency_registry,
    summarize_regime_factor_dependencies,
)


def test_regime_factor_dependencies():
    df, summary = build_regime_factor_dependency_registry()
    assert not df.empty
    assert summary["all_verified"] is True
    assert summary["all_non_signal"] is True

    phases = set(df["source_phase"])
    assert 122 in phases  # Phase 122 Factor Metadata
    assert 123 in phases  # Phase 123 Quality & Drift
    assert 121 in phases  # Phase 121 Validation
    assert 124 in phases  # Phase 124 FeatureStore

    summ = summarize_regime_factor_dependencies(df)
    assert summ["total_dependencies"] == len(df)
    assert summ["all_verified"] is True
