"""Test suite for Phase 135 Domain Registry."""

from advanced_regime_acceptance.regime_acceptance_domain_registry import (
    build_regime_acceptance_domain_registry,
    summarize_regime_acceptance_domains,
)


def test_domain_registry_builder():
    df, summary = build_regime_acceptance_domain_registry()
    assert not df.empty
    assert len(df) == 11
    assert summary["phase_start"] == 126
    assert summary["phase_end"] == 135
    assert summary["handoff_phase"] == 136
    assert summary["non_signal"] is True

    s2 = summarize_regime_acceptance_domains(df)
    assert s2["total_domains"] == 11
    assert 126 in s2["phases"]
    assert 135 in s2["phases"]
    assert 136 in s2["phases"]
