"""Tests for Cross-Asset Regime Domain Registry."""

from advanced_cross_asset_regime_context.cross_asset_regime_labels import (
    CROSS_ASSET_REGIME_DOMAIN_LABELS,
)
from advanced_cross_asset_regime_context.cross_asset_regime_domain_registry import (
    build_cross_asset_regime_domain_registry,
)


def test_cross_asset_regime_domains():
    assert len(CROSS_ASSET_REGIME_DOMAIN_LABELS) >= 30
    df, summary = build_cross_asset_regime_domain_registry()
    assert len(df) == len(CROSS_ASSET_REGIME_DOMAIN_LABELS)
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True
