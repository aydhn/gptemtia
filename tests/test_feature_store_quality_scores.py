from advanced_feature_store_integration.feature_store_quality_scores import (
    build_feature_store_quality_score_registry,
    summarize_feature_store_quality_scores,
)

def test_quality_scores():
    df, s = build_feature_store_quality_score_registry()
    assert not df.empty
    assert s["total_quality_scores"] >= 6
    assert 0.0 <= s["mean_quality_score"] <= 1.0
    assert all(df["non_signal"])
    assert all(df["source_preserved"])
