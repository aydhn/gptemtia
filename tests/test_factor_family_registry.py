import pytest
from advanced_factor_metadata.factor_family_registry import build_factor_family_registry


def test_build_factor_family_registry():
    df, summary = build_factor_family_registry()
    assert not df.empty
    assert summary["total_families"] == 12
    assert summary["ready_families"] >= 8
    assert summary["placeholder_families"] >= 3
    assert summary["non_signal"] is True

    families = list(df["family_label"])
    assert "factor_family_trend" in families
    assert "factor_family_momentum" in families
    assert "factor_family_volatility" in families
    assert "factor_family_mean_reversion" in families
    assert "factor_family_return" in families
    assert "factor_family_quote_microstructure" in families
    assert "factor_family_macro_context" in families
    assert "factor_family_calendar_event" in families
    assert "factor_family_news_attention" in families
    assert "factor_family_cross_asset_context" in families
    assert "factor_family_regime_prep" in families
    assert "factor_family_composite" in families
