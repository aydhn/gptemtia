"""Tests for Fusion Feature System Validation."""

from advanced_feature_fusion.fusion_feature_validation import validate_all_fusion_feature_components


def test_system_validation():
    val = validate_all_fusion_feature_components()
    assert val["valid"] is True
    assert len(val["errors"]) == 0
    assert val["profiles_count"] >= 3
    assert val["domains_count"] == 35
    assert val["policies_checked"] == 15
    assert val["zero_signal_guarantee"] is True
    assert val["metadata_only_news_guarantee"] is True
