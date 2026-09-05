"""Tests for Transition Manual Review Queue."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.transition_manual_review import (
    build_transition_manual_review_queue,
    summarize_transition_manual_review_queue,
    SAMPLE_REVIEW_ITEMS,
)


def test_build_transition_manual_review_queue():
    profile = get_default_regime_transition_profile()
    df, summary = build_transition_manual_review_queue(profile)

    assert not df.empty
    assert len(df) == 4
    assert "review_id" in df.columns
    assert (df["auto_fix_forbidden"] == True).all()
    assert (df["manual_review_required"] == True).all()

    assert summary["total_review_items"] == 4
    assert summary["auto_fix_forbidden_certified"] is True
    assert summary["forbidden_actions_avoided"] is True


def test_summarize_transition_manual_review_queue():
    profile = get_default_regime_transition_profile()
    df, _ = build_transition_manual_review_queue(profile)
    summary = summarize_transition_manual_review_queue(df)
    assert summary["total_review_items"] == 4
    assert summary["forbidden_actions_avoided"] is True
