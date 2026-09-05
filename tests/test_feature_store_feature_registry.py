from advanced_feature_store_integration.feature_store_feature_registry import (
    build_feature_store_feature_registry,
    summarize_feature_store_feature_registry,
)

def test_feature_registry():
    df, s = build_feature_store_feature_registry()
    assert not df.empty
    assert s["total_features"] >= 9
    assert 117 in s["source_phases"]
    assert 118 in s["source_phases"]
    assert 119 in s["source_phases"]
    assert 120 in s["source_phases"]
    assert 121 in s["source_phases"]
    assert 123 in s["source_phases"]
    assert all(df["non_signal"])
    assert all(df["source_preserved"])
    assert not any(df["contains_target_or_prediction"])
    summary = summarize_feature_store_feature_registry(df)
    assert summary["all_non_signal"] is True
