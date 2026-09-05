from advanced_feature_store_integration.feature_store_validation_status import (
    build_feature_store_validation_status_registry,
    summarize_feature_store_validation_status,
)

def test_validation_status():
    df, s = build_feature_store_validation_status_registry()
    assert not df.empty
    assert s["total_validation_statuses"] >= 5
    assert s["pass_count"] >= 2
    assert s["non_signal"] is True
    summary = summarize_feature_store_validation_status(df)
    assert summary["all_non_signal"] is True
