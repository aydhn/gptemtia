from advanced_regime_foundation.regime_family_registry import (
    build_regime_family_registry,
    summarize_regime_family_registry,
)


def test_regime_family_registry():
    df, summary = build_regime_family_registry()
    assert not df.empty
    assert summary["all_non_signal"] is True
    assert summary["model_training_executed"] is False
    assert summary["clustering_executed"] is False

    family_names = list(df["family_name"])
    assert "regime_family_volatility" in family_names
    assert "regime_family_trend" in family_names
    assert "regime_family_range" in family_names
    assert "regime_family_liquidity_placeholder" in family_names
    assert "regime_family_macro_context" in family_names
    assert "regime_family_event_context" in family_names
    assert "regime_family_news_metadata_context" in family_names
    assert "regime_family_cross_asset_context" in family_names

    summ = summarize_regime_family_registry(df)
    assert summ["total_families"] == len(df)
    assert summ["non_signal"] is True
