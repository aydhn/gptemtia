"""Tests for Transition Quality Dependencies."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.transition_quality_dependencies import (
    build_transition_quality_dependency_report,
    summarize_transition_quality_dependencies,
    QUALITY_DEPENDENCIES,
)


def test_build_transition_quality_dependency_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_transition_quality_dependency_report(profile)

    assert not df.empty
    assert len(df) == 5
    assert "dependency_name" in df.columns
    assert (df["is_blocking"] == True).all()

    assert summary["total_quality_dependencies"] == 5
    assert summary["all_satisfied"] is True
    assert summary["all_blocking"] is True


def test_summarize_transition_quality_dependencies():
    profile = get_default_regime_transition_profile()
    df, _ = build_transition_quality_dependency_report(profile)
    summary = summarize_transition_quality_dependencies(df)
    assert summary["total_quality_dependencies"] == 5
    assert summary["all_satisfied"] is True
