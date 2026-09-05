from advanced_feature_store_integration.feature_store_lineage_references import (
    build_feature_store_lineage_reference_registry,
    summarize_feature_store_lineage_references,
)

def test_lineage_references():
    df, s = build_feature_store_lineage_reference_registry()
    assert not df.empty
    assert s["total_lineage_references"] >= 4
    assert 114 in s["source_phases"]
    assert 121 in s["source_phases"]
    assert 122 in s["source_phases"]
    assert 123 in s["source_phases"]
