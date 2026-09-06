"""Tests for Phase 134 Regime Manual Review Blocker Store."""

from advanced_regime_featurestore_integration.regime_manual_review_blocker_store import (
    build_regime_manual_review_blocker_store_registry,
    summarize_regime_manual_review_blocker_store,
)


def test_manual_review_blockers():
    df, summary = build_regime_manual_review_blocker_store_registry()
    assert not df.empty
    assert len(df) >= 7
    assert (df["auto_fix_allowed"] == False).all()
    assert (df["destructive_action_allowed"] == False).all()

    s_res = summarize_regime_manual_review_blocker_store(df)
    assert s_res["auto_fix_allowed"] is False
    assert s_res["destructive_allowed"] is False
