from advanced_regime_rule_free.regime_candidate_feature_sets import (
    build_regime_candidate_feature_set_registry,
    summarize_regime_candidate_feature_sets,
)


def test_build_regime_candidate_feature_set_registry():
    df, summary = build_regime_candidate_feature_set_registry()
    assert len(df) == 7
    assert summary["total_candidate_features"] >= 30
    assert summary["all_non_signal"] is True
    assert summary["feature_sets_status"] == "VALID"

    ids = df["feature_set_id"].tolist()
    assert "cfs_technical_volatility" in ids
    assert "cfs_technical_trend" in ids
    assert "cfs_range_mean_reversion" in ids
    assert "cfs_cross_asset_alignment" in ids
    assert "cfs_macro_event_context" in ids
    assert "cfs_news_metadata_attention" in ids
    assert "cfs_quality_drift_diagnostics" in ids
