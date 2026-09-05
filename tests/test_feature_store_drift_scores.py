from advanced_feature_store_integration.feature_store_drift_scores import (
    build_feature_store_drift_score_registry,
    summarize_feature_store_drift_scores,
)

def test_drift_scores():
    df, s = build_feature_store_drift_score_registry()
    assert not df.empty
    assert s["total_drift_scores"] >= 6
    assert 0.0 <= s["mean_drift_score"] <= 1.0
    assert all(df["non_signal"])
