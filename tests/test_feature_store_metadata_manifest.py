from advanced_feature_store_integration.feature_store_metadata_manifest import (
    build_feature_store_metadata_manifest,
    create_feature_store_metadata_manifest,
    summarize_feature_store_metadata_manifest,
)

def test_metadata_manifest():
    manifest = create_feature_store_metadata_manifest()
    assert manifest.non_signal is True
    assert manifest.source_preserved is True
    assert manifest.official_approval is False
    assert manifest.production_ready is False
    assert manifest.broker_ready is False
    assert manifest.contains_target_or_prediction is False

    df, s = build_feature_store_metadata_manifest()
    assert not df.empty
    assert s["non_signal"] is True
    assert s["source_preserved"] is True
    assert s["official_approval"] is False
    assert s["production_ready"] is False
    assert s["broker_ready"] is False
    summary = summarize_feature_store_metadata_manifest(df)
    assert summary["all_non_signal"] is True
