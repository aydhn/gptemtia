"""Test suite for Phase 135 Component Acceptance."""

from advanced_regime_acceptance.regime_block_component_acceptance import (
    build_regime_block_component_acceptance_report,
    summarize_regime_block_component_acceptance,
)


def test_component_acceptance():
    df, summary = build_regime_block_component_acceptance_report()
    assert len(df) == 10
    assert summary["total_components"] == 10
    assert summary["all_accepted"] is True
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True
    assert summary["phase_start"] == 126
    assert summary["phase_end"] == 135

    s2 = summarize_regime_block_component_acceptance(df)
    assert s2["component_count"] == 10
    assert s2["all_accepted"] is True
    assert s2["all_non_signal"] is True
