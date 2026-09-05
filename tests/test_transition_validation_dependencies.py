"""Tests for Transition Validation Dependencies."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.transition_validation_dependencies import (
    build_transition_validation_dependency_report,
    summarize_transition_validation_dependencies,
    VALIDATION_DEPENDENCIES,
)


def test_build_transition_validation_dependency_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_transition_validation_dependency_report(profile)

    assert not df.empty
    assert len(df) == 6
    assert "validation_id" in df.columns
    assert (df["is_blocking"] == True).all()

    assert summary["total_validation_dependencies"] == 6
    assert summary["all_passed"] is True
    assert summary["all_blocking"] is True


def test_summarize_transition_validation_dependencies():
    profile = get_default_regime_transition_profile()
    df, _ = build_transition_validation_dependency_report(profile)
    summary = summarize_transition_validation_dependencies(df)
    assert summary["total_validation_dependencies"] == 6
    assert summary["all_passed"] is True
