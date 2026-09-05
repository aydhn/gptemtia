from advanced_market_behavior_diagnostics.regime_family_quality import (
    build_regime_family_quality_report,
    summarize_regime_family_quality,
    CORE_REGIME_FAMILIES,
)


def test_regime_family_quality():
    df, summary = build_regime_family_quality_report()

    assert not df.empty
    assert len(df) == len(CORE_REGIME_FAMILIES)
    assert "family_name" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["ready_count"] == len(CORE_REGIME_FAMILIES)
    assert summary["average_consistency"] >= 0.90
    assert summary["phase_130_ready"] is True
