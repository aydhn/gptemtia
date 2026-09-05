from advanced_regime_foundation.trend_regime_families import (
    build_trend_regime_family_registry,
    summarize_trend_regime_families,
)


def test_trend_regime_families():
    df, summary = build_trend_regime_family_registry()
    assert not df.empty
    assert summary["all_non_signal"] is True
    assert summary["no_trading_recommendations"] is True

    sub_names = list(df["sub_family_name"])
    assert "moving_average_trend_context" in sub_names
    assert "macd_context_placeholder" in sub_names
    assert "donchian_trend_context" in sub_names
    assert "trend_persistence_placeholder" in sub_names
    assert "trend_transition_placeholder" in sub_names

    summ = summarize_trend_regime_families(df)
    assert summ["total_sub_families"] == 5
    assert summ["non_signal"] is True
