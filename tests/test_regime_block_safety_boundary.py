"""Test suite for Phase 135 Regime Block Safety Boundary."""

from advanced_regime_acceptance.regime_block_safety_boundary import (
    build_regime_block_safety_boundary_report,
    build_regime_block_no_go_conditions,
    build_regime_block_safe_go_conditions,
    summarize_regime_block_safety_boundary,
)


def test_safety_boundary_report():
    df, summary = build_regime_block_safety_boundary_report()
    assert not df.empty
    assert summary["no_go_rules_count"] >= 19
    assert summary["safe_go_principles_count"] >= 8
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True

    s2 = summarize_regime_block_safety_boundary(df)
    assert s2["all_compliant"] is True

    nogo_df = build_regime_block_no_go_conditions()
    assert len(nogo_df) >= 19
    assert bool(nogo_df["enforced"].all()) is True

    safego_df = build_regime_block_safe_go_conditions()
    assert len(safego_df) >= 8
    assert bool(safego_df["active"].all()) is True
