"""Test suite for Phase 135 Regime Block Dependencies."""

from advanced_regime_acceptance.regime_block_dependencies import (
    build_regime_block_dependency_report,
    summarize_regime_block_dependencies,
)


def test_block_dependencies():
    df, summary = build_regime_block_dependency_report()
    assert len(df) == 10
    assert summary["total_dependency_steps"] == 10
    assert summary["all_satisfied"] is True
    assert summary["all_non_signal"] is True
    assert "126" in summary["flow"]
    assert "135" in summary["flow"]
    assert "136" in summary["flow"]

    s2 = summarize_regime_block_dependencies(df)
    assert s2["dependency_count"] == 10
    assert s2["all_satisfied"] is True
