"""Tests for Transition Stability Scoring."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.transition_stability_scoring import (
    build_transition_stability_score_report,
    calculate_transition_stability_score,
    summarize_transition_stability_scores,
)


def test_build_transition_stability_score_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_transition_stability_score_report(profile)

    assert not df.empty
    assert len(df) == 1
    assert "stability_score" in df.columns
    assert "classification" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["stability_score"] == 0.82
    assert summary["classification"] == "high_stability"
    assert summary["non_signal_guaranteed"] is True


def test_summarize_transition_stability_scores():
    profile = get_default_regime_transition_profile()
    df, _ = build_transition_stability_score_report(profile)
    summary = summarize_transition_stability_scores(df)
    assert summary["stability_score"] == 0.82
    assert summary["classification"] == "high_stability"
