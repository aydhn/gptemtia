"""Tests for Regime Quality Dependency Acceptance."""

from advanced_regime_validation_acceptance.regime_quality_dependency_acceptance import (
    build_regime_quality_dependency_acceptance_report,
    summarize_regime_quality_dependency_acceptance,
)


def test_quality_dependency_acceptance():
    df, summary = build_regime_quality_dependency_acceptance_report()
    assert not df.empty
    assert summary["all_satisfied"] is True
    assert summary["satisfied_dependencies"] == len(df)

    s_df = summarize_regime_quality_dependency_acceptance(df)
    assert s_df["all_satisfied"] is True
