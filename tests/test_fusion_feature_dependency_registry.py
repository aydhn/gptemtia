"""Tests for Fusion Feature Dependency Registry."""

from advanced_feature_fusion.fusion_feature_dependency_registry import (
    get_fusion_feature_dependency_registry,
    get_fusion_feature_dependency_summary,
    validate_dependencies_satisfied,
)


def test_dependency_registry():
    deps = get_fusion_feature_dependency_registry()
    assert len(deps) == 17
    summary = get_fusion_feature_dependency_summary()
    assert summary["tracked_feature_count"] == 17
    assert summary["zero_signal_guarantee"] is True


def test_validate_dependencies_satisfied():
    # macro_value_change requires ['macro_value']
    assert validate_dependencies_satisfied("macro_value_change", ["macro_value", "other_col"]) is True
    assert validate_dependencies_satisfied("macro_value_change", ["wrong_col"]) is False
    assert validate_dependencies_satisfied("non_existent_feature", ["any"]) is False
