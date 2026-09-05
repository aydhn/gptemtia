"""Tests for Cross-Asset Transition Alignment."""

from advanced_cross_asset_regime_context.cross_asset_transition_alignment import (
    TRANSITION_ALIGNMENT_RECORDS,
    build_cross_asset_transition_alignment_registry,
)


def test_build_cross_asset_transition_alignment_registry():
    assert len(TRANSITION_ALIGNMENT_RECORDS) >= 4
    df, summary = build_cross_asset_transition_alignment_registry()
    assert len(df) >= 4
    assert "alignment_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["zero_trading_signals"] is True
    assert summary["mean_readiness_score"] > 0.0
