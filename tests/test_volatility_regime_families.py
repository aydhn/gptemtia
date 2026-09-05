from advanced_regime_foundation.volatility_regime_families import (
    build_volatility_regime_family_registry,
    summarize_volatility_regime_families,
)


def test_volatility_regime_families():
    df, summary = build_volatility_regime_family_registry()
    assert not df.empty
    assert summary["all_non_signal"] is True
    assert summary["no_trading_recommendations"] is True

    sub_names = list(df["sub_family_name"])
    assert "volatility_level_context" in sub_names
    assert "volatility_expansion_context" in sub_names
    assert "volatility_compression_context" in sub_names
    assert "atr_realized_volatility_context" in sub_names
    assert "bollinger_width_context" in sub_names

    summ = summarize_volatility_regime_families(df)
    assert summ["total_sub_families"] == 5
    assert summ["non_signal"] is True
