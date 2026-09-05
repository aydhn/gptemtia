from advanced_market_behavior_diagnostics.behavior_quality_manual_review import (
    build_behavior_quality_manual_review_queue,
    summarize_behavior_quality_manual_review_queue,
    CORE_MANUAL_REVIEW_ITEMS,
)


def test_behavior_quality_manual_review():
    df, summary = build_behavior_quality_manual_review_queue()

    assert not df.empty
    assert len(df) == len(CORE_MANUAL_REVIEW_ITEMS)
    assert "review_id" in df.columns
    assert summary["destructive_action_allowed"] is False
    assert summary["blocking_items_count"] == 0
    assert summary["non_signal"] is True
