"""Tests for Regime Validation Acceptance Domain Registry."""

from advanced_regime_validation_acceptance.regime_validation_acceptance_domain_registry import (
    build_regime_validation_acceptance_domain_registry,
    summarize_regime_validation_acceptance_domains,
)


def test_domain_registry():
    df, summary = build_regime_validation_acceptance_domain_registry()
    assert not df.empty
    assert len(df) >= 28
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True

    s_df = summarize_regime_validation_acceptance_domains(df)
    assert s_df["total_domains"] == len(df)
