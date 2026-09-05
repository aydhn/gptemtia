"""Tests for Cross-Asset Lead-Lag Placeholders."""

from advanced_cross_asset_regime_context.cross_asset_lead_lag_placeholders import (
    LEAD_LAG_PLACEHOLDER_RECORDS,
    build_cross_asset_lead_lag_placeholder_registry,
)


def test_build_cross_asset_lead_lag_placeholder_registry():
    assert len(LEAD_LAG_PLACEHOLDER_RECORDS) >= 3
    df, summary = build_cross_asset_lead_lag_placeholder_registry()
    assert len(df) >= 3
    assert "placeholder_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["zero_trading_signals"] is True
    assert summary["zero_forecasting_models"] is True
