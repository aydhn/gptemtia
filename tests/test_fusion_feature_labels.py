"""Tests for Fusion Feature Labels."""

import pytest
from advanced_feature_fusion.fusion_feature_labels import (
    validate_fusion_feature_domain_label,
    validate_fusion_family_label,
    validate_fusion_status_label,
    validate_fusion_join_policy_label,
    list_fusion_feature_domain_labels,
    list_fusion_family_labels,
    list_fusion_status_labels,
    list_fusion_join_policy_labels,
)


def test_fusion_labels_valid():
    assert validate_fusion_feature_domain_label("macro_feature_fusion_domain") is True
    assert validate_fusion_family_label("fusion_family_macro") is True
    assert validate_fusion_status_label("fusion_ready") is True
    assert validate_fusion_join_policy_label("fusion_join_policy_backward_asof") is True


def test_fusion_labels_invalid():
    with pytest.raises(ValueError):
        validate_fusion_feature_domain_label("non_existent_domain")
    with pytest.raises(ValueError):
        validate_fusion_family_label("non_existent_family")
    with pytest.raises(ValueError):
        validate_fusion_status_label("invalid_status")
    with pytest.raises(ValueError):
        validate_fusion_join_policy_label("invalid_policy")


def test_list_functions():
    assert len(list_fusion_feature_domain_labels()) > 0
    assert len(list_fusion_family_labels()) > 0
    assert len(list_fusion_status_labels()) > 0
    assert len(list_fusion_join_policy_labels()) > 0
