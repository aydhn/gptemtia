from advanced_feature_store_integration.feature_store_contract_registry import (
    build_feature_store_contract_registry,
    summarize_feature_store_contract_registry,
)

def test_contract_registry():
    df, s = build_feature_store_contract_registry()
    assert not df.empty
    assert s["total_contracts"] >= 7
    expected = [
        "technical_feature_store_contract",
        "multi_window_feature_grid_store_contract",
        "cross_asset_feature_store_contract",
        "macro_calendar_news_fusion_store_contract",
        "factor_metadata_store_contract",
        "quality_drift_metadata_store_contract",
        "validation_status_store_contract",
    ]
    present = list(df["store_name"])
    for c in expected:
        assert c in present
    assert s["all_non_signal"] is True
    assert s["all_source_preserved"] is True
    summary = summarize_feature_store_contract_registry(df)
    assert summary["total_contracts"] >= 7
