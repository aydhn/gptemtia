"""Tests for Cross-Asset Regime Context Scoring."""

from advanced_cross_asset_regime_context.cross_asset_regime_context_scoring import (
    build_cross_asset_regime_context_score_report,
)


def test_build_cross_asset_regime_context_score_report():
    df, summary = build_cross_asset_regime_context_score_report()
    assert len(df) == 1
    assert summary["context_score"] >= 0.8
    assert summary["all_non_signal"] is True
    assert summary["official_approval_claim"] is False
    assert summary["production_ready_claim"] is False
