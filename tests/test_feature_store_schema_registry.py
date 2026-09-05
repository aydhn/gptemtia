import pandas as pd
from advanced_feature_store_integration.feature_store_schema_registry import (
    build_feature_store_schema_registry,
    validate_feature_store_schema,
    summarize_feature_store_schema_registry,
)

def test_schema_registry_and_validation():
    df, s = build_feature_store_schema_registry()
    assert not df.empty
    assert s["total_schemas"] >= 3

    # Test schema validator with valid dataframe
    sample_df = pd.DataFrame({
        "store_key": ["k1"],
        "entity_type": ["fx"],
        "entity_id": ["eurusd"],
        "timestamp_field": ["timestamp"],
        "feature_name": ["sma_20"],
        "feature_family": ["tech"],
        "source_phase": [117],
        "validation_status": ["pass"],
        "quality_score_ref": [0.99],
        "drift_score_ref": [0.01],
        "lineage_ref": ["lin_1"],
        "manual_review_required": [False],
        "non_signal": [True],
    })
    res = validate_feature_store_schema(sample_df)
    assert res["is_valid"] is True

    # Test schema validator with missing columns
    res_bad = validate_feature_store_schema(pd.DataFrame({"store_key": ["k1"]}))
    assert res_bad["is_valid"] is False
    assert res_bad["missing_count"] > 0
