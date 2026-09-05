from advanced_market_behavior_diagnostics.regime_family_coverage import (
    build_regime_family_coverage_report,
    summarize_regime_family_coverage,
)


def test_regime_family_coverage():
    df, summary = build_regime_family_coverage_report()

    assert not df.empty
    assert "family_name" in df.columns
    assert "overall_family_coverage" in df.columns
    assert summary["all_families_covered"] is True
    assert summary["average_coverage"] == 1.0
    assert summary["non_signal"] is True
