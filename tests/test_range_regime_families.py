from advanced_regime_foundation.range_regime_families import (
    build_range_regime_family_registry,
    summarize_range_regime_families,
)


def test_range_regime_families():
    df, summary = build_range_regime_family_registry()
    assert not df.empty
    assert summary["all_non_signal"] is True
    assert summary["no_trading_recommendations"] is True

    sub_names = list(df["sub_family_name"])
    assert "range_bound_context" in sub_names
    assert "mean_reversion_context" in sub_names
    assert "zscore_context" in sub_names
    assert "channel_position_context" in sub_names
    assert "compression_range_context" in sub_names

    summ = summarize_range_regime_families(df)
    assert summ["total_sub_families"] == 5
    assert summ["non_signal"] is True
