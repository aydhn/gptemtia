from advanced_feature_store_integration.feature_store_manual_review_blockers import (
    build_feature_store_manual_review_blocker_registry,
    summarize_feature_store_manual_review_blockers,
)

def test_manual_review_blockers():
    df, s = build_feature_store_manual_review_blocker_registry()
    assert not df.empty
    assert s["total_blockers"] >= 4
    assert s["active_blocking_count"] >= 4
    assert s["destructive_action_allowed"] is False
    assert s["auto_fix_allowed"] is False
    assert s["auto_drop_allowed"] is False
    assert s["non_signal"] is True
    summary = summarize_feature_store_manual_review_blockers(df)
    assert summary["destructive_action_allowed"] is False
