from advanced_feature_store_integration.feature_store_integration_health import (
    build_feature_store_integration_health_check,
    summarize_feature_store_integration_health,
)

def test_health_check():
    df, s = build_feature_store_integration_health_check()
    assert not df.empty
    assert s["status"] in ["HEALTHY", "DEGRADED"]
    assert s["total_checks"] >= 10
    summary = summarize_feature_store_integration_health(df)
    assert summary["total_checks"] >= 10
