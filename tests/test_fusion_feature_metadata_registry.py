"""Tests for Fusion Feature Metadata Registry."""

from advanced_feature_fusion.fusion_feature_metadata_registry import (
    get_fusion_feature_metadata_registry,
    get_fusion_feature_metadata_summary,
    get_feature_metadata_by_id,
)


def test_metadata_registry():
    features = get_fusion_feature_metadata_registry()
    assert len(features) == 17
    summary = get_fusion_feature_metadata_summary()
    assert summary["total_features"] == 17
    assert summary["zero_signal_guarantee"] is True
    assert summary["strictly_metadata_only"] is True


def test_get_by_id():
    f = get_feature_metadata_by_id("macro_value_change")
    assert f is not None
    assert f.feature_id == "macro_value_change"
    assert f.domain == "macroeconomic"

    f_none = get_feature_metadata_by_id("non_existent_id")
    assert f_none is None
