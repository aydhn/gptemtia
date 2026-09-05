"""Tests for Cross-Asset Regime Context Manifest."""

from advanced_cross_asset_regime_context.cross_asset_regime_context_manifest import (
    build_cross_asset_regime_context_manifest,
)


def test_build_cross_asset_regime_context_manifest():
    df, summary = build_cross_asset_regime_context_manifest()
    assert len(df) == 1
    assert summary["manifest_status"] == "MANIFEST_VALID"
    assert summary["current_phase"] == 131
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 132
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
    assert summary["zero_model_training"] is True
    assert summary["zero_clustering"] is True
