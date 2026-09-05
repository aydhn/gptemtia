from advanced_regime_foundation.regime_state_taxonomy import (
    build_regime_state_taxonomy_registry,
    summarize_regime_state_taxonomy,
)


def test_regime_state_taxonomy():
    df, summary = build_regime_state_taxonomy_registry()
    assert not df.empty
    assert summary["all_prefixed_correctly"] is True
    assert summary["all_non_signal"] is True
    assert summary["no_targets_or_predictions"] is True
    assert summary["no_trading_recommendations"] is True

    state_names = list(df["regime_state_name"])
    for name in state_names:
        assert name.startswith("regime_state_")
        assert "target" not in name.lower()
        assert "prediction" not in name.lower()
        assert "buy" not in name.lower()
        assert "sell" not in name.lower()

    assert "regime_state_trend_context" in state_names
    assert "regime_state_range_context" in state_names
    assert "regime_state_volatility_high_context" in state_names
    assert "regime_state_volatility_low_context" in state_names
    assert "regime_state_macro_event_context" in state_names

    summ = summarize_regime_state_taxonomy(df)
    assert summ["total_items"] == len(df)
    assert summ["all_non_signal"] is True
