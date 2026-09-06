"""Tests for Phase 134 Regime FeatureStore Schema."""

import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_schema import (
    build_regime_featurestore_schema_registry,
    validate_regime_featurestore_schema,
    summarize_regime_featurestore_schema,
)


def test_schema_registry():
    df, summary = build_regime_featurestore_schema_registry()
    assert not df.empty
    assert len(df) >= 10
    assert summary["forbidden_columns_count"] >= 15

    s_res = summarize_regime_featurestore_schema(df)
    assert s_res["total_fields"] == len(df)


def test_schema_validation():
    valid_df = pd.DataFrame(columns=[
        "store_key", "store_entity_type", "entity_id", "timestamp_utc",
        "component_name", "source_phase", "source_component_ref",
        "validation_acceptance_ref", "no_lookahead_acceptance_ref",
        "metadata_only_news_acceptance_ref", "source_preservation_ref",
        "quality_dependency_ref", "validation_dependency_ref",
        "lineage_ref", "manual_review_required", "non_signal"
    ])
    res = validate_regime_featurestore_schema(valid_df)
    assert res["is_valid"] is True
    assert res["non_signal"] is True

    # With forbidden column
    forbidden_df = valid_df.copy()
    forbidden_df["signal"] = 1
    res_f = validate_regime_featurestore_schema(forbidden_df)
    assert res_f["is_valid"] is False
    assert res_f["non_signal"] is False
    assert "signal" in res_f["found_forbidden_columns"]
