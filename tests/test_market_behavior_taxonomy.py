from advanced_regime_foundation.market_behavior_taxonomy import (
    build_market_behavior_taxonomy_registry,
    summarize_market_behavior_taxonomy,
)


def test_market_behavior_taxonomy():
    df, summary = build_market_behavior_taxonomy_registry()
    assert not df.empty
    assert len(df) == 12
    assert summary["all_non_signal"] is True
    assert summary["no_trading_recommendations"] is True

    behavior_names = list(df["behavior_name"])
    assert "trending_behavior" in behavior_names
    assert "ranging_behavior" in behavior_names
    assert "high_volatility_behavior" in behavior_names
    assert "low_volatility_behavior" in behavior_names
    assert "volatility_expansion_behavior" in behavior_names
    assert "volatility_compression_behavior" in behavior_names
    assert "event_sensitive_behavior" in behavior_names
    assert "macro_sensitive_behavior" in behavior_names
    assert "cross_asset_sensitive_behavior" in behavior_names
    assert "liquidity_sensitive_placeholder" in behavior_names
    assert "transition_behavior_placeholder" in behavior_names
    assert "uncertain_behavior_placeholder" in behavior_names

    # Check that forbidden directional words like bullish/bearish are not in behavior names
    for name in behavior_names:
        assert "bullish" not in name.lower()
        assert "bearish" not in name.lower()
        assert "buy" not in name.lower()
        assert "sell" not in name.lower()

    summ = summarize_market_behavior_taxonomy(df)
    assert summ["total_items"] == 12
    assert summ["all_non_signal"] is True
