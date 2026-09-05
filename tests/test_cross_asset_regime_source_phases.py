"""Tests for Cross-Asset Regime Source Phases."""

from advanced_cross_asset_regime_context.cross_asset_regime_source_phases import (
    SOURCE_PHASES,
    build_cross_asset_regime_source_phase_registry,
)


def test_build_cross_asset_regime_source_phase_registry():
    assert len(SOURCE_PHASES) >= 7
    df, summary = build_cross_asset_regime_source_phase_registry()
    assert len(df) >= 7
    assert "source_phase_num" in df.columns
    assert summary["all_source_preserved"] is True
    assert summary["all_non_signal"] is True
