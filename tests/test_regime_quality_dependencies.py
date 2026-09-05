from advanced_market_behavior_diagnostics.regime_quality_dependencies import (
    build_regime_quality_dependency_report,
    summarize_regime_quality_dependencies,
    CORE_REGIME_QUALITY_DEPENDENCIES,
)


def test_regime_quality_dependencies():
    df, summary = build_regime_quality_dependency_report()

    assert not df.empty
    assert len(df) == len(CORE_REGIME_QUALITY_DEPENDENCIES)
    assert "dependency_name" in df.columns
    assert summary["all_satisfied"] is True
    assert summary["blocking_dependencies_passed"] is True
    assert summary["non_signal"] is True
