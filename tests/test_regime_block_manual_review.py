"""Test suite for Phase 135 Regime Block Manual Review Queue."""

from advanced_regime_acceptance.regime_block_manual_review import (
    build_regime_block_manual_review_queue,
    summarize_regime_block_manual_review_queue,
    FORBIDDEN_RECOMMENDATIONS,
)


def test_manual_review_queue():
    df, summary = build_regime_block_manual_review_queue()
    assert summary["forbidden_recommendations_enforced"] is True
    assert summary["auto_destructive_allowed"] is False
    assert summary["non_signal"] is True

    s2 = summarize_regime_block_manual_review_queue(df)
    assert s2["non_signal"] is True

    for _, row in df.iterrows():
        assert row["auto_destructive_action_allowed"] is False
        rec = row["recommendation"].lower()
        for forbidden in FORBIDDEN_RECOMMENDATIONS:
            assert forbidden not in rec
