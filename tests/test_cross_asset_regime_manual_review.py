"""Tests for Cross-Asset Regime Manual Review Queue."""

from advanced_cross_asset_regime_context.cross_asset_regime_manual_review import (
    MANUAL_REVIEW_ITEMS,
    build_cross_asset_regime_manual_review_queue,
)


def test_build_cross_asset_regime_manual_review_queue():
    assert len(MANUAL_REVIEW_ITEMS) >= 5
    df, summary = build_cross_asset_regime_manual_review_queue()
    assert len(df) >= 5
    assert "item_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["auto_fix_allowed"] is False
    assert summary["destructive_action_allowed"] is False
