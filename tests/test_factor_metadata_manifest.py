import pytest
from advanced_factor_metadata.factor_metadata_manifest import (
    build_factor_metadata_manifest,
    create_factor_metadata_manifest,
    summarize_factor_metadata_manifest,
)


def test_build_factor_metadata_manifest():
    df, summary = build_factor_metadata_manifest()
    assert not df.empty
    assert summary["total_manifest_items"] == 12
    assert summary["all_non_signal"] is True
    assert summary["zero_target_or_prediction"] is True
    assert summary["zero_trading_recommendation"] is True
    assert summary["all_source_preserved"] is True
    assert summary["status"] == "factor_ready"

    stats = summarize_factor_metadata_manifest(df)
    assert stats["total_factors"] == 12
    assert stats["all_non_signal"] is True
    assert stats["zero_predictions"] is True


def test_create_factor_metadata_manifest():
    item = create_factor_metadata_manifest(
        factor_name="factor_trend_test",
        factor_family="trend",
        input_feature_count=3,
        dependency_count=2,
        validation_dependency_count=5,
        quality_dependency_count=4,
    )
    assert item.non_signal is True
    assert item.contains_target_or_prediction is False
    assert item.contains_trading_recommendation is False
    assert item.source_preserved is True
