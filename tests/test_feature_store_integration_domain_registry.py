from advanced_feature_store_integration.feature_store_integration_domain_registry import (
    build_feature_store_integration_domain_registry,
    summarize_feature_store_integration_domain_registry,
)

def test_domain_registry():
    df, s = build_feature_store_integration_domain_registry()
    assert not df.empty
    assert s["total_domains"] >= 25
    assert s["non_signal"] is True
    assert s["source_preserved"] is True
    summary = summarize_feature_store_integration_domain_registry(df)
    assert summary["total_domains"] >= 25
