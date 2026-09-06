"""Tests for Regime Manual Review Acceptance."""

from advanced_regime_validation_acceptance.regime_manual_review_acceptance import (
    build_regime_manual_review_acceptance_queue,
    summarize_regime_manual_review_acceptance_queue,
    FORBIDDEN_REVIEW_ACTIONS,
)


def test_manual_review_acceptance():
    df, summary = build_regime_manual_review_acceptance_queue()
    assert not df.empty
    assert summary["destructive_actions_allowed"] is False
    assert (df["destructive_action_allowed"] == False).all()
    assert (df["auto_fix_allowed"] == False).all()
    assert (df["auto_drop_allowed"] == False).all()

    for forbidden in FORBIDDEN_REVIEW_ACTIONS:
        for action in df["suggested_action"]:
            assert forbidden not in action.lower()

    s_df = summarize_regime_manual_review_acceptance_queue(df)
    assert s_df["zero_destructive_actions"] is True
