"""Tests for Cross-Asset Regime Context Findings."""

from advanced_cross_asset_regime_context.cross_asset_regime_context_findings import (
    SAMPLE_FINDINGS,
    build_cross_asset_regime_context_findings_registry,
)


def test_build_cross_asset_regime_context_findings_registry():
    assert len(SAMPLE_FINDINGS) >= 2
    df, summary = build_cross_asset_regime_context_findings_registry()
    assert len(df) >= 2
    assert "finding_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["destructive_action_allowed"] is False
    assert summary["auto_fix_allowed"] is False
