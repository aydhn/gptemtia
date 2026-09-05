from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.technical_indicator_catalog_expansion import build_technical_indicator_catalog_expansion


def test_technical_indicator_catalog_expansion():
    prof = get_default_technical_indicator_profile()
    df, summary = build_technical_indicator_catalog_expansion(prof)

    assert not df.empty
    assert len(df) >= 30
    assert summary["total_families"] >= 12
    assert summary["non_signal_guaranteed"] is True
    assert "family_price_action" in summary["families"]
    assert "family_returns" in summary["families"]
    assert "family_moving_average" in summary["families"]
    assert "family_trend" in summary["families"]
    assert "family_momentum" in summary["families"]
    assert "family_oscillator" in summary["families"]
    assert "family_volatility" in summary["families"]
    assert "family_range" in summary["families"]
    assert "family_channel" in summary["families"]
    assert "family_candle_anatomy" in summary["families"]
    assert "family_quote_microstructure" in summary["families"]
    assert "family_mean_reversion" in summary["families"]
