from advanced_regime_foundation.liquidity_regime_placeholders import (
    build_liquidity_regime_placeholder_registry,
    summarize_liquidity_regime_placeholders,
)


def test_liquidity_regime_placeholders():
    df, summary = build_liquidity_regime_placeholder_registry()
    assert not df.empty
    assert summary["all_non_signal"] is True
    assert summary["no_trading_recommendations"] is True

    ph_names = list(df["placeholder_name"])
    assert "quote_spread_context_placeholder" in ph_names
    assert "quote_staleness_context_placeholder" in ph_names
    assert "market_session_liquidity_placeholder" in ph_names
    assert "data_availability_liquidity_placeholder" in ph_names

    summ = summarize_liquidity_regime_placeholders(df)
    assert summ["total_placeholders"] == 4
    assert summ["non_signal"] is True
