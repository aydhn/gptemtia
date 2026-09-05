from advanced_feature_store_integration.feature_store_entity_registry import (
    build_feature_store_entity_registry,
    summarize_feature_store_entity_registry,
)

def test_entity_registry():
    df, s = build_feature_store_entity_registry()
    assert not df.empty
    assert s["total_entities"] >= 7
    expected_types = [
        "entity_fx_pair",
        "entity_commodity_symbol",
        "entity_macro_indicator",
        "entity_calendar_event",
        "entity_news_metadata",
        "entity_cross_asset_context",
        "entity_factor_family",
    ]
    present_types = list(df["entity_type"])
    for t in expected_types:
        assert t in present_types
    assert s["non_signal"] is True
    summary = summarize_feature_store_entity_registry(df)
    assert summary["total_entities"] >= 7
