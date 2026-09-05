import pytest
from advanced_factor_metadata.factor_manual_review_registry import (
    build_factor_manual_review_registry,
    summarize_factor_manual_review_registry,
)


def test_build_factor_manual_review_registry():
    df, summary = build_factor_manual_review_registry()
    assert not df.empty
    assert summary["total_review_items"] >= 5
    assert summary["destructive_action_allowed"] is False
    assert summary["non_signal"] is True

    assert "review_reason" in df.columns
    assert "suggested_action" in df.columns
    assert "destructive_action_allowed" in df.columns
    assert (~df["destructive_action_allowed"]).all()

    stats = summarize_factor_manual_review_registry(df)
    assert stats["destructive_action_allowed"] is False
    assert stats["non_signal"] is True
