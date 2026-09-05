"""Tests for Transition Quality Findings."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.transition_quality_findings import (
    build_transition_quality_findings_registry,
    summarize_transition_quality_findings,
    DEFAULT_FINDINGS,
)


def test_build_transition_quality_findings_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_transition_quality_findings_registry(profile)

    assert not df.empty
    assert len(df) == 2
    assert "finding_id" in df.columns
    assert (df["auto_fix_forbidden"] == True).all()

    assert summary["total_findings"] == 2
    assert summary["all_auto_fix_forbidden"] is True
    assert summary["manual_review_required"] is True


def test_summarize_transition_quality_findings():
    profile = get_default_regime_transition_profile()
    df, _ = build_transition_quality_findings_registry(profile)
    summary = summarize_transition_quality_findings(df)
    assert summary["total_findings"] == 2
    assert summary["all_auto_fix_forbidden"] is True
